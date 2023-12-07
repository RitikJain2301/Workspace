import win32com.client

li=["Ritik", "Bhayana", "Komal"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")
for i in li:
    speaker.Speak(f"Hi {i} how are you?")
 
########

import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
for i in li:
    spk.Speak(f"Hi {i} how are you?")