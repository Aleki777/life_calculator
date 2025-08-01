import streamlit as st
import urllib.parse

def lead_form(premium=None):
    st.markdown("### 📋 Get a Free Quote or Speak to an Insurance Advisor")
    
    with st.form("lead_capture"):
        name = st.text_input("Your Name")
        contact = st.text_input("Phone Number or Email")
        message = st.text_area("Anything else you'd like to add?")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success("✅ Thank you! We’ll be in touch shortly.")

            # ✅ WhatsApp integration — send to YOUR number
            your_whatsapp_number = "254728753367"  # ← Replace with your WhatsApp number
            
            user_message = f"""
📥 *New Insurance Lead*:
👤 Name: {name}
📞 Contact: {contact}
💰 Estimated Premium: KES {premium}
📝 Message: {message}
            """
            encoded_msg = urllib.parse.quote(user_message)
            whatsapp_url = f"https://wa.me/{your_whatsapp_number}?text={encoded_msg}"

            st.markdown("📲 Click below to send this lead info to your WhatsApp")
            st.markdown(f"[Send via WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
