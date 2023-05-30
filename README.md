# PaLM API Chatbot

This is a Python application that provides a chatbot interface for interacting with
the [Google PaLM API](https://developers.generativeai.google/).

## Requirements

To run this application, you'll need the following:

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- Have a valid PaLM API key

Also, you need to be located in the USA (The API key won't work otherwise).

## Installation

1. Clone this repository: `git clone https://github.com/Renzodef/palm-api-chatbot.git`
2. Install dependencies: `pip install -r requirements.txt`
   (It is advised to use a virtual environment management tool like [Virtualenv](https://virtualenv.pypa.io/)).
3. Copy the `.env.example` to `.env` and set your `PALM_API_KEY`.

## Usage

This application uses [Gradio](https://gradio.app/) to provide a user interface for interacting with the chatbot.
Follow these steps to use the application:

1. To start the server run: `python app.py`
2. Once the server is running, open your preferred web browser and enter the following URL: http://localhost:78604.
3. In the Gradio interface, you can enter your questions or messages in the provided input field.
   The chatbot will process your input and generate responses based on the PaLM model.
4. You can continue the conversation by entering additional questions or messages in the input field.
   The chatbot will respond accordingly.
5. To stop the server, go back to the terminal or command prompt where the server is running and press `Ctrl + C`.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

## License

This project is licensed under the MIT License.
