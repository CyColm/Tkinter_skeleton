# -*- coding: utf-8 -*-

from ihm import mainWindow as mw
import tkinter as tk
from tkinter import filedialog


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.container = tk.Frame(self)
        self.container.pack(expand=True)

        # Label
        label1 = tk.Label(self.container,
                          text='Select a file :')
        label1.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)

        # Entry
        self.entry1_content = tk.StringVar()
        entry1 = tk.Entry(self.container, textvariable=self.entry1_content)
        entry1.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

        # Text
        self.text1 = tk.Text(self.container)
        self.text1Content = 'Hello World!'
        self.setText1Content(self.text1Content)
        self.text1.grid(row=3, column=0, columnspan=3)

        # Buttons
        btn1 = tk.Button(self.container, text="...",
                         command=lambda: self.setEntry1Content())
        btn1.grid(row=1, column=2, sticky=tk.E)

        btn2 = tk.Button(self.container, text="1",
                         command=lambda: self.Action1())
        btn2.grid(row=2, column=0, sticky=tk.NSEW, pady=10)

        btn2 = tk.Button(self.container, text="2",
                         command=lambda: self.Action2())
        btn2.grid(row=2, column=1, sticky=tk.NSEW, pady=10)

        btn3 = tk.Button(self.container, text="3",
                         command=lambda: self.Action3())
        btn3.grid(row=2, column=2, sticky=tk.NSEW, pady=10)

        btnReturn = tk.Button(self.container,
                              text='Back',
                              command=lambda: self.controller.showFrame(
                                  mw.MainFrame.__name__
                              ))
        btnReturn.grid(row=4, column=0, columnspan=3,
                       sticky=tk.NSEW, pady=10)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def setEntry1Content(self):
        content = self.selectFile()
        self.entry1_content.set(content)
        if self.entry1_content != ' ':
            self.setText1Content(content + ' selected')

    def selectFile(self):
        file_directory = filedialog.askopenfilename(
            initialdir=self.controller.pathFolder
        )
        return file_directory

    def setText1Content(self, message):
        self.text1.config(state="normal")
        self.text1Content = message
        self.text1.delete("1.0", "end")
        self.text1.insert(tk.INSERT, self.text1Content)
        self.text1.config(state="disable")

    def Action1(self):
        self.setText1Content("1 clicked")

    def Action2(self):
        self.setText1Content("2 clicked")

    def Action3(self):
        self.setText1Content("3 clicked")


if __name__ == '__main__':
    Frame2()
