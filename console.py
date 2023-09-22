#!/usr/bin/python3
""" console"""

import cmd
import uuid
from models.base_model import BaseModel
from models.user import User
from models.mapbox import Mappoints


classes = {"User": User, "BaseModel": BaseModel, "mapbox": Mappoints}


class BONGANICommand(cmd.Cmd):
    """BONGANI Console"""
    prompt = '(bongani) '

    def __init__(self):
        super().__init__()
        self.users = [] #Define the users list
        self.sessions = {} # Define the sessions dictionary
        self.selected_option = None #Track selected menu option

    def set_prompt(self, option):
        self.selected_option = option
        self.prompt = f'(bongani - {option}) '

    def register_user(self, username, password, role):
        for user in self.users:
            if user["username"] == username:
                print("Username already exists. Please choose another.")
                return
        self.users.append({"username": username, "password": password, "role": role})
        print("Registration successful!")
        self.set_prompt(None)

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                session_id = str(uuid.uuid4())
                self.sessions[session_id] = {"username": username, "role": user["role"]}
                print(f"Login successful. Session ID: {session_id}")
                return session_id # Return the session ID for later use
        print("Invalid username or password.")
        self.set_prompt(None)

    def logout(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
            print("Logout successful.")
        else:
            print("Invalid session ID.")
        self.set_prompt(None)

    def do_menu(self, line):
        """Display the menu options"""
        while True:
            print("\nOptions:")
            print("1. Register")
            print("2. Login")
            print("3. Logout")
            print("4. Quit")

            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (Driver/Parent): ")
                self.register_user(username, password, role)
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                session_id = self.login(username, password)
                if session_id:
                    print(f"Session ID: {session_id}")
            elif choice == "3":
                session_id = input("Enter session ID: ")
                self.logout(session_id)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
        
    def do_register(self, line):
        """Register a user"""
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (driver/parent): ")
        self.set_prompt("Register") # Set the prompt to "Register"
        self.register_user(username, password, role)

    def do_login(self, line):
        """Login"""
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.set_prompt("Login") # Set the prompt to "Login"
        session_id = self.login(username, password)
        if session_id:
            print(f"Session ID: {session_id}")

    def do_login(self, line):
        """Logout"""
        session_id = input("Enter session ID: ")
        self.set_prompt("Logout") # Set the prompt to "Logout"
        self.logout(session_id)

    def do_quit(self, line):
        """Quit the program"""
        return True

    def cmdloop(self):
        self.do_menu(None)
        print("Are you sure you want to quit!")
        print("\nType: menu or quit")
        super().cmdloop()
        print("\nGood-Bye")


def main():
    BONGANICommand().cmdloop()


if __name__ == "__main__":
    main()
