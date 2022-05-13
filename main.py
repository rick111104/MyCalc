from tkinter import *

expression = ""


def press(num):

	global expression

	expression = expression + str(num)

	equation.set(expression)


def equalpress():

	try:

		global expression

		total = str(eval(expression))

		equation.set(total)

		expression = ""

	except:

		equation.set(" error ")
		expression = ""


def destroy():
	global expression
	expression = ""
	equation.set("")


if __name__ == "__main__":

	gui = Tk()

	gui.configure(background="orange")

	gui.title("Rick's Calculator")


	gui.geometry("500x500")

	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation)

	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(gui, text=' I ', fg='purple', bg='green',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' II ', fg='purple', bg='green',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' III ', fg='purple', bg='green',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' IV ', fg='purple', bg='green',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' V ', fg='purple', bg='green',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' VI ', fg='purple', bg='green',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' VII ', fg='purple', bg='green',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' VIII ', fg='purple', bg='green',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' IX ', fg='purple', bg='green',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' I - I ', fg='purple', bg='green',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='purple', bg='green',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='purple', bg='green',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='purple', bg='green',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='purple', bg='green',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='purple', bg='green',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Destroy', fg='purple', bg='green',
				command=destroy, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='purple', bg='green',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)

	gui.mainloop()