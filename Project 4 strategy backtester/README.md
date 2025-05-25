# Trading Strategy Backtester

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.16.1-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A web-based application for backtesting moving average crossover trading strategies with comprehensive performance analysis.

## ✨ Features

- **Interactive Web Interface:** Modern, responsive design
- **Strategy Customization:** Adjust all trading parameters
- **Real-time Visualization:** Interactive charts
- **Performance Metrics:** Detailed trade analysis
- **Educational Tool:** Learn algorithmic trading concepts

## 📋 Prerequisites

- Python 3.7+
- Flask 2.3.3+
- NumPy 1.25.2+
- pandas 2.1.0+
- Plotly 5.16.1+

##🔍 Usage
1) Configure Strategy Parameters

* Set the number of days to simulate

* Adjust price volatility and starting price

* Choose between Simple and Exponential Moving Averages

* Set short-term and long-term MA periods

* Configure initial capital and stop-loss percentage

2) Run the Backtest

* Click "Run Backtest" to execute the simulation

* View the results in the interactive dashboard

3) Analyze Performance

* Review metrics like total return, win rate, and drawdown

* Examine trade history and signals

* Visualize price and portfolio performance

## 📊 Technical Overview
This project utilizes basic programming concepts such as:

* Conditional Statements: for decision-making

* Loops: to simulate market activity

* Logical Operators: for signal generation

* Nested Control Structures: for complex trade conditions

The application architecture includes:

* Flask Backend: Handles logic and routes

* Plotly Visualizations: For dynamic charts

* Bootstrap Frontend: For user-friendly layout

## 🔧 Extending the Project
This project can be expanded in many ways:

1) Add New Strategy Types

* Include technical indicators like RSI, MACD, or Bollinger Bands

2) Connect to Real Market Data

* Use APIs to download actual historical price data

3) Optimize Strategy Parameters

* Implement grid search or walk-forward testing

4) Advanced Risk Management

* Add trailing stops, dynamic position sizing, and risk control mechanisms
