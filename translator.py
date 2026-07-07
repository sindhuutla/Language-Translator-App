import streamlit as st
from googletrans import Translator

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #b3e5fc, #ce93d8);
);
}

h1 {
    color: #1565c0;
    text-align: center;
}

.stButton button {
    background-color: #1565c0;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 150px;
    font-size: 18px;
}

.stButton button:hover {
    background-color: #0d47a1;
}

</style>
""", unsafe_allow_html=True)


st.title("🌍 Language Translation Tool")
st.write("✨ Translate your text into different languages easily")


text = st.text_area("✍️ Enter Text", height=150)


languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}


col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "🔤 Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "🌐 Target Language",
        list(languages.keys())
    )


if st.button("🚀 Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        translator = Translator()
        translated = translator.translate(
            text,
            src=languages[source],
            dest=languages[target]
        )

        st.success("Translation Result:")
        st.write(translated.text)
