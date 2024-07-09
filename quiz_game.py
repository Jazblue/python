def ask_question(question, correct_answer):
    answer = input(question + " ").strip().lower()
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("Incorrect.")
        return False

def main():
    print("Welcome to my computer quiz!")
    
    playing = input("Do you want to play? ").strip().lower()
    if playing != "yes":
        print("Maybe next time! Goodbye!")
        quit()
    
    print("Okay! Let's play :)")
    
    questions = {
        "What does CPU stand for?": "central processing unit",
        "What does GPU stand for?": "graphics processing unit",
        "What does RAM stand for?": "random access memory",
        "What does PSU stand for?": "power supply unit"
    }
    
    score = 0
    
    for question, correct_answer in questions.items():
        if ask_question(question, correct_answer):
            score += 1
    
    print(f"You got {score} questions correct!")
    print(f"You got {score / len(questions) * 100}%")
    
if __name__ == "__main__":
    main()
