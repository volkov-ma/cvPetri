import time
from picamera2 import Picamera2, Preview

# Create an instance of the PiCamera2 class
picam2 = Picamera2()

# Create a preview configuration with full sensor resolution (4056x3040)
preview_config = picam2.create_preview_configuration(main={"size": (4056, 3040)})

# Apply the configuration to the camera
picam2.configure(preview_config)

# Start the preview window using Qt-based OpenGL preview
picam2.start_preview(Preview.QTGL)

# Start the camera
picam2.start()

try:
    print("Preview started at 4056x3040 resolution. Press Ctrl+C to exit.")
    # Keep the preview running indefinitely
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the preview gracefully when Ctrl+C is pressed
    print("\nStopping preview...")
finally:
    picam2.stop_preview()
    picam2.stop()
