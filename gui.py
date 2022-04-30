from curses import A_COLOR
import tkinter as tk
import random
from database import guitarChords
import time

window = tk.Tk()
window.title("Fretboard Learning")
window.geometry("500x500")


value = ''

chordArray = ['F', 'C', 'E', 'A', 'D', 'G', 'B']


def randChord():
	global chordArray
	global guitarBox
	global guitarWindow
	x = random.randint(0,6)
	global randomChord
	randomChord = chordArray[x]


def updateGuitar():
	chordLabel = tk.Label(guitarWindow, text=randomChord, font=("Helvetica", 15)).grid(row=7, column=5)
	guitarWindow.after(100, updateGuitar)

def updateBass():
	chordLabel = tk.Label(bassWindow, text=randomChord, font=("Helvetica", 15)).grid(row=5, column=5)
	bassWindow.after(100, updateBass)


def updateRightGuitar():
	correctGuitar = tk.Label(guitarWindow, text=' Right ', bg='green').grid(row = 8, column = 1)
	guitarWindow
	
def bassLabelDestroy():
	yourNote.destroy()

def updateWrongGuitar():
	wrongGuitar = tk.Label(guitarWindow, text='Wrong', bg='red').grid(row = 8, column = 1)
	guitarWindow

def updateRightBass():
	global yourNote
	wrongBass = tk.Label(bassWindow, text=' Right ', bg='green').grid(row = 7, column = 1)
	bassWindow
	

def updateWrongBass():
	wrongBass = tk.Label(bassWindow, text='Wrong', bg='red').grid(row = 7, column = 1)
	bassWindow


def E():
	global value
	value = 'E'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()
	
def A():
	global value
	value = 'A'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def D():
	global value
	value = 'D'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def G():
	global value
	value = 'G'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def B():
	global value
	value = 'B'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def C():
	global value
	value = 'C'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def F():
	global value
	value = 'F'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def Wrong():
	global value
	value = 'Wrong'
	if value == randomChord:
		updateRightGuitar()
	else:
		updateWrongGuitar()

def Ebass():
	global value
	value = 'E'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()
	
def Abass():
	global value
	value = 'A'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Dbass():
	global value
	value = 'D'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Gbass():
	global value
	value = 'G'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Bbass():
	global value
	value = 'B'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Cbass():
	global value
	value = 'C'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Fbass():
	global value
	value = 'F'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()

def Wrongbass():
	global value
	value = 'Wrong'
	if value == randomChord:
		updateRightBass()
	else:
		updateWrongBass()


