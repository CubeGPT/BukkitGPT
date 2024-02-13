import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk

import os

import core

# Define global variables
CurrentProject = None
artifact_name = None
description = None
package_id = None

# Define BuildProject function
def BuildProject():
    # Uncompleted
    # main.generate_plugin()
    message = "some \n result"
    return message

def DeleteProject():
    # Uncompleted
    pass

# Define HomePage class
class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.logo = tk.PhotoImage(file="ui/logo.png")
        self.logo_label = ttk.Label(self, image=self.logo)  # Change tk.Label to ttk.Label
        self.logo_label.pack(pady=(10))
        self.create_button = ttk.Button(self, text="Create", command=lambda: self.create_project(), width=15)
        self.create_button.pack(pady=(10, 5))
        self.settings_button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage), width=15)
        self.settings_button.pack(pady=(5, 30))

    def create_project(self):
        global CurrentProject
        CurrentProject = "New"
        self.controller.show_frame(ProjectPage)

# Define ProjectPage class
class ProjectPage(ttk.Frame):  # Change tk.Frame to ttk.Frame
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_label = ttk.Label(self, text="")
        self.title_label.pack(pady=10)
        self.text1 = ttk.Label(self, text="artifact_name")
        self.text1.pack(anchor="w")
        self.text2 = ttk.Label(self, text="sometext here")
        self.text2.pack(anchor="w")
        self.input1 = ttk.Entry(self)
        self.input1.pack(anchor="w")
        self.text3 = ttk.Label(self, text="description")
        self.text3.pack(anchor="w")
        self.text4 = ttk.Label(self, text="sometext here")
        self.text4.pack(anchor="w")
        self.input2 = ttk.Entry(self)
        self.input2.pack(anchor="w", width=30, lenth=30)
        self.text5 = ttk.Label(self, text="package_id")
        self.text5.pack(anchor="w")
        self.text6 = ttk.Label(self, text="sometext here")
        self.text6.pack(anchor="w")
        self.input3 = ttk.Entry(self)
        self.input3.pack(anchor="w")
        self.generate_button = ttk.Button(self, text="Generate", command=lambda: self.generate_project())
        self.generate_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.delete_button = ttk.Button(self, text="Delete", command=lambda: self.delete_project(), style="Red.TButton")
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def generate_project(self):
        global artifact_name, description, package_id
        artifact_name = self.input1.get()
        description = self.input2.get()
        package_id = self.input3.get()
        self.generate_button.config(text="Generating", state=tk.DISABLED)
        info = BuildProject()
        messagebox.showinfo("Result", info)
        self.generate_button.config(text="Generate", state=tk.NORMAL)

    def delete_project(self):
        global CurrentProject
        DeleteProject()
        self.controller.show_frame(HomePage)

    def update_title(self):
        self.title_label.config(text=CurrentProject)

# Define SettingsPage class
class SettingsPage(ttk.Frame):  # Change tk.Frame to ttk.Frame
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_label = ttk.Label(self, text="Settings")
        self.title_label.pack(pady=10)

# Define App class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set the window title
        self.title("BukkitGPT")
        # Set the window size
        self.geometry("800x600")
        # Create a container frame
        self.container = tk.Frame(self, bg="white")
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Create a sidebar frame
        self.sidebar = tk.Frame(self, bg="white")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        # Create a title label for the sidebar
        self.sidebar_title = tk.Label(self.sidebar, text="Projects")
        self.sidebar_title.pack(pady=10)
        # Create a listbox for the sidebar
        self.sidebar_list = tk.Listbox(self.sidebar)
        self.sidebar_list.pack(fill=tk.Y, expand=True)
        # Bind the listbox selection to a callback function
        self.sidebar_list.bind("<<ListboxSelect>>", self.on_select)
        # Create Home and Settings buttons under the sidebar
        self.home_button = ttk.Button(self.sidebar, text="Home", command=lambda: self.show_frame(HomePage), width=15)
        self.home_button.pack(pady=(30, 5))
        self.settings_button_sidebar = ttk.Button(self.sidebar, text="Settings", command=lambda: self.show_frame(SettingsPage), width=15)
        self.settings_button_sidebar.pack(pady=(5, 30))
        # Populate the listbox with the names of the folders in projects/
        self.populate_list()
        # Create a dictionary of frames
        self.frames = {}
        # Loop through the HomePage, ProjectPage, and SettingsPage classes
        for F in (HomePage, ProjectPage, SettingsPage):
            # Create a frame for each class
            frame = F(self.container, self)
            # Store the frame in the dictionary
            self.frames[F] = frame
            # Place the frame in the container
            frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.show_frame(HomePage)

        # Configure the style for the red button
        self.style = ttk.Style()
        self.style.configure("Red.TButton", fg="white", background="red")

    def show_frame(self, frame_class):
        # Show the frame corresponding to the frame_class
        frame = self.frames[frame_class]
        frame.tkraise()
        # If the frame is ProjectPage, update the title
        if frame_class == ProjectPage:
            frame.update_title()

    def populate_list(self):
        # Populate the listbox with the names of the folders in projects/
        # Clear the listbox first
        self.sidebar_list.delete(0, tk.END)
        # Get the list of folders in projects/
        folders = [folder for folder in os.listdir("projects/") if folder != "template"]  # Ignore the "template" folder
        # Loop through the folders
        for folder in folders:
            # Insert the folder name to the listbox
            self.sidebar_list.insert(tk.END, folder)

    def on_select(self, event):
        # This function is called when the user selects an item in the listbox
        # Get the index of the selected item
        index = self.sidebar_list.curselection()[0]
        # Get the name of the selected item
        name = self.sidebar_list.get(index)
        # Set the CurrentProject variable to the name
        global CurrentProject
        CurrentProject = name
        # Show the ProjectPage frame
        self.show_frame(ProjectPage)

# Create an app object
app = App()
# Start the main loop
app.after(1, sv_ttk.use_light_theme)
app.mainloop()
