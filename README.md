# Image to Pencil Sketch App

This repository contains a simple application that converts an image into a pencil sketch using OpenCV. The script reads an image, processes it to create a pencil sketch effect, and displays both the original and the sketch images.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Image to Pencil Sketch App utilizes OpenCV to transform an image into a pencil sketch. This is achieved by converting the image to grayscale, inverting it, applying a Gaussian blur, and then combining the original grayscale image with the inverted, blurred image to produce a sketch-like effect.

## Features

- Convert any image to a pencil sketch.
- Display the original image alongside the pencil sketch version.

## Installation

To run this project, you need to have Python and OpenCV installed. You can install OpenCV using pip:

```bash
pip install opencv-python
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-to-pencil-sketch.git
   cd image-to-pencil-sketch
   ```

2. Place your image in the desired directory. Update the path in the script if necessary.

3. Run the script:
   ```bash
   python sketch.py
   ```

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request. Please ensure your contributions adhere to the repository's guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code and use the provided script to convert your images into pencil sketches. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.
