import glob

import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog

from tkinter import font

import tkinter.font as fnt

from ttkthemes import ThemedStyle

import os

import natsort

import vlc

import subprocess

import numpy as np


import cv2

import datetime


result = []
backUpResult = []
path = ''

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder='', cnf={}, fg='black',
                 fg_placeholder='grey50', *args, **kw):
        super().__init__(master=None, cnf={}, bg='white', *args, **kw)
        self.fg = fg
        self.fg_placeholder = fg_placeholder
        self.placeholder = placeholder
        self.bind('<FocusOut>', lambda event: self.fill_placeholder())
        self.bind('<FocusIn>', lambda event: self.clear_box())
        self.fill_placeholder()

    def clear_box(self):
        if not self.get() and super().get():
            self.config(fg=self.fg)
            self.delete(0, tk.END)

    def fill_placeholder(self):
        if not super().get():
            self.config(fg=self.fg_placeholder)
            self.insert(0, self.placeholder)
    
    def get(self):
        content = super().get()
        if content == self.placeholder:
            return ''
        return content

# create root window
root = tk.Tk()

#root = ThemedTk(theme="awdark")
root.title('Easy Search')
root.geometry('500x400')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


themeIndex = 0


hightlightBackgroundColors = [
    '#2C001E' ,
    '#212529' ,
    '#354f52'
]


backgroundColors = [ 
    '#5E2750' , 
    '#495057' ,
    '#52796f'
]


selectedForegroundColors = [
    '#ffb703' ,
    '#fca311' ,
    '#ffb703' ,
]

foregroundColors = [ 
    '#e9edc9' , 
    '#cad2c5' ,
    '#e9edc9' ,
]

rowHeight = 23
fontSize = 12
font_properties = ( "ubuntu", fontSize )

#style = ttk.Style()

style = ThemedStyle(root)
style.set_theme("black")   

    
    
    

#print(style.theme_names())

style.configure("Treeview", font=font_properties )
style.configure('Treeview', rowheight=rowHeight)

#style.map('Treeview',  background=backgroundColors[1] , foreground=foregroundColors[1])


#style.theme_use("aqua")


#style.map('Treeview',  background=[('selected', 'invalid' , '#264653')] , foreground=[('selected', 'invalid' , '#ffb703')])
style.map('Treeview',  background=[('selected', 'invalid' , '#264653')] , foreground=[('selected' , selectedForegroundColors[themeIndex])])
#('aqua', 'step', 'clam', 'alt', 'default', 'classic')

topFrame = ttk.Frame(root )

# create a treeview
tree = ttk.Treeview( root , show="tree")

vsby = ttk.Scrollbar( root , orient="vertical" ,command=tree.yview)
#vsbx = ttk.Scrollbar( root , orient="horizontal",command=tree.xview)


vsby.pack( side=tkinter.RIGHT , fill='both' )
#vsbx.pack( side=tkinter.TOP , fill='both' )


tree.configure(yscrollcommand=vsby.set)
#tree.configure(xscrollcommand=vsbx.set)



selection_index = None


def on_tree_row_click(event):
    global selection_index
    # Get the index of the clicked row
    item = tree.identify_row(event.y)
    selection_index = int(item)





def HighLightRow(event):
    global tree 
    global till
    global themeIndex

    item = tree.selection()
    index = int(item[0])
    
    addIfNotInTill(index)
    saveWatchedVideos()
    
    tree.tag_configure( index , background =hightlightBackgroundColors[themeIndex] , foreground =foregroundColors[themeIndex] )




def DeHightLightRow(event):
    global tree 
    global till
    global themeIndex

    item = tree.selection()
    index = int(item[0])
    
    removeIfInTill(index)
    saveWatchedVideos()
    
    tree.tag_configure( index , background =backgroundColors[themeIndex] , foreground =foregroundColors[themeIndex] )




till = []


def addIfNotInTill(index) :
    global till
    found = False
    for item in till:
        if index == item :
            found = True
    
    if (found == False) :
        till.append(index)


def removeIfInTill(index) :
    global till
    found = False
    counter = 0
    while counter < len(till) :
        if index == till[counter] :
            till.remove(index)
            break
        counter += 1
    


def saveWatchedVideos() :
    global path
    global till
    
    lengthOfTill = len(till)
    f = open( path.replace("/" , "\\") + "\\saved.txt" , "w")
    
    counter = 0
    while counter < len(till) :
        f.write( str(till[counter]) + "\n" )
        counter += 1
    
    f.close()




