Black-Scholes Option Pricing Calculator
This is a simple Streamlit application that calculates the price of European options (Call and Put) using the Black-Scholes model and also computes the associated "Greeks" (Delta, Gamma, Theta, Vega, and Rho).

📊 About the Black-Scholes Model
The Black-Scholes model is a mathematical model for the dynamics of a financial market containing derivative investment instruments. From the model, one can deduce the Black-Scholes formula, which gives a theoretical estimate of the price of European-style options.

✨ Features
Option Pricing: Calculates the theoretical price for both Call and Put options.

Greeks Calculation: Provides key risk measures:

Δ (Delta): Measures the sensitivity of the option's price to a change in the underlying asset's price.

Γ (Gamma): Measures the rate of change of Delta with respect to a change in the underlying asset's price.

Θ (Theta): Measures the sensitivity of the option's price to the passage of time (time decay).

ν (Vega): Measures the sensitivity of the option's price to changes in the volatility of the underlying asset.

ρ (Rho): Measures the sensitivity of the option's price to a change in the risk-free interest rate.

🚀 How to Run
Follow these steps to get the application up and running on your local machine.

Prerequisites
Make sure you have Python installed on your system (Python 3.7+ is recommended).

Running the Application
Once the dependencies are installed and the virtual environment is activated, run the Streamlit app:

streamlit run app.py


This command will open a new tab in your web browser with the Black-Scholes Option Pricing Calculator.

👨‍💻 Usage
Input Parameters: On the left sidebar (or main area, depending on layout), you will see input fields for:

Spot Price (S): Current price of the underlying asset.

Strike Price (K): Price at which the option can be exercised.

Time to Expiry (T): Time remaining until the option expires, in years.

Risk Free Interest Rate (r): The annual risk-free interest rate.

Volatility (σ): The standard deviation of the underlying asset's returns.

Calculate: After entering all the parameters, click the "Calculate" button.

View Results: The application will display the calculated price for both Call and Put options, along with their respective Greeks.

📜 Black-Scholes Formulas (Simplified) and Calculation Details
The core of the calculation uses the Black-Scholes formula:

For a Call Option:
C=SN(d 
1
​
 )−Ke 
−rT
 N(d 
2
​
 )

For a Put Option:
P=Ke 
−rT
 N(−d 
2
​
 )−SN(−d 
1
​
 )

Where:
d 
1
​
 = 
σ 
T
​
 
ln(S/K)+(r+σ 
2
 /2)T
​
 
d 
2
​
 =d 
1
​
 −σ 
T
​
 

And N(x) is the cumulative standard normal distribution function.

The "Greeks" are calculated based on these parameters and the intermediate values d 
1
​
  and d 
2
​
 :

Delta (Δ):

Call: N(d 
1
​
 )

Put: N(d 
1
​
 )−1 (or −N(−d 
1
​
 ))

Gamma (Γ):

Sσ 
T
​
 
N 
′
 (d 
1
​
 )
​
  where N 
′
 (x) is the standard normal probability density function.

Theta (Θ):

Call: − 
2 
T
​
 
SN 
′
 (d 
1
​
 )σ
​
 −rKe 
−rT
 N(d 
2
​
 )

Put: − 
2 
T
​
 
SN 
′
 (d 
1
​
 )σ
​
 +rKe 
−rT
 N(−d 
2
​
 )

Vega (ν):

SN 
′
 (d 
1
​
 ) 
T
​
  (often divided by 100 as it's sensitivity per 1% change in volatility)

Rho (ρ):

Call: KTe 
−rT
 N(d 
2
​
 ) (often divided by 100 as it's sensitivity per 1% change in interest rate)

Put: −KTe 
−rT
 N(−d 
2
​
 ) (often divided by 100 as it's sensitivity per 1% change in interest rate)

🤝 Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

📄 License
This project is open-source and available under the MIT License.
