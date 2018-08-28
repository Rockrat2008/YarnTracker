#  AUTHOR:  Michael O'Brien
#  CREATED:  20 August 2018
#  UPDATED:  28 August 2018
#  DESCRIPTION:  GUI application for managing a yarn collection

#  Modules needed for application
from tkinter import *
import tkinter.ttk as ttk
from backendDb import *

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


def btnView_Yarn():
    lstDisplayBox.delete(0, END)
    for rows in apidb.view_data():
        lstDisplayBox.insert(END, rows)


#  Creates the main window and assigns the title of the application
master = Tk()
master.wm_title('YARN TRACKER')


#  Labels and data entry boxes
manufacturerChoices = view_Manufacturer()
lblManufacturer = Label(master, text = 'MANUFACTURER')
lblManufacturer.grid(row = 0, column = 0)
strManufacturer = StringVar()
comboBoxManufacturer = ttk.Combobox(master, values = manufacturerChoices)
comboBoxManufacturer.grid(row = 0, column = 1)

lblYarnName = Label(master, text = 'YARN NAME')
lblYarnName.grid(row = 0, column = 2)
strYarnName = StringVar()
entryYarnName = Entry(master, textvariable = strYarnName)
entryYarnName.grid(row = 0, column = 3)

colorChoices = view_Color()
lblYarnColor = Label(master, text = 'YARN COLOR')
lblYarnColor.grid(row = 0, column = 4)
strYarnColor = StringVar()
comboBoxYarnColor = ttk.Combobox(master, values = colorChoices)
comboBoxYarnColor.grid(row = 0, column = 5)

weightChoices = view_Weight()
lblYarnWeight = Label(master, text = 'WEIGHT')
lblYarnWeight.grid(row = 1, column = 0)
strYarnWeight = StringVar()
comboBoxWeight = ttk.Combobox(master, values = weightChoices)
comboBoxWeight.grid(row = 1, column = 1)

nbrSkeinsChoices = [.25, .5, .75, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lblNbrSkeins = Label(master, text = 'NBR OF SKEINS')
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
btnViewAll = Button(master, text = 'View All Yarn', width = 12, command = btnView_Yarn)
btnViewAll.grid(row = 4, column = 5, sticky = E)

btnClose = Button(master, text = 'Close', width = 12, command = master.destroy)
btnClose.grid(row = 12, column = 5, sticky = E)


master.mainloop()
