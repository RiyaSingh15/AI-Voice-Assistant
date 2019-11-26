import datetime
from datetime import datetime
import eel
import os
import platform
import psutil
import pyttsx3
import speech_recognition as sr
import sqlite3
import sys
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)


@eel.expose
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


@eel.expose
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Ask me something")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in').lower()
        eel.said(query)

        if "boot" in query:
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            disk_io = psutil.disk_io_counters()
            net_io = psutil.net_io_counters()
            eel.bootinfo(bt.year, bt.month, bt.day, bt.hour, bt.minute, bt.second, get_size(disk_io.read_bytes), get_size(
                disk_io.write_bytes), get_size(net_io.bytes_sent), get_size(net_io.bytes_recv))
            speak(
                f"Boot Time: {bt.year}{bt.month}{bt.day} {bt.hour}{bt.minute}{bt.second}")
            speak(f"Total read: {get_size(disk_io.read_bytes)}")
            speak(f"Total write: {get_size(disk_io.write_bytes)}")
            speak(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
            speak(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
            command()

        elif "cpu" in query:
            cpufreq = psutil.cpu_freq()
            eel.cpuinfo(psutil.cpu_count(logical=False), psutil.cpu_count(
                logical=True), cpufreq.max, cpufreq.min, cpufreq.current, psutil.cpu_percent())
            speak("CPU Information")
            speak(f"Physical cores: {psutil.cpu_count(logical=False)}")
            speak(f"Total cores: {psutil.cpu_count(logical=True)}")
            speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
            speak(f"Total CPU Usage: {psutil.cpu_percent()}%")
            command()

        elif "date" in query:
            date = (datetime.now())
            eel.dateinfo(date.strftime('%A'), date.strftime('%d'),
                         date.strftime('%B'), date.strftime('%Y'))
            speak("Date")
            speak(
                f"{date.strftime('%A')}{date.strftime('%d')}{date.strftime('%B')}{date.strftime('%Y')}")
            command()

        elif "disk" in query:
            speak("Disk Information")
            speak("Partitions and Usage:")
            partitions = psutil.disk_partitions()
            for partition in partitions:
                speak(f"Device: {partition.device}")
                speak(f"  Mountpoint: {partition.mountpoint}")
                speak(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                speak(f"  Total Size: {get_size(partition_usage.total)}")
                speak(f"  Used: {get_size(partition_usage.used)}")
                speak(f"  Free: {get_size(partition_usage.free)}")
                speak(f"  Percentage: {partition_usage.percent}%")
            command()

        elif "memory" in query:
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            eel.memoryinfo(get_size(svmem.total), get_size(svmem.available), get_size(
                svmem.used), svmem.percent, get_size(swap.total), get_size(swap.free), get_size(swap.used), swap.percent)
            speak("Memory Information")
            speak(f"Total: {get_size(svmem.total)}")
            speak(f"Available: {get_size(svmem.available)}")
            speak(f"Used: {get_size(svmem.used)}")
            speak(f"Percentage: {svmem.percent}%")
            speak("SWAP")
            speak(f"Total: {get_size(swap.total)}")
            speak(f"Free: {get_size(swap.free)}")
            speak(f"Used: {get_size(swap.used)}")
            speak(f"Percentage: {swap.percent}%")
            command()

        elif 'open command prompt' in query:
            eel.cmdinfo()
            cmdPath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(cmdPath)
            speak("Opening Command Prompt")
            eel.sleep(2.0)
            command()

        elif 'open db browser' in query:
            eel.dbinfo()
            dbPath = "D:\\Softwares\\DB Browser\\DB Browser for SQLite.exe"
            os.startfile(dbPath)
            speak('Opening DB Browser')
            eel.sleep(2.0)
            command()

        elif 'open downloads' in query:
            eel.downloadifo()
            downloadsPath = "C:\\Users\\rriya\\Downloads"
            os.startfile(downloadsPath)
            speak('Opening Downloads')
            eel.sleep(2.0)
            command()

        elif 'open git bash' in query:
            eel.bashinfo()
            dbPath = "D:\Softwares\Git\git-bash.exe"
            os.startfile(dbPath)
            speak('Opening Git-Bash')
            eel.sleep(2.0)
            command()

        elif 'open git cmd' in query:
            eel.gitinfo()
            dbPath = "D:\Softwares\Git\git-cmd.exe"
            os.startfile(dbPath)
            speak('Opening Git-Cmd')
            eel.sleep(2.0)
            command()

        elif 'open github' in query:
            eel.githubinfo()
            webbrowser.open('github.com')
            speak('Opening GitHub')
            eel.sleep(2.0)
            command()

        elif 'open google' in query:
            eel.googleinfo()
            webbrowser.open('google.com')
            speak('Opening Google')
            eel.sleep(2.0)
            command()

        elif 'open psiphon'in query:
            eel.psiphoninfo()
            psiphonPath = "D:\\Softwares\\psiphon3.exe"
            os.startfile(psiphonPath)
            speak("Opening Psiphon")
            eel.sleep(2.0)
            command()

        elif 'open spotify' in query:
            eel.spotifyinfo()
            spotifyPath = "C:\\Users\\rriya\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)
            speak("Opening Spotify")
            eel.sleep(2.0)
            command()

        elif 'open stackoverflow' in query:
            eel.stackinfo()
            webbrowser.open('stackoverflow.com')
            speak('Opening StackOverFlow')
            eel.sleep(2.0)
            command()

        elif 'open video' in query:
            eel.videoinfo()
            videosPath = "C:\\Users\\rriya\\Videos"
            os.startfile(videosPath)
            speak("Opening Videos")
            eel.sleep(2.0)
            command()

        elif 'open vs code' in query:
            eel.vscinfo()
            codePath = "D:\\Softwares\\VSCode\\Code.exe"
            os.startfile(codePath)
            speak('Opening VSCode')
            eel.sleep(2.0)
            command()

        elif 'open youtube' in query:
            eel.youtubeinfo()
            webbrowser.open('youtube.com')
            speak('Opening YouTube')
            eel.sleep(2.0)
            command()

        elif 'open xampp control' in query:
            eel.xamppinfo()
            xamppPath = "D:\\Softwares\\XAMPP\\xampp-control.exe"
            os.startfile(xamppPath)
            speak('Opening Xampp-Control')
            eel.sleep(2.0)
            command()

        elif 'play music' in query:
            eel.playinfo()
            music_dir = 'C:\\Users\\rriya\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak('Playing Music')
            eel.sleep(2.0)
            command()

        elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('Searching Wikipedia')
            eel.wikiinfo(results)
            speak('According to Wikipidea')
            speak(results)
            command()

        elif "system" in query:
            uname = platform.uname()
            eel.sysinfo(uname.system, uname.node, uname.release,
                        uname.version, uname.machine, uname.processor)
            speak("System Information")
            speak(f"System: {uname.system}")
            speak(f"Node Name: {uname.node}")
            speak(f"Release: {uname.release}")
            speak(f"Version: {uname.version}")
            speak(f"Machine: {uname.machine}")
            speak(f"Processor: {uname.processor}")
            command()

        elif "time" in query:
            speak("Time: ")
            date = (datetime.now())
            eel.timeinfo(date.strftime('%I'), date.strftime(
                '%M'), date.strftime('%S'))
            speak(
                f"{date.strftime('%I')}{date.strftime('%p')} {date.strftime('%M')}Minutes{date.strftime('%S')}Seconds")
            command()

        else:
            speak("Command not recognized.")
            command()

    except Exception as e:
        speak("Command not recognized.")
        command()


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@eel.expose
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"assistant.db")
        c = conn.cursor() 
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.execute(
                '''CREATE TABLE IF NOT EXISTS CREDENTIALS (INTEGER PRIMARY KEY AUTOINCREMENT ,ASSISTANT_NAME TEXT, USER_NAME TEXT);''')
            c.execute("SELECT COUNT(*) FROM CREDENTIALS")
            count= c.fetchall()
            if( count[0][0] == 0):
                conn.execute(
                '''INSERT INTO CREDENTIALS (ASSISTANT_NAME, USER_NAME) VALUES ('AI Voice Assistant','User')''')
        conn.commit()
        conn.close()
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    cur = c.execute('''Select * FROM CREDENTIALS''')
    assName = str()
    userName = str()
    for row in cur:
        assName = row[0]
        userName = row[1]
    if(assName == "AI Voice Assistant" and userName == "User"):
        speak("I am AI Voice Assistant. What do you want to call me?")
        query = str(ask())
        new = "Do you want to call me "+query
        speak(new)
        confirm = str(ask())
        if 'yes' in confirm:
            conn.execute("UPDATE CREDENTIALS set ASSISTANT_NAME = '" +
                         query+"' where USER_NAME = 'User'")
            conn.commit()
            speak("What should I call you?")
            query = ask()
            new = "Do you me to call you "+query
            speak(new)
            confirm = ask()
            if 'yes' in confirm:
                conn.execute("UPDATE CREDENTIALS set USER_NAME = '" +
                             query+"' where USER_NAME = 'User'")
                conn.commit()
                cur = c.execute('''Select * FROM CREDENTIALS''')
                assName = str()
                userName = str()
                for row in cur:
                    assName = row[0]
                    userName = row[0]
                    speak("Hello")
                    speak(userName)
                    speak("I am")
                    speak(assName)
                    command()

    else:
        speak("Hello")
        speak(userName)
        speak("I am")
        speak(assName)
        command()


def ask():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in').lower()
        eel.said(query)
        return query
    except Exception as e:
        ask()


eel.init('gui')
if __name__ == "__main__":
    eel.start('assistant.html')
