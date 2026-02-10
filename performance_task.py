#Performance Task
def medical_help(illness):
    medical_advice = {
        "covid-19": ["To treat yourself, do this: ", "Over-the-counter medications like acetaminophen and ibuprofen can help relieve fever and body aches.", "Staying hydrated is important.", "It is also important to avoid high-sugar drinks and processed foods."  ], 
        "flu": ["To treat yourself, do this: ", "Nasal Spray and humidifiers can relieve congestion and discomfort.", "Use cough suppressants for dry coughs or expectorants to loosen mucus in the throat.", "Natural remedies include chicken soup, ginger tea, and zinc supplements which may help ease symptoms and support immune function" ],
        "allergies": ["To treat yourself, do this: ", "Avoid exposure to allergens like pollen, dust mites, and pet dander.", "Use antihistamines or nasal sprays to reduce symptoms.", "Consult a doctor for severe or persistent allergies."],
    } #This is our list with the medical advice we will be referencing and referring to in the future
    
    if illness in medical_advice:
        for line in medical_advice[illness]:
            input(line) #This will show the user the medical advice for the illness they are asking about.
    else:
        print("Sorry, we don't have treatment for that illness.") # This shows the user that we do not have advice for the illness they are asking about.
print("Welcome! We are here to help you with medical advice!") #This is the welcome message for the user when they start the program.
choice = input("Do you need medical assistance? (yes/no) ") #This is the first question that the user will be asked, and it will determine if they will be able to get medical advice or not.
if choice == "no":
    print("Okay, stay healthy and fit!") #This if statement wil end the program if the user does not need medical help.
while choice == "yes":
    print("We are here to help you!")
    question = input("Do you need help with a covid-19, flu, or allergies? ")
    medical_help(question)
    choice = input("Do you need more medical advice? (yes/finished) ") #This while loop will allow the user to ask for more medical advice if they need it, and it will end the program if they are finished.
if choice == "finished":
    rate = int(input("Please rate our service 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend our service to a friend? (yes/maybe/no) ") #This is the final question of the program, and it will ask the user if they would recommend our service to a friend.

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry we could not meet your expectations. ") #This is the end of the program, and it will thank the user for their feedback or apologize if they were not satisfied with the service.