def guitarBox(): # box for the guitar fretboard quiz
	global window
	global value
	global randomChord
	global guitarWindow
	guitarWindow = tk.Toplevel(window)
	guitarWindow.title("Guitar Fretboard")
	guitarWindow.geometry("560x250")
	Labele = tk.Label(guitarWindow, text = 'e').grid(row = 1, column = 0)
	LabelB = tk.Label(guitarWindow, text = 'B').grid(row = 2, column = 0)
	LabelG = tk.Label(guitarWindow, text = 'G').grid(row = 3, column = 0)
	LabelD = tk.Label(guitarWindow, text = 'D').grid(row = 4, column = 0)
	LabelA = tk.Label(guitarWindow, text = 'A').grid(row = 5, column = 0)
	LabelE = tk.Label(guitarWindow, text = 'E').grid(row = 6, column = 0)
	Btn1 = tk.Button(guitarWindow, text = '1st Fret', command=F)
	Btn1.grid(row = 1, column = 1)
	Btn2 = tk.Button(guitarWindow, text = '1st Fret', command=C)
	Btn2.grid(row = 2, column = 1)
	Btn3 = tk.Button(guitarWindow, text = '1st Fret', command=Wrong)
	Btn3.grid(row = 3, column = 1)
	Btn4 = tk.Button(guitarWindow, text = '1st Fret', command=Wrong)
	Btn4.grid(row = 4, column = 1)
	Btn5 = tk.Button(guitarWindow, text = '1st Fret', command=Wrong)
	Btn5.grid(row = 5, column = 1)
	Btn6 = tk.Button(guitarWindow, text = '1st Fret', command=F)
	Btn6.grid(row = 6, column = 1)
	Btn7 = tk.Button(guitarWindow, text = '2nd Fret', command=Wrong)
	Btn7.grid(row = 1, column = 2)
	Btn8 = tk.Button(guitarWindow, text = '2nd Fret', command=Wrong)
	Btn8.grid(row = 2, column = 2)
	Btn9 = tk.Button(guitarWindow, text = '2nd Fret', command=A)
	Btn9.grid(row = 3, column = 2)
	Btn10 = tk.Button(guitarWindow, text = '2nd Fret', command=E)
	Btn10.grid(row = 4, column = 2)
	Btn11 = tk.Button(guitarWindow, text = '2nd Fret', command=B)
	Btn11.grid(row = 5, column = 2)
	Btn12 = tk.Button(guitarWindow, text = '2nd Fret', command=Wrong)
	Btn12.grid(row = 6, column = 2)
	Btn13 = tk.Button(guitarWindow, text = '3rd Fret', command=G)
	Btn13.grid(row = 1, column = 3)
	Btn14 = tk.Button(guitarWindow, text = '3rd Fret', command=D)
	Btn14.grid(row = 2, column = 3)
	Btn15 = tk.Button(guitarWindow, text = '3rd Fret', command=Wrong)
	Btn15.grid(row = 3, column = 3)
	Btn16 = tk.Button(guitarWindow, text = '3rd Fret', command=F)
	Btn16.grid(row = 4, column = 3)
	Btn17 = tk.Button(guitarWindow, text = '3rd Fret', command=C)
	Btn17.grid(row = 5, column = 3)
	Btn18 = tk.Button(guitarWindow, text = '3rd Fret', command=G)
	Btn18.grid(row = 6, column = 3)
	Btn19 = tk.Button(guitarWindow, text = '4th Fret', command=Wrong)
	Btn19.grid(row = 1, column = 4)
	Btn20 = tk.Button(guitarWindow, text = '4th Fret', command=Wrong)
	Btn20.grid(row = 2, column = 4)
	Btn21 = tk.Button(guitarWindow, text = '4th Fret', command=B)
	Btn21.grid(row = 3, column = 4)
	Btn22 = tk.Button(guitarWindow, text = '4th Fret', command=Wrong)
	Btn22.grid(row = 4, column = 4)
	Btn23 = tk.Button(guitarWindow, text = '4th Fret', command=Wrong)
	Btn23.grid(row = 5, column = 4)
	Btn24 = tk.Button(guitarWindow, text = '4th Fret', command=Wrong)
	Btn24.grid(row = 6, column = 4)
	Btn25 = tk.Button(guitarWindow, text = '5th Fret', command=A)
	Btn25.grid(row = 1, column = 5)
	Btn26 = tk.Button(guitarWindow, text = '5th Fret', command=E)
	Btn26.grid(row = 2, column = 5)
	Btn27 = tk.Button(guitarWindow, text = '5th Fret', command=C)
	Btn27.grid(row = 3, column = 5)
	Btn28 = tk.Button(guitarWindow, text = '5th Fret', command=G)
	Btn28.grid(row = 4, column = 5)
	Btn29 = tk.Button(guitarWindow, text = '5th Fret', command=D)
	Btn29.grid(row = 5, column = 5)
	Btn30 = tk.Button(guitarWindow, text = '5th Fret', command=A)
	Btn30.grid(row = 6, column = 5)
	chordBtn = tk.Button(guitarWindow, text = 'Get Random Chord', command=randChord)
	chordBtn.grid(row=6, column=6)
	instructions = tk.Label(guitarWindow, text='Click', font=("Helvetica", 15)).grid(row=7, column=1)
	instructions2 = tk.Label(guitarWindow, text='The', font=("Helvetica", 15)).grid(row=7, column=2)
	instructions3 = tk.Label(guitarWindow, text='Note:', font=("Helvetica", 15)).grid(row=7, column=3)
	guitarWindow.after(1000, updateGuitar)


