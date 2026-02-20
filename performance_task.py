#Performance Task
#Purpose- Help people with medical advice for covid-19, flu, and allergies that may not have access to a doctor or medical professional. This program will provide advice on how to treat these illnesses at home, and it will also ask for feedback from the user to improve the service.
                                                                  
medical_advice = {
    "covid-19": [
        "Over-the-counter medications like acetaminophen and ibuprofen can help relieve fever and body aches.",
        "Staying hydrated is important.",
        "Avoid high-sugar drinks and processed foods."
    ],

    "flu": [
        "Nasal spray and humidifiers can relieve congestion and discomfort.",
        "Use cough suppressants for dry coughs or expectorants to loosen mucus.",
        "Natural remedies like chicken soup, ginger tea, and zinc may help ease symptoms."
    ],

    "allergies": [
        "Avoid exposure to allergens like pollen, dust mites, and pet dander.",
        "Use antihistamines or nasal sprays to reduce symptoms.",
        "Consult a doctor for severe or persistent allergies."
    ]
} #This is our list with the medical advice we will be referencing and referring to in the future

def medical_help(illness): #This is the function that will provide the medical advice to the user based on the illness they are asking about.
    if illness in medical_advice: #This if statement will check if the illness the user is asking about is in our list of medical advice, and if it is, it will provide the advice to the user.
        print("To treat yourself, do this:")
        for line in medical_advice[illness]:
            input(line)  # pauses after each line
    else:
        print("Sorry, we don't have treatment for that illness.")

print("Welcome! We are here to help you with medical advice!")
choice = input("Do you need medical assistance? (yes/no) ") #This is the first question that the user will be asked, and it will determine if they will be able to get medical advice or not.
#Input is used to get the user's response to the question, and it will be stored in the variable choice for later use.

if choice == "no": #If the user selects no, this if statement will end the program and thank them for using our service.
    print("Okay, stay healthy and fit!")

while choice == "yes": #While the user selects yes, this while loop will allow them to ask for medical advice and it will continue to ask if they need more medical advice until they select finished.
    print("We are here to help you!")

    # Show available illnesses
    print("Available illnesses:", ", ".join(medical_advice.keys())) #This line will show the user the available illnesses that they can ask for medical advice about, and it will join the keys of the medical_advice dictionary with a comma and space for better readability.

    question = input("Which illness do you need help with? ")

    medical_help(question) #This line will call the medical_help function with the user's question as the argument, and it will provide the medical advice for that illness if it is available.

    if question in medical_advice: #This if statement will check if the user's question is in the medical_advice dictionary, and if it is, it will delete that illness from the dictionary so that it cannot be chosen again in the future.
        del medical_advice[question]

    if len(medical_advice) == 0: #This if statement will check if there are no more illnesses available in the medical_advice dictionary, and if there are not, it will print a message to the user and end the program.
        print("No more illnesses available.")
        choice = "finished"
        break #This break statement will exit the while loop if there are no more illnesses available, and it will set the choice variable to "finished" to indicate that the user is done with the medical advice.

    choice = input("Do you need more medical advice? (yes/finished) ")

if choice == "finished": 
    rate = int(input("Please rate our service 1–10: ")) #This line will ask the user to rate our service on a scale of 1 to 10, and it will convert the user's input into an integer for later use in calculating the final score.
    final_score = rate * 10
    print(str(final_score) + "% satisfaction rate") #This line will calculate the final score by multiplying the user's rating by 10, and it will print the final score as a percentage.

    friend = input("Would you recommend our service to a friend? (yes/maybe/no) ") #This line will ask the user if they would recommend our service to a friend, and it will store their response in the variable friend for later use in providing feedback.

    if friend == "yes" or friend == "maybe": #This if statement will check if the user's response is "yes" or "maybe", and if it is, it will print a message thanking them for their feedback and appreciation for recommending our service to a friend.
        print("Thanks, we appreciate it.")
    else:
        print("Sorry we could not meet your expectations.")
