import cv2
from process import process_image

######################################################################################
# Version 1.5
# Program for real-time hand detection and finger counting using OpenCV.
#
# main()
#       Parameters: None
#       Return: None
#       Description: Captures webcam feed, flips frame, processes image, displays result,
#                    and exits on 'q' key press.
#
# process_image()
#       Parameters: image frame
#       Return: processed frame with contours, convex hull, and detected finger count
#       Description: Extracts region of interest (ROI), applies grayscale and thresholding,
#                    finds largest contour, computes convex hull, identifies convexity
#                    defects, and passes results to detect_fingers().
#
# detect_fingers()
#       Parameters: convexity defects, hand contour, ROI, original frame
#       Return: frame with fingertip markers and overlaid finger count
#       Description: Analyzes convexity defects to count fingers, filters noise using
#                    angle and depth thresholds, handles special cases for closed fist
#                    (0) and one finger (1), and overlays the result on the frame.
#
######################################################################################

################################## PSEUDOCODE #######################################
#
# 1. Start webcam capture
# 2. While camera is active:
#       a. Capture and flip frame
#       b. Define region of interest (ROI) for hand
#       c. Convert ROI to grayscale, blur, and apply thresholding
#       d. Find contours and select the largest one (hand)
#       e. Draw contour and convex hull
#       f. Compute convexity defects between hull points
#       g. Pass defects and contour to detect_fingers():
#            - Loop over defects, compute angles and distances
#            - Count valid finger gaps
#            - If no defects, decide between fist (0) and one finger (1)
#            - Otherwise, fingers = defects + 1
#       h. Overlay finger count on frame
#       i. Display result window
#       j. Exit on 'q' key press
# 3. Release webcam and close OpenCV windows
#
######################################################################################


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        processed = process_image(frame)

        cv2.imshow("Hand Detection", processed)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
