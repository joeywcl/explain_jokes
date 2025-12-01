import streamlit as st
import openai
import os

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

st.title("Joke Explainer")

# Text input for the joke
joke = st.text_area("Enter your joke here:")

if st.button("Submit"):
    if not joke.strip():
        st.warning("Please enter a joke before submitting.")
    else:
        with st.spinner("Explaining the joke..."):
            try:
                # Call OpenAI API with GPT-4.1 mini model
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that explains jokes clearly and concisely."},
                        {"role": "user", "content": f"Explain the following joke:\n{joke}"}
                    ],
                    max_tokens=300,
                    temperature=0.7,
                )
                explanation = response.choices[0].message.content.strip()
                st.subheader("Explanation")
                st.write(explanation)
            except Exception as e:
                st.error(f"An error occurred: {e}")