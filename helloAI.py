print("Hello, I am an AI BOT....")
name = input("Enter your name to start : ")
print(f"Nice to meet you, {name}!")

while True :

    mood = input("How are you feeling today :  good | bad | okay ? ")
    mood = mood.lower()

    if mood == 'good':
        print("I am glad to hear that your day is good")
    elif mood == 'bad':
        print("Sorry to hear that your not happy today")
    elif mood == 'okay':
        print("Git it, sometimes 'okay' is just right")
    else:
        print("Sometimes its hard to put feeling into words")

    hobby = input("What do you like to do in your free time? ")
    print(f"{hobby} sounds like a great way to spend time")

    choice = input("Would you like to keep chatting :  yes |exit ?")
    choice = choice.lower()

    if choice == "exit":
     print(f"It was nice chatting with you, {name} !! Goodbye")
     break







