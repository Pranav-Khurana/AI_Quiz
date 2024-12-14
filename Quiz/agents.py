from crewai import Agent, LLM


class QuizAgents:

    def examiner(self, topic: str, llm: LLM):
        return Agent(
            role=f"Examiner",
            goal=f"Gather insights about {topic}",
            backstory=f"""An Expert in {topic}, having practial and theoretical knowledge about {topic} who can easily generate various types of questions on the important concepts of the {topic}""",
            verbose=True,
            llm=llm,
        )

    def teacher(self, topic: str, llm: LLM):
        return Agent(
            role=f"{topic} Expert",
            goal=f"Provide knowledge and insight on {topic}",
            backstory=f"""You are a briliant educator and an expert on {topic}. You can easily compile all information available about {topic} into short meaningful points.""",
            verbose=True,
            llm=llm,
        )
