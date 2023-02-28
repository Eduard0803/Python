import os
import speech_recognition as sr     #biblioteca para o reconhecimento de fala
import pyttsx3      #biblioteca para a saida de audio

rec = sr.Recognizer()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)       #ajusta o microfone para descartar os ruidos do ambiente
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")       #interpreta a fala para pt-BR e guarda na atring texto
    texto = texto.lower()       #transforma todos os caracteres da string em minusculo
    print(texto)

if texto == "abrir a calculadora":
    engine = pyttsx3.init()
    engine.say("abrindo a calculadora")     #o computador diz a string informada
    engine.runAndWait()
    os.system("calc")       #comando do sistema operacional para abrir a calculadora

if texto == "abrir o bloco de notas":
    engine = pyttsx3.init()
    engine.say("abrindo o bloco de notas")     #o computador diz a string informada
    engine.runAndWait()
    os.system("notepad")       #comando do sistema operacional para abrir o bloco de notas

if texto == "abir o paint":
    engine = pyttsx3.init()
    engine.say("abrindo o paint")     #o computador diz a string informada
    engine.runAndWait()
    os.system("mspaint")       #comando do sistema operacional para abrir o paint

os.system("pause")
