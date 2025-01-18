from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 10, "normal")



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text="Some text",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(row=2, column=1)
        score = 0
        self.score_label = Label(
            self.window,
            text=f"Score: {score}",
            font=FONT_SCORE,
            bg=THEME_COLOR,
            fg="white"
        )
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_question)
        else:
            messagebox.showinfo(
                title="Finished!",
                message=f"Thank you for playing!\nFinal score: {self.quiz.score}"
            )
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def answer_true(self):
        if self.quiz.check_answer(True):
            messagebox.showinfo(title="Correct!", message="Congratulations, you got it right!")
            self.canvas.config(bg="green")
        else:
            messagebox.showinfo(title="Wrong!", message="Sorry, you got it wrong!")
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def answer_false(self):
        if self.quiz.check_answer(False):
            messagebox.showinfo(title="Correct!", message="Congratulations, you got it right!")
            self.canvas.config(bg="green")
        else:
            messagebox.showinfo(title="Wrong!", message="Sorry, you got it wrong!")
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

