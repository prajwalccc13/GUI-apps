from tkinter import *
from tkinter import filedialog
import wikipedia
import tkinter.messagebox
from io import StringIO


class text_editor:
    current_open_file = "no_file"

    def open_file(self):
        open_return = filedialog.askopenfile(initialdir = "/",title = "Select file to open", filetypes = (("text files","*.txt"),("all files","*.*")))
        if(open_return != None):
            self.text_area.delete(1.0, END)
            for line in open_return:
                guess_lexer_for_filename(open_return)
            self.current_open_file = open_return.name
            open_return.close()


    def save_as_file(self):
        f = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
        if f is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()


    def save_file(self):
        if self.current_open_file == "no_file":
            self.save_as_file()
        else:
            f = open(self.current_open_file, "w+")
            f.write(self.text_area.get(1.0, END))
            f.close()


    def new_file(self):
        self.text_area.delete(1.0, END)
        self.current_open_file = "no_file"


    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())


    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")


    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())





    def search_wiki(self):
        def get_me():
            entry_value = entry.get()
            answer.delete(1.0, END)
            print("a")
            try:
                answer_value = wikipedia.summary(entry_value)
                answer.insert(INSERT, answer_value)
                print("b")
            except:
                answer.insert(INSERT, "Please check your input or inernet connection")

        top = Toplevel()
        top.title("Search in Wikipedia")

        topframe = Frame(top)

        entry = Entry(topframe)
        entry.pack()

        button = Button(topframe, text = "Search", command = get_me)
        button.pack()

        topframe.pack()

        scroll = Scrollbar(topframe)
        scroll.pack(side = RIGHT, fill = Y)
        answer = Text(topframe, width = 100, height = 30, yscrollcommand = scroll.set, wrap = WORD)
        scroll.config(command = answer.yview)
        answer.pack()



    def run(self):
        try:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(self.text_area.get(1.0, END))
            sys.stdout = old_stdout
            tkinter.messagebox.showinfo("Result", redirected_output.getvalue())
        except SyntaxError:
            tkinter.messagebox.showinfo("Result", "SyntaxError: unexpected EOF while parsing")


    def user_Guide(self):
        top = Toplevel()
        top.title("User Guide")
        text = Text(top)
        text.pack()
        f = open("/home/prajwal/python-test/pythonTkinter/writeOn/userGuide.txt", "r")
        for line in f:
            text.insert(END, line)




    def about_us(self):
        top = Toplevel()
        top.title("About Us")
        text = Text(top)
        text.pack()
        f = open("/home/prajwal/python-test/pythonTkinter/writeOn/aboutUs.txt", "r")
        for line in f:
            text.insert(END, line)



    def __init__(self, master): # self = its object i.e t"e" here
        self.master = master
        master.title("WriteOn")

        self.frame = Frame(self.master)
        self.scrolla = Scrollbar(self.frame)
        self.scrolla.pack(side = RIGHT, fill = Y)
        self.text_area = Text(self.master,yscrollcommand = self.scrolla.set, wrap = WORD, undo = True)
        self.scrolla.config(command = self.text_area.yview)
        self.text_area.pack(fill = BOTH, expand = 1)

        self.main_menu = Menu()
        self.master.config(menu = self.main_menu)

        #creating file_menu
        self.file_menu = Menu(self.main_menu, tearoff = False,)
        self.main_menu.add_cascade(label = "     File     ", menu = self.file_menu)
        self.file_menu.add_command(label = "New File", command = self.new_file)
        self.file_menu.add_command(label = "Open File", command = self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Save As", command = self.save_as_file)
        self.file_menu.add_command(label = "Save", command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = master.quit)

        #creating edit_menu
        self.edit_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "     Edit     ", menu = self.edit_menu)
        self.edit_menu.add_command(label = "Undo", command = self.text_area.edit_undo)
        self.edit_menu.add_command(label = "Redo", command = self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label = "Copy", command = self.copy_text)
        self.edit_menu.add_command(label = "Cut", command = self.cut_text)
        self.edit_menu.add_command(label = "Paste", command = self.paste_text)

        #creating compile_menu
        self.compile_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "   Compile   ", menu = self.compile_menu)
        self.compile_menu.add_command(label = "Compile and Run", command =  self.run)

        #creating search_menu
        self.search_menu = Menu(self.main_menu,tearoff = False)
        self.main_menu.add_cascade(label = "    Search    ", menu = self.search_menu)
        self.search_menu.add_command(label = "Find")
        self.search_menu.add_command(label = "Search in Wikipedia", command = self.search_wiki)

        #creating help_menu
        self.help_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "     Help     ", menu = self.help_menu)
        self.help_menu.add_command(label = "User Guide", command = self.user_Guide)
        self.help_menu.add_command(label = "About", command = self.about_us)


root = Tk()

te = text_editor(root)

root.geometry("1200x680+200+200")

root.mainloop()
