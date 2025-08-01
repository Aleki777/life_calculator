# app.py

import streamlit as st
from lead_form import lead_form

def income_x10_method(annual_income):
    return annual_income * 10

def dime_method(debt, annual_income, years_to_cover, mortgage, education):
    return debt + (annual_income * years_to_cover) + mortgage + education

def estimate_premium(cover_needed, base_rate=2.5):
    return round((cover_needed / 1000) * base_rate, 2)

# UI
st.title("💼 Term Life Insurance Calculator (Kenya)")
st.write("Estimate your life cover needs using either the Income ×10 method or the DIME method.")

method = st.radio("Choose a method", ["Income ×10 Method", "DIME Method"])

if method == "Income ×10 Method":
    income = st.number_input("Annual Income (KES)", min_value=0.0, step=1000.0)
    if st.button("Calculate Cover"):
        cover = income_x10_method(income)
        st.success(f"📌 Estimated Cover: KES {cover:,.2f}")
        premium = estimate_premium(cover)
        st.info(f"💰 Estimated Annual Premium (KES 2.5 per 1,000): KES {premium:,.2f}")
        st.session_state.premium = premium  # Store in session_state

elif method == "DIME Method":
    debt = st.number_input("Total Personal Debts (KES)", min_value=0.0, step=1000.0)
    income = st.number_input("Annual Income (KES)", min_value=0.0, step=1000.0)
    years = st.slider("Years of Income Replacement", min_value=1, max_value=40, value=10)
    mortgage = st.number_input("Mortgage or Rent Balance (KES)", min_value=0.0, step=1000.0)
    education = st.number_input("Estimated Education Costs for Children (KES)", min_value=0.0, step=1000.0)
 
    if st.button("Calculate Cover"):
        cover = dime_method(debt, income, years, mortgage, education)
        st.success(f"📌 Estimated Cover: KES {cover:,.2f}")
        premium = estimate_premium(cover)
        st.info(f"💰 Estimated Annual Premium (KES 2.5 per 1,000): KES {premium:,.2f}")
        st.session_state.premium = premium  # Store in session_state

st.markdown("---")

# Show lead form and optional WhatsApp link
lead_form(st.session_state.get("premium", None))