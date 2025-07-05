#import openai
import os

openai.api_key = os.getenv("YOUR_API_KEY")  # Use environment variable for safety

def summarize_text(transcript_text):
    prompt = f"Summarize this meeting transcript in bullet points:\n\n{transcript_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes meeting transcripts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )
    
    return response["choices"][0]["message"]["content"]
