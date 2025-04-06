import sys
import pyperclip
import json
import os

# File to store clipboard data
CLIPBOARD_FILE = "clipboard.json"

def save_clipboard_data(data):
    with open(CLIPBOARD_FILE, 'w') as file:
        json.dump(data, file)

def load_clipboard_data():
    if os.path.exists(CLIPBOARD_FILE):
        with open(CLIPBOARD_FILE, 'r') as file:
            return json.load(file)
    return {}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [save|load|list] [key]")
        sys.exit(1)

    command = sys.argv[1]
    clipboard_data = load_clipboard_data()

    if command == "save":
        if len(sys.argv) < 3:
            print("Usage: python main.py save [key]")
            sys.exit(1)
        key = sys.argv[2]
        clipboard_data[key] = pyperclip.paste()
        save_clipboard_data(clipboard_data)
        print(f"Saved clipboard content to key '{key}'.")

    elif command == "load":
        if len(sys.argv) < 3:
            print("Usage: python main.py load [key]")
            sys.exit(1)
        key = sys.argv[2]
        if key in clipboard_data:
            pyperclip.copy(clipboard_data[key])
            print(f"Loaded content from key '{key}' to clipboard.")
        else:
            print(f"Key '{key}' not found.")

    elif command == "list":
        if clipboard_data:
            print("Saved keys:")
            for key in clipboard_data:
                print(f"- {key}")
        else:
            print("No saved keys.")

    else:
        print("Invalid command. Use 'save', 'load', or 'list'.")

if __name__ == "__main__":
    main()

# This script allows you to save, load, and list clipboard contents using keys.
# Usage:

