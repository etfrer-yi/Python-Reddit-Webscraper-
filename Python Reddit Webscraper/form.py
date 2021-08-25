# Code derived from Tkinter documentation and possibly other Stackoverflow posts

from tkinter import *
from tkinter import ttk

class Form():

    reddit_categories = ["hot", "gilded", "controversial", "new", "rising", "top"]
    title_or_content = ["content", "title"]

    def __init__(self, form_name):
        self.window = Tk()
        self.window.title(form_name)
        self.window.geometry('300x150')
        self.window.configure(background = "grey")
        self.form_fields = {}
        self.category_variable = StringVar(self.window, self.reddit_categories[0])
        self.title_or_content_variable = StringVar(self.window, self.title_or_content[0])

    def generate_crawler_info_form(self):
        window = self.window

        # Labels
        self.subreddit = Label(window , text = "Which subreddit? ", anchor = 'w', width = 20).grid(row=0, column=0)
        self.category = Label(window , text = "Which category?", anchor = 'w', width = 20).grid(row=1, column=0)
        self.title_or_content = Label(window, text = "Post titles or content?", anchor = 'w', width = 20).grid(row=2, column=0)
        self.post_limit = Label(window, text = "How many posts?", anchor = 'w', width = 20).grid(row=3, column=0)

        # Entries
        self.subreddit_input_area = Entry(window)
        self.subreddit_input_area.grid(row=0, column=1, sticky="ew")
        self.post_limit_input_area = Entry(window)
        self.post_limit_input_area.grid(row=3, column=1, sticky="ew")
        
        # Option Menus 
        self.category_input_area = OptionMenu(window, self.category_variable, *Form.reddit_categories)
        self.category_input_area.grid(row=1, column=1, sticky="ew")
        self.title_or_content_input_area = OptionMenu(window, self.title_or_content_variable, *Form.title_or_content)
        self.title_or_content_input_area.grid(row=2, column=1, sticky="ew")

        # Buttons
        self.submit_button = Button(window, text = "Submit", command = self.submit).grid(row=4, column = 0, columnspan = 3)

        # Start window 
        window.mainloop()

    def submit(self):
        self.form_fields['subreddit'] = self.subreddit_input_area.get()
        self.form_fields['category'] = self.category_variable.get()
        self.form_fields['title_or_content'] = self.title_or_content_variable.get()
        self.form_fields['post_limit'] = self.post_limit_input_area.get()
        self.window.destroy()
        
    def get_form_fields(self):
        return self.form_fields