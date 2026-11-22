import speech_recognition as sr
import subprocess
import sys

recognizer = sr.Recognizer()


def _falar_powershell(texto):
    """Fala via PowerShell usando System.Speech.Synthesis do .NET (Windows nativo)."""
    ps_script = f'''
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToDefaultAudioDevice()
$synth.Volume = 100
$synth.Rate = 0
try {{
    $synth.Speak("{texto}")
}} catch {{
    Write-Error "Erro ao falar: $($_.Exception.Message)"
}}
$synth.Dispose()
'''
    try:
        resultado = subprocess.run(
            ["powershell", "-Command", ps_script],
            capture_output=True, text=True, timeout=30
        )
        if resultado.returncode == 0:
            return True
        else:
            print(f"[ERRO DE ÁUDIO] PowerShell falhou: {resultado.stderr[:200]}")
            return False
    except Exception as e:
        print(f"[ERRO DE ÁUDIO] Exceção no PowerShell: {e}")
        return False


def _falar_win32com(texto):
    """Fala via win32com.client (SAPI.SpVoice) como fallback."""
    try:
        import pythoncom
        import win32com.client

        pythoncom.CoInitialize()
        voice = win32com.client.Dispatch("SAPI.SpVoice")
        voice.Volume = 100
        voice.Rate = 0
        voice.Speak(texto)
        return True
    except Exception as e:
        print(f"[ERRO DE ÁUDIO] win32com falhou: {e}")
        return False


def speak(text):
    if not text:
        return
    print("DESTINO:", text)

    # Tenta PowerShell primeiro (mais confiável no Windows)
    if _falar_powershell(text):
        return

    # Fallback: win32com
    if _falar_win32com(text):
        return

    print("[ERRO DE ÁUDIO] Não consegui falar por nenhum método disponível.")


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
