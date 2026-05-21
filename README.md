# Mini Voicebot 🤖

A voice-activated chatbot that listens to voice commands, recognizes speech using Google's Speech Recognition API, and responds using text-to-speech synthesis.

## Features

- 🎤 **Voice Recognition** - Uses Google Speech Recognition to convert voice to text
- 🔊 **Text-to-Speech** - Responds with synthesized speech using pyttsx3
- 🕐 **Datetime Integration** - Provides current date and time information
- 💬 **Interactive Commands** - Responds to natural language commands like:
  - "hello" or "hi" - Get a greeting with current date/time
  - "tell me the time" - Get the current time
  - "exit" or "quit" - Close the application
- 📝 **Text-Based Demo Mode** - Falls back to text input when audio hardware is unavailable
- 🎙️ **Audio Recording** - Includes a separate audio recording module

## Project Structure

```
mini-voicebot/
├── voicebot.py         # Main voicebot application
├── voicebot_demo.py    # Text-based demo version (no audio dependencies)
├── record.py           # Audio recording utility
└── README.md           # This file
```

## Installation

### Prerequisites

- Python 3.10 or earlier (for PyAudio support)
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/DigitalDreamer5/mini-voicebot.git
cd mini-voicebot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate # On macOS/Linux
```

3. Install dependencies:
```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

## Usage

### Run the Demo Version (Recommended - No Audio Dependencies)
```bash
.\.venv\Scripts\python voicebot_demo.py
```

This version accepts text input instead of voice commands and doesn't require PyAudio.

### Run the Full Voicebot (Requires PyAudio)
```bash
.\.venv\Scripts\python voicebot.py
```

### Record Audio
```bash
.\.venv\Scripts\python record.py
```

Records 5 seconds of audio and saves it as `output.wav`.

## Commands

Once running, the voicebot accepts these commands:

| Command | Response |
|---------|----------|
| `hello` or `hi` | Greeting with current date/time |
| `tell me the time` | Current date and time |
| `exit` or `quit` | Exit the program |
| Other input | "I didn't understand" message |

## Requirements

- **SpeechRecognition** - Speech recognition library
- **pyttsx3** - Text-to-speech engine
- **PyAudio** - Audio I/O (Python 3.10 and earlier only)

## Troubleshooting

### PyAudio Installation Issues

PyAudio is difficult to install on Windows with Python 3.13+. Solutions:

1. **Use the demo version** - `voicebot_demo.py` works without PyAudio
2. **Use Python 3.10 or earlier** - PyAudio has pre-built wheels for these versions
3. **Use Conda** - Has pre-built PyAudio packages
4. **Install Microsoft C++ Build Tools** - Build PyAudio from source (advanced)

## Self-Review 💭

This project was one of my very first attempts at building an application at the beginning of my first year. It took me a considerable amount of time to research, understand the various libraries, and troubleshoot issues with audio dependencies. While challenging, it was an incredibly rewarding experience that taught me so much about:

- Working with APIs and external libraries
- Audio processing and speech recognition technology
- Error handling and fallback mechanisms
- Project structure and documentation
- Debugging dependency conflicts
- Creating robust, user-friendly applications

After completing this project, I felt immensely proud and happy. It was a great learning experience that gave me confidence in my ability to tackle complex problems and build functional applications from scratch. The lessons learned here have been invaluable to my growth as a developer.

## License

This is a personal learning project.

## Author

Created by DigitalDreamer5
