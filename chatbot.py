import gradio as gr
from ollama import Client
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST")


client = Client(host=OLLAMA_HOST)


def get_response(user_input, model):
    client.pull(model)
    response = client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    return response["message"]["content"]


# Create Gradio interface
iface = gr.Interface(
    fn=get_response,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your message here..."),
            gr.Textbox(lines=2, placeholder="Model ex: llama3:8b")],
    outputs="text",
    title="Chatbot Interface",
    description="Enter a message to get a response from the model."
)

# Launch the interface
iface.launch(server_port=8080)
