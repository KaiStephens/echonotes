# echonotes - summarize lectures with AI

When installing you can chose to use the OpenAI API to create a transcription, or you can optionally install whisper locally (you would still need an OpenAI API key for summarization) This program uses GPT-4o-mini initially but can be changed in the aiSummarizer.py under model="". 

## Requirements

You need to have Python3 with pip installed to run this on your machine

The requirements for the basic installation are listed below:

openai==1.42.0

PyAudio==0.2.14

pydub==0.25.1

You can either manually install them or use the command (after installtion):

```bash
pip install -r requirements.txt
```

## Basic installation

First off, clone the repo using: 

```bash
git clone https://github.com/KaiStephens/echonotes
```
