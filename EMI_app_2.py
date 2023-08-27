import streamlit as st 
def calculate_emi(p, n, r):
	emi=p*(r/100)*(1 + r/100)**n/((1+r/100)**n -1)
	st.write("EMI Calculated: ", emi)
def outstanding_balance(p, n, r, m):
	balance = (p * ((1+r/100)**n - (1+r/100)**m) )/ ((1+r/100)**n - 1)
	st.write("Outstanding Loan Balance Calculated is : ",balance)	
st.title("EMI Calculator")      
principal = st.slider("Loan Amount", 1000.0, 100000.0)
tenure = st.slider("Tenure in years", 1, 30)
rate = st.slider("Interest Rate", 1, 15)
period = st.slider("Period", 1, tenure * 12)
n = tenure * 12
r = rate / 12
emi_button = st.button("Calculate EMI")
balance_button = st.button("Calculate Outstanding Loan Balance")
if emi_button:
	calculate_emi(principal, n, r)
elif balance_button:
	outstanding_balance(principal, n, r, period)