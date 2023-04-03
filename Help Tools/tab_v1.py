# TabEditor_v1
import tkinter as tk
from tkinter import ttk

class TabEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TabEditor_v1')
        self.geometry('400x100+200+200')
        
        # Create Notebook
        self.new_count = 1
        self.notebook = ttk.Notebook(self)
        self.notebook.bind("<<NotebookTabChanged>>", self.handleTabChange)
        self.notebook.grid(sticky='news')
        # Tab + (adauga new tab)
        frame = tk.Frame()
        self.notebook.add(frame, text="+")
    
    # Fuction create tab    
    def handleTabChange(self, event):
        self.new_count += 1
        self.name = 'New' + str(self.new_count-1)
       
        if self.notebook.select() == self.notebook.tabs()[-1]:
            index = len(self.notebook.tabs())-1
            frame = tk.Frame(self.notebook)
            self.notebook.insert(index, frame, text=self.name)
            self.notebook.select(index)
            
        
if __name__ == "__main__":
    app = TabEditor()
    app.mainloop()
