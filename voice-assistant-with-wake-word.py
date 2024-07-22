import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
from neuralintents import BasicAssistant

class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)
        self.assistant = BasicAssistant("intent.json")
        # self.assistant.train_model()

        self.root = tk.Tk()
        self.label = tk.Label(text="👨🏻", font=("Arial", 120, "bold"))
        self.label.pack()

        # Start the assistant thread
        self.thread = threading.Thread(target=self.run_assistant)
        self.thread.daemon = True
        self.thread.start()

        # Start the Tkinter main loop
        self.root.mainloop()

    def update_label_color(self, color):
        # Use Tkinter's after method to safely update the GUI
        self.root.after(0, self.label.config, {'fg': color})

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "hey jake" in text:
                        self.update_label_color("red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        
                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.root.quit()  # Quit Tkinter's main loop
                            sys.exit()
                        else:
                            if text:
                                response = self.assistant.request(text)
                                if response:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.update_label_color("black")
            except speech_recognition.UnknownValueError:
                continue  # Continue listening if speech is not recognized
            except speech_recognition.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
                self.update_label_color("black")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                self.update_label_color("black")

Assistant()
