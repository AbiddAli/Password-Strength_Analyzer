import streamlit as st
import re

# Custom CSS for polished look
st.markdown(
    """
    <style>
        .strength-box {
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            font-weight: bold;
            font-size: 1.2rem;
            margin-top: 1rem;
        }
        .weak {background-color: #ef4444; color: white;}          /* Red */
        .moderate {background-color: #facc15; color: black;}      /* Yellow */
        .strong {background-color: #fb923c; color: white;}        /* Orange */
        .very-strong {background-color: #22c55e; color: white;}   /* Green */

        .stButton > button {
            background-color: #2563eb !important;
            color: white !important;
            border-radius: 0.375rem;
            padding: 0.6rem 1.2rem;
            border: none;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #1d4ed8 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Password strength checker logic
def check_password_strength(password: str):
    strength = 0
    css_class = "weak"
    label = "Weak"

    # Password validation checks
    if len(password) >= 8:
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Classification
    if strength == 5:
        css_class = "very-strong"
        label = "Very Strong"
    elif strength == 4:
        css_class = "strong"
        label = "Strong"
    elif strength == 3:
        css_class = "moderate"
        label = "Moderate"

    return label, css_class

# UI
st.title("🔐 Password Strength Analyzer")
st.subheader("Check how secure your password is")

with st.form("password_form"):
    password = st.text_input("Enter your password", type="password", help="Must be at least 8 characters long")
    submitted = st.form_submit_button("Check Strength")

if submitted:
    if password:
        label, css_class = check_password_strength(password)
        st.markdown(f'<div class="strength-box {css_class}">{label}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a password.")
