This is a Python program I developed for my Comp-Sci 101 course that reads and analyzes a CSV file of video game transactions. It cleans the data, filters out invalid rows, calculates total and average spending, identifies top-selling games and the highest-spending customer, and marks each game’s popularity tier based on quantity sold. The program uses a simple menu to let the user view summary stats, see top games and top customer, and export the processed data to a new CSV file. :contentReference[oaicite:1]{index=1}

## Features

- Prompts for a CSV filename and validates it before reading  
- Uses `csv.DictReader` to process transaction records  
- Skips invalid or malformed rows with clear error messages instead of crashing  
- Computes total revenue and average transaction value  
- Finds the top 3 best-selling games by sales amount  
- Finds the highest-spending customer  
- Marks each transaction with a popularity label based on quantity sold  
- Lets the user save cleaned, annotated data to a new `processed_*.csv` file via a menu

## Requirements

- Python 3.x  
- Standard library only (`csv`, no external dependencies)

## Expected CSV format

The input file should be a CSV with headers similar to:

- `TransactionID`  
- `Date`  
- `Customer`  
- `GameTitle`  
- `Platform`  
- `Genre`  
- `Price`  
- `Quantity`  
- `PaymentMethod`

The program calculates an `Amount` field for each valid transaction.

## How to run

1. Make sure your CSV file is in the same directory as the script.
2. Run the program from the terminal:

   ```bash
   python Program4.py
