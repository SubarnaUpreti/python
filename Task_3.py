import random


def random_str(x):
    return random.choice(x)


def check_mail(mail='', domain=''):
    message = "is invalid at"
    validity = False
    if len(mail.split('@')) == 2:
        username, mail_dom = mail.split('@')
        if len(username) >= 2 and mail_dom == domain:
            message = "is valid at"
            validity = True
    print(f"{mail} {message} {domain}.")
    return validity


def get_name(mail=''):
    return mail.split('@')[0].split('.')[0].capitalize()


def system_program():
    operator_list = ["Janice", "Mark", "Lucy", "Fiona", "Candace", "Tina", "Ruby", "Paul", "Henry"]
    function_words = ["library", "wifi", "deadline"]
    random_phrase = ["Hmmm", "Oh, yes, I see", "Tell me more", "That's great", "Nice one", "Sure, that will be good"]
    exit_words = ["bye", "exit", "quit", "cancel", "help"]
    error_chance = 10
    print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")
    mail = input("Please enter your Poppleton email address: ")
    if check_mail(mail, "pop.ac.uk"):
        print(f"Hi, {get_name(mail)}! Thank you, and Welcome to PopChat!")
        print(f"My name is {random_str(operator_list)}, and it will be my pleasure to help you.")
        while True:
            if random.choices([True, False], [error_chance, 100-error_chance], k=1)[0]:
                print("*** NETWORK ERROR ***")
                break
            x = input("--->")
            if any(word.lower() in x.lower() for word in function_words):
                if "library" in x.lower():
                    print("The library is closed today.")
                elif "wifi" in x.lower():
                    print("WiFi is excellent across the campus.")
                elif "deadline" in x.lower():
                    print("Your deadline has been extended by two working days.")
            elif any(word.lower() in x.lower() for word in exit_words):
                break
            else:
                print(f"{random_str(random_phrase)}")
        print(f"\nThanks, {get_name(mail)}, for using PopChat. See you again soon!")
    else:
        print("Sorry, you don't have access to PopChat")


if __name__ == '__main__':
    system_program()
