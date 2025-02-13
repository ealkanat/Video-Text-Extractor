# Video Text Extractor

A Python tool that extracts text from video frames at specified timestamps and saves screenshots.

## Features
- Extract text from specific timestamps in a video
- Save screenshots of processed frames
- Generate detailed output report with timestamps
- Support for multiple timestamps
- Customizable output file path

## Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher
- pip (Python package installer)

## Installation Guide

### 1. Set Up Virtual Environment

#### For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### For Linux/MacOS:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Python Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

#### Windows:
1. Download Tesseract installer from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run installer
3. Add Tesseract to system PATH
4. Add this line at the start of your script if needed:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### Linux:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### MacOS:
```bash
brew install tesseract
```

## Usage

### Basic Command Structure
```bash
python video_text_extractor.py VIDEO_PATH --timestamps TIMESTAMP1 TIMESTAMP2 ... [--output OUTPUT_FILE]
```

### Examples

1. Extract text at specific timestamps:
```bash
python video_text_extractor.py video.mp4 --timestamps 1.5 3.0 5.5
```

2. With custom output file:
```bash
python video_text_extractor.py video.mp4 --timestamps 1.5 3.0 5.5 --output results.txt
```

## Project Structure
```
video_text_extractor/
├── venv/                      # Virtual environment folder
├── video_text_extractor.py    # Main script
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## Troubleshooting

### Common Issues

1. **"Unable to import 'cv2'" error:**
```bash
# Make sure you're in your virtual environment, then:
pip uninstall opencv-python
pip install opencv-python-headless
```

2. **"tesseract is not recognized":**
- Verify Tesseract is installed
- Check system PATH
- Set correct path in script (Windows)

## Notes
- Always activate virtual environment before running the script
- Timestamps beyond video duration are skipped
- Frames without text marked as "<NO TEXT DETECTED>"
- All processed frames saved as screenshots

## Uninstallation

### 1. Deactivate Virtual Environment
```bash
# If your virtual environment is active, deactivate it
deactivate
```

### 2. Remove Project Files
#### Windows:
```bash
# Remove virtual environment and project files
rmdir /s /q venv
del video_text_extractor.py
del requirements.txt
del README.md
```

#### Linux/MacOS:
```bash
# Remove virtual environment and project files
rm -rf venv
rm video_text_extractor.py
rm requirements.txt
rm README.md
```

### 3. Uninstall Tesseract OCR (Optional)

#### Windows:
1. Go to Control Panel
2. Select "Programs and Features"
3. Find Tesseract OCR in the list
4. Click "Uninstall"

#### Linux:
```bash
sudo apt-get remove tesseract-ocr
```

#### MacOS:
```bash
brew uninstall tesseract
```

Note: If you want to keep any generated output files or screenshots, make sure to back them up before removing the project files.
