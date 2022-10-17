# -*- coding: utf-8 -*-

import tkinter as tk
from functions import config
from ihm import frame1, frame2
import os
from pathlib import Path


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Window parameters
        self.getConfig()
        self.pathFolder = Path(os.path.dirname(__file__)).parent
        self.geometry(self.width+"x"+self.height)
        self.minsize(width=int(self.width), height=int(self.height))
        self.title(self.window_name)

        # Menu
        self.menu = tk.Menu(self)
        item = tk.Menu(self.menu)
        item.add_command(label='New')
        self.menu.add_cascade(label='File', menu=item)
        self.config(menu=self.menu)

        # Frame
        self.container = tk.Frame(self)
        self.container.pack()

        # Frame
        self.frames = {}

        # Ajout des frames dans la liste
        self.addFrame(MainFrame)
        self.addFrame(frame1.Frame1)
        self.addFrame(frame2.Frame2)

        self.showFrame(MainFrame.__name__)

    def addFrame(self, frame):
        self.frames[frame.__name__] = frame(parent=self.container,
                                            controller=self)
        self.frames[frame.__name__].grid(row=0, column=0,
                                         sticky=tk.NSEW, padx=10, pady=10)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def showFrame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def getConfig(self):
        conf = config.Config()
        is_width_defined, self.width = conf.get('Window',
                                                'width',
                                                'str')
        if not is_width_defined:  # default width
            self.width = "800"
        is_height_defined, self.height = conf.get('Window',
                                                  'height',
                                                  'str')
        if not is_height_defined:  # default height
            self.width = "600"
        _, self.window_name = conf.get('Window', 'title', 'str')


class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.container = tk.Frame(self)
        self.container.pack(expand=True)

        # Label
        label1 = tk.Label(self.container,
                          text='Select option :')
        label1.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        btn1 = tk.Button(self.container,
                         text="Frame 1",
                         command=lambda: controller.showFrame(
                            frame1.Frame1.__name__
                         ))
        btn1.grid(row=1, column=0, columnspan=2, pady=10)

        btn2 = tk.Button(self.container,
                         text="Frame 2",
                         command=lambda: controller.showFrame(
                            frame2.Frame2.__name__
                         ))
        btn2.grid(row=2, column=0, columnspan=2, pady=10)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)


if __name__ == '__main__':
    MainWindow()
