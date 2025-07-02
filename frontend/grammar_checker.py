import streamlit as st
import requests

def grammar_checker_section():
    st.subheader("✏️ Grammar & Spelling Checker")

    if "word_input" not in st.session_state:
        st.session_state.word_input = ""
    if "apply_suggestion" not in st.session_state:
        st.session_state.apply_suggestion = False
    if "suggestion" not in st.session_state:
        st.session_state.suggestion = ""

    if st.session_state.apply_suggestion:
        st.session_state.word_input = st.session_state.suggestion
        st.session_state.apply_suggestion = False
        st.rerun()

    word = st.text_input("🔍 Enter a sentence:", key="word_input")

    suggestion = None
    if word:
        url = "https://api.languagetool.org/v2/check"
        params = {"text": word, "language": "en-US"}

        try:
            response = requests.post(url, data=params)
            result = response.json()
            if result["matches"]:
                match = result["matches"][0]
                replacement = match["replacements"][0]["value"]
                start = match["offset"]
                end = match["offset"] + match["length"]
                suggestion = word[:start] + replacement + word[end:]
                st.session_state.suggestion = suggestion
        except Exception as e:
            st.error(f"LanguageTool API error: {e}")

    if suggestion and suggestion != word:
        st.warning(f"💡 Did you mean: **{suggestion}**?")
        if st.button("✅ Use Suggestion"):
            st.session_state.apply_suggestion = True
            st.rerun()

    if st.button("📤 Send to Server"):
        if not word:
            st.warning("Please enter a sentence first.")
        else:
            st.success(f"✅ Ready to send: {word}")
