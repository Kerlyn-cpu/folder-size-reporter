# Directory File Size Reporter

## Description
A system administration script that scans specific folders in the user's home directory, calculates the size of every file, and exports a detailed report to a CSV file on the Desktop.

## Features
- Accepts multiple folder names separated by commas.
- Uses `pathlib.rglob()` to search through directories.
- Calculates file sizes and converts them to Megabytes (MB).
- Exports the final report to `file_report.csv`.

## Technologies Used
- Python 3
- `pathlib` module
- `csv` module

## How to Run
1. Run the script:
   `python3 File_Reporter.py`
2. Enter the folder names you want to scan (e.g., `Downloads, Documents`).
3. Check your Desktop for the generated `file_report.csv` file.
