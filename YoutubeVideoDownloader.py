from tkinter import *
from pytube import YouTube
from pytube import Stream
from tkinter import filedialog
import tkinter.messagebox

#==============================functiions=================================
def download_video():
    #global search_entry
    #given_url = search_entry.get()
    #yt = YouTube(str(given_url))
    #choices_video = yt.streams.all()
    destination = filedialog.askdirectory(title = "Select Folder")
    for loop in range(0,j):
        if(loop == i.get()):
            vid = choices_video[loop]
            vid.download(destination)
    root.quit()




def display_video():
    top = Toplevel()
    top.title("Download Links")
    top.geometry("500x500+200+40")
    new_frame = Frame(top)
    global search_entry
    given_url = search_entry.get()
    yt = YouTube(str(given_url))
    #choices_video = yt.streams.filter(file_extension = 'mp4').all()
    global choices_video
    choices_video = yt.streams.all()
    title = Label(new_frame, text = yt.title)
    title.pack(side = TOP)
    s = 0
    video_label = Label(new_frame, text = "Videos").pack()
    for v in choices_video:
        print(v)
        if (v.type == 'video'):
            file_type = v.resolution + " " + v.subtype + " " + str(v.filesize/1024) + "KB"
            print("a")
            #file_type = "abcd"
            radio_btn.append(Radiobutton(new_frame, text = file_type, value = s, variable = i))
            radio_btn[s].pack()
            s += 1
    audio_label = Label(new_frame, text = "Audio").pack()
    for v in choices_video:
        if (v.type == 'audio'):
            file_type = v.abr + "Kbps " + v.subtype + " " + str(v.filesize/1024) + "KB"
            radio_btn.append(Radiobutton(new_frame, text = file_type, value = s, variable = i))
            radio_btn[s].pack()
            s += 1
    global j
    j = s - 1
    download_btn = Button(new_frame, text = "Download", bg = "crimson", fg = "white", command = download_video)
    download_btn.pack()
    destroy_btn = Button(new_frame, text = "destroy", command = top.destroy).pack()
    new_frame.pack()

""""
def download_video():
    given_url = search_entry.get()
    yt = YouTube(str(given_url))
    choices_video = yt.streams.all()
    vid = choices_video[]
    vid.download("/home/prajwal/python-test/pythonTkinter/youtubeDownloader")
"""



#================================MAIN============================
root = Tk()

root.title("Youtube Downloader")

download_label = []
choice_number = []
radio_btn = []
i = IntVar()

top_frame = Frame(root, padx = 10, pady = 20)

search_entry = Entry(top_frame, width = 100, bg = "white smoke")
search_entry.pack(side = LEFT)

search_btn = Button(top_frame, text = "Search", width = 20, command = display_video, bg = "snow2")
search_btn.pack(side = RIGHT)

top_frame.pack(side = TOP)


bottom_frame = Frame(root)
"""
scroll = Scrollbar(bottom_frame, orient = VERTICAL)
scroll.pack(side = RIGHT, fill =Y)
"""
"""
choices_text = Text(bottom_frame, width = 150, height = 40, yscrollcommand = scroll.set, wrap = WORD, bg = "gray72")
"""
"""
#scroll.config()
#choices_text.pack(side = TOP)
"""

bottom_frame.pack()

root.geometry("1000x700+300+40")
root.resizable(0,0)

root.mainloop()

#=======================================================================command = choices_text.yview
