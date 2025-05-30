# OpenCV Blemish Removal Project

This repository contains a Python script that uses OpenCV to remove blemishes from an image by selecting a patch with minimum Laplacian variance around a user-clicked point and blending it using seamless cloning. The project is part of an OpenCV University assessment.

## Project Overview

The script (`submission.py`) performs the following tasks:
- Loads an image (`blemish.png`).
- Allows users to click on blemishes to remove them interactively.
- For each click, extracts a central patch (20x20 pixels) and eight surrounding patches (40x40 pixels).
- Computes the Laplacian variance of each surrounding patch to select the one with the least texture.
- Blends the selected patch over the blemish using `cv2.seamlessClone`.
- Saves the final edited image as `output_blemish_removed.png`.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/OpenCV-Blemish-Removal.git
   cd OpenCV-Blemish-Removal
   ```
2. Ensure `blemish.png` is in the project directory.
3. Run the script:
   ```bash
   python submission.py
   ```
4. In the displayed window, left-click on blemishes to remove them. The image updates in real-time.
5. Press any key to save the final image as `output_blemish_removed.png` and exit.

## Results

The script produces an output image (`output_blemish_removed.png`), included in the repository, with blemishes removed.

- **Input Image** (`blemish.png`):
  ![Input Image with Blemishes](blemish.png)
- **Output Image** (`output_blemish_removed.png`):
  ![Output Image without Blemishes](output_blemish_removed.png)

## Acknowledgments

- OpenCV University for providing the project structure.
- OpenCV for the seamless cloning and image processing tools.