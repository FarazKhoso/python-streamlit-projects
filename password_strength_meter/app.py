import streamlit as st
import re
import random

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Common Passwords List
    common_passwords = ["password123", "12345678", "qwerty", "letmein", "123456", "iloveyou"]

    if password in common_passwords:
        return 0, ["❌ This password is too common! Try something unique."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.sample(characters, 12))

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input Field
password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)

    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password! 💪")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    # Feedback
    for tip in feedback:
        st.write(tip)

# Generate Strong Password Button
if st.button("Generate a Strong Password 🔑"):
    strong_password = generate_strong_password()
    st.text("💡 Suggested Password: " + strong_password)