def OnDoubleClick(event):
    global searchString
    global result
    global filteredResult
    global backUpResult
    global tree 
    global till
    global themeIndex

    result = backUpResult

    item = tree.selection()
    #print(item)
    index = int(item[0])
    
    
    addIfNotInTill(index)
    saveWatchedVideos()
    
    
    tree.tag_configure( index , background =hightlightBackgroundColors[themeIndex] , foreground =foregroundColors[themeIndex] )
    #print(index)
    #searchString = index
    #path = searchTheTable()
    #path = path[0].replace("/" , "\\")
    path = result[index].replace("/" , "\\")
    #print(path)
    subprocess.Popen(f"vlc \"{path}\"")
    
    #vlc_instance = vlc.Instance()
    # creating a media player
    #player = vlc_instance.media_player_new()
    # creating a media
    #media = vlc_instance.media_new(path)
    # setting media to the player
    #player.set_media(media)
    # play the video
    #player.play()
    
    #print("you clicked on", tree.item(i, "values"))


"""
backgroundColors = [ 'blue' , 'black' , 
    '#03045e' , 
    '#023e8a' , 
    '#0077b6' , 
    '#0096c7' ,
    '#00b4d8' ,
    '#48cae4' ,
    '#90e0ef' ,
    '#ade8f4' ,
    ]
"""




def checkToSeeIfThereIsParents(parentArray , theIndex , currentIndex , parrantIndex) :
    global result
    global tree
    global backgroundColors
    global foregroundColors
    global themeIndex
    
    if ( currentIndex == 0 ) :
        return
    else :
        #print('try : ' , f'{parentArray[parrantIndex]}' , parentArray[currentIndex] , currentIndex , parrantIndex )
        checkToSeeIfThereIsParents(parentArray , theIndex - 1 , currentIndex - 1 , parrantIndex - 1 )
        tree.insert( parentArray[parrantIndex], tk.END, iid = parentArray[currentIndex] , text=parentArray[currentIndex], open=False , tags = (currentIndex) )
        tree.tag_configure( theIndex-1 , background =backgroundColors[themeIndex] , foreground = foregroundColors[theIndex-1])
        
    """
    try :
        print('try : ' , f'{parentArray[parrantIndex]}' , parentArray[currentIndex] , currentIndex , parrantIndex )
        if ( currentIndex == 0 ) :
            return
        else :
            tree.insert( parentArray[parrantIndex], tk.END, iid = parentArray[currentIndex] , text=parentArray[currentIndex], open=False , tags = (currentIndex) )
            tree.tag_configure( theIndex-1 , background = backgroundColors[theIndex-1] , foreground = foregroundColors[theIndex-1])
    except : 
        #tree.insert(parentArray[theIndex-1-2], tk.END, iid = parentArray[len(parentArray)-1-1] , text=parentArray[theIndex-1-1], open=False , tags = (theIndex) )
        #counter-=1
        print('error : ' , parentArray[parrantIndex] , parentArray[currentIndex] , currentIndex , parrantIndex )
        if ( currentIndex == 0 ) :
            return
        else :
            checkToSeeIfThereIsParents(parentArray , theIndex - 1 , currentIndex - 1 , parrantIndex - 1 )
    """

