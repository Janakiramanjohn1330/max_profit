import streamlit as st
from typing import Dict, Tuple

st.set_page_config(page_title="Max Profit App", layout="centered")
st.title("🏗 Max Profit Optimization")

BUILDINGS = {
    "T": {"name": "Theatre", "time": 5, "earning": 1500},
    "P": {"name": "Pub", "time": 4, "earning": 1000},
    "C": {"name": "Commercial Park", "time": 10, "earning": 2000},
}

def calculate_earnings(counts: Dict[str, int]) -> int:
    return sum(BUILDINGS[k]["earning"] * v for k, v in counts.items())

def calculate_time(counts: Dict[str, int]) -> int:
    return sum(BUILDINGS[k]["time"] * v for k, v in counts.items())

def max_profit(n: int) -> Tuple[Dict[str, int], int]:
    best_profit = 0
    best_combo = {"T": 0, "P": 0, "C": 0}

    for t in range(n // BUILDINGS["T"]["time"] + 1):
        for p in range(n // BUILDINGS["P"]["time"] + 1):
            for c in range(n // BUILDINGS["C"]["time"] + 1):
                combo = {"T": t, "P": p, "C": c}
                if calculate_time(combo) <= n:
                    profit = calculate_earnings(combo)
                    if profit > best_profit:
                        best_profit = profit
                        best_combo = combo.copy()

    return best_combo, best_profit

time_units = st.slider("Total Time Units", 0, 50, 10)

if st.button("Calculate"):
    result, profit = max_profit(time_units)
    st.metric("💰 Total Profit", profit)
    st.metric("⏱ Time Used", calculate_time(result))
    st.json(result)
