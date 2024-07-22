# Voice Assistant with Tkinter and Speech Recognition

This project is a voice assistant application that uses Tkinter for the GUI, `SpeechRecognition` for capturing voice commands, and `pyttsx3` for text-to-speech. The assistant is triggered by the phrase "hey jake" and can respond to various commands defined in an `intent.json` file.

## Features

- Voice activation with the phrase "hey jake"
- Responds to voice commands
- Changes the GUI label color to red when activated
- Stops on the command "stop"
- Text-to-speech responses

## Requirements

- Python 3.x
- `tkinter`
- `SpeechRecognition`
- `pyttsx3`
- `neuralintents`
- `PyAudio`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/voice-assistant.git
    cd voice-assistant
    ```

2. **Install the required packages**:

    ### On Windows:
    
    - Install the packages:
      ```bash
      pip install SpeechRecognition pyttsx3 neuralintents
      ```

3. **Create your `intent.json` file**:
    - Create a `intent.json` file in the project directory. This file should define the intents and responses for the assistant.

## Usage

Run the `assistant.py` script to start the voice assistant:

```bash
python assistant.py
