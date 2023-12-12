import os
import time

class WhatsAppSimulator:
    def __init__(self, user):
        self.user = user
        self.chat_file = f"{user}_chat.txt"

    def load_chat(self):
        if os.path.exists(self.chat_file):
            with open(self.chat_file, 'r') as file:
                return file.read()
        return "Chat started."

    def save_message(self, sender, message):
        with open(self.chat_file, 'a') as file:
            file.write(f"{sender}: {message}\n")

    def send_message(self, receiver, message):
        print(f"Sending message to {receiver}...")
        time.sleep(1)  # Simulating network delay
        receiver_chat = WhatsAppSimulator(receiver)
        receiver_chat.save_message(self.user, message)
        print("Message sent successfully!")

    def chat_loop(self):
        print("Welcome to WhatsApp Simulator!")
        print("Loading chat...\n")
        print(self.load_chat())

        while True:
            receiver = input("Enter the recipient's username (type 'exit' to end): ")
            if receiver.lower() == 'exit':
                print("Exiting WhatsApp Simulator. Goodbye!")
                break

            message = input("Type your message: ")
            self.send_message(receiver, message)
            self.save_message(self.user, message)

if __name__ == "__main__":
    username = input("Enter your username: ")
    user_chat = WhatsAppSimulator(username)
    user_chat.chat_loop()