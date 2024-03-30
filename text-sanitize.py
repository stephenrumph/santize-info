import tkinter as tk
from tkinter import scrolledtext, ttk  # Use ttk for themed widgets
import re

# Initialize the application's main window
window = tk.Tk()
window.title("Input Sanitizer")
window.geometry('1200x600')  # Adjust size to accommodate side-by-side frames comfortably

# Apply a theme for ttk widgets and configure styles
style = ttk.Style()
style.theme_use('classic')  # 'clam' theme for a modern look. Adjust based on your OS and preferences.

# Configure styles for ttk widget types
style.configure('TLabel', font=('Helvetica', 15), background='#f0f0f0')
style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#333333')
style.configure('TFrame', background='#f0f0f0')
style.configure('TScrolledText', font=('Helvetica', 14))  # This line might need adjustment

# Define the sanitize input function with detailed regex patterns
def sanitize_input():
    text = input_text_box.get("1.0", tk.END)
    # Sanitization logic
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    text = re.sub(ip_pattern, '[REDACTED IP]', text)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    text = re.sub(email_pattern, '[REDACTED EMAIL]', text)
    api_key_pattern = r'\b(token|key)-[\w-]+\b'
    text = re.sub(api_key_pattern, '[REDACTED API]', text)
    server_name_pattern = r'\bserver[\w.-]+\b'
    text = re.sub(server_name_pattern, '[REDACTED SERVER]', text)
    password_pattern = r'("password"\s*:\s*)"[^"]+"'
    text = re.sub(password_pattern, r'\1 [REDACTED]', text)
    access_code_pattern = r'\b(vpn-access|access-code|updater-key|auth-token)-[\w\d]+\b'
    text = re.sub(access_code_pattern, '[REDACTED ACCESS CODE]', text)
    phone_pattern = r'\+\d{1,3}[-\s]?\(?\d{1,3}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}'
    text = re.sub(phone_pattern, '[REDACTED PHONE]', text)

    url_pattern = r'\b[\w.-]+\.[a-zA-Z]{2,}(?::\d+)?\b'
    text = re.sub(url_pattern, '[REDACTED URL]', text)
    # Display the sanitized text
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.INSERT, text)

# Main frame for layout management
main_frame = ttk.Frame(window)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Input Frame configuration
input_frame = ttk.Frame(main_frame, padding="10")
input_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=5, pady=5)

input_label = ttk.Label(input_frame, text="Input Text")
input_label.pack(fill='x', padx=5, pady=5)

input_text_box = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD)
input_text_box.pack(expand=True, fill='both', padx=5, pady=5)

# Output Frame configuration
output_frame = ttk.Frame(main_frame, padding="10")
output_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=5, pady=5)

output_label = ttk.Label(output_frame, text="Sanitized Text")
output_label.pack(fill='x', padx=5, pady=5)

output_text_box = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD)
output_text_box.pack(expand=True, fill='both', padx=5, pady=5)

# Sanitize Button configuration
sanitize_button = ttk.Button(window, text="Sanitize", command=sanitize_input)
sanitize_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
