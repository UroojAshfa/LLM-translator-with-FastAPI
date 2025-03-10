# LLM Language Translator

A simple language translation application powered by a Large Language Model (LLM) using FastAPI for the backend and Streamlit for the frontend.

## Features

- Accepts text input and target language from the user
- Uses a Groq-powered LLM for translation
- Exposes an API endpoint via FastAPI
- Provides a simple UI using Streamlit

## Technologies Used

- FastAPI (Backend API)
- Streamlit (Frontend UI)
- LangChain (Prompt Handling)
- Langserve (API Routing)
- Groq API (LLM Translation)
- dotenv (Environment Variables Handling)
- Uvicorn (Server Execution)
- Requests (API Communication)

## Installation

### Prerequisites

Ensure you have Python installed on your system. You will also need a Groq API key.

### Setup

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/llm-translator.git
   cd llm-translator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Groq API key:
   ```sh
   GROQ_API_KEY=your_api_key_here
   ```

## Running the Project

### Start the FastAPI Server

```sh
python server.py
```

### Start the Streamlit Frontend

```sh
streamlit run client.py
```

## API Usage

The FastAPI server exposes an endpoint:

- **POST** `/chain/invoke`
  - **Request Body:**
    ```json
    {
      "input": {
        "language": "Spanish",
        "text": "Hello, how are you?"
      }
    }
    ```
  - **Response:**
    ```json
    {
      "output": "Hola, ¿cómo estás?"
    }
    ```

## How It Works

1. The user enters text and selects a target language in the Streamlit UI.
2. The frontend makes a request to the FastAPI backend.
3. The backend processes the request using LangChain and the Groq API.
4. The translated text is returned and displayed in the UI.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork the repo and submit pull requests!

## Author

Your Name - [Your GitHub](https://github.com/your-profile)

