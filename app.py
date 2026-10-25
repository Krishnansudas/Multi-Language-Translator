import os
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Add it to the .env file in the project folder.")

client = genai.Client(api_key=GEMINI_API_KEY)

languages = {
    "Hindi": "Translate the given sentence into Hindi.",
    "Telugu": "Translate the given sentence into Telugu.",
    "French": "Translate the given sentence into French."
}

def language_translator(sentence, language):
    system_prompt = languages[language]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=sentence
    )
    return response.text


# Gradio Interface
demo = gr.Interface(
    fn=language_translator,
    inputs=[
        gr.Textbox(
            lines=3,
            placeholder="Enter a sentence to translate...",
            label="Input Sentence"
        ),
        gr.Radio(
            choices=list(languages.keys()),
            value="Hindi",
            label="Target Language"
        )
    ],
    outputs=gr.Textbox(lines=5, label="Translated Output"),
    title="Language Translator",
    description="Translate a sentence into Hindi, Telugu, or French using Gemini."
)

demo.launch(debug=True)