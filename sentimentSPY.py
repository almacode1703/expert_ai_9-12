from textblob import  TextBlob
import colorama
from colorama import Fore, Style
import sys
import time

# Initialize colorama so in the terminal colors change after each output
colorama.init(autoreset=True)

#Globar Variables
user_name = " "
conversion_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_processing_animation():
    print(f"{Fore.CYAN} Detecting Sentiment", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(f"{Fore.GREEN}.", end="")
        sys.stdout.flush()


def analyze_sentiment(text):
    global positive_count, negative_count, neutral_count
    
    try : 
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity;
        conversion_history.append(text)
       # print(sentiment)

        if sentiment > 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN}🤐 Very Positive sentiment Detected, Your Sentiment Score : {sentiment}"
        
        elif 0.25 < sentiment < 0.75:
            positive_count += 1
            return f"\n{Fore.LIGHTGREEN_EX}😄 Positive sentiment Detected, Your Sentiment Score : {sentiment}"
        
        elif -0.25 < sentiment < 0.25:
            neutral_count += 1
            return f"\n{Fore.YELLOW}😐 Neutral sentiment Detected, Your Sentiment Score : {sentiment}"
        
        elif -0.75 < sentiment < -0.25:
            negative_count += 1
            return f"\n{Fore.RED}😢 Negative sentiment Detected, Your Sentiment Score : {sentiment}"
        
        else:
            negative_count += 1
            return f"\n{Fore.RED}😞 Very negative sentiment,  Your Sentiment Score :{sentiment}"
            
    except Exception as e:
        return f"{Fore.RED} An error occured during sentiment analysis {str(e)}"
    

def get_valid_name():
    while True:
        name = input("What's your name? ").strip()
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED}, Please enter valid name characters..")

def execute_command(command):
    global conversation_history, positive_count, negative_count, neutral_count
    if command == "summary":
        return (f"{Fore.CYAN} 😎 Missing Report : \n"
                f"{Fore.GREEN} There are {positive_count} Positive Sentiment Detected"
                f"{Fore.RED} There are {negative_count} Negative Sentiment Detected"
                f"{Fore.WHITE} There are {neutral_count} Neutral Sentiment Detected"
                )
    elif command == "reset":
        conversion_history.clear()
        positive_count = negative_count = neutral_count = 0
        return f"{Fore.CYAN} Mission Reset...!! All previous data clear"
    
    elif command == "history":
        return "\n".join([f"{Fore.CYAN} Message {i+1} : {msg}" for i, msg in enumerate(conversion_history)])
    
    elif command == "help":
          return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")

    else:
        return f"{Fore.RED} Unknown Command !! Plese type 'help' to see available commands"


def save_sentiment_report():
    global user_name, positive_count,negative_count,neutral_count
    filename = f"{user_name}_sentiment_analysis.txt"
    with open(filename, "w") as file:
        file.write(f"Sentiment Analysis Report for Agent {user_name}\n")
        file.write(f"Positive Sentiments: {positive_count}\n")
        file.write(f"Negative Sentiments: {negative_count}\n")
        file.write(f"Neutral Sentiments: {neutral_count}\n")
        file.write(f"\nConversation History:\n")

        for idx, sentence in enumerate(conversion_history):
            file.write(f"{idx + 1}. {sentence}\n")
    print(f"{Fore.CYAN} Sentiment analysis report saved as {filename}")


def start_sentiment_chat():
    print(f"{Fore.CYAN}{Style.BRIGHT} 😎 Welcome to Sentiment Spy !! Your personal emotion detective is here !!")
    global user_name
    
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN}Nice to meet you, Agent {Fore.YELLOW}{user_name}! Type your sentences to analyze emotions. Type 'help' for options.")

    while True:
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}, Agent {user_name} : {Style.RESET_ALL}").strip()

        if not user_input:
            print(f"{Fore.RED} Please enter a non empty message or type 'help'")
            continue

        if user_input.lower() == 'exit':
            print(f"\n{Fore.BLUE} Mission Complete !! ")
            print(execute_command("summary"))
            save_sentiment_report()
            break

        elif user_input.lower() in ['summary', 'reset', 'history','help']:
            print(execute_command(user_input.lower()))
        
        else:
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)

#Entry Point 
if __name__ == "__main__":
    start_sentiment_chat()

            
        
