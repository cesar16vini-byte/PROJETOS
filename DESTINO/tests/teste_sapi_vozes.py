import sys

print("=" * 60)
print("TESTE SAPI COM DISPOSITIVO DE ÁUDIO EXPLÍCITO")
print("=" * 60)

try:
    import pythoncom
    import win32com.client
    import comtypes
    from comtypes.client import CreateObject
except ImportError as e:
    print(f"[ERRO] Dependências não disponíveis: {e}")
    sys.exit(1)

pythoncom.CoInitialize()

try:
    voice = win32com.client.Dispatch("SAPI.SpVoice")
    print("[OK] SAPI.SpVoice criado")
except Exception as e:
    print(f"[ERRO] Não consegui criar SAPI.SpVoice: {e}")
    sys.exit(1)

# Listar vozes
voices = voice.GetVoices()
print(f"\n[OK] {voices.Count} voz(es):")
for i in range(voices.Count):
    v = voices.Item(i)
    print(f"     [{i}] {v.GetDescription()}")
    # Tentar definir cada voz e falar
    try:
        voice.Voice = v
        print(f"     -> Voz {i} selecionada: {v.GetDescription()}")
        voice.Speak(f"Teste da voz {i}.")
        print(f"     -> Fala da voz {i} concluída")
    except Exception as e:
        print(f"     -> ERRO com voz {i}: {e}")

# Tentar falar com volume máximo
print("\n--- Teste com volume máximo ---")
try:
    voice.Volume = 100
    voice.Rate = 0
    voice.Speak("Volume máximo, taxa normal.")
    print("[OK] Fala com volume máximo concluída")
except Exception as e:
    print(f"[ERRO]: {e}")

# Tentar falar assíncrono
print("\n--- Teste fala assíncrona ---")
try:
    voice.Speak("Teste de fala assíncrona.", 1)  # 1 = SPF_ASYNC
    print("[OK] Fala assíncrona iniciada")
    import time
    time.sleep(3)  # Esperar a fala terminar
    print("[OK] Fala assíncrona concluída")
except Exception as e:
    print(f"[ERRO]: {e}")

print("\n" + "=" * 60)
print("TESTE CONCLUÍDO")
print("=" * 60)
