from openai import OpenAI
import os

from apiInputs import openAPIKey

def summarizeText(file_content):
	os.environ["OPENAI_API_KEY"] = openAPIKey
	client = OpenAI()
	chat_completion = client.chat.completions.create(
	    messages=[
	        {
	            "role": "user",
	            "content": "here is a transcript of a lesson from my teacher, give me a short summary of the lesson (there might be random sounds in the back every once its a while its fine just ignore them)" +  file_content,
	        }
	    ],
	    model="gpt-4o-mini",
	)
	return chat_completion.choices[0].message.content

