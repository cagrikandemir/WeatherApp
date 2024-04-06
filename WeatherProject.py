from tkinter import *
from PIL import ImageTk,Image
import requests
url ='https://api.openweathermap.org/data/2.5/weather'
apikey='1ac6ac487468b1d7b617ddafa5037b46'
iconlink='https://openweathermap.org/img/wn/{}@2x.png'


def getWheather(city):
    params={'q':city,'appid':apikey,'lang':'tr'}
    data=requests.get(url,params=params).json()
    if data:
        city= data['name'].capitalize()
        country=data['sys']['country']
        temp=int(data['main']['temp']-273.15)
        icon=data['weather'][0]['icon']
        condition=data['weather'][0]['description']
        return(city,country,temp,icon,condition)
    
def main():
    city=cityEntry.get()
    weather=getWheather(city)
    if weather:
        locationlabel['text']='{}{}'.format(weather[0],weather[1])
        templelabel['text']='{}°C'.format(weather[2])
        conditionlabel['text']=weather[4]
        icon=ImageTk.PhotoImage(Image.open(requests.get(iconlink.format(weather[3]),stream=True),raw))
        iconLabel.configure(image=icon)
        iconLabel.image=icon



app=Tk()
app.geometry('300x450')
app.title('Hava Durumu')

cityEntry=Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=10,pady=5)
cityEntry.focus()

searchButton=Button(app,text='Arama',font=('Arial,15'),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel=Label(app)
iconLabel.pack()

locationlabel=Label(app,font=('Arial,15'))
locationlabel.pack()

templelabel=Label(app,font=('Arial,15'))
templelabel.pack()

conditionlabel=Label(app,font=('Arial,15'))
conditionlabel.pack()

app.mainloop()




