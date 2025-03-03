# Screen Recorder

This Python script records your screen and saves it as a video file. It uses the OpenCV library for video writing and PyAutoGUI for taking screenshots. The script also provides a live preview of the recording.

## Requirements

Before running the script, install the necessary libraries using the following commands:

```bash
pip install numpy
pip install pyautogui
pip install opencv-python
python -m pip install --upgrade pyscreeze pillow
```

Ensure that you're using the correct Python interpreter where these libraries are installed. You can check this with:

```bash
pip show opencv-python
```

Alternatively, you can use the command `Ctrl + Shift + P` and select **Python: Select Interpreter** to confirm.

## Code Description

The code captures the screen in real-time, saves the recorded video, and displays a live preview. The recording stops when the user presses the 'q' key.

### Key Parameters:
- **Output File**: The recorded video will be saved as `Recording.mp4`. You can change the file name by modifying the `filename` variable.
- **Codec**: The video will be encoded in MP4 format using `mp4v` codec.
- **FPS**: The default frames per second is set to 30.0, but you can change it as needed.
- **Resolution**: The video will be recorded at 1920x1080 resolution.

### Live Preview:
- The live preview of the screen is shown in a window titled "Live".
- You can resize and move the window based on your preference.

## How to Use

1. Ensure you have the required libraries installed.
2. Run the script. It will begin recording the screen.
3. The live preview window will appear showing the recording.
4. To stop the recording, simply press 'q'.

## License

This project is free to use and modify for personal or internal purposes. If you use or modify this work, you must provide proper attribution. Redistribution is **not allowed** without permission.

## Acknowledgments

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

