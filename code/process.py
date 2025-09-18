import cv2
from detect import detect_fingers

######################################################################################
# process.py
# - process_image(): Extracts ROI, applies grayscale + thresholding, finds contour,
#                    computes convex hull, detects convexity defects, and forwards
#                    results to detect_fingers().
######################################################################################

def process_image(frame):
    roi = frame[50:400, 50:400]  # adjust based on your camera position
    cv2.rectangle(frame, (50, 50), (400, 400), (255, 0, 0), 2)  # draw ROI for reference
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 2)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return frame, 0

    cnt = max(contours, key=cv2.contourArea)
    if cv2.contourArea(cnt) < 3000:  # ignore small objects
        return frame, 0

    hull = cv2.convexHull(cnt)
    cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
    cv2.drawContours(roi, [hull], -1, (0, 0, 255), 2)

    hull_indices = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull_indices)

    if defects is None:
        return frame, 0
    
    return detect_fingers(defects, cnt, roi, frame)