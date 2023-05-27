import re
import random
import time
from colorama import Fore

patterns = {
    'what are you': ["I am a Chat Bot called CodeIQ ACS, I am developed by CodeIQ's Lead Developer & Founder, Logan.",
                     'I am a Chat Bot called CodeIQ ACS with capabilities of talking to humans', 'I am CodeIQ ACS and I want to help all humans acomplish their coding dreams!'],
    'hello': ['Hi there!', 'Hello!', 'Hey!'],
    'how are you': ['I am doing well, thanks for asking. What about you?', 'I am fine, thank you. How about you?',
                    'I am great, how about you?'],
    'what is your name': ['My name is CodeIQ ACS. How can I help you today?', 'I am CodeIQ ACS!',
                          'I go by CodeIQ ACS. ASC means Automated Chatter System!'],
    'bye': ['Goodbye!', 'See you later.', 'It was nice talking to you.'],
    'cunt nmber': ['Okay, which number do you want me to count to?'],
    'count to': ['Okay, counting now!!', 'Sure, here are the numbers:']
}


def match_pattern(user_input):
    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            if pattern == "how are you":
                return random.choice(patterns[pattern])
                print(Fore.LIGHTGREEN_EX + "\nTell me more!")



            elif pattern == "count to":
                print(Fore.LIGHTGREEN_EX + random.choice(patterns[pattern]))
                try:
                    number = int(re.findall(r'\d+', user_input)[0])
                    return count_numbers(number, patterns[pattern][1].format(number))
                except:
                    return "I'm sorry, I didn't catch the number you want me to count to."
            else:
                return random.choice(patterns[pattern])

    return "I'm sorry, I don't understand what you mean."


def count_numbers(number, message):
    output = ""
    for i in range(1, number + 1):
        output += str(i) + " "
        time.sleep(0)
    return message + " " + output


# main chat loop
print(Fore.LIGHTMAGENTA_EX + "Hi there! I am CodeIQ ACS.")
while True:
    user_input = input(Fore.WHITE + "\n> ")
    response = match_pattern(user_input)
    print(Fore.LIGHTGREEN_EX + response)
    if response == "Goodbye!" or response == "See you later.":
        break
