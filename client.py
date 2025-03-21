import requests
import streamlit as st

# Function to get translation response from FastAPI server
def get_translation_response(language, text):
    try:
        response = requests.post(
            "http://localhost:8000/chain/invoke",
            json={'input': {'language': language, 'text': text}}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        st.error(f"Error making the request: {e}")
        return None
    except KeyError as e:
        st.error(f"Error parsing the response: {e}")
        return None

# Streamlit framework
st.title('Translation Demo with FastAPI Server')

# Input fields
language = st.text_input("Enter the target language (e.g., French, Spanish):")
text = st.text_input("Enter the text to translate:")

# Translate button
if st.button("Translate"):
    if language and text:
        translation_response = get_translation_response(language, text)
        if translation_response:
            st.write("Translated Text:")
            st.write(translation_response)
        else:
            st.write("Failed to generate a translation. Please try again.")
    else:
        st.warning("Please provide both the target language and the text to translate.")
