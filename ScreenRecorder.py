# importing the required packages
import cv2
import pyautogui
import numpy as np

# Specify output file name and format
filename = "Recording.avi" # Replace with desired file path
codec = cv2.VideoWriter_fourcc(*"mp4v") # MP4 format
fps = 30.0 # Can be changed
resolution = (1920, 1080)

# Create a VideoWriter Object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Display recording in real time
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270) # Resize
cv2.moveWindow("Live", 100, 100) # Position

# Loop that takes screenshots (eliminates when user presses 'q')
while True:

    # Take screenshot and convert to numpy array
    img = pyautogui.screenshot()
    frame = np.array(img) 

    # Convert from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write to output file
    out.write(frame)

    # Show live preview
    cv2.imshow('Live', frame)

    # Stop recording when user presses 'q'
    if cv2.waitKey(1) == ord('q'):
        break 

# Release resources
out.release()
cv2.destroyAllWindows()