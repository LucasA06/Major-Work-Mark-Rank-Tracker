from tkinter import *
import customtkinter as ctk
import pandas as pd

# Create main customtkinter window
win = ctk.CTk()
win.title("Main Menu")
win.geometry("300x500")

df = pd.read_csv('project.csv')
subjects = df['Subject'].tolist()
subj_buttons = []

#Function to save changes to the dataframe
def save_changes(subject, mark_textboxes, mark_textboxes_outof, rank_textboxes, rank_textboxes_outof, edit_win):
    index = subjects.index(subject)
    for i in range(4):
        df.iloc[index, i*4+1] = mark_textboxes[i].get("1.0", "end-1c")
        df.iloc[index, i*4+3] = rank_textboxes[i].get("1.0", "end-1c")
        df.iloc[index, i*4+2] = mark_textboxes_outof[i].get("1.0", "end-1c")
        df.iloc[index, i*4+4] = rank_textboxes_outof[i].get("1.0", "end-1c")

    df.to_csv('project.csv', index=False)
    edit_win.destroy()

#Function to open an edit window
def open_edit_window(subject, toplevel):
    index = subjects.index(subject)
    edit_win = ctk.CTkToplevel(toplevel)
    edit_win.title(str(subject) + ' Marks/Ranks')
    edit_win.geometry("350x400")

    mark_textboxes = []
    mark_textboxes_outof = []
    rank_textboxes = []
    rank_textboxes_outof = []

    for i in range(4):
        ctk.CTkLabel(edit_win, text='Task ' + str(i+1)).place(x=10,y=10+80*i)
        ctk.CTkLabel(edit_win, text='Mark').place(x=75,y=10+80*i)
        ctk.CTkLabel(edit_win, text='Rank').place(x=75,y=50+80*i)
        ctk.CTkLabel(edit_win, text='Out Of').place(x=200,y=10+80*i)
        ctk.CTkLabel(edit_win, text='Out Of').place(x=200,y=50+80*i)

        mark_textbox = ctk.CTkTextbox(edit_win, height=1, width=50)
        mark_textbox.place(x=125,y=10+80*i)
        mark_textbox.insert(END, df.iloc[index, i*4+1])
        mark_textboxes.append(mark_textbox)

        mark_textbox_outof = ctk.CTkTextbox(edit_win, height=1, width=50)
        mark_textbox_outof.place(x=250,y=10+80*i)
        mark_textbox_outof.insert(END, df.iloc[index, i*4+2])
        mark_textboxes_outof.append(mark_textbox_outof)

        rank_textbox = ctk.CTkTextbox(edit_win, height=1, width=50)
        rank_textbox.place(x=125,y=50+80*i)
        rank_textbox.insert(END, df.iloc[index, i*4+3])
        rank_textboxes.append(rank_textbox)

        rank_textbox_outof = ctk.CTkTextbox(edit_win, height=1, width=50)
        rank_textbox_outof.place(x=250,y=50+80*i)
        rank_textbox_outof.insert(END, df.iloc[index, i*4+4])
        rank_textboxes_outof.append(rank_textbox_outof)

    # Create a button to save the changes
    save_button = ctk.CTkButton(edit_win, text='Save Changes', command= lambda: save_changes(subject, mark_textboxes, mark_textboxes_outof, rank_textboxes, rank_textboxes_outof, edit_win))
    save_button.place(x=125,y=320)
    

#Function to open a subject homepage
def open_subject(index):
    subject = subjects[index]

    toplevel = ctk.CTkToplevel(win)
    toplevel.title(subject)
    toplevel.geometry("300x300")

    ctk.CTkLabel(toplevel, text=subject, font=('Calibri', 40, 'bold', 'underline')).pack(pady=10)

    edit_button = ctk.CTkButton(toplevel, text='Edit Marks/Ranks', command= lambda subject=subject: open_edit_window(subject, toplevel))
    edit_button.pack(pady=10)

    close_button = ctk.CTkButton(toplevel, text='Close', command= toplevel.destroy)
    close_button.pack(pady=10)


# Create a button for each existing subject
index = 0

for subject in subjects:
    subj_buttons.append(ctk.CTkButton(win, text=subject, command= lambda index=index: open_subject(index)).pack(pady=10))
    index += 1

win.mainloop()