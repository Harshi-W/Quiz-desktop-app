from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Interface:


    def __init__(self, quiz_brain: QuizBrain ):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR, )


        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=200, background="white")
        self.question = self.canvas.create_text(150,125,width=280, text="bla bla bla", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.image_left = PhotoImage(file="images/true.png")
        self.button_left = Button(highlightthickness=0, image=self.image_left, command=self.get_answer_true)
        self.button_left.grid(column=0, row=2, pady=10)

        self.image_ryt = PhotoImage(file="images/false.png")
        self.button_ryt = Button(highlightthickness=0, image=self.image_ryt, command=self.get_answer_wrong)
        self.button_ryt.grid(column=1, row=2, pady=10)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="Questions are over..")
            self.button_left.config(state="disabled")
            self.button_left.config(state="disabled")



    def get_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def get_answer_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="red")
        else:
            self.canvas.config(background="blue")

        self.window.after(1000, self.get_next_q)



