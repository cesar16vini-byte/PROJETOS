import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()

def configure_destino_voice():
    voices = engine.getProperty("voices")
    for voice in voices:
        name = (voice.name or "").lower()
        if any(word in name for word in ("david", "mark", "male", "masculino")):
            engine.setProperty("voice", voice.id)
            print(f"Voz selecionada: {voice.name}")
            return
    print("Nenhuma voz masculina encontrada; usando a voz padrão do sistema.")

configure_destino_voice()

def speak(text):
    if not text:
        return
    print("DESTINO:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
    except sr.WaitTimeoutError:
        print("Não ouvi nada.")
        return ""

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", text)
        return text
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro ao conectar ao serviço de reconhecimento: {e}")
        return ""