# Programming in Python - Elective

This repository contains Python practice programs and mini projects created for the Semester 6 Python elective. The code is organized by topic, moving from core Python basics to GUI programming, file handling, object-oriented programming, Turtle graphics, and OpenCV image processing.

## What's Inside

| Folder               | Contents                                                                                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `Programs/`          | General Python exercises such as leap year checking, palindrome logic, expression evaluation, scope examples, and math programs. |
| `Strings/`           | String operations including slicing, case conversion, replacement, splitting/joining, counting, and validation methods.          |
| `Lists/`             | List operations such as adding, removing, extending, searching, sorting, copying, and repetition.                                |
| `tuple/`             | Tuple basics, tuple methods, and tuple-related practice programs.                                                                |
| `Sets/`              | Basic set operations in Python.                                                                                                  |
| `Dictionary/`        | Dictionary activities and nested dictionary examples.                                                                            |
| `Date_Time/`         | Date formatting, date/time usage, and date arithmetic.                                                                           |
| `ExceptionHandling/` | `try-except`, `else`, `finally`, custom exceptions, and error-handling examples.                                                 |
| `FileHandling/`      | Reading, writing, copying, and modifying file contents.                                                                          |
| `Oops/`              | Object-oriented programming concepts including inheritance, polymorphism, encapsulation, abstract methods, and dunder methods.   |
| `Tkinter/`           | GUI programs built with Python's built-in Tkinter library.                                                                       |
| `BreezyPythonGui/`   | GUI examples using the `breezypythongui` package, including a calculator and unit converter.                                     |
| `Turtle/`            | Turtle graphics drawings and level-based drawing programs.                                                                       |
| `OpenCV/`            | Image processing examples such as grayscale conversion, borders, blurring, and image augmentation.                               |

## Requirements

Most programs only need Python 3.

Some folders need extra libraries:

- `Tkinter/`: Tkinter is included with most standard Python installations.
- `BreezyPythonGui/`: requires `breezypythongui`.
- `OpenCV/`: requires `opencv-python`.

Install the optional dependencies with:

```bash
pip install breezypythongui opencv-python
```

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd Elective_S6
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install optional dependencies if you want to run the GUI and OpenCV examples:

```bash
pip install breezypythongui opencv-python
```

## Running Programs

Run any script from the repository root using:

```bash
python path/to/script.py
```

Examples:

```bash
python Programs/leapYear.py
python Strings/reverse_string.py
python Tkinter/q2.py
python BreezyPythonGui/converter.py
```

For OpenCV scripts, run them from inside the `OpenCV/` folder when they use local image files:

```bash
cd OpenCV
python imageAugmentation.py
```

## Notes

- GUI programs open separate windows, so they should be run in a desktop environment.
- OpenCV examples may require image files from the `OpenCV/` folder.
- This repository is mainly for learning and practice, so files are grouped by concept rather than packaged as a single application.

## Suggested Learning Path

1. Start with `Programs/`, `Strings/`, `Lists/`, `tuple/`, `Sets/`, and `Dictionary/`.
2. Move to `Date_Time/`, `FileHandling/`, and `ExceptionHandling/`.
3. Practice OOP concepts in `Oops/`.
4. Explore GUI programming with `Tkinter/` and `BreezyPythonGui/`.
5. Try visual programming examples in `Turtle/` and image processing in `OpenCV/`.

## Author: Ash

Maintained as part of the Python elective coursework.
