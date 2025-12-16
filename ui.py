from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", font=("Arial", 20), bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150, 125, text="French", font=("Arial", 20, "italic"), width=280)

        tick_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=tick_image, bg=THEME_COLOR, command=self.check_correct)
        self.correct_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, bg=THEME_COLOR, command=self.check_wrong)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reach the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_background)

    def reset_background(self):
        self.canvas.config(bg="white")
        self.get_next_question()