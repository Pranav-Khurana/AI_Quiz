import json
from Quiz.quiz import QuizCrew
from config import Config

if __name__ == "__main__":
    print("AI QUIZ GENERATOR")
    topic = input("Please provide a topic on which you want to generate a quiz: ")
    question_count = int(
        input("Please provide the number of questions you want me to generate: ")
    )
    my_quiz = QuizCrew(topic, question_count, Config.GEMINI_KEY)
    output = my_quiz.run()

    print("\n\nOUTPUT DETAILS:-")

    try:
        print(f"RAW:- \n  {output.raw}")
    except:
        print("Unable to Generate **raw** output")

    try:
        print(f"JSON DICT:- \n  {output.json_dict}")
    except:
        print("Unable to Generate **json_dict** output")

    try:
        print(f"PYDANTIC:- \n  {output.pydantic}")
    except:
        print("Unable to Generate **pydantic** output")

    try:
        print(f"TOKEN USAGE:- \n  {output.token_usage}")
    except:
        print("Unable to Generate **token_usage** output")

    try:
        print(f"TASKS OUTPUT:- \n  {output.tasks_output}")
    except:
        print("Unable to Generate **tasks_output** output")

    with open("QuizOutput/data.json", "w") as json_file:
        json.dump(output.raw, json_file, indent=4)

    print("AI QUIZ GENERATED")
