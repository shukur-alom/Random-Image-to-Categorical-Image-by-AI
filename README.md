# Image Classification with NASNet Large


## Overview

This project uses the NASNet Large deep learning model to classify images into predefined categories. The model can identify the primary object or subject matter in an image and move image according category.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [License](#license)

## Introduction

Image classification is a fundamental task in computer vision. This project showcases the use of the NASNet Large model to classify images, making it suitable for applications like object recognition, content tagging, and more.

## Features

- Utilizes the NASNet Large model for accurate image classification.
- Can categorize images into predefined categories.
- Move image according category
- Easily customizable for specific image classification tasks.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Keras
- NASNet Large weights (e.g., "NASNet-large.h5")
- Images for classification (place in the "random image" directory)

## Installation

1. Clone this repository to your local machine:

```shell
   git clone https://github.com/yourusername/image-classification-nasnet.git
```
2. Install requirement
```shell
   pip3 install -r requirements.txt
```

## Usage
1. Prepare your images for classification by placing them in the "random image" directory.

2. Run the provided Python script to classify the images and move them to their respective categories:
   
```shell
   python main.py
```

## Model
This project uses the NASNet Large model for image classification. You can replace the weights with your own pre-trained model if needed.

## Results
The script will print out the top predicted categories and their confidence scores for each image. It will also organize the images into folders within the "categories image" directory.

## License
This project is licensed under the MIT License - see the [MIT LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
