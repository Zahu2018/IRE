# TabEditor_v2
# v2 adaugam editorul
# TODO - Fix
#   - New 1, New 2, ...
#   - Tab Size to 4

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class TabEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TabEditor_v2')
        #self.geometry('500x450+200+200')
        
        # Create Notebook
        self.new_count = 1
        self.notebook = ttk.Notebook(self)
        self.notebook.bind("<<NotebookTabChanged>>", self.addNewTab)
        self.notebook.grid(sticky='news')
        # Tab + (adauga new tab)
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="+")
    
    # Fuction create tab    
    def addNewTab(self, event):
        self.new_count += 1
        self.name = 'New ' + str(self.new_count-1)
        if self.notebook.select() == self.notebook.tabs()[-1]:
            index = len(self.notebook.tabs())-1
            frame = tk.Frame(self.notebook)
            # Expand Text Area when resize window
            self.grid_rowconfigure(0, weight=1)   
            self.grid_columnconfigure(0, weight=1) 
            frame.grid_rowconfigure(0, weight=1)        
            frame.grid_columnconfigure(0, weight=1)
            # Create Text Area 
            text_area = scrolledtext.ScrolledText(frame, wrap = tk.WORD, 
                                                  width = 60, height = 30, 
                                                  font = ("Consolas",9))
            text_area.grid(row=0, column=0, sticky='news')
            text_area.focus()
            self.notebook.insert(index, frame, text=self.name)
            self.notebook.select(index)
            
            
        
if __name__ == "__main__":
    app = TabEditor()
    app.mainloop()
