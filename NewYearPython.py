from win32com.client import Dispatch


def speak(str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
     speak("We are almost at end of 2021.May Craetor remove our sorrows and sadness by good bye 2021  .And make our 2022 more beautiful and fillfil our wishes.so lets wish our friend happy new year in different languages ")
     with open("allhappy.txt") as f:
         for item in f.readlines():

             print(item)
             speak(item)