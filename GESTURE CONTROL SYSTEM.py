import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

def get_gesture(defects_count, area_ratio):
    if defects_count == 0:
        return "FIST"

    if defects_count == 1:
        if area_ratio < 12:
            return "OK"
        else:
            return "THUMB UP"

    if defects_count == 2:
        return "PEACE"

    if defects_count >= 4:
        return "OPEN HAND"

    return "UNKNOWN"


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # 🔥 GRAND CADRE DE DETECTION 🔥
    top, bottom = 100, 500
    left, right = 100, 500

    roi = frame[top:bottom, left:right]

    # Dessiner le grand cadre
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 3)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Plage couleur peau
    lower = np.array([0, 30, 60])
    upper = np.array([20, 150, 255])
    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        hull = cv2.convexHull(cnt)
        area_cnt = cv2.contourArea(cnt)
        area_hull = cv2.contourArea(hull)
        area_ratio = ((area_hull - area_cnt) / area_cnt) * 100

        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)

        defects_count = 0

        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])

                a = math.dist(start, end)
                b = math.dist(start, far)
                c = math.dist(end, far)

                angle = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c + 1e-5)))

                if angle <= 80:
                    defects_count += 1
                    cv2.circle(roi, far, 5, (0, 0, 255), -1)

        gesture = get_gesture(defects_count, area_ratio)

        cv2.putText(frame, f"Gesture: {gesture}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3)

        cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
