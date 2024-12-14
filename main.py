import json
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

    print("\n\nOUTPUT DETAILS:-")

    try:
        print(f"TOKEN USAGE:- \n  {output.token_usage}")
    except:
        print(
            "Unable to Generate **token_usage** output",
            end="-" * 10 + "start" + "-" * 10 + "\n",
        )

    for output in output.tasks_output:
        print(
            f"Agent: {output.agent} \n JSON: {output.json_dict}", end="-" * 30 + "\n\n"
        )

    # with open("QuizOutput/data.json", "w") as json_file:
    #     json.dump(output.raw, json_file, indent=4)

    print("AI QUIZ GENERATED")
