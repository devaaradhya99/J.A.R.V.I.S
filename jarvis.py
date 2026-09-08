import datetime, subprocess, os, webbrowser, ctypes, psutil, sys, time, requests, json, pyautogui, pyperclip, random
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.setProperty('rate', 155)

FS = 44100
AUDIO_FILE = r"D:\JARVIS\temp_voice.wav"
KNOWLEDGE_FILE = r"D:\JARVIS\knowledge.json"
NOTE_FILE = r"D:\JARVIS\notes.txt"

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2:0.5b"

CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
APPS = {'chrome': CHROME, 'notepad': 'notepad.exe', 'calculator': 'calc.exe',
        'paint': 'mspaint.exe', 'cmd': 'cmd.exe', 'powershell': 'powershell.exe',
        'task manager': 'taskmgr.exe', 'settings': 'ms-settings:',
        'vs code': r"C:\Users\Nice\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        'word': 'winword.exe', 'excel': 'excel.exe'}
WEBSITES = {'youtube': 'https://www.youtube.com', 'google': 'https://www.google.com',
            'gmail': 'https://mail.google.com', 'facebook': 'https://www.facebook.com',
            'instagram': 'https://www.instagram.com', 'github': 'https://github.com',
            'netflix': 'https://www.netflix.com', 'amazon': 'https://www.amazon.in',
            'reddit': 'https://www.reddit.com', 'wikipedia': 'https://www.wikipedia.com',
            'maps': 'https://maps.google.com', 'spotify': 'https://open.spotify.com',
            'chatgpt': 'https://chat.openai.com', 'openai': 'https://chat.openai.com',
            'claude': 'https://claude.ai', 'gemini': 'https://gemini.google.com',
            'bing': 'https://www.bing.com', 'twitter': 'https://twitter.com',
            'x': 'https://twitter.com', 'linkedin': 'https://www.linkedin.com',
            'discord': 'https://discord.com/app', 'whatsapp': 'https://web.whatsapp.com',
            'telegram': 'https://web.telegram.org', 'pinterest': 'https://www.pinterest.com',
            'stackoverflow': 'https://stackoverflow.com', 'medium': 'https://medium.com',
            'hotstar': 'https://www.hotstar.com', 'jio cinema': 'https://www.jiocinema.com',
            'zomato': 'https://www.zomato.com', 'swiggy': 'https://www.swiggy.com',
            'flipkart': 'https://www.flipkart.com', 'snapchat': 'https://www.snapchat.com',
            'canva': 'https://www.canva.com', 'notion': 'https://www.notion.so',
            'figma': 'https://www.figma.com', 'chess': 'https://www.chess.com'}

def load_knowledge():
    try:
        with open(KNOWLEDGE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_knowledge(data):
    with open(KNOWLEDGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    print("\n[LISTENING...]")
    try:
        audio = sd.rec(int(5 * FS), samplerate=FS, channels=1, dtype='int16')
        sd.wait()
        sf.write(AUDIO_FILE, audio, FS)
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(f"YOU: {text}")
        return text.lower().strip()
    except:
        print("[Could not understand]")
        return ""

def wiki_search(query):
    try:
        r = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ','_')}", headers={'User-Agent': 'JARVIS/1.0'}, timeout=5)
        if r.status_code == 200 and 'extract' in r.json():
            return r.json()['extract'][:400]
    except:
        pass
    return None

def ask_ollama(prompt):
    try:
        r = requests.post(OLLAMA_URL, json={'model': OLLAMA_MODEL, 'prompt': f"You are JARVIS. Be concise. {prompt}", 'stream': False}, timeout=30)
        return r.json()['response'].strip()
    except:
        return None

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ','+')}")

def think(text, knowledge):
    t = text.lower().strip()

    if t.startswith('type '):
        words = text[5:].strip()
        pyperclip.copy(words)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.press('enter')
        return f"Typed {words}"

    if t.startswith('learn '):
        parts = t[6:].strip().split(' - ', 1)
        if len(parts) == 2:
            cat = parts[0].split()[0] if parts[0].split() else 'general'
            if cat not in knowledge: knowledge[cat] = {}
            knowledge[cat][parts[0].strip()] = parts[1].strip()
            save_knowledge(knowledge)
            return f"Learned: {parts[0].strip()}"
        return "Say learn question dash answer"

    for trigger in ['open ', 'launch ', 'start ', 'kholo ']:
        if t.startswith(trigger):
            name = t[len(trigger):]
            for k in WEBSITES:
                if k in name:
                    webbrowser.open(WEBSITES[k])
                    return f"Opening {k}"
            for k in APPS:
                if k in name:
                    subprocess.Popen([APPS[k]]) if os.path.exists(APPS[k]) else os.startfile(APPS[k])
                    return f"Opening {k}"
            return f"Can't open {name}"

    for trigger in ['close ', 'band ']:
        if t.startswith(trigger):
            name = t[len(trigger):]
            procs = {'chrome':'chrome.exe','firefox':'firefox.exe','notepad':'notepad.exe'}
            for k,p in procs.items():
                if k in name:
                    subprocess.run(f'taskkill /f /im {p}', shell=True, capture_output=True)
                    return f"Closed {k}"
            return f"Can't close {name}"

    if 'search google ' in t:
        q = t.split('search google ',1)[1]
        search_google(q)
        return f"Searching {q}"
    if 'google search ' in t:
        q = t.split('google search ',1)[1]
        search_google(q)
        return f"Searching {q}"
    if 'youtube search ' in t:
        q = t.split('youtube search ',1)[1]
        webbrowser.open(f"https://www.youtube.com/results?search_query={q.replace(' ','+')}")
        return f"Searching {q} on YouTube"
    if 'search youtube ' in t:
        q = t.split('search youtube ',1)[1]
        webbrowser.open(f"https://www.youtube.com/results?search_query={q.replace(' ','+')}")
        return f"Searching {q} on YouTube"
    if t.startswith('search ') or t.startswith('find '):
        q = t.split(' ',1)[1]
        if ' on ' in q:
            parts = q.split(' on ',1)
            search_google(f"{parts[0]} site:{parts[1]}")
        else:
            search_google(q)
        return f"Searching {q}"

    if t in ['hello','hi','hey'] or t.startswith('good morning'):
        return random.choice(["Hello Sir!","At your service, Sir.","Welcome back, Sir."])
    if 'time' in t:
        return f"Time is {datetime.datetime.now().strftime('%I:%M %p')}"
    if 'date' in t or 'today' in t:
        return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"
    if 'your name' in t or 'who are you' in t:
        return "I am JARVIS. Just A Rather Very Intelligent System."
    if 'thank' in t:
        return random.choice(["You're welcome.","Happy to help.","At your service."])
    if 'weather' in t or 'mausam' in t:
        search_google("weather today")
        return "Opening weather"
    if 'status' in t or 'system' in t:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        bat = psutil.sensors_battery()
        return f"CPU {cpu} percent, RAM {mem.percent} percent, Battery {bat.percent if bat else 'N A'} percent"
    if 'volume up' in t or 'awaz badhao' in t:
        for _ in range(5): subprocess.run('powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]175)"', shell=True, capture_output=True)
        return "Volume up"
    if 'volume down' in t or 'awaz kam' in t:
        for _ in range(5): subprocess.run('powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]174)"', shell=True, capture_output=True)
        return "Volume down"
    if 'mute' in t:
        subprocess.run('powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"', shell=True, capture_output=True)
        return "Muted"
    if 'screenshot' in t:
        subprocess.run(['powershell','-Command','Add-Type -AssemblyName System.Windows.Forms;Add-Type -AssemblyName System.Drawing;$b=New-Object System.Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width,[System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height);$g=[System.Drawing.Graphics]::FromImage($b);$g.CopyFromScreen(0,0,0,0,$b.Size);$b.Save("$HOME\\Pictures\\screenshot.png")'], capture_output=True)
        return "Screenshot saved"
    if 'lock' in t:
        ctypes.windll.user32.LockWorkStation()
        return "Screen locked"
    if 'scroll up' in t or 'upar scroll' in t:
        for _ in range(5): pyautogui.scroll(3)
        return "Scrolling up"
    if 'scroll down' in t or 'niche scroll' in t:
        for _ in range(5): pyautogui.scroll(-3)
        return "Scrolling down"
    if 'page down' in t or 'niche jao' in t:
        pyautogui.press('pagedown')
        return "Page down"
    if 'page up' in t or 'upar jao' in t:
        pyautogui.press('pageup')
        return "Page up"
    if 'enter' in t or 'dabao' in t:
        pyautogui.press('enter')
        return "Pressed enter"
    if 'escape' in t or 'back' in t:
        pyautogui.press('escape')
        return "Pressed escape"
    if 'note' in t or 'yaad' in t:
        for w in ['take note','note down','save note','note','yaad rakh']:
            if w in t:
                after = t.split(w,1)[1].strip()
                if after:
                    with open(NOTE_FILE,'a',encoding='utf-8') as f: f.write(f"[{datetime.datetime.now().strftime('%H:%M')}] {after}\n")
                    return f"Noted: {after}"
    if 'shutdown' in t or 'shut down' in t:
        subprocess.run('shutdown /s /t 30', shell=True)
        return "Shutting down in 30 seconds"
    if 'restart' in t:
        subprocess.run('shutdown /r /t 10', shell=True)
        return "Restarting in 10 seconds"
    if 'cancel' in t:
        subprocess.run('shutdown /a', shell=True, capture_output=True)
        return "Cancelled"
    if 'play music' in t or 'gaana' in t:
        webbrowser.open('https://www.youtube.com/results?search_query=music')
        return "Playing music"
    if 'news' in t:
        webbrowser.open('https://news.google.com')
        return "Opening news"
    if 'email' in t or 'mail' in t:
        webbrowser.open('https://mail.google.com')
        return "Opening Gmail"
    if 'ip' in t:
        r = subprocess.run('ipconfig | findstr /i "IPv4"', shell=True, capture_output=True, text=True)
        return r.stdout.strip()[:200] or "No IP found"

    for cat, items in knowledge.items():
        for k, v in items.items():
            if t in k or k in t:
                return v

    if 'what is' in t or 'who is' in t or 'tell me' in t or 'explain' in t or 'kya hai' in t:
        w = wiki_search(t)
        if w: return w

    o = ask_ollama(text)
    if o: return o

    w = wiki_search(text)
    if w: return w

    search_google(text)
    return f"Searching Google for {text}"

def main():
    os.system('cls')
    print("=" * 50)
    print("   J.A.R.V.I.S - Voice Assistant")
    print("=" * 50)
    speak("JARVIS online. I am listening.")
    print("-" * 50)
    knowledge = load_knowledge()

    while True:
        try:
            user = listen()
            if not user:
                continue
            if user in ['quit','exit','bye']:
                speak("Goodbye Sir!")
                break
            reply = think(user, knowledge)
            speak(reply)
        except KeyboardInterrupt:
            speak("Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
