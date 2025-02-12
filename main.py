# Console Chat
import sys
import os


class Observer:
    def update(self, event):
        pass


class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, event):
        print(f"\033[F{event.author}: {event.text}")


class Message:
    def __init__(self, author: User, text: str):
        self.author = author
        self.text = text

    def send(self):
        pass


class TextMessage(Message):
    def send(self, reciver: str = "global"):
        if reciver != "global":
            self.author.update(self)
        else:
            print(f"\033[F{self.author.name}: {self.text}")


class CommandMessage(Message):
    def send(self):
        if self.text == "/help":
            print("There is no help for u hahaha")
        if self.text == "/exit":
            print("Really? U so weak. Bye loser!")
            raise 0


def main():
    print("Welcome! Enter your username")
    user = User(input())
    print("Now you can start chatting!")

    while True:
        msg = input("> ")

        if msg.startswith("/"):
            msg = CommandMessage(user, msg)
        else:
            msg = TextMessage(user, msg)

        msg.send()


if __name__ == "__main__":
    main()
