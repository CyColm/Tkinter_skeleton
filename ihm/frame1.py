# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from ihm import mainWindow as mw


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.container = tk.Frame(self)
        self.container.pack(expand=True)

        # Label
        label1 = tk.Label(self.container,
                          text='Select a folder :')
        label1.grid(row=0, column=0, columnspan=10)

        # Entry
        self.entry1_content = tk.StringVar()
        entry1 = tk.Entry(self.container, textvariable=self.entry1_content)
        entry1.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

        # Text
        self.text1 = tk.Text(self.container)
        self.text1Content = 'Hello World!'
        self.setText1Content(self.text1Content)
        self.text1.grid(row=2, column=0, columnspan=3)

        # Button
        btn1 = tk.Button(self.container, text="...",
                         command=lambda: self.setEntry1Content())
        btn1.grid(row=1, column=2, sticky=tk.E)

        btnReturn = tk.Button(self.container,
                              text="Back",
                              command=lambda: self.controller.showFrame(
                                  mw.MainFrame.__name__
                              ))
        btnReturn.grid(row=3, column=0, columnspan=3, pady=20)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def setEntry1Content(self):
        content = self.selectFolder()
        self.entry1_content.set(content)
        self.setText1Content(content + ' selected')

    def selectFolder(self):
        folder_directory = filedialog.askdirectory(
            initialdir=self.controller.pathFolder
        )
        return folder_directory

    def setText1Content(self, message):
        self.text1.config(state="normal")
        self.text1Content = message
        self.text1.delete("1.0", "end")
        self.text1.insert(tk.INSERT, self.text1Content)
        self.text1.config(state="disable")


if __name__ == '__main__':
    Frame1()
