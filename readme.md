# Text Rewriter

## Description

A Python script that automatically rewrites selected text using Google's Gemini AI. When you select text by holding down the mouse button, the script copies and condenses the text to approximately 70% of its original length.

## Installation

1. Install required libraries:
```bash
pip install pywin32 pyautogui pyperclip google-generativeai
```

2. Create a `key.py` file with your Google AI API key:
```python
API_KEY = 'your_google_ai_api_key_here'
```

## Usage

1. Run the script:
```bash
python text_rewriter.py
```

2. Select text by holding down the mouse button
3. The script will automatically:
   - Copy the selected text
   - Generate a condensed version using Gemini AI
   - Print the rewritten text

Note: Currently supports Windows only.