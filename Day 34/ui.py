from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}",  # {QuizBrain(data.question_data).score}
                           bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Question",
                                                font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_button_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, command=self.answer_true)
        self.right_button.grid(row=2, column=0)

        wrong_button_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.answer_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(400, self.get_next_question)
