import os

import google.generativeai as palm
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
palm_api_key = os.getenv("PALM_API_KEY")
palm.configure(api_key=palm_api_key)

global_response = None


def palm_chatbot(your_question):
    global global_response
    if global_response is None:
        global_response = palm.chat(messages=your_question)
    else:
        global_response = global_response.reply(your_question)
    return global_response.last


iface = gr.Interface(fn=palm_chatbot, inputs="text", outputs="text")
iface.launch()
