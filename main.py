from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(650, 500)
        self.setStyleSheet(
            "background-color: #282a36; color: #f8f8f2;"
        )  # Set a dark theme background and light text

        # Set the window to be semi-transparent
        self.setWindowOpacity(0.95)  # Adjust the value as needed
        # Add chat area widgets
        self.chat_area = QTextEdit(self)
        self.chat_area.setStyleSheet(
            "background-color: #22375a; padding: 10px; border-radius: 5px;"
        )  # Style chat area
        self.chat_area.setReadOnly(True)
        self.chat_area.setFixedHeight(400)
        self.chat_area.setFixedWidth(500)
        self.chat_area.move(10, 10)
        self.chat_area.setPlainText("Welcome to the chatbot")

        # Add user input widgets
        self.user_input = QLineEdit(self)
        self.user_input.setStyleSheet(
            "background-color: #22375a; padding: 5px; border-radius: 5px;"
        )  # Style user input
        self.user_input.setFixedHeight(40)
        self.user_input.setFixedWidth(500)
        self.user_input.move(10, 420)
        self.user_input.returnPressed.connect(self.send_message)

        # Add button
        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet(
            "QPushButton { background-color: #50fa7b; color: #282a36; \
            padding: 5px; border-radius: 5px; }"
            "QPushButton:hover { background-color: #64ff7d; }"  # Add hover effect
        )  # Style send button
        self.send_button.setFixedHeight(40)
        self.send_button.setFixedWidth(120)
        self.send_button.move(520, 420)
        self.send_button.clicked.connect(self.send_message)
        self.show()

        # Initialize the chatbot
        self.chatbot = Chatbot()

    def send_message(self):
        user_text = self.user_input.text()
        self.user_input.clear()
        self.chat_area.append(f"You: {user_text}")
        thread = threading.Thread(target=self.get_bot_response, args=(user_text,))
        thread.start()
    
    def get_bot_response(self, user_text):
        bot_response = self.chatbot.get_response(user_text)
        self.chat_area.append(f"Bot: {bot_response}")


class Chatbot:
    load_dotenv()

    def __init__(self, model="text-davinci-003"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def get_response(self, prompt_text):
        try:
            completion = self.client.completions.create(
                model=self.model, prompt=prompt_text, max_tokens=3000
            )
            return completion.choices[0].text.strip()
        except Exception as e:
            print(f"Error: {e}")
            return None


app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())
