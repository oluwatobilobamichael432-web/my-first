def gather_information():
    # using questions to determine the persons behaviour instead of directly asking them how they behave.
    questions = {
        "honesty": [
            "Do you tell the truth even when it could get you into trouble?",
            "Have you ever deliberately lied about something important?"
        ],
        "respect": [
            "Do you respect other people's boundaries?",
            "Do you sometimes dismiss other people's opinions or values?"
        ],
        "trust": [
            "Do you keep promises and commitments you make to others?",
            "Have you ever shared something someone told you in confidence without their permission?"
        ],
        "emo_intel": [
            "Do you consider how your actions and words affect other people's feelings?",
            "Do you struggle to remain calm when disagreements arise?"
        ],
        "ambition": [
            "Do you actively work towards achieving your personal goals?",
            "Do you give up easily when faced with challenges?"
        ],
        "networking_value": [
            "Do you actively build relationships with people who can create meaningful opportunities?",
            "Are you willing to connect people in your network when you believe they could benefit from knowing each other?"
        ],
        "exposure": [
            "Are you willing to share your knowledge and expertise with others?",
            "Do you actively seek opportunities to learn new skills and gain knowledge?"
        ],
        "growth_mindset": [
            "Are you willing to acknowledge your mistakes and learn from them?",
            "Do you encourage the people around you to improve themselves?"
        ],
        "influence": [
            "Do you consciously try to set a positive example for the people around you?",
            "Have you ever encouraged someone to make a decision you knew could harm them?"
        ],
        "reputation": [
            "Do you make an effort to maintain a good reputation through your actions?",
            "Have your actions ever damaged the trust people have in you?"
        ]
    }

    answers = {}

    for parameter, questions_list in questions.items():
        #print(f"\n--- {parameter.upper()} ---")
        answers[parameter] = []

        for question in questions_list:
            #Using a while loop to continously ask the question as long as questions remain.
            while True:
                response = input(question + " (Options: Yes/Sometimes/No): ").lower().strip()
                # Just incase the user enters a wrong/invalid input.
                if response in ["yes", "sometimes", "no"]:
                    answers[parameter].append(response)
                    break

                print("Invalid response. Try again.")

    return answers


def calculate_scores(answers):
    scores = {}

    # The second question in each pair is negatively worded.
    for parameter, responses in answers.items():
        positive_score = {
            "yes": 5,
            "sometimes": 2.5,
            "no": 0
        }

        negative_score = {
            "yes": 0,
            "sometimes": 2.5,
            "no": 5
        }

        scores[parameter] = (
            positive_score[responses[0]] +
            negative_score[responses[1]]
        )

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

#Just some little bit of extras i added on my own to show how everything was scored.
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

print("\n========== EVALUATION ==========")

for parameter, score in scores.items():
    print(f"{parameter}: {score}/10")

print(f"\nTotal Score: {total}/100")
print(f"Final Evaluation: {grade}")