import cv2
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (1280, 720)})
picam2.configure(preview_config)
picam2.start()

while True:
    frame = picam2.capture_array()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian filter to detect edges
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    abs_lap = np.uint8(np.absolute(laplacian))

    # Threshold to find strong edges
    _, mask = cv2.threshold(abs_lap, 20, 255, cv2.THRESH_BINARY)

    # Create a red mask for peaking
    red_mask = np.zeros_like(frame)
    red_mask[:, :, 2] = mask  # Red channel

    # Overlay the red mask onto the original frame
    highlighted = cv2.addWeighted(frame, 1.0, red_mask, 0.5, 0)

    cv2.imshow("Focus Peaking", highlighted)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()
	
