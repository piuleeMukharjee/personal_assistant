#🎙️ Python Voice Assistant 
--
📌 Overview

This project is a Python-based Personal Voice Assistant that can recognize voice commands and perform various tasks such as:

Searching Wikipedia

Opening websites and applications

Playing music

Displaying the current time

Closing applications

It demonstrates the use of Speech Recognition, Text-to-Speech (TTS), and automation using Python.

--
🚀 Features

Voice Recognition using speech_recognition library

Text-to-Speech with pyttsx3 (offline support)

Wikipedia search results with voice output

Open and close system applications (e.g., Notepad)

Launch websites like YouTube, Google, Gmail, WhatsApp, Netflix, Spotify

Tell the current time

Personalized greetings based on time of day
--

📂 Project Structure
src/
│── assistant.py   // Main voice assistant code

--

🛠️ Requirements

Install dependencies before running:

pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia


Also, make sure PyAudio is installed for microphone access:

pip install pyaudio
--

🖥️ How to Run

Clone or download the project.

Open a terminal in the project directory.

Run the script:

python assistant.py


Speak a command (e.g., "open YouTube", "wikipedia Python", "the time", "exit").
--
📌 Example Commands
Command	Action
"wikipedia Albert Einstein"	Searches and reads Wikipedia summary
"open notepad"	Opens Notepad
"close notepad"	Closes Notepad
"open youtube"	Opens YouTube in browser
"play music"	Opens Spotify
"the time"	Reads the current time
"exit"	Closes the assistant

--

🎯 Learning Outcomes

Hands-on experience with speech recognition

Using text-to-speech (TTS) in Python

Integrating APIs like Wikipedia

Automating tasks with Python scripts
