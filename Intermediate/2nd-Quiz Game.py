class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


# Quiz data
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The capital of France is Berlin.", "answer": "False"},
    {"text": "The human body has 206 bones.", "answer": "True"},
    {"text": "Python is a type of snake.", "answer": "True"},
    {"text": "The Sun revolves around the Earth.", "answer": "False"},
]

# Build question bank
question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

# Run quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
