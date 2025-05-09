import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
from context import context, context2


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


st.set_page_config(page_title="AI Humanizer", layout="centered")


st.markdown("<h1 style='text-align: center;'>AI Humanizer</h1>", unsafe_allow_html=True)


Prompt = st.text_area("Enter your prompt:")


if st.button("Humanize"):
    with st.spinner("Generating response..."):
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=(
                "\n You are an English Professor and writing an essay. no use of too much fillers but not too normal either have a unique personality\n",
                context,
                "The Prompt is\n",
                Prompt,
                "\nTry To Generate something in this tone and while generating the output self check if it is too AI like or too human like try to make it human like otherwise\n",
                context2
            )
        )
        Finalresponse = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=(
                "You are an AI detector overlooking this piece of text, your job is to change everything that is too ai in this and make it 100 percent human, Do not give anything other than the desired output\n",response
            )
        )

        st.subheader("Humanized Output:")
        st.write(Finalresponse.text)
