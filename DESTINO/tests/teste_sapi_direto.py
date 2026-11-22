import sys
import os

print("=" * 60)
print("TESTE SAPI DIRETO (win32com.client)")
print("=" * 60)

try:
    import pythoncom
    import win32com.client
except ImportError as e:
    print(f"[ERRO] win32com não disponível: {e}")
    sys.exit(1)

# Inicializar COM
pythoncom.CoInitialize()

# Criar o objeto SpVoice
try:
    voice = win32com.client.Dispatch("SAPI.SpVoice")
    print("[OK] SAPI.SpVoice criado com sucesso")
except Exception as e:
    print(f"[ERRO] Não consegui criar SAPI.SpVoice: {e}")
    sys.exit(1)

# Listar vozes
try:
    voices = voice.GetVoices()
    print(f"\n[OK] {voices.Count} voz(es) disponível(ões):")
    for i in range(voices.Count):
        v = voices.Item(i)
        print(f"     [{i}] {v.GetDescription()}")
except Exception as e:
    print(f"[ERRO] Não consegui listar vozes: {e}")

# Configurar volume e rate
try:
    voice.Volume = 100  # 0-100
    voice.Rate = 0      # -10 a 10, 0 = normal
    print("\n[OK] Volume=100, Rate=0 configurados")
except Exception as e:
    print(f"[ERRO] Não consegui configurar volume/rate: {e}")

# Testar fala 1: texto curto
print("\n--- TESTE 1: Texto curto ---")
try:
    voice.Speak("Olá, sou o destino. Teste de voz curta.")
    print("[OK] Fala curta concluída sem exceção")
except Exception as e:
    print(f"[ERRO] Falha na fala curta: {e}")

# Testar fala 2: texto longo
print("\n--- TESTE 2: Texto longo ---")
try:
    texto = (
        "A capital do Brasil é Brasília. Essa cidade foi inaugurada como capital em 1960. "
        "O design da cidade foi baseado no conceito de Oscar Niemeyer."
    )
    voice.Speak(texto)
    print("[OK] Fala longa concluída sem exceção")
except Exception as e:
    print(f"[ERRO] Falha na fala longa: {e}")

# Testar fala 3: falar novamente após primeira
print("\n--- TESTE 3: Segunda fala após a primeira ---")
try:
    voice.Speak("Esta é a segunda fala do teste.")
    print("[OK] Segunda fala concluída sem exceção")
except Exception as e:
    print(f"[ERRO] Falha na segunda fala: {e}")

print("\n" + "=" * 60)
print("TESTE CONCLUÍDO")
print("=" * 60)
print("Responda: Você ouviu alguma das três falas acima?")
