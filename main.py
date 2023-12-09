from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

import sys
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(650, 500)

        # Add chat area widgets
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setFixedHeight(400)
        self.chat_area.setFixedWidth(500)
        self.chat_area.move(10, 10)
        self.chat_area.setPlainText("Welcome to the chatbot")
        
        # Add user input widgets
        self.user_input = QLineEdit(self)
        self.user_input.setFixedHeight(40)
        self.user_input.setFixedWidth(500)
        self.user_input.move(10, 420)
        # Add button
        self.send_button = QPushButton("Send", self)
        self.send_button.move(520, 420)
        self.show()
class Chatbot:
    pass

app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())