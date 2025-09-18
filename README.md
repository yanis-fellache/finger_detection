# Finger Detection and Counting using OpenCV

## Version
**1.5**

## Overview
This project is a real-time hand and finger detection system using Python and OpenCV.  
It captures video from a webcam, detects a hand within a defined region of interest (ROI), and counts the number of fingers extended.  
The system handles special cases like a closed fist (0 fingers) and one finger raised, and overlays the detected finger count on the video feed.

---

## Features
- Real-time webcam capture and processing
- Hand detection using contours and convex hulls
- Finger counting using convexity defects with angle and depth filtering
- Handles closed fists and single-finger cases accurately
- ROI-based processing to reduce background interference
- Displays the processed frame with fingertip markers and finger count

---

## Dependencies

- Python 3.10+
- OpenCV (`cv2`)

---

## Instructions

- Run main.py
- A webcam window will open:
- Place your hand inside the blue rectangle (ROI)
- The detected fingers will be counted and displayed on screen
- Press 'q' to exit

---

## Module Descriptions

main.py
- main(): Captures webcam feed, flips the frame horizontally, sends frames to process_image(), displays the output, and handles exit on key press.

process.py
- process_image(frame):
    - Crops a region of interest (ROI) for hand detection
    - Converts ROI to grayscale and applies Gaussian blur
    - Applies thresholding to segment hand from background
    - Finds contours and selects the largest as the hand
    - Computes convex hull and convexity defects
    - Passes defects and contour to detect_fingers() for counting

detect.py
- detect_fingers(defects, cnt, roi, frame):
    - Analyzes convexity defects using angle and depth thresholds
    - Counts fingers as defects + 1
    - Handles special cases:
    - Closed fist → 0 fingers
    - One finger raised → 1 finger
    - Draws fingertip markers and overlays finger count on the frame

---

## Notes

- Adjust the ROI (roi = frame[50:400, 50:400]) to match your webcam setup.
- The HSV / grayscale threshold parameters can be tuned for different lighting conditions.
- The system currently supports up to 5 fingers detection.
- For best results, use a plain background that contrasts with hand and ensure good lighting.
- Proof and results in the results folder.

---

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
