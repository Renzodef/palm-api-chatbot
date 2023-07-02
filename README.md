
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>palm-api-chatbot
</h1>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
</p>
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---


## 📍 Overview

The palm-api-chatbot project is a Python application that provides a chatbot interface for interacting with the [Google PaLM API](https://developers.generativeai.google/).

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- A valid PaLM API key

Also, you need to be located in the USA (The API key won't work otherwise).

### 📦 Installation

1. Clone the rclone-decrypt-express repository:
```sh
git clone https://github.com/Renzodef/palm-api-chatbot.git
```

2. Change to the project directory:
```sh
cd palm-api-chatbot
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```
(It is advised to use a virtual environment management tool like [Virtualenv](https://virtualenv.pypa.io/))

4. Copy the `.env.example` to `.env` and set your `PALM_API_KEY`

### 🎮 Using palm-api-chatbot

This application uses [Gradio](https://gradio.app/) to provide a user interface for interacting with the chatbot.
Follow these steps to use the application:

1. To start the server run: `python app.py`
2. Once the server is running, open your preferred web browser and enter the following URL: http://localhost:78604
3. In the Gradio interface, you can enter your questions or messages in the provided input field, then
   the chatbot will process your input and generate responses based on the PaLM model.
4. To stop the server, go back to the terminal or command prompt where the server is running and press `Ctrl + C`

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Renzodef/palm-api-chatbot/blob/main/LICENSE) file for additional info.
