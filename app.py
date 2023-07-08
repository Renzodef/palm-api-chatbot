import os

from dotenv_vault import load_dotenv
import google.generativeai as palm
import gradio as gr

load_dotenv()
palm_api_key = os.getenv("PALM_API_KEY")
palm.configure(api_key=palm_api_key)

global_response = None


def palm_chatbot(your_question):
    global global_response
    if not your_question:
        return "Please provide a question."
    try:
        if global_response is None:
            global_response = palm.chat(messages=your_question)
        else:
            global_response = global_response.reply(your_question)
        if not global_response.last:
            return "I'm sorry, I don't have a response for that."
        return global_response.last
    except ValueError:
        return "I'm sorry, I wasn't able to generate a response."
    except Exception as e:
        return f"{str(e)}"


iface = gr.Interface(fn=palm_chatbot, inputs="text", outputs="text")
iface.launch()
