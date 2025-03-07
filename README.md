# 🕵️‍♂️ Steganography Tool

## 🔍 Overview
This project is a **steganography tool** that allows users to hide secret messages within images using the **LSB (Least Significant Bit) technique**. It provides both **encoding and decoding** functionalities.

## ✨ Features
✅ Hide text messages inside images  
✅ Extract hidden messages from images  
✅ Supports **PNG** and **BMP** image formats  
✅ Simple and intuitive **command-line interface (CLI)**  

## 📋 Requirements
Ensure you have the following dependencies installed before proceeding:
- 🐍 Python **3.x**
- 📦 pip (**Python package manager**)

Required Python libraries:
- 📌 `numpy`
- 📌 `Pillow`
- 📌 `opencv-python`

## ⚙️ Installation
Follow these steps to install and set up the project:

### 🛠️ 1. Clone the Repository
```bash
git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool
```

### 🏗️ 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 📥 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### 🔐 Encoding a Message into an Image
```bash
python steganography.py encode -i input.png -o output.png -m "Your secret message"
```

### 🔓 Decoding a Message from an Image
```bash
python steganography.py decode -i output.png
```

## 🎯 Example
**Encoding:**
```bash
python steganography.py encode -i original.png -o secret.png -m "Hello, this is a hidden message!"
```

**Decoding:**
```bash
python steganography.py decode -i secret.png
```

## ⚠️ Notes
- 🖼️ Ensure that the input image is in **PNG** or **BMP** format.
- 📌 The output image should be saved in **PNG** format to avoid **lossy compression**.
- 📏 The hidden message length should be within a reasonable limit based on **image size**.

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and distribute it.

## 👨‍💻 Author
Developed by **Om Jadiya** 🚀
