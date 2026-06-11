import streamlit as st

from src.constants import CURRENCIES
from src.api import get_exchange_rate
from src.converter import convert_currency


st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")

st.markdown("""
Convert between currencies using real-time exchange rates.
""")


base_currency = st.selectbox("From", CURRENCIES)
target_currency = st.selectbox("To", CURRENCIES)

amount = st.number_input("Amount", min_value=0.0, value=100.0)

if base_currency and target_currency and amount > 0:

    rate = get_exchange_rate(base_currency, target_currency)

    if rate:
        result = convert_currency(amount, rate)

        st.success(f"Rate: {rate:.4f}")

        col1, col2, col3 = st.columns(3)

        col1.metric("From", f"{amount:.2f} {base_currency}")

        col2.markdown("➡️")

        col3.metric("To", f"{result:.2f} {target_currency}")

    else:
        st.error("Failed to fetch exchange rate.")