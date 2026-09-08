# J.A.R.V.I.S

### Just A Rather Very Intelligent System

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=00F723&center=true&vCenter=true&width=435&lines=Voice+Assistant;AI+Powered;Open+Source" alt="JARVIS Typing SVG">
</p>

---

## Features

- ðŸŽ¤ **Voice Input** - Speak commands, JARVIS listens
- ðŸ”Š **Voice Output** - JARVIS speaks back answers
- ðŸ¤– **AI Brain** - Ollama + Wikipedia for smart answers
- ðŸŒ **Open Websites** - ChatGPT, Claude, YouTube, etc.
- ðŸ“± **Open Apps** - Chrome, VS Code, Notepad, etc.
- ðŸ” **Google Search** - Search anything by voice
- âŒ¨ï¸ **Type Text** - Multilingual typing (Hindi, English, etc.)
- ðŸ“Š **System Status** - CPU, RAM, Battery info
- ðŸ”Š **Volume Control** - Up, Down, Mute
- ðŸ“¸ **Screenshot** - Capture screen by voice
- ðŸ“ **Notes** - Save notes by voice
- ðŸ§  **Knowledge Base** - Learn and remember things
- ðŸ”„ **Scroll** - Scroll up/down by voice

## Commands

| Command | Action |
|---------|--------|
| `hello` | Greeting |
| `open youtube` | Opens YouTube |
| `open chatgpt` | Opens ChatGPT |
| `open claude` | Opens Claude |
| `search google weather` | Google search |
| `youtube search music` | YouTube search |
| `what is AI` | Wikipedia answer |
| `type hello world` | Types text |
| `scroll up / down` | Scroll page |
| `volume up / down` | Control volume |
| `screenshot` | Take screenshot |
| `status` | System info |
| `learn X - Y` | Teach something |
| `quit` | Exit |

## Requirements

- Python 3.13
- Windows 10/11
- Microphone
- Speakers

## Installation

1. Clone the repo:
```bash
git clone https://github.com/devaaradhya99/J.A.R.V.I.S.git
```

2. Install packages:
```bash
pip install pyttsx3 SpeechRecognition sounddevice soundfile requests psutil pyautogui pyperclip
```

3. Install & start Ollama:
```bash
ollama pull qwen2:0.5b
```

4. Run:
```bash
JARVIS.bat
```

## How It Works

```
User speaks â†’ Microphone records â†’ Google Speech-to-Text
    â†’ JARVIS processes command â†’ Response generated
    â†’ pyttsx3 speaks response back to user
```

## Tech Stack

- **Python** - Core language
- **pyttsx3** - Text to speech
- **SpeechRecognition** - Voice to text
- **Ollama** - Local AI model
- **Wikipedia API** - Knowledge base
- **pyautogui** - Screen automation

## Author

**devaaradhya99**

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=devaaradhya99&label=Profile%20Views&color=0e75b6&style=flat" alt="Profile Views">
</p>
