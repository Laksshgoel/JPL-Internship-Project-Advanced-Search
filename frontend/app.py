import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

def query_string():
 st.subheader("Object Image Search")
 query = st.text_input("Enter an object to search (e.g. : watch, umbrella, chair):")

 if st.button("Search") and query:
    response = requests.get(f"http://localhost:8000/search", params={"query": query})
    if response.status_code == 200:
        images = response.json().get("images", [])
        if images:
            for img_base64 in images:
                img = Image.open(BytesIO(base64.b64decode(img_base64)))
                st.image(img, use_container_width=True)
        else:
            st.warning("No images found for that object.")
    else:
        st.error("Error contacting the server.")
