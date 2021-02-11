from gtts import gTTS
from playsound import playsound

with open("contenido.txt", "w") as file:
    file.write("Hola amor te amo mucho")
    file.write("\n")
    file.write("¿Chupemelo amor que rico hijueputa?")
    file.close()


def voz(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.read()
    file = gTTS(text=text, lang=lang)
    filename = name_file
    file.save(filename)


voz("contenido.txt", "es", "voz.mp3")
print("Reproduciendo:")
audio = "voz.mp3"
playsound(audio)
print("Reproducido.")