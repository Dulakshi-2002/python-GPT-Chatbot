# Python GPT Chatbot

A simple chatbot application built using OpenAI's GPT-3.5 model. This project allows users to interact with the chatbot in a conversational manner via the terminal.

## Features

- Uses OpenAI's GPT-3.5 model for generating responses.
- Handles rate limit errors gracefully by retrying after a delay.
- Securely loads the OpenAI API key from a `.env` file.
- Simple and interactive terminal-based interface.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation

1. **Clone the Repository**:
   ```bash
   https://github.com/Dulakshi-2002/python-GPT-Chatbot.git
   cd python-GPT-Chatbot
   ```
2. **Set Up a Virtual Environment (optional but recommended):**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the .env File: Create a .env file in the root directory and add your OpenAI API key:**:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```
5. **Ensure .env is Ignored by Git: Verify that .env is listed in .gitignore to prevent accidental exposure of your API key:**:
   ```bash
   .env
   ```
## Usage

### Run the Chatbot:
 ```bash
  python main.py
  ```
### Interact with the Chatbot:

  - Type your message and press Enter.
  - To exit the chatbot, type quit, exit, or bye.

## Example Interaction

  ```bash
  You: Hello, how are you?
  GPT-3.5: I'm just a chatbot, but I'm here to help! How can I assist you today?

  You: Tell me a joke.
  GPT-3.5: Why don't scientists trust atoms? Because they make up everything!

  You: bye
```
## Error Handling
  - If the API rate limit is exceeded, the chatbot will wait for 10 seconds and retry.
  - If the API key is invalid or missing, the program will fail to run. Ensure your .env file is correctly configured.

## Project Structure
  ```bash
  python-GPT-Chatbot/
  ├── [main.py](http://_vscodecontentref_/1)          # Main script for running the chatbot
  ├── .env             # Environment file for storing the API key (not included in the repo)
  ├── .gitignore       # Git ignore file to exclude sensitive files like .env
  ├── requirements.txt # List of dependencies
  ```

## Dependencies
 ### The project uses the following Python libraries:
  - openai: For interacting with OpenAI's GPT API.
  - python-dotenv: For loading environment variables from a .env file.

### Install all dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## Troubleshooting

### Rate Limit Errors:
  - If you encounter a rate limit error, the chatbot will retry after 10 seconds. If the issue persists, check your OpenAI account usage and quota.

### API Key Issues:
  - Ensure your API key is correctly set in the .env file.
  - If your API key is compromised, regenerate it from the OpenAI Dashboard.

### Missing Dependencies:
  - Run pip install -r requirements.txt to ensure all dependencies are installed.

## Acknowledgments

  - OpenAI for providing the GPT-3.5 model.
  - Python Dotenv for managing environment variables.


   
