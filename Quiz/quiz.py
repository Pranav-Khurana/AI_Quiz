from crewai import Crew, LLM, Process
from Quiz.agents import QuizAgents
from Quiz.tasks import QuizTasks


class QuizCrew:

    def __init__(self, ai_key: str):
        self.ai_key = ai_key
        self.llm = LLM(model="gemini/gemini-1.5-pro-002", api_key=self.ai_key)

    def run(self, topic: str, count: int):

        # Agents
        examiner = QuizAgents.examiner(self, topic, self.llm)
        teacher = QuizAgents.teacher(self, topic, self.llm)

        # Tasks
        gather_knowledge = QuizTasks.gather_knowledge(self, teacher, topic)
        mcq_questions = QuizTasks.mcq_questions(
            self, examiner, topic, count, [gather_knowledge]
        )
        short_questions = QuizTasks.short_questions(
            self, examiner, topic, count, [gather_knowledge]
        )

        crew = Crew(
            tasks=[gather_knowledge, short_questions, mcq_questions],
            agents=[teacher, examiner],
            process=Process.sequential,
            verbose=True,
            full_output=True,
        )

        result = crew.kickoff()
        return result
