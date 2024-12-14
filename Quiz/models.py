from typing import List
from pydantic import BaseModel


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
    mcq: MCQQuestions
    short_question: ShortQuestions
