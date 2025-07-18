import streamlit as st
import pandas as pd
from datetime import datetime
import qrcode
from io import BytesIO
import base64

# Page configuration
st.set_page_config(page_title="Attendance Registration", page_icon="📝")

# Public URL of the app (replace this when deployed)
app_url = "https://movies-dataset-q8gsks5ohe.streamlit.app/"  # CHANGE THIS after deployment

# Title and form
st.title("📝 Attendance Registration")
st.write("Enter your name and email to register your attendance.")

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Submit"):
    if name.strip() and email.strip():
        # Save to local CSV
        df = pd.DataFrame([[name, email, datetime.now().isoformat()]],
                          columns=["Name", "Email", "Timestamp"])
        df.to_csv("attendance.csv", mode='a', index=False, header=False)
        st.success("✅ Attendance recorded!")
    else:
        st.warning("⚠️ Please fill in both fields.")

# Generate and display the QR code with the app URL
st.subheader("📱 Access this page from your phone")
qr = qrcode.make(app_url)
buf = BytesIO()
qr.save(buf, format="PNG")
st.image(buf.getvalue(), caption="Scan this QR to open the app", use_column_width=False)



