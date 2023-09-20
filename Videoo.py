from tkinter import *
from pytube import YouTube

# Settings
FONT = "FixedSys" # FixedSys # System # Helvetica
FSIZE = 16


def download():
    try:
        video_url = url_entry.get()
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        destination_folder = location_entry.get()
        stream.download(output_path=destination_folder)
        done_label = Label(window, text="The Video Downloded Successfuly", font=(FONT, FSIZE), fg="green").pack(pady=15)
    except Exception:
        error_label = Label(window, text="<!> Something Went Wrong <!>", font=(FONT, FSIZE), fg="red").place(x=150, y=260)
window = Tk()
window.title("YouTube VDownloader")
window.geometry("600x350")
window.iconbitmap("C:\\Users\\HP\OneDrive\\Desktop\\627b95375a3e2ac874a75745.png")

# Widgts \*
url_label = Label(window, text="Type a video URL here", font=(FONT, FSIZE))
url_label.pack(pady=15)
url_entry = Entry(window, font=(FONT, FSIZE), width=40, relief=RIDGE)
url_entry.pack()
location_label = Label(window, text="Type the video location here", font=(FONT, FSIZE))
location_label.pack(pady=15)
location_entry = Entry(window, font=(FONT, FSIZE), width=40, relief=RIDGE)
location_entry.pack()
download = Button(window, text="Download", font=(FONT, FSIZE), relief=RAISED, width=20, command=download, bg="#12e007")
download.pack(pady=20)
# */
window.mainloop()


