# Nifty 50 Stock Screener
## 🚀 Project Overview
This is a Flask web application designed to help users screen and analyze Nifty 50 stocks. It fetches live financial data from Yahoo Finance to provide insights based on various technical and fundamental criteria.

## ✨ Key Features
- Stock Screening: Filter Nifty 50 stocks by "All Stocks" or by a specific "Sector."
- Automated Analysis: Stocks are rated as "Strong Buy," "Moderate Buy," "Hold," or "Sell" based on predefined criteria (Moving Averages, P/E Ratio, Debt/Equity, Dividend Yield).
- Interactive Results: View analysis in a sortable table with key metrics.
- Detailed View (Modal): Get a comprehensive financial breakdown of any stock in a convenient pop-up window directly on the results page.
- Rating Distribution Chart: A pie chart visually summarizes the distribution of ratings among screened stocks, including counts and percentages.
## 🛠️ Tech Stack
* Backend: Python, Flask, Yfinance
* Frontend: HTML, CSS (Bootstrap), JavaScript, Chart.js, chartjs-plugin-datalabels
## ⚡ Quick Setup & Run
* Clone: git clone [(https://github.com/AnuragPatkar/Stock-Market-Projects/tree/main/Project%203%20nifty50%20stock%20screener)]
* Install: pip install Flask yfinance
* Run: python app.py
* Access: Open http://127.0.0.1:5000 in your browser.