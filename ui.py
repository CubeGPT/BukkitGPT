import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk

import os

import main

# Define global variables
CurrentProject = None
artifact_name = None
description = None
package_id = None

# Define BuildProject function
def BuildProject():
    # Uncompleted
    # main.generate_plugin()
    pass

# Define HomePage class
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Create a logo image
        self.logo = tk.PhotoImage(file="ui/logo.png")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack(pady=(0, 10))
        # Create a Create button
        self.create_button = tk.Button(self, text="Create", command=lambda: self.create_project())
        self.create_button.pack(pady=(10, 5))
        # Create a Settings button
        self.settings_button = tk.Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage))
        self.settings_button.pack(pady=(5, 30))

    def create_project(self):
        # Set the CurrentProject variable to New
        global CurrentProject
        CurrentProject = "New"
        # Show the ProjectPage frame
        self.controller.show_frame(ProjectPage)

# Define ProjectPage class
class ProjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Create a title label
        self.title_label = tk.Label(self, text="")
        self.title_label.pack(pady=10)
        # Create a text label for artifact_name
        self.text1 = tk.Label(self, text="artifact_name")
        self.text1.pack()
        # Create a text label for some text here
        self.text2 = tk.Label(self, text="sometext here")
        self.text2.pack()
        # Create an input box for artifact_name
        self.input1 = tk.Entry(self)
        self.input1.pack()
        # Create a text label for description
        self.text3 = tk.Label(self, text="description")
        self.text3.pack()
        # Create a text label for some text here
        self.text4 = tk.Label(self, text="sometext here")
        self.text4.pack()
        # Create an input box for description
        self.input2 = tk.Entry(self)
        self.input2.pack()
        # Create a text label for package_id
        self.text5 = tk.Label(self, text="package_id")
        self.text5.pack()
        # Create a text label for some text here
        self.text6 = tk.Label(self, text="sometext here")
        self.text6.pack()
        # Create an input box for package_id
        self.input3 = tk.Entry(self)
        self.input3.pack()
        # Create a Generate button
        self.generate_button = tk.Button(self, text="Generate", command=lambda: self.generate_project())
        self.generate_button.pack(side=tk.LEFT, padx=10, pady=10)
        # Create a Delete button
        self.delete_button = tk.Button(self, text="Delete", command=lambda: controller.show_frame(HomePage))
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def generate_project(self):
        # Set the global variables to the inputs in the boxes
        global artifact_name, description, package_id
        artifact_name = self.input1.get()
        description = self.input2.get()
        package_id = self.input3.get()
        # Change the button text to Generating and make it unclickable
        self.generate_button.config(text="Generating", state=tk.DISABLED)
        # Call the BuildProject function and get the information
        info = BuildProject()
        # Pop up a information box with the information
        messagebox.showinfo("Information", info)
        # Change back the button text and make it clickable
        self.generate_button.config(text="Generate", state=tk.NORMAL)

    def update_title(self):
        # Update the title label with the CurrentProject variable
        self.title_label.config(text=CurrentProject)

# Define SettingsPage class
class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Create a title label
        self.title_label = tk.Label(self, text="Settings")
        self.title_label.pack(pady=10)

# Define App class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set the window title
        self.title("Python Program Tkinter UI")
        # Set the window size
        self.geometry("800x600")
        # Create a container frame
        self.container = tk.Frame(self)
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Create a sidebar frame
        self.sidebar = tk.Frame(self)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        # Create a title label for the sidebar
        self.sidebar_title = tk.Label(self.sidebar, text="Projects")
        self.sidebar_title.pack(pady=10)
        # Create a listbox for the sidebar
        self.sidebar_list = tk.Listbox(self.sidebar)
        self.sidebar_list.pack(fill=tk.Y, expand=True)
        # Bind the listbox selection to a callback function
        self.sidebar_list.bind("<<ListboxSelect>>", self.on_select)
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
        # Show the HomePage frame
        self.show_frame(HomePage)

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
        folders = os.listdir("projects/")
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
sv_ttk.set_theme("dark")
app.mainloop()
