import math
import cv2

######################################################################################
# detect.py
# - detect_fingers(): Analyzes convexity defects, counts fingers using angle/depth
#                     filtering, handles special cases (fist vs 1 finger), and overlays
#                     finger count on the frame.
######################################################################################

def detect_fingers(defects, cnt, roi, frame):
    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        a = math.dist(start, end)
        b = math.dist(start, far)
        c = math.dist(end, far)

        angle = math.acos((b**2 + c**2 - a**2) / (2*b*c)) if b*c != 0 else 0

        if angle <= math.pi/2 and d > 10000:
            finger_count += 1
            cv2.circle(roi, far, 5, (255, 0, 0), -1)

        cv2.circle(roi, start, 5, (0, 0, 255), -1)
        cv2.circle(roi, end, 5, (0, 255, 0), -1)

    if finger_count == 0:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = h / float(w)

        if aspect_ratio > 1.3:  
            final_count = 1
        else:                   
            final_count = 0
    else:
        final_count = min(finger_count + 1, 5)
    cv2.putText(frame, f"Fingers: {final_count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    return frame