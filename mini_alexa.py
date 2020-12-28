import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import time

listener=sr.Recognizer()
print(listener)
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source) 
            print("voice",voice)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                talk(command)
        return command
    except:
         pass
    
def get_info():
    try:
        with sr.Microphone(device_index=0) as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source) 
            print("voice",voice)
            command=listener.recognize_google(voice)
            command=command.lower()
    except:
        pass
    return command
     
from threading import Timer    

def set_alarm1(seconds):    
    print('set alaraming')
    def start_alarm():
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()
    t = Timer(seconds, start_alarm)
    t.start() 
    
def calculate_timeDifference(dt_time):
    dt_time=dt_time.replace('hours','hour')
    dt_time=dt_time.replace('minutes','minute')
    hr=dt_time.split('hour')[0]
    mint=dt_time.split('hour')[1].split('minute')[0]
    print('Hour and minute',hr,mint)
    userdefined_seconds=int(hr)*3600+int(mint)*60
    print("Userss",userdefined_seconds)
    ct_seconds=datetime.datetime.now().strftime('%H:%M')
    ct_hr=int(ct_seconds.split(':')[0])
    ct_mint=int(ct_seconds.split(':')[1])
    print("current ",ct_hr,ct_mint)
    currenttime_seconds=int(ct_hr)*3600+int(ct_mint)*60
    print('current time',currenttime_seconds)
    total_sec=userdefined_seconds-currenttime_seconds
    return total_sec

def send_whatsapp(msg,mob_no,hr,minn,seconds):
    secondss=seconds
    print('sending msg')
    def start_whatsapp():
        pywhatkit.sendwhatmsg(mob_no,msg,hr,minn)
    t = Timer(secondss, start_whatsapp)
    t.start() 
    
def set_reminder_time(subject_msg,seconds):
    print('setting reminder')
    def start_reminder_time():
        talk('This is Reminder for'+subject_msg)
    t = Timer(seconds, start_reminder_time)
    t.start() 
    
def set_reminder_date(subject_msg,seconds):
    print('setting reminder')
    def start_reminder_date():
        talk('This is Reminder for'+subject_msg)
    t = Timer(seconds, start_reminder_date)
    t.start() 
    
def run_alexa():        
        command1=take_command()
        print(command1)
        if 'turn off' in command1:
            return 0
        if 'play' in command1:
            song=command1.replace('play','')
            talk('Playing.. '+song)
#            print('Playing')
            pywhatkit.playonyt(song)
        elif 'time' in command1:
            time1=datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is'+time1)
            print(time1)                
        elif 'joke' in command1:
            talk('JOKES',pyjokes.get_joke())
        elif 'google' in command1:
            text=command1.replace('google','')
            talk('Doing Google for..'+text)
            pywhatkit.search(text)
        elif 'set alarm' in command1:
            dt_time=command1.replace('set alarm at','')
            total_seconds=calculate_timeDifference(dt_time)
            print("total seconds",total_seconds)
            set_alarm1(total_seconds)
        elif 'set reminder' in command1:
            talk('for what you want to set the reminder?')
            subject_msg=get_info()
            talk('what kind of reminder you want timebased or date based ')
            command1=get_info()
            if 'time'in command1:
                talk('please tell time in 17 hour 20 minute format')
                dt_time=get_info()
                total_seconds=calculate_timeDifference(dt_time)
                set_reminder_time(subject_msg,total_seconds)
            elif 'date' in command1:
                from datetime import datetime,date,timedelta
                talk('please tell date in 21 june format')
                date1=get_info()
                talk('please tell time in 17 hour 20 minute format')
                talk('at what time on'+date1)
                dt_time=get_info()
                dt_time=dt_time.replace('hours','hour')
                dt_time=dt_time.replace('minutes','minute')
                hr=int(dt_time.split('hour')[0])
                mint=int(dt_time.split('hour')[1].split('minute')[0])
                dayy=int(date1.split(' ')[0])
                monthh1=date1.split(' ')[1]
                monthh=int(getMonth[monthh1])
                current_date=datetime.now()
                current_month=current_date.month
                current_day=current_date.day
                current_hour=current_date.hour
                current_minute=current_date.minute
#                current_second=current_date.second
                yearr=current_date.year
                t1=date(year=yearr,month=monthh,day=dayy,hour=hr,minute=mint)
                t2=date(year=yearr,month=current_month,day=current_day,hour=current_hour,minute=current_minute)
#                t3=timedelta(t2)-timedelta(t1)
                t3=t2-t1
                total_seconds=abs(t3.total_seconds())
                set_reminder_date(subject_msg,total_seconds)
#                print('current_date')

        elif 'whatsapp' in command1:
            
            text=command1.replace('whatsapp','')
            print("Here is text",text)
            talk('To whom do you want to send message')
            name=get_info()
            mob_no=contact[name]
            talk('please tell the message that you want to send')
            msg=get_info()
            talk('When you want to send the message something like 15 hour 20 minutes format')
            dt_time=get_info()
            dt_time=dt_time.replace('hours','hour')
            dt_time=dt_time.replace('minute','minute')
            hr=dt_time.split('hour')[0]
            mint=dt_time.split('hour')[1].split('minute')[0]
            pywhatkit.sendwhatmsg(mob_no,msg,hr,mint)
        else:
            talk('Please say the command again...')

x=1       
       
contact={'hiren':'+911234567809', 'ramesh':'+911234567899'}
getMonth={'january':'01','february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12'}

while True:
    x=run_alexa()
    if x==0:
        break
