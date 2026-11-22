import sys
import os

print("=" * 60)
print("DIAGNÓSTICO DE ÁUDIO - DESTINO")
print("=" * 60)

# Teste 1: winsound (áudio nativo do Windows)
print("\n[TESTE 1] Áudio nativo do Windows (winsound.Beep)...")
try:
    import winsound
    winsound.Beep(800, 500)  # 800 Hz por 500 ms
    print("  -> Beep executado. Você ouviu um som? Se sim, o áudio do Windows está OK.")
except Exception as e:
    print(f"  -> ERRO no winsound: {e}")

# Teste 2: pyttsx3 - listar vozes
print("\n[TESTE 2] pyttsx3 - Vozes disponíveis...")
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    print(f"  -> {len(voices)} voz(es) encontrada(s):")
    for v in voices:
        print(f"     - {v.name} ({v.id})")
except Exception as e:
    print(f"  -> ERRO ao inicializar pyttsx3: {e}")

# Teste 3: pyttsx3 - falar texto
print("\n[TESTE 3] pyttsx3 - Falar texto de teste...")
try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say("Teste de audio do destino. Se voce ouviu isto, o pyttsx3 esta funcionando.")
    engine.runAndWait()
    print("  -> Fala concluída. Você ouviu a voz?")
except Exception as e:
    print(f"  -> ERRO ao falar com pyttsx3: {e}")

print("\n" + "=" * 60)
print("FIM DO DIAGNÓSTICO")
print("=" * 60)
