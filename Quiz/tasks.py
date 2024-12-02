from crewai import Task
from textwrap import dedent


class QuizTasks:

    def create_questions(self, agent, topic, count):
        print("Create Question Task Started")
        return Task(
            description=dedent(
                f"""Do a research on {topic} and generate {count} unique multiple choice questions on the provided topic. 
            Make sure all questions are unique. All mcq questions should have four different choices as answer.
            Make sure all the questions have 1 correct choice and 3 incorrect choices."""
            ),
            expected_output="""You should return a json list of question dictionary in the following format:
                                   {[ question_statement:
                                        {
                                            correct: correct choice, 
                                            incorrect: [incorrect choices]
                                        }
                                   ]}""",
            agent=agent,
        )
