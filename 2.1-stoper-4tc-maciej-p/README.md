# ⏱ Stoper

A simple desktop stopwatch application built with **Python** and **tkinter**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

---

## Features

- **Start** – begins or resumes the timer
- **Stop** – pauses the timer (keeps elapsed time)
- **Reset** – sets everything back to `00:00:00.000`
- Millisecond-precision display refreshing at ~30 fps
- Dark colour theme

---

## Requirements

| Requirement | Details |
|-------------|---------|
| **Python**  | 3.8 or newer |
| **tkinter** | Included with the standard Python installer on Windows. On Linux run `sudo apt install python3-tk`. |

> No extra packages to install – only the Python standard library is used.

---

## How to open / run

### Windows

1. Open **File Explorer** and navigate to this folder.
2. Double-click **`stoper.py`** – the app should open automatically if Python is installed.

   *Alternatively*, open a terminal (Command Prompt or PowerShell) in this folder and run:

   ```
   python stoper.py
   ```

### macOS / Linux

Open a terminal in this folder and run:

```bash
python3 stoper.py
```

---

## Project structure

```
.
├── stoper.py   # main application
└── README.md   # this file
```

---

## License

Free to use for educational purposes.
