import streamlit as st

st.title("📈 Trading Signal Generator")
st.markdown("Enter the following metrics for your stock:")

# Get input from user
symbol = st.text_input("Enter stock symbol:").upper( )
current_price = st.number_input("Enter Current Price ($)", step=0.01)
ma_50 = st.number_input("Enter 50-day Moving Average ($)", step=0.01)
ma_200 = st.number_input("Enter 200-day Moving Average ($)", step=0.01)
rsi = st.slider("Enter RSI Value (1-100)", min_value=1, max_value=100)
volume = st.number_input("Enter Current Trading Volume", step=1)
avr_volume = st.number_input("Enter Average Trading Volume", step=1)

if st.button("Generate Signal"):
    st.subheader(f"Analyzing Metrics for {symbol}")

    golden_cross = ma_50 > ma_200
    death_cross = ma_200 > ma_50

    price_vs_ma50_percent = ((current_price - ma_50) / ma_50) * 100
    price_vs_ma200_percent = ((current_price - ma_200) / ma_200) * 100
    volume_vs_avr_volume = ((volume - avr_volume) / avr_volume) * 100

    st.write(f"Price vs 50-day MA: `{price_vs_ma50_percent:.2f}%`")
    st.write(f"Price vs 200-day MA: `{price_vs_ma200_percent:.2f}%`")
    st.write(f"Volume vs Average Volume: `{volume_vs_avr_volume:.2f}%`")

    if golden_cross:
        st.success("Golden Cross Detected: Bullish Signal")
    elif death_cross:
        st.warning("Death Cross Detected: Bearish Signal")
    else:
        st.info("No Cross Pattern Detected")

    # Signal Rules
    buy_signal = False
    sell_signal = False
    hold_signal = True

    if current_price > ma_50 and current_price > ma_200 and rsi > 40 and volume > avr_volume:
        buy_signal = True
        hold_signal = False
        signal_reason = "Price > MAs, RSI > 40, Volume > Average"
    elif (current_price < ma_50 and current_price < ma_200) or rsi > 75:
        sell_signal = True
        signal_reason = "Price < MAs or RSI > 75"

    st.divider()
    st.header(f"📊 Trading Recommendation for {symbol}")

    if buy_signal:
        st.markdown("### ✅ Recommendation: **BUY**")
        st.markdown(f"**Reason:** {signal_reason}")
        if golden_cross:
            st.info("Signal Strengthened by Golden Cross")
        if volume > avr_volume * 1.5:
            st.info("High Volume Boosts Buy Signal")

    elif sell_signal:
        st.markdown("### ❌ Recommendation: **SELL**")
        st.markdown(f"**Reason:** {signal_reason}")
        if death_cross:
            st.info("Signal Strengthened by Death Cross")
        if rsi > 75:
            st.info("Overbought RSI > 75")

    else:
        st.markdown("### 🟡 Recommendation: **HOLD**")
        st.markdown("Reason: Mixed or neutral signals")
        if current_price > ma_50 and current_price < ma_200:
            st.info("Price is between MAs")
        elif 40 < rsi < 60:
            st.info("RSI shows neutral momentum")

    st.warning("Note: This is a simplified analysis. Always do further research!")

