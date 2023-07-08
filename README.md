# palm-api-gradio

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---


## 📍 Overview

The project is a simple Python application that provides a [Gradio](https://www.gradio.app/) interface for interacting with the [Google PaLM APIs](https://developers.generativeai.google/).

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
- [Pyenv](https://github.com/pyenv/pyenv)
- A valid PaLM API key

Also, you need to be located in the USA (The API key won't work otherwise).

### 📦 Installation

1. Clone the project repository:
   ```sh
   git clone https://github.com/Renzodef/palm-api-gradio
   ```

2. Change to the project directory:
   ```sh
   cd palm-api-gradio
   ```

3. Copy the `.env.example` to `.env` and set your `PALM_API_KEY`

4. Install Python through Pyenv:
   ```sh
   pyenv install 3.10.0
   ```

5. Set the local Python version for the project:
   ```sh
   pyenv local 3.10.0
   ```

6. Install Pipenv:
   ```sh
   pip install pipenv
   ```

7. Install the dependencies:
   ```sh
   pipenv install
   ```

### 🎮 Using palm-api-gradio

To start the server, run the following command:

```sh
pipenv run python app.py
```

Once the server is running, open your preferred web browser and enter the following URL: [http://localhost:78604](http://localhost:78604).

In the Gradio interface, you can enter your questions or messages in the provided input field, then the application will process your input and generate responses based on the PaLM model.

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

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Renzodef/palm-api-gradio/blob/main/LICENSE) file for additional info.
