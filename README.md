# 🎯 Number Guessing Game

A simple Python guessing game where the player tries to guess a randomly generated number between 1 and 100.

This project is beginner-friendly and helps practice:

- ✅ Loops
- ✅ Conditional Statements
- ✅ Exception Handling
- ✅ Random Module
- ✅ User Input
- ✅ Game Logic

---

# 📌 Features

- Random number generation
- User input validation
- Limited attempts system
- Exit option
- Hint system:
  - Too high
  - Too low
- Error handling using `try-except`

---

# ▶️ How To Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## 2️⃣ Open Project Folder

```bash
cd your-repository-name
```

## 3️⃣ Run Program

```bash
python main.py
```
---

# 🧪 Example Output

```bash
Guess No or Exit(E) : 40
Attempts : 1
You entered too small number. Try a bigger number.

Guess No or Exit(E) : 70
Attempts : 2
You entered too big number. Try a smaller number.

Guess No or Exit(E) : 55
You guessed the number successfully.
```

---

# 📚 Concepts Used

| Concept | Description |
|---|---|
| `while loop` | Repeats game until user wins or exits |
| `if-elif-else` | Checks conditions |
| `random` module | Generates random number |
| `try-except` | Handles invalid input |
| `break` | Stops loop |

---

# 🚀 Future Improvements

You can improve this project by adding:

- Difficulty Levels
- Score System
- Multiplayer Mode
- GUI using Tkinter
- Sound Effects
- Timer Mode

---

# 👨‍💻 Author

**Wajid Ali**

Python Beginner Developer 🚀

---
Create a cross-platform command-line bulk file renaming tool in Python that works on Windows, Linux, and macOS terminals. The application should help users quickly rename large numbers of files using different customizable renaming methods while maintaining a simple and user-friendly CLI experience.
Main Features
Rename multiple files in a selected folder at once
Add prefixes or suffixes to filenames
Automatically number files sequentially
Find and replace specific text in filenames
Convert filenames to lowercase, uppercase, or title case
Change file extensions (e.g. .jpeg to .jpg)
Rename only specific file types if needed
Support recursive renaming inside subfolders (optional)
User Experience
Show a preview of filename changes before renaming
Ask for confirmation before applying changes
Display clear success and error messages
Handle duplicate filenames safely to avoid overwriting files
Optionally provide undo functionality to restore original names
Technical Requirements
Built entirely in Python
Works in Windows Command Prompt, Linux Terminal, and macOS Terminal
Use standard libraries such as:
pathlib
argparse
os
json
Follow clean and modular code structure
Include proper error handling for invalid paths or permission issues
Example Usage
Bash
python bulkrename.py --prefix vacation_
Bash
python bulkrename.py --replace IMG Photo
Bash
python bulkrename.py --number 001
Learning Goals
This project should help improve skills in:
File handling
Command-line interface development
Python scripting
Cross-platform compatibility
Error handling and validation
Writing clean and maintainable code
