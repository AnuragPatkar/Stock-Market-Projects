"""
TRADING SINGLE GENERATOR
"""

def main():
    print("="*70)
    print("Trading Signal Generator")
    print("="*70)
    print("Enter the following metrics for your stock:")

    #Get user input for stock metrics
    symbol=input("Enter stock symbol:")
    current_price=float(input("Enter the Current price of stock:$"))
    ma_50=float(input("Enter 50 day moving average price:$"))
    ma_200=float(input("Enter 200 day moving average price:$"))
    rsi=float(input("Enter rsi value(1-100):"))
    volume=int(input("Enter current trading volume:"))
    avr_volume=int(input("Enter average trading volume:"))


    print("\nEnter Analyzing metric for",symbol,"...")
    print("-"*70)


    #check for golden cross and death cross
    golden_cross=ma_50>ma_200
    death_cross=ma_200>ma_50

    #calculate percentage difference
    price_vs_ma50_percent=((current_price-ma_50)/ma_50)*100
    price_vs_ma200_percent=((current_price-ma_200)/ma_200)*100
    volume_vs_avr_volume=((volume-avr_volume)/avr_volume)*100

    #print technical analysis
    print(f"Price vs 50-day MA:{price_vs_ma50_percent:.2f}")
    print(f"Price vs 200-day MA:{price_vs_ma200_percent:.2f}")
    print(f"Volume vs Average Volume:{volume_vs_avr_volume:.2f}")

    if golden_cross:
        print("Golden Cross Detected: 50-day MA above 200 day MA(Bullish)")
    elif death_cross:
        print("Death Cross Detected: 50-day MA below 200 day MA(Bearish)")
    else:
        print("No Cross Pattern Detected")

    #define signal generation rule
    buy_signal=False
    sell_signal=False
    hold_signal=True

    # Rule 1: Buy if price is above both moving averages and RSI is above 40 AND volume is above average
    if current_price>ma_50 and current_price>ma_200 and rsi>40 and volume>avr_volume:
        buy_signal=True
        hold_signal=False
        signal_reason="price is above both moving averages and RSI is above 40 AND volume is above average"

    # Rule 2: Sell if price is below both moving averages OR RSI is above 75
    elif (current_price < ma_50 and current_price < ma_200) or rsi > 75:
        sell_signal=True
        hold_signal=True
        if current_price < ma_50 and current_price < ma_200:
            signal_reason="Price is below both moving averages"
        elif rsi>75:
            signal_reason="RSI indicate overbought condition"
        else:
            signal_reason="Multiple Bearish Conditions Detected"

    # final output
    print("\n","="*70)
    print("TRADING Signal Recommendation for",symbol)
    print("="*70)

    if buy_signal:
        print("Recommandation : BUY")
        print(f"Reason:{signal_reason}")

        #Additional buy signal strength indicator
        if golden_cross:
            print("Signal Strengthened by Golden Cross Pattern")
        if volume > avr_volume * 1.5:
            print("Signal strengthened by significantly above-average volume")
        
    elif sell_signal:
        print("Recommandation : SELL")
        print(f"Reason: {signal_reason}")
        
        # Additional sell signal strength indicator
        if death_cross:
            print("Signal strengthened by Death Cross pattern")
        if rsi > 75:
            print("Signal Strengthened by strongly overbought conditions")

    else:
        print("RECOMMENDATION: HOLD")
        print("Reason: Mixed or neutral signals - no clear buy or sell indication")
        
        # Additional context for hold recommendation
        if current_price > ma_50 and current_price < ma_200:
            print("Price is between 50-day and 200-day moving averages")
        elif rsi > 40 and rsi < 60:
            print("RSI indicates neutral momentum")
            
    print("-" * 70)
    print("Note: This is a simplified analysis. Always consider other factors")
    print("before making trading decisions.")

if __name__=="__main__":
    main()
