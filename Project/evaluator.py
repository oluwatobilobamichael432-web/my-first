def gather_information():
    # using questions to determine the persons behaviour instead of directly asking them how they behave.
    questions = {
        "honesty": ["On a scale of 1 to 10 how often do you tell the truth even when it could get you into trouble?"],

        "respect": ["On a scale of 1 to 10 how often do you respect other people's boundaries?"],

        "trust": ["On a scale of 1 to 10 how often do you keep promises and commitments you make to others?"],

        "emo_intel": ["On a scale of 1 to 10 how often do you consider how your actions and words affect other people's feelings?"],

        "ambition": ["On a scale of 1 to 10 how often do you actively work towards achieving your personal goals?"],

        "networking_value": ["On a scale of 1 to 10 how often do you actively build relationships with people who can create meaningful opportunities?"],

        "exposure": ["On a scale of 1 to 10 how often will you be willing to share your knowledge and expertise with others?"],

        "growth_mindset": ["On a scale of 1 to 10 how often will you be willing to acknowledge your mistakes and learn from them?"],

        "influence": ["On a scale of 1 to 10 how often do you consciously try to set a positive example for the people around you?"],

        "reputation": ["On a scale of 1 to 10, how frequently do your actions cause people to lose trust in you?"]

    }

    answers = {}

    for parameter, questions_list in questions.items():
        #print(f"\n--- {parameter.upper()} ---")
        answers[parameter] = []

        for question in questions_list:
            #Using a while loop to continously ask the question as long as questions remain.
            while True:
                try:
                    user_input = input(question + "\n")

                    if user_input.strip() == "":
                        print("Input cannot be empty. Please try again.")
                        continue
                    response = int(user_input)
                    # Just incase the user enters a wrong/invalid input.
                    if response >= 1 and response <= 10:
                        answers[parameter].append(response)
                        break

                    print("Input out of range. Try again.")
                except ValueError:
                    print("Invalid input, please enter a number.")

    return answers


def calculate_scores(answers):
    scores = {}

    for parameter, response in answers.items():
        if parameter == "reputation":
            scores[parameter] = 11 - response[0]
        else:
            scores[parameter] = response[0]

    return scores


def friendship_evaluator(
    honesty, respect, trust, emo_intel, ambition,
    networking_value, exposure, growth_mindset,
    influence, reputation
):
    total = (
        honesty + respect + trust + emo_intel + ambition +
        networking_value + exposure + growth_mindset +
        influence + reputation
    )

    if total >= 70:
        grade = "Great choice"
    elif total >= 40:
        grade = "Safe to proceed"
    else:
        grade = "Proceed with caution"

    return total, grade

#Just some little bit of extras i added on my own to show how everything was scored and a welcome message.
while True:
    start = input("Wellcome to Friendship Evaluator!, I will be asking you some questions and i need you to be very honest while answering them!, Thank you\nReply to this message with (Proceed) to continue or (Quit) to stop. ")

    if start.lower().strip() == "proceed":
        break
    elif start.lower().strip() == "quit":
        print("You dey go na😏, who even dey find you self😂😂")
        exit()
    else:
        print("Invalid option please try again!\n")

answers = gather_information()
scores = calculate_scores(answers)

total, grade = friendship_evaluator(
    scores["honesty"],
    scores["respect"],
    scores["trust"],
    scores["emo_intel"],
    scores["ambition"],
    scores["networking_value"],
    scores["exposure"],
    scores["growth_mindset"],
    scores["influence"],
    scores["reputation"]
)

print("\n\033[4mEVALUATION IN CHARACTER\033[0m\n")

for parameter, score in scores.items():
    print(f"{parameter}: {score}/10")

print(f"\nTotal Score: {total}/100")
print(f"Final Evaluation: {grade}")