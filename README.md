# Language Translator

A small Gradio app that uses Google Gemini to translate a sentence into Hindi,
Telugu, or French.

## Requirements

- Python
- A Google Gemini API key

## Setup

Open a terminal in this folder, create and activate a virtual environment, and
install the app's dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install gradio google-genai python-dotenv
```

Copy `.env.example` to `.env` and add your Gemini API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
```

Keep `.env` private; it is excluded from Git.

## Run

```powershell
python app.py
```

Open the local URL printed by Gradio, enter a sentence, and select a target
language.
