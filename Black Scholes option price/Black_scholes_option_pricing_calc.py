import streamlit as st
import numpy as np
from scipy.stats import norm


## Black-Scholes Function

# S-Spot Price	
# K-Strike Price
# T-Time to Expiry (in years)	
# r-Risk-Free Rate	
# sigma-Volatility	
# option_type-Call ya Put
def black_scholes_price(S,K,T,r,sigma,option_type):
    d1=(np.log(S/K) + (r + 0.5*sigma**2)*T)/(sigma * np.sqrt(T))
    d2=d1-sigma*(np.sqrt(T))

    if option_type=='Call':
        price= S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type=='Put':
        price=  K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        print("Give all parameter correctly")
        return None,None,None

    return price,d1,d2

#Greek Calculation
def calculate_greek(S, K, T, r, sigma, option_type):
    _, d1, d2 = black_scholes_price(S, K, T, r, sigma, option_type)

    delta=norm.cdf(d1) if option_type=='Call' else -norm.cdf(-d1)
    gamma=norm.pdf(d1) / (S * sigma *np.sqrt(T))
    theta_call=(-S *norm.pdf(d1) * sigma / (2 * np.sqrt(T))) - r * K *np.exp(-r * T) * norm.cdf(d2)
    theta_put=(-S *norm.pdf(d1) * sigma / (2 * np.sqrt(T))) + r * K *np.exp(-r * T) * norm.cdf(-d2)
    theta = theta_call if option_type == 'Call' else theta_put

    vega= S * norm.pdf(d1) *np.sqrt(T)/100
    rho_call= K * T * np.exp(-r * T) * norm.cdf(d2)/100
    rho_put= -K * T * np.exp(-r * T) * norm.cdf(-d2)/100
    rho =rho_call if option_type=='Call' else rho_put

    return delta,gamma,theta,vega,rho



## Streamlit UI
st.set_page_config(page_title="Black-Scholes Calculator",layout="centered")
st.title("Black-Scholes Option Pricing Calculator")
S = st.number_input("Spot Price(S)",value=100.0,format="%.2f")
K = st.number_input("Strike Price(K)",value=100.0,format="%.2f")
T = st.number_input("Time to Expiry(T)",value=0.5,format="%.2f")
r = st.number_input("Risk Free Interest Rate(r)",value=0.05,format="%.4f")
sigma = st.number_input("Volatility (σ)",value=0.2,format="%0.4f")

if st.button("Calculate"):
    for option_type in ['Call','Put']:
        st.subheader(f"{option_type.capitalize()} Option")
        price,_,_ = black_scholes_price(S,K,T,r,sigma,option_type)
        delta, gamma, theta, vega, rho = calculate_greek(S, K, T, r, sigma, option_type)

        st.write(f"**Price:** ₹ {price:.2f}")
        st.markdown("**Greeks:**")
        st.write(f"🔹 Delta: {delta:.4f}")
        st.write(f"🔹 Gamma: {gamma:.4f}")
        st.write(f"🔹 Theta: {theta:.4f}")
        st.write(f"🔹 Vega: {vega:.4f}")
        st.write(f"🔹 Rho: {rho:.4f}")
else:
    st.info("Please enter parameters and click 'Calculate'.")
