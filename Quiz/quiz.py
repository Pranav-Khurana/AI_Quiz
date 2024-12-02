from crewai import Crew, LLM
from Quiz.agents import QuizAgents
from Quiz.tasks import QuizTasks


class QuizCrew:

    def __init__(self, topic, count, ai_key):
        self.topic = topic
        self.count = count
        self.ai_key = ai_key
        self.llm = LLM(model="gemini/gemini-1.5-pro-002", api_key=self.ai_key)

    def run(self):
        agent = QuizAgents.generate_question(self, self.topic, self.llm)
        task = QuizTasks.create_questions(self, agent, self.topic, self.count)
        crew = Crew(agents=[agent], tasks=[task], verbose=True, full_output=True)
        result = crew.kickoff()
        return result
