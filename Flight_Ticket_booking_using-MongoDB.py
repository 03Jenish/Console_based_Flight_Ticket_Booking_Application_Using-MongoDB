import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://jenishadlin56:gTW2.b.AQa2RRHX@cluster0.yglxoat.mongodb.net/?retryWrites=true&w=majority")
database = client["flight_booking"]
users_collection = database["users"]

def register_user(username, password):
    # Check if the username already exists
    if users_collection.find_one({"username": username}):
        print("Username already exists. Try a different one.")
        return False

    # Create a new user
    new_user = {"username": username, "password": password}
    users_collection.insert_one(new_user)
    print("Registration successful!")
    return True

def login_user(username, password):
    
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def add_flight(flight_name, flight_date, flight_number, available_seats):
    new_flight = {
        "name": flight_name,
        "date": flight_date,
        "number": flight_number,
        "available_seats": available_seats
    }
    flights_collection.insert_one(new_flight)
    print("Flight added successfully!")


while True:
    print("Welcome to the Flight Ticket Booking System")
    print("If you're a new user please register")
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Implement user login
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_user(username, password)
        
    elif choice == "2":
        # Implement user registration
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
        
    else:
        print("Invalid choice. Please try again.")
