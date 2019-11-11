from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import csv,os
import time


#Task1
oldf1 = open('2000_BoysNames.txt','r')
newf1 = open('2000_BoysNames2.txt','w')
newf1.write('Fist Name,Count'+'\n')


for a in oldf1:
    newli = a.split()
    newstr = ','.join(newli)
    newf1.write(newstr+'\n')
oldf1.close()
newf1.close()
os.rename('2000_BoysNames2.txt','2000_BoysNames.csv')

oldf2 = open('2000_GirlsNames.txt','r')
newf2 = open('2000_GirlsNames2.txt','w')
newf2.write('Fist Name,Count'+'\n')


for a in oldf2:
    newli = a.split()
    newstr = ','.join(newli)
    newf2.write(newstr+'\n')
oldf2.close()
newf2.close()
os.rename('2000_GirlsNames2.txt','2000_GirlsNames.csv')

#Task2
mycsv=input("Please enter the file name (include '.csv'): ")
f=open(mycsv,"r")
reader = csv.reader(f)
next(reader,None)  #skip first row
for line in f:
    line = line.split()
    print(line)
f.close()


#Task3

def generateDictionary(mydict={},oldfin = open('font3.txt','r+')): 
    for row in oldfin:
        key=row[-2]
        value=row[2:18]
        mydict[key]=value
    oldfin.close()
    return(mydict)

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()

def displayObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


#Program
nowdict = generateDictionary(mydict={},oldfin = open('font3.txt','r+'))
userCharacter = input('Please enter a character: ')
if nowdict.__contains__(userCharacter) == True:
    objectmom = nowdict[userCharacter]
    #print(objectmom)
    i=0
    mylist=[]
    for n in range(0,int(len(objectmom)/2)+1):
        if i+2<=int(len(objectmom)):
            str1 = objectmom[i:i+2]                         #divide 8 charactors to 4 2-charactor
            #print(i)  for testing
            Obbin1=bin(int(str1[0],16))                 #conver first hex number to bin
            bin1=Obbin1[2:]                             #remove '0b'
            Obbin2=bin(int(str1[1],16))                 #conver second hex number to bin
            bin2=Obbin2[2:]
            trans8to2='0'*(4-len(bin1))+bin1+'0'*(4-len(bin2))+bin2    #add proper '0' making the number 4-digit
            s2l=list(trans8to2)  #convert string to int, then to list
            listSToListI=[int(m) for m in s2l ]
            mylist.append(listSToListI)
            
            i+=2
    #print(mylist)     for testing
    lcd.clear()
    backlight.set_all(255,0,255)
    backlight.show()
    displayObject(mylist,60,28)
    time.sleep(3)
    clearBacklight()
else:
    lcd.clear()
    backlight.set_all(255,0,0)
    backlight.show()
    displayText('Not in dictionary',lcd,5,12)
    time.sleep(3)
    clearBacklight()
    