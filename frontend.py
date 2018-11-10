from tkinter import *
from backend import Database


database = Database("todo_list.db")


class Window(object):

	def __init__(self, window):
		self.window = window
		self.window.wm_title("// TODO")

		l1 = Label(window, text='Entry')
		l1.grid(row=0)

		self.entry = StringVar()
		self.e1 = Entry(window, textvariable=self.entry)
		self.e1.grid(row=0, column=1)

		# List box and scroll bar for it.
		self.lb = Listbox(window, height=8, width=40)
		self.lb.grid(row=2, column=0, rowspan=10, columnspan=5)

		sb = Scrollbar(window)
		sb.grid(row=2, column=6, rowspan=8)

		self.lb.configure(yscrollcommand=sb.set)
		sb.configure(command=self.lb.yview)

		self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

		# Buttons.
		b1=Button(window, text='Add New', width=14, command=self.add_command)
		b1.grid(row=0, column=7)

		b2=Button(window, text='Refresh / View All', width=14, command=self.view_command)
		b2.grid(row=7, column=7)

		b3=Button(window, text='Edit Selected', width=14, command=self.edit_command)
		b3.grid(row=8, column=7)

		b4=Button(window, text='Delete Selected', width=14, command=self.delete_command)
		b4.grid(row=9, column=7)

		b5=Button(window, text='Close', width=14, command=window.destroy)
		b5.grid(row=10, column=7)

	# Helper for when selecting items from the list is needed.
	def get_selected_row(self, event):
		try:
			index = self.lb.curselection()[0]
			self.selected_tuple = self.lb.get(index)
			self.e1.delete(0, END)
			self.e1.insert(END, self.selected_tuple[1])
			self.e2.delete(0, END)
			self.e2.insert(END, self.selected_tuple[2])
			self.e3.delete(0, END)
			self.e3.insert(END, self.selected_tuple[3])
			self.e4.delete(0, END)
			self.e4.insert(END, self.selected_tuple[4])
		# Bypass useless index error.
		except IndexError:
			pass

	# Adding functionality to the buttons.
	def view_command(self):
		self.lb.delete(0 ,END)
		for row in database.view():
			self.lb.insert(END,row)

	def add_command(self):
		database.insert(self.entry.get())
		self.lb.delete(0, END)
		self.lb.insert(END, (self.entry.get()))

	def delete_command(self):
		database.delete(self.selected_tuple[0])

	def edit_command(self):
		database.edit(self.selected_tuple[0], self.entry.get())


# Creating the window object.
window = Tk()
Window(window)

# All done!
window.mainloop()
