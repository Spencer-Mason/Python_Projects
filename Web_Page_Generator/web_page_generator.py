import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # Window title
        self.master.title("Web Page Generator")

        # Label for input box
        self.lbl_prompt = Label(self.master, text = 'Enter custom text or click the Default HTML Page button')
        self.lbl_prompt.grid(row = 0, column = 0, padx = (25, 0), sticky = W)

        # Text input box for custom HTML page
        self.entry = Entry(self.master, text = '', width = 100)
        self.entry.grid(row = 1, column = 0, padx = (20, 20), columnspan = 2)

        # Button for default page
        self.btn_default = Button(self.master, text = "Default HTML Page", width = 30, height = 2, command = self.defaultHTML)
        self.btn_default.grid(row = 2, column = 0, padx = (10, 10), pady = (10, 10), sticky = E)

        # Button for custom page
        self.btn_default = Button(self.master, text = "Custom Text HTML Page", width = 30, height = 2, command = self.customHTML)
        self.btn_default.grid(row = 2, column = 1, padx = (10, 10), pady = (10, 10))

    # Function to open a new tab with hardcoded content
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Function to open a new tab with custom text content
    def customHTML(self):
        htmlText = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