def add_data() :
    global result
    global path
    global tree
    global backgroundColors
    global foregroundColors
    global selection_index
    global themeIndex
    global video_duration_array

    length = len(result)

    for i in tree.get_children():
        tree.delete(i)


    """
    tree.insert('', 'end', 'item1',text ='GeeksforGeeks')
 
    # Inserting child
    tree.insert('', 'end', 'item2',text ='Computer Science')
    tree.insert('', 'end', 'item3',text ='GATE papers')
    tree.insert('', 'end', 'item4',text ='Programming Languages')

    # Inserting more than one attribute of an item
    tree.insert('item2', 'end', 'Algorithm',text ='Algorithm') 
    tree.insert('item2', 'end', 'Data structure',text ='Data structure')
    tree.insert('item3', 'end', '2018 paper',text ='2018 paper') 
    tree.insert('item3', 'end', '2019 paper',text ='2019 paper')
    tree.insert('item4', 'end', 'Python',text ='Python')
    tree.insert('item4', 'end', 'Java',text ='Java')

    # Placing each child items in parent widget
    tree.move('item2', 'item1', 'end')
    tree.move('item3', 'item1', 'end')
    tree.move('item4', 'item1', 'end')
    """
    

    counter = 0
    while counter < length :
        thePath = result[counter].replace( path , '' )
        parentArray = thePath.split('\\')
        theIndex = len(parentArray)
        currentIndex = theIndex - 1
        parrantIndex = theIndex - 1 - 1
        #print(result[counter])
        precedence = '0' * ( abs(len(str(counter+1)) - len(str(len(result)))) )
        
        if treeCompleteString == True : 
            pass 
        else : 
            arr = np.array(parentArray)
            arr = arr[2:len(arr)]
            thePath = " \\ ".join(arr)
        
        #print(thePath)
        
        if os.path.isfile(result[counter]) :
            eachTextString = "[" + str(video_duration_array[counter]) + "]" + " - " + precedence + str(counter+1) + " - " + thePath[1:]
            tree.insert('', tk.END, text=eachTextString.replace( "\\" , "  \\  " ) , iid=counter, open=False , tags = counter )
            tree.tag_configure( counter , background =backgroundColors[themeIndex] , foreground =foregroundColors[themeIndex] )
        #checkToSeeIfThereIsParents(parentArray , theIndex , currentIndex , parrantIndex)
        counter += 1
    
    style.map('Treeview',  background=[('selected', 'invalid' , '#264653')] , foreground=[('selected' , selectedForegroundColors[themeIndex])])
    
    if selection_index != None :
        tree.selection_set(selection_index)
    # adding children of first node
    # tree.insert('', tk.END, text='John Doe', iid=5, open=False)
    # tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
    # tree.move(5, 0, 0)
    # tree.move(6, 0, 1)













def get_length(filename):
    video = cv2.VideoCapture(filename)

    #duration = video.get(cv2.CAP_PROP_POS_MSEC)
    #frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    # count the number of frames
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
      
    # calculate duration of the video
    seconds = round(frames / fps)
    video_time = datetime.timedelta(seconds=seconds)
    
    return video_time
    



video_duration_array = []




def fetchAllFilesFromPath() :
    global search
    global result
    global path
    global backUpResult
    global video_duration_array
    
    
    video_duration_array = []

    #print(path)

    if( path.strip() == '') :
        return

    
    search.delete(0,tkinter.END)
    result = glob.glob(path + '/**/*.mp4', recursive=True)
    result = natsort.natsorted(result)
    for item in result :
        video_length = get_length(item)
        video_duration_array.append(video_length)
        #print(video_length)
    #print(result)
    add_data()
    highlightWatchedVideos()
    backUpResult = result
    label.config(text=(path + f" ({len(result)} files)"))
    







untill = ''




def fetchSavedHistory() : 
    global untill
    global path
    global till
    
    till = []
    #print(path.replace("/" , "\\") + "\\saved.txt")

    f = open( path.replace("/" , "\\") + "\\saved.txt" , "r")
    #line = f.readline()
    for line in f:
        # All lines and strip last line which is newline
        till.append(int(line.strip()))
    f.close()





def highlightWatchedVideos() :
    global tree
    global till
    global themeIndex
    
    counter = 0
    while counter < len(till) :
        tree.tag_configure( till[counter] , background =hightlightBackgroundColors[themeIndex] , foreground =foregroundColors[themeIndex] )
        counter += 1
                
            





    



def openfile():
    global backUpResult
    global result
    global path
    result = []
    path = filedialog.askdirectory()
    #print(f"#{path}#")
    if( path.strip() == '' ) :
        pass
    else :
        fetchSavedHistory()
        fetchAllFilesFromPath()
        #return filedialog.askopenfilename()
    


buttonFont = fnt.Font(family='ubuntu', size=36, weight='bold')

style.configure( 'my.TButton', font=font_properties )
label = ttk.Label(topFrame , text='select folder to load directories ...' , font=font_properties )
button = ttk.Button(topFrame , text = 'browse' , command=openfile , style='my.TButton'  )


#label.place( relx=0.5 , rely=0.5 )
#button.place( relx=0.5 , rely=0.5 )

label.pack( expand=True , fill='both'  , side=tkinter.LEFT , anchor=tkinter.NW)
button.pack( expand=False  , fill='none'  , side=tkinter.RIGHT  , anchor=tkinter.NE)

topFrame.pack(  fill='both' )

sv = tkinter.StringVar()

searchString = ''


def searchTree():
    global searchString
    global tree
    query = searchString
    selections = []
    for child in tree.get_children():
        if query.lower() in tree.item(child)['text'].lower():   # compare strings in  lower cases.
            #print(tree.item(child)['text'])
            selections.append(child)
    #print(selections)
    tree.selection_set(selections)


