import urllib.request																					#Importing required libraries
import nltk
from bs4 import BeautifulSoup					
from nltk.corpus import opinion_lexicon
import matplotlib.pyplot as plt
import tkinter
from tkinter import *

#https://play.google.com/store/apps/details?id=com.tecpop.deletrec.viewhats&showAllReviews=true
#https://play.google.com/store/apps/details?id=com.whatsapp&showAllReviews=true

with urllib.request.urlopen("https://play.google.com/store/apps/details?id=com.tecpop.deletrec.viewhats&hl=en&showAllReviews=true") as url:	#app review url
    html = url.read()																					#fetching data from the url
#html=response.read()
soup=BeautifulSoup(html,"html5lib")
text=soup.get_text(strip=True)
tokens=[t for t in text.split()]																		#storing the data into a tokens

opinion_lexicon.words('positive-words.txt')																#using opinoion lexicon from nltk
opinion_lexicon.words('negative-words.txt')
#print tokens
count = 0
count1 = 0
#bigrm = nltk.bigrams(tokens)
#print ', '.join(' '.join((a, b)) for a, b in bigrm)
print ("-------------------------------Positive-----------------------------------")					
for token in tokens:																					#comparing positive words
     if token.lower() in opinion_lexicon.words('positive-words.txt'):
        print (token)
        count+=1
print ("Positive words: ",count)

print ("-------------------------------Negative-----------------------------------")
for token1 in tokens:																					#comparing negative words
     if token1.lower() in opinion_lexicon.words('negative-words.txt'):
        print (token1)
        count1+=1
print ("Negative words: ",count1) 
de = count+count1
print (de)

calc_pos = (float(count)/de)*100
print ("Positive %: ",calc_pos, "%") 																		#calculating percentage
calc_neg = (float(count1)/de)*100
print ("Negative %ds: ",calc_neg, "%") 


win=tkinter.Tk()																						#creating window
win.geometry("2000x1000")
#win.configure(background="black")
photo = PhotoImage(file = "/home/jayesh/bg1.png")														#importing bg image
w = Label(win, image=photo)
w.pack()
#ent = Entry(win)
#ent.pack()
#ent.focus_set()
#Setting it up
'''
img = ImageTk.PhotoImage(Image.open("final.jpeg"))
#Displaying it
imglabel = Label(mainWindow, image=img).grid(row=1, column=1)
'''

lbl1=Label(win,text=" WELCOME TO FAKE APP DETECTION SYSTEM ",fg="red",bg="black",font="Times 24 bold").place(x=550,y=60)
def show():																								#function to display the graph

	labels = ['Positive', 'Negative']
	sizes = [count, count1]
	colors = ['green', 'red']
	patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
	plt.legend(patches, labels, loc="best")
	plt.axis('equal')
	plt.tight_layout()
	plt.show()

def res():																								#function to display the result
	'''x=int(calc_pos, "%")
	y=int(calc_neg, "%")
	msg = Label(win, text = x,fg="green",bg="white",font="Arial 18 bold").place(x=250,y=300)
	msg1 = Label(win, text = y,fg="brown",bg="white",font="Arial 18 bold").place(x=250,y=300)'''
	if (calc_pos > calc_neg):
		Label(win,text="~ APP IS LEGITIMATE ~",fg="green",bg="black",font="Arial 22 bold").place(x=780,y=500)
	elif (calc_pos < calc_neg):
		Label(win,text="~ APP IS FAKE ~",fg="brown",bg="black",font="Arial 22 bold").place(x=800,y=500)
	else:
		Label(win,text="~ Neutral Review ~",fg="yellow",bg="black",font="Arial 22 bold").place(x=850,y=500)
	

'''buttons to trigger show() and res() function'''
btn1=Button(win,text='SHOW GRAPH',bg="black",fg="orange",height=3,width=17,font="Arial 17 bold",command=show).place(x=600,y=300)
btn1=Button(win,text='SHOW RESULT',bg="black",fg="orange",height=3,width=17,font="Arial 17 bold",command=res).place(x=1000,y=300)

win.mainloop()


