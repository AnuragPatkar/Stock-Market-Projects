from flask import Flask, render_template, request, redirect, url_for, flash
import yfinance as yf
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' # Needed for flash messages

# --- Context Processor for Global Variables ---
@app.context_processor
def inject_global_vars():
    return {'now': datetime.now()}

# Nifty 50 stocks with sectors (Ensure this list is complete and correct in your app.py)
NIFTY_50 = [
    {"symbol": "RELIANCE.NS", "name": "Reliance Industries", "sector": "Oil & Gas"},
    {"symbol": "TCS.NS", "name": "Tata Consultancy Services", "sector": "IT"},
    {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "sector": "Banking"},
    {"symbol": "ICICIBANK.NS", "name": "ICICI Bank", "sector": "Banking"},
    {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever", "sector": "FMCG"},
    {"symbol": "INFY.NS", "name": "Infosys", "sector": "IT"},
    {"symbol": "ITC.NS", "name": "ITC", "sector": "FMCG"},
    {"symbol": "SBIN.NS", "name": "State Bank of India", "sector": "Banking"},
    {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel", "sector": "Telecom"},
    {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank", "sector": "Banking"},
    {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance", "sector": "Financial Services"},
    {"symbol": "LICI.NS", "name": "LIC India", "sector": "Insurance"},
    {"symbol": "LT.NS", "name": "Larsen & Toubro", "sector": "Construction"},
    {"symbol": "HCLTECH.NS", "name": "HCL Technologies", "sector": "IT"},
    {"symbol": "ASIANPAINT.NS", "name": "Asian Paints", "sector": "Consumer Goods"},
    {"symbol": "AXISBANK.NS", "name": "Axis Bank", "sector": "Banking"},
    {"symbol": "MARUTI.NS", "name": "Maruti Suzuki", "sector": "Automobile"},
    {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma", "sector": "Pharma"},
    {"symbol": "TITAN.NS", "name": "Titan Company", "sector": "Consumer Goods"},
    {"symbol": "DMART.NS", "name": "Avenue Supermarts", "sector": "Retail"},
    {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement", "sector": "Cement"},
    {"symbol": "BAJAJFINSV.NS", "name": "Bajaj Finserv", "sector": "Financial Services"},
    {"symbol": "WIPRO.NS", "name": "Wipro", "sector": "IT"},
    {"symbol": "ADANIENT.NS", "name": "Adani Enterprises", "sector": "Conglomerate"},
    {"symbol": "ONGC.NS", "name": "ONGC", "sector": "Oil & Gas"},
    {"symbol": "NTPC.NS", "name": "NTPC", "sector": "Power"},
    {"symbol": "JSWSTEEL.NS", "name": "JSW Steel", "sector": "Metals"},
    {"symbol": "POWERGRID.NS", "name": "Power Grid Corp", "sector": "Power"},
    {"symbol": "M&M.NS", "name": "Mahindra & Mahindra", "sector": "Automobile"},
    {"symbol": "COALINDIA.NS", "name": "Coal India", "sector": "Mining"},
    {"symbol": "TATASTEEL.NS", "name": "Tata Steel", "sector": "Metals"},
    {"symbol": "HINDALCO.NS", "name": "Hindalco", "sector": "Metals"},
    {"symbol": "DIVISLAB.NS", "name": "Divis Labs", "sector": "Pharma"},
    {"symbol": "SBILIFE.NS", "name": "SBI Life Insurance", "sector": "Insurance"},
    {"symbol": "GRASIM.NS", "name": "Grasim", "sector": "Cement"},
    {"symbol": "ADANIPORTS.NS", "name": "Adani Ports", "sector": "Infrastructure"},
    {"symbol": "TECHM.NS", "name": "Tech Mahindra", "sector": "IT"},
    {"symbol": "BRITANNIA.NS", "name": "Britannia", "sector": "FMCG"},
    {"symbol": "EICHERMOT.NS", "name": "Eicher Motors", "sector": "Automobile"},
    {"symbol": "HEROMOTOCO.NS", "name": "Hero MotoCorp", "sector": "Automobile"},
    {"symbol": "DRREDDY.NS", "name": "Dr Reddy's", "sector": "Pharma"},
    {"symbol": "CIPLA.NS", "name": "Cipla", "sector": "Pharma"},
    {"symbol": "BPCL.NS", "name": "BPCL", "sector": "Oil & Gas"},
    {"symbol": "SHREECEM.NS", "name": "Shree Cement", "sector": "Cement"},
    {"symbol": "INDUSINDBK.NS", "name": "IndusInd Bank", "sector": "Banking"},
    {"symbol": "HDFCLIFE.NS", "name": "HDFC Life Insurance", "sector": "Insurance"},
    {"symbol": "APOLLOHOSP.NS", "name": "Apollo Hospitals", "sector": "Healthcare"},
    {"symbol": "BAJAJ-AUTO.NS", "name": "Bajaj Auto", "sector": "Automobile"},
    {"symbol": "TATACONSUM.NS", "name": "Tata Consumer", "sector": "FMCG"},
    {"symbol": "NESTLEIND.NS", "name": "Nestle India", "sector": "FMCG"}
]

SECTORS = sorted(list(set(stock["sector"] for stock in NIFTY_50)))

def fetch_stock_data(symbol):
    """
    Fetches stock data from Yahoo Finance for a given symbol.
    Includes current price, moving averages, and key fundamental ratios.
    Handles potential data fetching errors gracefully.
    """
    try:
        stock = yf.Ticker(symbol)
        # Fetch 1 year of historical data for moving averages
        hist = stock.history(period="1y")
        
        if hist.empty:
            print(f"No historical data found for {symbol}")
            return None
            
        # Calculate moving averages
        ma_50 = hist['Close'].rolling(window=50).mean().iloc[-1]
        ma_200 = hist['Close'].rolling(window=200).mean().iloc[-1]
        
        # Fetch comprehensive stock info
        info = stock.info
        
        # Extract data, providing defaults if a key is missing
        return {
            "symbol": symbol.replace(".NS", ""), # Remove .NS for cleaner display
            "full_symbol": symbol, # Keep full symbol for yfinance in detail page for lookup
            "name": info.get('shortName', symbol.replace(".NS", "")),
            "current_price": info.get('currentPrice', hist['Close'].iloc[-1]),
            "ma_50": ma_50,
            "ma_200": ma_200,
            # Ensure PE and Debt/Equity are handled if not present or are zero/negative
            "pe_ratio": info.get('trailingPE', info.get('forwardPE', None)),
            "debt_equity": info.get('debtToEquity', None),
            "dividend_yield": info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
            "sector": info.get('sector', 'N/A'),
            "market_cap": info.get('marketCap', 'N/A'),
            "volume": info.get('volume', 'N/A'),
            "52_week_high": info.get('fiftyTwoWeekHigh', 'N/A'),
            "52_week_low": info.get('fiftyTwoWeekLow', 'N/A'),
            "beta": info.get('beta', 'N/A'),
            "currency": info.get('currency', 'N/A'),
            "exchange": info.get('exchange', 'N/A'),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def analyze_stock(stock_data):
    """
    Analyzes stock based on predefined technical and fundamental factors,
    assigning a score and a rating.
    """
    if not stock_data:
        return None
        
    technical_score = 0
    value_score = 0
    financial_health_score = 0
    income_score = 0
    
    # --- Technical analysis ---
    # Price vs. Moving Averages
    if stock_data['current_price'] is not None and stock_data['ma_50'] is not None and stock_data['ma_200'] is not None:
        if stock_data['current_price'] > stock_data['ma_50'] and stock_data['current_price'] > stock_data['ma_200']:
            technical_score += 2
        elif stock_data['current_price'] > stock_data['ma_50']:
            technical_score += 1
        elif stock_data['current_price'] < stock_data['ma_50'] and stock_data['current_price'] < stock_data['ma_200']:
            technical_score -= 2
    
    # Golden Cross
    if stock_data['ma_50'] is not None and stock_data['ma_200'] is not None and stock_data['ma_50'] > stock_data['ma_200']:
        technical_score += 1
    
    # --- Value analysis ---
    # P/E Ratio
    if stock_data['pe_ratio'] is not None and stock_data['pe_ratio'] > 0: # Ensure PE is positive and exists
        if stock_data['pe_ratio'] < 15:
            value_score += 2
        elif stock_data['pe_ratio'] < 25:
            value_score += 1
        elif stock_data['pe_ratio'] > 40:
            value_score -= 1
    
    # --- Financial health analysis ---
    # Debt to Equity Ratio
    if stock_data['debt_equity'] is not None: # Check for None
        if stock_data['debt_equity'] < 0.3:
            financial_health_score += 2
        elif stock_data['debt_equity'] < 0.7:
            financial_health_score += 1
        elif stock_data['debt_equity'] > 1.5:
            financial_health_score -= 2
    
    # --- Income analysis ---
    # Dividend Yield
    if stock_data['dividend_yield'] is not None:
        if stock_data['dividend_yield'] > 4.0:
            income_score += 2
        elif stock_data['dividend_yield'] > 2.0:
            income_score += 1
    
    total_score = technical_score + value_score + financial_health_score + income_score
    
    # Determine rating based on total score
    if total_score >= 5:
        rating = "Strong Buy"
    elif total_score >= 2:
        rating = "Moderate Buy"
    elif total_score >= -1: # Covers 1, 0, -1
        rating = "Hold"
    else:
        rating = "Sell"
    
    return {
        "rating": rating,
        "total_score": total_score,
        "technical_score": technical_score,
        "value_score": value_score,
        "financial_score": financial_health_score,
        "income_score": income_score,
        "analysis_date": datetime.now().strftime("%Y-%m-%d")
    }

# --- Flask Routes ---
@app.route('/')
def index():
    return render_template('index.html', stocks=NIFTY_50, sectors=SECTORS)

@app.route('/screen', methods=['POST'])
def screen():
    screen_type = request.form.get('screen_type')
    
    stocks_to_analyze = []
    if screen_type == 'all':
        stocks_to_analyze = NIFTY_50
    elif screen_type == 'sector':
        sector = request.form.get('sector')
        if not sector:
            flash('Please select a sector.', 'warning')
            return redirect(url_for('index'))
        stocks_to_analyze = [s for s in NIFTY_50 if s.get('sector') == sector]
        if not stocks_to_analyze:
            flash(f'No stocks found for the sector: {sector}.', 'info')
            return redirect(url_for('index'))
    else:
        flash('Invalid screening option selected.', 'danger')
        return redirect(url_for('index'))
    
    results = []
    for stock_info in stocks_to_analyze:
        # Pass the full symbol (e.g., RELIANCE.NS) to yfinance
        stock_data = fetch_stock_data(stock_info['symbol'])
        if stock_data:
            analysis = analyze_stock(stock_data)
            if analysis:
                results.append({**stock_data, **analysis})
        time.sleep(0.2) # Be gentle with the API to avoid being blocked
    
    # Sort by total score (highest first)
    results.sort(key=lambda x: x.get('total_score', 0), reverse=True)
    
    return render_template('results.html', results=results)

@app.route('/criteria')
def criteria():
    return render_template('criteria.html')

# The '/stock/<string:symbol>' route and stock_detail function are intentionally removed for modal approach

if __name__ == '__main__':
    # Set host to '0.0.0.0' to make it accessible from other devices on the network
    # For local development, '127.0.0.1' or just app.run(debug=True) is fine.
    app.run(debug=True, host='0.0.0.0')