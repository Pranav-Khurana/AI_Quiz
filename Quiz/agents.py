from crewai import Agent


class QuizAgents:

    def generate_question(self, topic, llm):
        print("Generate Question Agent Triggered")
        return Agent(
            role=f"{topic} Expert",
            goal=f"Gather insights about {topic}",
            backstory=f"""An Expert in {topic}, having practial and theoretical knowledge about {topic} who can easily generate Multiple Choice Questions on the important concepts of the {topic}""",
            verbose=True,
            llm=llm,
        )
