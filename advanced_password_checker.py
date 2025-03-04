import streamlit as st

# Custom CSS for orangish theme
st.markdown(
    """
    <style>
    .stTextInput input {
        background-color: #FFE4B5;
        color: #FF4500;
    }
    .stButton button {
        background-color: #FF8C00;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #FF4500;
    }
    .stProgress > div > div > div {
        background-color: #FF8C00;
    }
    .stMarkdown h1 {
        color: #FF4500;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase check
    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        strength += 1
    else:
        remarks.append("Password should contain at least one lowercase letter.")

    # Digit check
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks.append("Password should contain at least one digit.")

    # Special character check
    special_chars = "!@#$%^&*()_+=-[]{};:,.<>/?"
    if any(char in special_chars for char in password):
        strength += 1
    else:
        remarks.append("Password should contain at least one special character.")

    # Common password check (basic example)
    common_passwords = ["password", "123456", "qwerty", "admin"]
    if password.lower() in common_passwords:
        strength = 0
        remarks.append("Password is too common. Choose a more unique password.")

    # Determine strength level
    if strength >= 5:
        return "Very Strong 💪", remarks, strength
    elif strength >= 3:
        return "Strong 👍", remarks, strength
    elif strength >= 2:
        return "Moderate 🤔", remarks, strength
    else:
        return "Weak 🚨", remarks, strength

def main():
    st.title("🔐 Advanced Password Strength Checker")
    st.markdown("Enter your password below to check its strength.")

    password = st.text_input("Password:", type="password", placeholder="Enter your password...")

    if st.button("Check Strength"):
        if password:
            strength, remarks, score = check_password_strength(password)
            
            # Display strength level with emoji
            st.subheader(f"Password Strength: {strength}")

            # Visual strength meter (progress bar)
            st.progress(score / 6)  # Max score is 6

            # Display remarks
            if remarks:
                st.warning("Remarks:")
                for remark in remarks:
                    st.write(f"- {remark}")
        else:
            st.error("Please enter a password to check its strength.")

if __name__ == "__main__":
    main()