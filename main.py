import speech_recognition as sr

# Testing SpeechRecognition
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said: " + recognized_text)

    # Write the recognized text to a file
    with open("/Users/aamirnaved/Downloads/write with voice/output.txt", "a") as file:
        file.write(recognized_text + "\n")
        print("Recognized text written to 'output.txt'")
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


# /Users/aamirnaved/Downloads/
# /Users/aamirnaved/Downloads/write with voice