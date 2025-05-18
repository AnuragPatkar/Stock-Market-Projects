# Stock Portfolio Calculator
Python Status License Beginner Friendly

A beginner-friendly Python program that tracks stock portfolio performance and calculates key metrics. This project demonstrates fundamental Python concepts.

🌟 Features
Track multiple stock positions (symbol, purchase price, current price, shares)
Calculate current value, profit/loss in dollars, and percentage returns
Generate a complete portfolio summary with overall performance metrics
Beginner-friendly implementation using only basic Python concepts
Visual indicators (emojis) to easily identify profitable positions


📋 Prerequisites
Python 3.6 or higher (for local installation)
No external libraries required - uses only Python standard library
No programming experience required!

💻 Local Installation
If you prefer to run the program on your own computer:

Install Python:

Download and install Python from python.org
Make sure to check "Add Python to PATH" during installation (Windows)
Download the Code:

Download the portfolio_calculator.py file from this repository
Or create a new file and copy-paste the code
Run the Program:

Open a terminal/command prompt
Navigate to the folder containing the file
Run: python stock_portfolio.py (or python3 portfolio_calculator.py on Mac/Linux)
Follow the prompts to enter your stock information
🎓 Educational Value
This project demonstrates several fundamental Python concepts:

Variables and Data Types: Using strings, integers, and floats
Lists: Storing collections of related data
Input/Output: Getting user input and displaying formatted results
Arithmetic Operations: Calculating financial metrics
Conditional Logic: Determining portfolio performance status
Loops: Processing multiple stock positions
It's an excellent starting point for beginners interested in financial applications of Python.

📊 Example Output
===== STOCK PORTFOLIO SUMMARY CALCULATOR =====
Enter details for your stock positions below:

Stock #1:
Enter stock symbol (e.g., SBIN): SBIN
Enter purchase price per share: $150
Enter current price per share: $175.25
Enter number of shares: 10

... (additional stocks) ...

============================================================
📊 STOCK PORTFOLIO SUMMARY 📊
============================================================

📈 INDIVIDUAL STOCK PERFORMANCE:
------------------------------------------------------------
SYMBOL   SHARES   PURCHASE    CURRENT     VALUE        P/L($)        P/L(%)    
------------------------------------------------------------
AAPL     10       $150.00     $175.25     $1752.50     $252.50       16.83%    🟢
MSFT     5        $250.00     $265.75     $1328.75     $78.75        6.30%     🟢
GOOGL    2        $2500.00    $2450.50    $4901.00     $-199.00      -2.00%    🔴

💼 PORTFOLIO SUMMARY:
------------------------------------------------------------
Total Investment: $5750.00
Current Portfolio Value: $7982.25
Overall Profit/Loss: $132.25 (2.30%) 🟢

🎉 Your portfolio is performing well with positive returns!
