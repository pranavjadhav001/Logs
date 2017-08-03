from tkinter import filedialog
from tkinter import messagebox
import time
import os
import pyaudio
from tkinter import *
import wave
import datetime

import numpy as np
import cv2



def video():

    messagebox.showinfo("VIDEO","Press 'q' key to stop recording")
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    nhina = str(timestr)+".avi"


    out = cv2.VideoWriter(nhina, fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 180)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def khol():
    curr = os.getcwd()


    f = filedialog.askopenfile(initialdir=curr,filetypes=(("text files","*.txt"),("video files","*.avi"),("audio files","*.wav")))


def band():
    pass
def edit():
    print("u can do it")

def audio():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 20
    timestr = time.strftime("%Y%m%d-%H%M%S")
    WAVE_OUTPUT_FILENAME = str(timestr) + "aud.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    messagebox.showinfo("AUDIO", "Recording for 1 min only")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    messagebox.showinfo("AUDIO", "Recording finished!")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
def likh():
    print("I like this stuff")



def baap():
    global t
    global root

    root = Tk()

    root.title("HYHY logs")


    smenu = Menu(root)
    root.config(menu=smenu)
    submenu = Menu(smenu)
    smenu.add_cascade(label="Type of Input:",menu = submenu)
    submenu.add_command(label="Video",command=video)
    submenu.add_command(label="Audio",command=audio)
    submenu.add_command(label="Text",command = likh)
    editmenu= Menu(smenu)
    smenu.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label="Open",command = khol)
    editmenu.add_command(label="Save",command=save)
    editmenu.add_command(label="Delete",command = band)


    t = Text(root, height=10, width=40)
    t.pack()






    root.mainloop()

def save():
    tata = t.get(0.0,END)

    frame= Frame(root,bg="powder blue",height=10,width=40)
    frame.pack(side=BOTTOM)


    with open("parent.txt",'a') as w:
        w.write(str(datetime.datetime.today()))
        w.write("\n")
        w.write(tata)
    z = Label(frame,text=str(datetime.datetime.today()),anchor=W)
    z.pack(side=LEFT)
    y = Label(frame,text=tata,anchor=W)
    y.pack(side=LEFT)



