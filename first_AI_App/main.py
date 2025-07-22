import gradio as gr
import openai
import os
import requests

from dotenv import load_dotenv

# Retrieve the OpenAI API key from the environment variables
load_dotenv()
openai.api_key= os.getenv('OPENAI_API_KEY')
print("OpenAI API key loaded successfully.")

# Function to generate a short Python lesson using GPT-4o-mini
def generate_python_lesson():
    """
    Generates a concise Python tip for beginners in data science and AI 
    engineering, focusing on practical, unique, and visually appealing code examples.
    """
    # List of messages for the chat-based model
    messages = [
        {
	    # System message to help assistant understand its role
            "role": "system",
            "content": (
                "You are a helpful assistant. Your task is to provide clear, concise Python tips "
                "for beginners in data science and AI."
            ),
        },
        {
	    # User message to specify task
            "role": "user",
            "content": (
                "Generate a 1-2 sentence Python tip for beginners in data science and AI engineering. "
                "Include a practical code example that can help improve programming skills."
            ),
        },
    ]
    
    # Get a response from the OpenAI chat-completions API
    response = openai.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",  
        messages=messages,               
        max_tokens=150                   
    )
    
    # Extract and return the lesson text
    lesson = response.choices[0].message.content.strip()
    return lesson


# Create a Gradio interface to display the result as Markdown
def create_interface():
    
    # Create the Gradio interface with the custom HTML footer
    iface = gr.Interface(
        fn=generate_python_lesson,  # The function to be executed when the interface is used
        inputs=None,                # No inputs are required from the user
        outputs=gr.Markdown(),      # The output is displayed as Markdown
        live=True,                  # Enables real-time updates as the function runs
        title="Daily Python Tips",  # Title displayed at the top of the interface
        clear_btn=None,             # Disables the "Clear" button in the interface
        allow_flagging="never",     # Disables the flagging feature for user feedback
    )
    
    return iface

# Launch the interface
iface = create_interface()
iface.launch()