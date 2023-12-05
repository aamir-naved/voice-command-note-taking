import os
import speech_recognition as sr
from datetime import datetime


def create_new_note():
    # Specify the base path for the notes
    base_path = "/Users/aamirnaved/Downloads/write_with_voice"

    # Create a directory with the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    note_directory = os.path.join(base_path, current_date)

    if not os.path.exists(note_directory):
        os.makedirs(note_directory)

    # Get the current date-time string for the note filename
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    note_filename = f"note_{current_time}.txt"

    # Prompt the user for the note content
    print("What's your note?")

    # Use SpeechRecognition to capture the note content
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Recognize the speech and write it to the note file
        note_content = recognizer.recognize_google(audio)
        note_path = os.path.join(note_directory, note_filename)

        with open(note_path, "a") as note_file:
            note_file.write(note_content + "\n")

        print("Note created successfully at:", note_path)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    # Trigger the creation of a new note when the command is spoken
    command = "create a new note"

    while True:
        print(f"Say '{command}' to create a new note. or Exit.")

        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for commands...")
            audio = recognizer.listen(source)

        try:
            # Recognize the command and create a new note if it matches
            spoken_command = recognizer.recognize_google(audio).lower()
            if spoken_command == command:
                create_new_note()
            elif spoken_command.lower() == 'exit':
                print("Exiting the loop.")
                break
            else:
                print(f"Command '{spoken_command}' not recognized.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
