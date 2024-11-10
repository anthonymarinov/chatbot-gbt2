# GPT-2 Based Chatbot

This project is a chatbot application that uses a GPT-2 model to generate conversational responses. The application has two main components:
- **Frontend (React)**: Allows users to interact with the chatbot through a message box.
- **Backend (Flask)**: Processes user input using a GPT-2 language model and returns the generated responses.

## Project Structure

- **`index.tsx`**: Implements the user interface using React, allowing users to send messages to the chatbot and view responses.
- **`app.py`**: Implements the backend using Flask, handling the chatbot responses using GPT-2.

## Features

- **User Interface**: A simple text-based UI for sending and receiving messages.
- **GPT-2 Text Generation**: Uses a pre-trained GPT-2 model to generate responses based on user input.
- **Cross-Origin Communication**: Flask server is configured with CORS to enable communication with the React frontend.

## Installation

### Prerequisites

1. **Python 3.6+** and **Node.js** are required.
2. Install the necessary Python and Node.js packages.
3. Clone or download this repository containing all neccessary setup files.

### Backend Setup

1. Install Python dependencies:
   ```bash
   pip install flask flask-cors transformers tensorflow

2. Start the Flask backend server:
3. ```bash
   python app.py

### Frontend Setup

1. Make sure node.js is downloaded, and npm is accessible in the terminal. This repository contains the necessary configuration files to run the application. 

2. Start the React application:
   ```bash
   npm run dev

The backend runs on **`localhost:5000`**. The front end runs on and can be found at **`https://localhost:3000`**. They communicate with each other through CORS.

## Usage

- Open the frontend application in a browser at **`https://localhost:3000`**.
- Enter a message and oress "Send" to interact with the chatbot.
- The chatbot response is generated using GPT-2 and displayed below the user's message.

## API Endpoints

- **POST** **`/chatbot`**: Accepts a JSON payload with a **`"message`** field containing the user's input text. Returns a generated response.

## Notes

- Current rendition uses a small version of GPT-2 to improve response times, and therefore has a limited reply scope.
