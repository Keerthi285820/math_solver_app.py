import streamlit as st
from sympy import sympify, simplify, solve, Symbol
from sympy.core.sympify import SympifyError

# Page Config
st.set_page_config(page_title="Math Solver", page_icon="🧮", layout="centered")

# Title with style
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🧠 Smart Math Solver</h1>", unsafe_allow_html=True)
st.markdown("---")

# Solver Type
option = st.selectbox("📌 Choose Solver Type", ["Arithmetic Evaluator", "Algebra Simplifier", "Equation Solver"])

# Expression Input
user_input = st.text_input("✍️ Enter your expression (e.g., 2*x + 3*x or 2+5*3):")

# Solve Button
if st.button("✅ Solve"):
    try:
        if option == "Arithmetic Evaluator":
            result = eval(user_input)
            st.success(f"✅ Result: {result}")

        elif option == "Algebra Simplifier":
            result = simplify(sympify(user_input))
            st.success(f"📉 Simplified: {result}")

        elif option == "Equation Solver":
            x = Symbol('x')
            equation = sympify(user_input.replace("=", "-(") + ")")
            result = solve(equation, x)
            st.success(f"🧮 Solution for x: {result}")

    except (SympifyError, SyntaxError, NameError, ZeroDivisionError):
        st.error("❌ Invalid expression! Try using valid numbers, symbols, and 'x' for variables.")
