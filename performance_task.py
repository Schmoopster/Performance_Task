#Performance Task
def medical_help(illness):
    medical_advice = {
        "covid-19": ["To treat yourself, do this: ", "Over-the-counter medications like acetaminophen and ibuprofen can help relieve fever and body aches.", "Staying hydrated is important.", "It is also important to avoid high-sugar drinks and processed foods."  ], 
        "flu": ["To treat yourself, do this: ", "Nasal Spray and humidifiers can relieve congestion and discomfort.", "Use cough suppressants for dry coughs or expectorants to loosen mucus in the throat.", "Natural remedies include chicken soup, ginger tea, and zinc supplements which may help ease symptoms and support immune function" ],
        "allergies": ["To treat yourself, do this: ", "Avoid exposure to allergens like pollen, dust mites, and pet dander.", "Use antihistamines or nasal sprays to reduce symptoms.", "Consult a doctor for severe or persistent allergies."],
    } #This is our list with the medical advice we will be referencing and referring to in the future
    
    if illness in medical_advice:
        for line in medical_advice[illness]:
            input(line)
    else:
        print("Sorry, we don't have treatment for that illness.")
print("Welcome! We are here to help you with medical advice!") 
choice = input("Do you need medical assistance? (yes/no) ")
if choice == "no":
    print("Okay, stay healthy and fit!")
while choice == "yes":
    print("We are here to help you!")
    question = input("Do you need help with a covid-19, flu, or allergies? ")
    medical_help(question)
    choice = input("Do you need more medical advice? (yes/finished) ")
if choice == "finished":
    rate = int(input("Please rate our service 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend our service to a friend? (yes/maybe/no) ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry we could not meet your expectations. ")


# def joke_game(joke_choice):
#     jokes = {
#         "wizards": ["Where does a scientist wizard work?", "In a labracadrabratory\U0001F923",  ], #"\U0001F923" Is code for the importation of an emoji
#         "bears": ["What do you call a bear with no teeth?", "A gummy bear\U0001F923", ],
#         "pirates": ["Why couldn’t the pirate find his playing cards?", "He was standing on the deck\U0001F923", ],
#     } #This is our list with the jokes we will be referencing and referring to in the future
    
#     if joke_choice in jokes:
#         for line in jokes[joke_choice]:
#             input(line)
#     else:
#         print("Sorry, we don't have that joke.")
# print("Welcome to the Joke Game!") 
# joke = input("Do you want to hear a joke? (yes/no) ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about wizards, bears, or pirates? ")
#     joke_game(question)
#     joke = input("Do you want to hear another joke or are you finished? (yes/finished) ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? (yes/maybe/no) ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")


