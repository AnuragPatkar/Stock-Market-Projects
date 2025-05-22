# Black-Scholes Option Pricing Calculator
This is a simple Streamlit application that calculates the price of European options (Call and Put) using the Black-Scholes model and also computes the associated "Greeks" (Delta, Gamma, Theta, Vega, and Rho).

## 📊 About the Black-Scholes Model
The Black-Scholes model is a mathematical model for the dynamics of a financial market containing derivative investment instruments. From the model, one can deduce the Black-Scholes formula, which gives a theoretical estimate of the price of European-style options.

## ✨ Features
Option Pricing: Calculates the theoretical price for both Call and Put options.

### Greeks Calculation: Provides key risk measures:

* Δ (Delta): Measures the sensitivity of the option's price to a change in the underlying asset's price.

* Γ (Gamma): Measures the rate of change of Delta with respect to a change in the underlying asset's price.

* Θ (Theta): Measures the sensitivity of the option's price to the passage of time (time decay).

* ν (Vega): Measures the sensitivity of the option's price to changes in the volatility of the underlying asset.

* ρ (Rho): Measures the sensitivity of the option's price to a change in the risk-free interest rate.

## 👨‍💻 Usage
Input Parameters: On the left sidebar (or main area, depending on layout), you will see input fields for:

* Spot Price (S): Current price of the underlying asset.

* Strike Price (K): Price at which the option can be exercised.

* Time to Expiry (T): Time remaining until the option expires, in years.

* Risk Free Interest Rate (r): The annual risk-free interest rate.

* Volatility (σ): The standard deviation of the underlying asset's returns.

* Calculate: After entering all the parameters, click the "Calculate" button.

View Results: The application will display the calculated price for both Call and Put options, along with their respective Greeks.

# Black-Scholes Option Pricing Model

## Core Formulas

### Call Option Price
\[ C = S N(d_1) - K e^{-rT} N(d_2) \]

### Put Option Price
\[ P = K e^{-rT} N(-d_2) - S N(-d_1) \]

### Intermediate Calculations
\[ d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}} \]
\[ d_2 = d_1 - \sigma \sqrt{T} \]

Where:
- \( S \) = Current stock price
- \( K \) = Strike price
- \( T \) = Time to expiration (in years)
- \( r \) = Risk-free interest rate
- \( \sigma \) = Volatility of the underlying asset
- \( N(x) \) = Cumulative standard normal distribution function

## Option Greeks

### Delta (Δ)
- **Call**: \( N(d_1) \)
- **Put**: \( N(d_1) - 1 \) (or \( -N(-d_1) \))

### Gamma (Γ)
\[ \Gamma = \frac{N'(d_1)}{S \sigma \sqrt{T}} \]
Where \( N'(x) \) is the standard normal probability density function.

### Theta (Θ)
- **Call**: 
  \[ -\frac{S N'(d_1) \sigma}{2 \sqrt{T}} - r K e^{-rT} N(d_2) \]
- **Put**: 
  \[ -\frac{S N'(d_1) \sigma}{2 \sqrt{T}} + r K e^{-rT} N(-d_2) \]

### Vega (ν)
\[ \nu = S N'(d_1) \sqrt{T} \]
*Note: Often divided by 100 to represent sensitivity per 1% change in volatility*

### Rho (ρ)
- **Call**: 
  \[ K T e^{-rT} N(d_2) \]
- **Put**: 
  \[ -K T e^{-rT} N(-d_2) \]
*Note: Often divided by 100 to represent sensitivity per 1% change in interest rate*

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests.