def bassBox(): # box for the bass fretboard quiz
	global window
	global value
	global bassWindow
	bassWindow = tk.Toplevel(window)
	bassWindow.title("Bass Window")
	bassWindow.geometry("560x250")
	LabelG = tk.Label(bassWindow, text = 'G').grid(row = 1, column = 0)
	LabelD = tk.Label(bassWindow, text = 'D').grid(row = 2, column = 0)
	LabelA = tk.Label(bassWindow, text = 'A').grid(row = 3, column = 0)
	LabelE = tk.Label(bassWindow, text = 'E').grid(row = 4, column = 0)
	bassBtn1 = tk.Button(bassWindow, text = '1st Fret', command=Wrongbass).grid(row = 1, column = 1)
	bassBtn2 = tk.Button(bassWindow, text = '1st Fret', command=Wrongbass).grid(row = 2, column = 1)
	bassBtn3 = tk.Button(bassWindow, text = '1st Fret', command=Wrongbass).grid(row = 3, column = 1)
	bassBtn4 = tk.Button(bassWindow, text = '1st Fret', command=Fbass).grid(row = 4, column = 1)
	bassBtn5 = tk.Button(bassWindow, text = '2nd Fret', command=Abass).grid(row = 1, column = 2)
	bassBtn6 = tk.Button(bassWindow, text = '2nd Fret', command=Ebass).grid(row = 2, column = 2)
	bassBtn7 = tk.Button(bassWindow, text = '2nd Fret', command=Bbass).grid(row = 3, column = 2)
	bassBtn8 = tk.Button(bassWindow, text = '2nd Fret', command=Wrongbass).grid(row = 4, column = 2)
	bassBtn9 = tk.Button(bassWindow, text = '3rd Fret', command=Wrongbass).grid(row = 1, column = 3)
	bassBtn10 = tk.Button(bassWindow, text = '3rd Fret', command=Fbass).grid(row = 2, column = 3)
	bassBtn11 = tk.Button(bassWindow, text = '3rd Fret', command=Cbass).grid(row = 3, column = 3)
	bassBtn12 = tk.Button(bassWindow, text = '3rd Fret', command=Gbass).grid(row = 4, column = 3)
	bassBtn13 = tk.Button(bassWindow, text = '4th Fret', command=Bbass).grid(row = 1, column = 4)
	bassBtn14 = tk.Button(bassWindow, text = '4th Fret', command=Wrongbass).grid(row = 2, column = 4)
	bassBtn15 = tk.Button(bassWindow, text = '4th Fret', command=Wrongbass).grid(row = 3, column = 4)
	bassBtn16 = tk.Button(bassWindow, text = '4th Fret', command=Wrongbass).grid(row = 4, column = 4)
	bassBtn17 = tk.Button(bassWindow, text = '5th Fret', command=Cbass).grid(row = 1, column = 5)
	bassBtn18 = tk.Button(bassWindow, text = '5th Fret', command=Gbass).grid(row = 2, column = 5)
	bassBtn19 = tk.Button(bassWindow, text = '5th Fret', command=Dbass).grid(row = 3, column = 5)
	bassBtn20 = tk.Button(bassWindow, text = '5th Fret', command=Abass).grid(row = 4, column = 5)
	chordBtn = tk.Button(bassWindow, text = 'Get Random Chord', command=randChord)
	chordBtn.grid(row=5, column=6)
	instructions = tk.Label(bassWindow, text='Click', font=("Helvetica", 15)).grid(row=5, column=1)
	instructions2 = tk.Label(bassWindow, text='The', font=("Helvetica", 15)).grid(row=5, column=2)
	instructions3 = tk.Label(bassWindow, text='Note:', font=("Helvetica", 15)).grid(row=5, column=3)
	bassWindow.after(100, updateBass)

def quiting():
	window.destroy()

def both():
	randChord()
	guitarBox()

def bothBass():
	randChord()
	bassBox()

TopLabel = tk.Label(text="Pick which instrument you would like to practice!")
TopLabel.pack(pady = 25)
guitarQuiz = tk.Button(text="Click for Guitar Practice", command = both)
guitarQuiz.pack(pady = 50)
bassQuiz = tk.Button(text='Click for Bass Practice', command = bothBass)
bassQuiz.pack(pady = 25)
QuitBtn = tk.Button(text='Quit', command = quiting)
QuitBtn.pack(pady = 25)

tk.mainloop()