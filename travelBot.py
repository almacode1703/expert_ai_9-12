import re, random  #importing regular expression , random
import colorama
from colorama import Fore, Style,init

#initialize colorama 
colorama.init(autoreset=True)

destinations = {
    "beaches" : ["bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "himalayas"],
    "cities":["Tokyos","Paris", "New York" ]
}

jokes = [
    "Why programmers don't like nature ? Too many bugs",
    "Why did the computer go to the doctor? Because it had a virus!!",
    "Why do travelers always feel warm ? Because of all their hot spots!! "
]

def normalize_input(text):
    return re.sub(r"\s+", " ",  text.strip().lower())

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def recommend_places():
    print(f"{Fore.GREEN}, Travel Bot : Where do you love to go ? beaches | mountains | cities ?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"How about {Fore.LIGHTCYAN_EX}{suggestion}")
        print("Do you like it? yes | no")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot : Awesome ! Enjoy your vacation")
        
        elif answer == "no":
            print(Fore.RED + "TravelBot : Let's try another")
            recommend_places()
        
        else:
            print(Fore.RED + "TravelBot : I will suggest again")
            recommend_places()
    else : 
        print(Fore.RED +"TravelBot : Sorry, Idont have that type of destination")


# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    
    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend_places()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")


# Run the chatbot
if __name__ == "__main__":
    chat()