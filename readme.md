# Clipboard Text Rewriter  

This script monitors the clipboard for copied text and rewrites it using AI to make it more concise while preserving its structure.  

## Installation  

1. Install Python 3.9 or later.  
2. Install required packages:  

```bash  
pip install pyautogui pyperclip pywin32 requests google-generativeai  
```  

3. Add your Google Generative AI API key in a `key.py` file:  

```python  
API_KEY = 'your-api-key-here'  
```  

## Usage  

Run the script:  

```bash  
python rewrite_clipboard.py  
```  

When you copy text, the rewritten version will be displayed in the terminal.  

---  
