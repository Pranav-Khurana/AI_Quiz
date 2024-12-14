import json, os
from datetime import datetime
from Quiz.quiz import QuizCrew
from config import Config

if __name__ == "__main__":
    print("AI QUIZ GENERATOR")
    topic = input("Please provide a topic on which you want to generate a quiz: ")
    question_count = int(
        input("Please provide the number of questions you want me to generate: ")
    )
    my_quiz = QuizCrew(Config.GEMINI_KEY)
    output = my_quiz.run(topic, question_count)

    os.makedirs("QuizOutput", exist_ok=True)
    filename = f"QuizOutput/{topic.replace(' ','_')}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    with open(filename, "w") as json_file:
        json.dump(output, json_file, indent=4)

    print("AI QUIZ GENERATED AND FILE SAVED IN QUIZOUTPUT")
