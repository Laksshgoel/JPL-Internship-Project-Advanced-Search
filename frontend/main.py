import streamlit as st
from grammar_checker import grammar_checker_section
from object_detection import object_detection_section

st.set_page_config(page_title="Smart Language + Vision App", layout="centered")
st.title("🧠 Smart Language + Vision App")


grammar_checker_section()

st.markdown("---") 

object_detection_section()
