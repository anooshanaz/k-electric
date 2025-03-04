
# unit = int(input("Enter your current:"))

# if unit == 1:
#     print("K-Electric On💡")
# elif unit == 0:
#     print("UPS On 📈")
# else:
#     print("Oh sorry! only two digit allow 0 and 1 try again 💪")

import streamlit as st

def main():
    st.set_page_config(page_title="Electricity Status", page_icon="⚡", layout="centered")
    
    st.title("🔌 Electricity Status Checker")
    st.write("Enter the current status (0 or 1) to check the electricity source.")
    
    unit = st.text_input("Enter 0 for UPS, 1 for K-Electric:", value="", max_chars=1)
    
    if unit:
        try:
            unit = int(unit)
            if unit == 1:
                st.success("✅ K-Electric is On 💡")
            elif unit == 0:
                st.warning("⚠️ UPS is On 📈")
            else:
                st.error("❌ Only 0 and 1 are allowed. Try again 💪")
        except ValueError:
            st.error("❌ Please enter a valid number (0 or 1).")

    st.markdown("---")
    st.info("This app helps you check the electricity source quickly and easily.")
    
if __name__ == "__main__":
    main()
