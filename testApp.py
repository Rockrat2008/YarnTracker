

#  Modules needed for application
import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import testDb


#  Functions for button actions
def get_selected_row(event):
    try:
        global selected_row
        index = lstDisplayBox.curselection()[0]
        selected_row = lstDisplayBox.get(index)
        entryManufacturer.delete(0, END)
        entryManufacturer.insert(END, selected_row[2])
        entryYarnName.delete(0, END)
        entryYarnName.insert(END, selected_row[1])
    except IndexError:
        pass


def btnView_Colors():
    lstDisplayBox.delete(0, END)
    for rows in testDb.view_Color():
        lstDisplayBox.insert(END, rows)


def colorChoices():
    print()
#    dbConnection = sqlite3.connect('testDb.db')
#    dbCursorObject = dbConnection.cursor()
#    dbCursorObject.execute('SELECT * FROM color')
#    colorChoices = []
#    for color in dbCursorObject.fetchall():
#        colorChoices.append(color[0])
#    return colorChoices


#  Creates the main window and assigns the title of the application
master = Tk()
master.wm_title('YARN TRACKER')


#  Labels and data entry boxes
manufacturerChoices = ['Ancient Arts', 'Brown Sheep Co', 'Darn Good Yarn', 'Lion Brand', "Lorna's Laces", 'Jimmy Beans Wool', 'Miss Babs', 'Premier', 'Red Heart', 'Sullivans USA', 'Yarnspirations']
lblManufacturer = Label(master, text = 'MANUFACTURER', padx=10, pady=10)
lblManufacturer.grid(row = 0, column = 0)
strManufacturer = StringVar()
comboBoxManufacturer = ttk.Combobox(master, values = manufacturerChoices)
comboBoxManufacturer.grid(row = 0, column = 1)

lblYarnName = Label(master, text = 'YARN NAME', padx=10, pady=10)
lblYarnName.grid(row = 0, column = 2)
strYarnName = StringVar()
entryYarnName = Entry(master, textvariable = strYarnName)
entryYarnName.grid(row = 0, column = 3)

#colorChoices = ['Blue', 'Brown', 'Gray - Dark', 'Gray - Light', 'Green', 'Orange', 'Purple', 'Red', 'White', 'Yellow']
#colorChoices = []
lblYarnColor = Label(master, text = 'YARN COLOR', padx=10, pady=10)
lblYarnColor.grid(row = 0, column = 4)
strYarnColor = StringVar()
comboBoxYarnColor = ttk.Combobox(master, values = colorChoices)
comboBoxYarnColor.grid(row = 0, column = 5)
comboBoxYarnColor['colorChoices'] = colorChoices()

weightChoices = ['Chunky', 'DK', 'Fingering', 'Jumbo', 'Light Worsted', 'K2', 'Sock', 'Worsted', 'Yowsa']
lblYarnWeight = Label(master, text = 'WEIGHT', padx=10, pady=10)
lblYarnWeight.grid(row = 1, column = 0)
strYarnWeight = StringVar()
comboBoxWeight = ttk.Combobox(master, values = weightChoices)
comboBoxWeight.grid(row = 1, column = 1)

nbrSkeinsChoices = [.25, .5, .75, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lblNbrSkeins = Label(master, text = 'NBR OF SKEINS', padx=10, pady=10)
lblNbrSkeins.grid(row = 1, column = 2)
comboBoxNbrSkeins = ttk.Combobox(master, values = nbrSkeinsChoices)
comboBoxNbrSkeins.grid(row = 1, column = 3)


#  List Display Box for output and scrollbax
lstDisplayBox = Listbox(master, height = 35, width = 75)
lstDisplayBox.grid(row = 4, column=0, rowspan = 10, columnspan = 40)

scrollbarDisplayBox = Scrollbar(master)
scrollbarDisplayBox.grid(row = 5, column = 4, rowspan = 10, sticky = N+S+E+W)

lstDisplayBox.configure(yscrollcommand = scrollbarDisplayBox.set)
scrollbarDisplayBox.configure(command = lstDisplayBox.yview)

lstDisplayBox.bind('<<ListboxSelect>>', get_selected_row)


#  Buttons
btnViewAll = Button(master, text = 'View All Yarn', width = 12, command = btnView_Colors)
btnViewAll.grid(row = 4, column = 5, sticky = E)

btnClose = Button(master, text = 'Close', width = 12, command = master.destroy)
btnClose.grid(row = 12, column = 5, sticky = E)


master.mainloop()