def searchTheTable() :
    global result
    global filteredResult
    global searchString
    global path

    length = len(result)
    
    filteredResult = []
    counter = 0

    #print('----------------------------------')
    while counter < length : 
        #print(result[counter].find(searchString))
        if( (result[counter].replace(path , '').lower()).find(searchString.lower()) != -1 ) :
            #print(result[counter])
            filteredResult.append(result[counter])
        else :
            pass
        counter += 1
    #print('----------------------------------')
    

    #result = filteredResult
    return filteredResult




def return_pressed(event):
    global result
    global backUpResult
    global searchString

    if ( len(searchString) > len( str(search.get()) ) ) :
        result = backUpResult

    searchString = str(search.get())

    #print(searchString)

    if( searchString.strip() == '' ) :
        result = backUpResult
        add_data()
        return
    

    result = searchTheTable()

    #searchTree()
    
    #print(result)
    add_data()
     

#sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
#create search bar
search = ttk.Entry( root  , font=font_properties )
#search.bind('<Return>', return_pressed)
search.bind('<KeyRelease>', return_pressed)

search.pack(fill="both")


#tree.heading('#0', text='', anchor=tk.W)
#tree.bind("<Double-1>", OnDoubleClick)
tree.bind("<Double-1>", OnDoubleClick)
tree.bind("<Return>", OnDoubleClick)
tree.bind("<Button-1>", on_tree_row_click)


tree.bind("<A>", HighLightRow)
tree.bind("<a>", HighLightRow)
tree.bind("<R>", DeHightLightRow)
tree.bind("<r>", DeHightLightRow)



# place the Searchbar widget on the root window
# search.grid(row=0, column=0 , sticky=tk.W , ipady = 2  )

# place the Treeview widget on the root window
#tree.grid(row=1, column=0, sticky=tk.NSEW )
#tree.pack( anchor=tk.NW , fill="y" , expand=True)
tree.pack( fill="both" , expand=True )


treeCompleteString = True


def toggle_check():
    global treeCompleteString
    # Get the current state of the checkbox
    treeCompleteString = check_var.get()
    fetchAllFilesFromPath()

        


menubar = tkinter.Menu(root)

menubar.configure(background=backgroundColors[1], foreground=foregroundColors[1])

root.config(menu=menubar)

file_menu = tkinter.Menu(menubar , tearoff=0)

#file_menu.configure(background=backgroundColors[1], foreground=foregroundColors[1])

file_menu.add_command(
    label='Exit',
    command=root.destroy,
)

options_menu = tkinter.Menu(menubar , tearoff=0)


#options_menu.configure(background=backgroundColors[1], foreground=foregroundColors[1])


options_menu.add_command(
    label='Refresh',
    command=fetchAllFilesFromPath,
)

check_var = tk.BooleanVar(value=True)  # Variable to store the checkbox state
options_menu.add_checkbutton(label="Complete Path", variable=check_var, command=toggle_check)





theme_menu = tkinter.Menu(menubar , tearoff=0)

#theme_menu.configure(background=backgroundColors[1], foreground=foregroundColors[1])


firstTheme =  tk.BooleanVar(value=True)
secondTheme = tk.BooleanVar(value=False)
thirdTheme = tk.BooleanVar(value=False)


def deSelectAllTheme() :
    firstTheme.set(False)
    secondTheme.set(False)
    thirdTheme.set(False)

def applyFirstTheme() :
    global themeIndex
    deSelectAllTheme()
    firstTheme.set(True)
    themeIndex = 0
    fetchAllFilesFromPath()
    
def applySecondTheme() :
    global themeIndex
    deSelectAllTheme()
    secondTheme.set(True)
    themeIndex = 1
    fetchAllFilesFromPath()
    
def applyThirdTheme() :
    global themeIndex
    deSelectAllTheme()
    thirdTheme.set(True)
    themeIndex = 2
    fetchAllFilesFromPath()


theme_menu.add_checkbutton(label="First Theme", variable=firstTheme , command=applyFirstTheme )

theme_menu.add_checkbutton(label="Second Theme", variable=secondTheme , command=applySecondTheme )

theme_menu.add_checkbutton(label="Third Theme", variable=thirdTheme , command=applyThirdTheme )



menubar.add_cascade(
    label="File",
    menu=file_menu,
)


menubar.add_cascade(
    label="Options",
    menu=options_menu,
)


menubar.add_cascade(
    label="Theme",
    menu=theme_menu,
)



# run the app
root.mainloop()



