import tkinter as tk
from tkinter import ttk as ttk
from aria2c import Aria2c


class AppWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        aria2c_cnf = {
                "aria2c_path": "aria2c.exe",
                "config_path": "E:\\Program Files\\aria2c\\aria2c.conf"
                }
        self.aria2c = Aria2c(**aria2c_cnf)
        self.build_widgets()

    def build_widgets(self):
        # Aria2c
        self.labelframe_aria2c = ttk.LabelFrame(self, text="Aria2c")
        self.labelframe_aria2c.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.button_open_aria2c = ttk.Button(self.labelframe_aria2c, text="open aria2c", command=self.open_aria2c)
        self.button_open_aria2c.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.button_close_aria2c = ttk.Button(self.labelframe_aria2c, text="close aria2c", command=self.close_aria2c)
        self.button_close_aria2c.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

        # AriaNg
        self.labelframe_ariang = ttk.LabelFrame(self, text="AriaNg")
        self.labelframe_ariang.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.button_open_ariang = ttk.Button(self.labelframe_ariang, text="open ariang", command=self.open_ariang)
        self.button_open_ariang.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.button_close_ariang = ttk.Button(self.labelframe_ariang, text="close ariang", command=self.close_ariang)
        self.button_close_ariang.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        

    def open_aria2c(self):
        self.aria2c.open_aria2c()

    def close_aria2c(self):
        self.aria2c.close_aria2c()

    def open_ariang(self):
        pass

    def close_ariang(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aria2cU")
        self.center_window(250, 500)
        self.on_start()

    def on_start(self):
        app_window = AppWindow(self)
        app_window.pack(expand=tk.YES, fill=tk.BOTH)

    def center_window(self, width=None, height=None):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = width if width is not None else self.winfo_width()
        height = height if height is not None else self.winfo_width()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.geometry("{w}x{h}+{x}+{y}".format(w=width, h=height, x=x, y=y))


if __name__ == "__main__":
    app = App()
    app.mainloop()
