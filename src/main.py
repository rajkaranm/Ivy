import speech_recognition as sr
import pyttsx3 #import the library
import webbrowser

eng = pyttsx3.init() #initialize an instance
voice = eng.getProperty('voices') #get the available voices
eng.setProperty('rate', 180) # setting up new voice rate
eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice

def say(text):
    eng.say(text) #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command
    
def take_command():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"command: {query}")
            return query
        except Exception as err:
            print(err)
            # say("Can you repeat sir")
            return None

if __name__ == "__main__":
    say("Rebooting up, Welcome Sir")
    # password = take_command()
    # if password is not None:
    #     if password.lower() == "spider":
    #         say("welcome Mr Rajkaran")
    #     else:
    #         sys.quit()
    
    # take_command()

    sites = [["youtube", "https://youtube.com"], 
             ["instagram", "https://instagram.com"],
             ["google", "https://google.com"]]

    while True:
        query = take_command()
        if query is not None:
            if "iv" in query.lower():
                say("Yes sir, How can i help you")
            elif "who are you" in query.lower():
                say("I am Ivy, I was developed by Rajkaran ")
            for site in sites:
                if f"open {site[0]}" in query.lower():
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])