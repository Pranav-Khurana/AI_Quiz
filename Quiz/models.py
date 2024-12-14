from typing import List, Union
from pydantic import BaseModel
from crewai.types.usage_metrics import UsageMetrics


class Points(BaseModel):
    heading: str
    content: List[str]


class Info(BaseModel):
    topic: str
    points: List[Points]


class ShortQuestion(BaseModel):
    question_statement: str
    associated_marks: int
    difficulty_level: str
    answer: str


class ShortQuestions(BaseModel):
    short_answer_questions: List[ShortQuestion]


class MCQAnswer(BaseModel):
    correct: str
    incorrect: List[str]


class MCQQuestion(BaseModel):
    question_statement: str
    associated_marks: int
    difficulty_level: str
    answers: MCQAnswer


class MCQQuestions(BaseModel):
    multiple_choice_questions: List[MCQQuestion]


class Article(BaseModel):
    information: Info
    questions: List[Union[ShortQuestions, MCQQuestions]]
    token_usage: UsageMetrics
