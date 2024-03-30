# Input Sanitizer Application

## Overview
The Input Sanitizer Application is a Python-based GUI tool designed to redact sensitive information from text inputs. It targets various types of sensitive data, including IP addresses, email addresses, API keys, URLs, passwords, and phone numbers, replacing them with `[REDACTED]` placeholders. This tool is particularly useful for ensuring that logs, configuration files, or any text containing sensitive info can be shared or stored more securely.

## Prerequisites
Before running the Input Sanitizer Application, ensure you have the following installed:

- Python 3.6 or newer
- Tkinter (usually comes with Python, but you may need to install it separately on Linux)

## Installation
No additional installation steps are required for the core functionality. Simply ensure your Python environment is set up according to the prerequisites.

## How to Run
To run the application, follow these steps:

1. Save the script to a file named `input_sanitizer.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `input_sanitizer.py` is saved.
4. Run the script by executing:

```bash
python input_sanitizer.py
```
Once the GUI opens, you can paste or type text into the "Input Text" box.  
Click the "Sanitize" button to process the text.  
The application will display the sanitized text in the "Sanitized Text" box, where sensitive information is replaced with `[REDACTED]` placeholders.
