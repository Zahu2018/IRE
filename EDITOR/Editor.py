# Editor v1
'''
-------------------------------------------
| Menu           frame_menu           | X |
-------------------------------------------
| Tabbs / + /    frame_editor             |
-------------------------------------------
| Text Editor    frame_editor             |
|                                         |
|                                         |
|                                         |
|                                         |
-------------------------------------------
| Consola        frame_consola            |
-------------------------------------------
'''
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from hashlib import md5
import os

class Document:
    '''Item in dictionar tabs unde se pastreaza tab+continut.'''
    def __init__(self, TextWidget, FileDir): # frame+scroll, New1
        self.file_dir = FileDir
        self.file_name = os.path.basename(FileDir)
        self.textbox = TextWidget
        self.status = md5(self.textbox.get(1.0, 'end').encode('utf-8'))


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor_v1')
        self.geometry('400x100+200+200')

        ### =================================================================       
        ### MENUBAR
        ### =================================================================
        frame_menu = tk.Frame(self)
        frame_menu.grid( row=0, column=0, sticky='ew')
        
        mainmenu = tk.Menu(frame_menu)
        self.config(menu = mainmenu)
        
        ### File Menu
        filemenu = tk.Menu(frame_menu, tearoff=0)
        filemenu.add_command(label = "New File", command=self.new_file)
        filemenu.add_command(label = "Save", command=self.func)
        filemenu.add_command(label = "Load", command=self.func)
        filemenu.add_separator()
        # Submenu Export
        exportmenu = tk.Menu(frame_menu, tearoff=0)
        exportmenu.add_command(label="Export as .PDF", command=self.func)
        exportmenu.add_command(label="Export as .JPG", command=self.func)
        exportmenu.add_command(label="Export as .MP4", command=self.func)
        filemenu.add_cascade(label = "Export", menu = exportmenu)
        mainmenu.add_cascade(label = "File", menu = filemenu)
        
        ### Edit Menu
        editmenu = tk.Menu(frame_menu, tearoff=0)
        editmenu.add_command(label = "Copy", command=self.func)
        mainmenu.add_cascade(label = "Edit", menu = editmenu)
        
        ### =================================================================       
        ### TEXT EDITOR
        ### =================================================================
        self.tabs = {} # { index: text widget }
        self.untitled_count = 1

        self.frame_editor = tk.Frame(self, bg='#FFFFFF')
        self.frame_editor.grid(row=1, column=0, sticky='news')
        
        # Create Notebook bar ( for tabs ).
        self.nb = ttk.Notebook(self.frame_editor)
        self.nb.grid(sticky='news')
        self.nb.enable_traversal()
        self.nb.bind("<<NotebookTabChanged>>", self.tab_change)
        
        # Create Initial Tab
        first_tab = tk.Frame(self.nb)
        self.nb.add(first_tab, text='New')
        self.first_tab = self.create_text_widget(first_tab)
        

        ### =================================================================       
        ### CONSOLA
        ### =================================================================
        frame_console = tk.Frame(self)
        frame_console.grid(row=2, column=0, sticky='we')
        
    ### =================================================================       
    ### FUNCTII
    ### =================================================================
    
    # MENU -> FILE
    def new_file(self):                
        # Create new tab
        new_tab = tk.Frame(self.nb)
        self.nb.add(new_tab, text='Unu')
        self.nb.insert(self.nb.index[-1], text='Unu')
        self.tabs[new_tab] = self.create_text_widget(new_tab)
        #self.tabs[new_tab].textbox.config(wrap='word' if self.word_wrap.get() else 'none')
        #self.nb.insert(self.nb.index('end')-1, new_tab, text=self.tabs[new_tab].file_name)
        #self.nb.select(new_tab)
    
    def tab_change(self, event):
        # If last tab was selected, create new tab
        if self.nb.select() == self.nb.tabs()[-1]:
            self.new_file()

        
    def default_filename(self, *args):
        self.untitled_count += 1
        return 'New' + str(self.untitled_count-1)
        
               
    def create_text_widget(self, frame):
        # Horizontal Scroll Bar 
        xscrollbar = tk.Scrollbar(frame, orient='horizontal')
        xscrollbar.pack(side='bottom', fill='x')
        
        # Vertical Scroll Bar
        yscrollbar = tk.Scrollbar(frame)
        yscrollbar.pack(side='right', fill='y')

        # Create Text Editor Box
        textbox = tk.Text(frame, relief='sunken', borderwidth=0, wrap='none')
        textbox.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, undo=True, autoseparators=True)

        # Keyboard / Click Bindings
        textbox.bind('<Control-s>', self.save_file)
        textbox.bind('<Control-o>', self.open_file)
        textbox.bind('<Control-n>', self.new_file)
        textbox.bind('<Control-a>', self.select_all)
        textbox.bind('<Control-w>', self.close_tab)
        textbox.bind('<Button-3>', self.right_click)

        # Pack the textbox
        textbox.pack(fill='both', expand=True)        
        
        # Configure Scrollbars
        xscrollbar.config(command=textbox.xview)
        yscrollbar.config(command=textbox.yview)
       
        return textbox


    def func(self):
        ...
    def select_all(self):
        ...
    def right_click(self):
        ...
    def new_file(self):
        ...
    def save_file(self):
        ...
    def open_file(self):
        ...
    def close_tab(self):
        ...
    def move_tab(self):
        ...
    def tab_change(self):
        ...

        
if __name__ == "__main__":
    app = Editor()
    app.mainloop()
