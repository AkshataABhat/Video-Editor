from tkinter import *
from typing import final
from moviepy.editor import *
clip1=VideoFileClip("1.mp4")
clip2=VideoFileClip("2.mp4")
clip3=VideoFileClip("3.mp4")


def mix():
    final_clip=concatenate_videoclips([clip1,clip2,clip3])
    final_clip.write_videofile("Final Video.mp4")

def mirror():
    clip_mirror=clip1.fx(vfx.mirror_x)
    clip_mirror.write_videofile("Final Video.mp4")

def resize():
    r=float(input("Enter the size:"))
    clip_resize=clip1.resize(r)
    clip_resize.write_videofile("Final Video.mp4")

def Effects_speed():
    speed=float(input("Enter the speed:"))
    clip_speed=clip1.fx(vfx.speedx,speed)
    clip_speed.write_videofile("Final Video.mp4")


def Effects_colour():
    colour=float(input("Enter the value of darkness:"))
    clip_colour=clip1.fx(vfx.colorx,colour)
    clip_colour.write_videofile("Final Video.mp4")


def trim():
    starting=int(input("Enter starting point:"))
    ending=int(input("Enter ending point:"))
    clip_trim=clip1.cutout(starting,ending)
    clip_trim.write_videofile("Final Video.mp4")

def audio():
    import moviepy.editor as mpe
    audioclip=mpe.AudioFileClip("audio.mp3")
    videoclip=mpe.videoclip.set_audio(audioclip)
    final_clip=videoclip.set_audio(audioclip)
    final_clip.write_videofile("Final Video.mp4")

root = Tk()
root.title("Video Editor")
root.geometry("750x200")
root.minsize(750,200)
root.maxsize(750,200)
root.config(bg="#44063A")






b=Button(root,text="Merge",relief=GROOVE,bg="#6A4BFF",fg="white",command=mix)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

b=Button(root,text="Crop",relief=GROOVE,bg="#6A4BFF",fg="white",command=mirror)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

b=Button(root,text="Resize",relief=GROOVE,bg="#6A4BFF",fg="white",command=resize)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

b=Button(root,text="Speed",relief=GROOVE,bg="#6A4BFF",fg="white",command=Effects_speed)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

b=Button(root,text="Colour",relief=GROOVE,bg="#6A4BFF",fg="white",command=Effects_colour)
b.pack(side="left",padx=20)
b.config(width=8,height=3)


b=Button(root,text="Trim",relief=GROOVE,bg="#6A4BFF",fg="white",command=trim)
b.pack(side="left",padx=20)
b.config(width=8,height=3)


b=Button(root,text="Audio",relief=GROOVE,bg="#6A4BFF",fg="white",command=audio)
b.pack(side="left",padx=20)
b.config(width=8,height=3)


root.mainloop()

