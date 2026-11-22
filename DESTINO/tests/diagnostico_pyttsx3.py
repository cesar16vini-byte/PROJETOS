import sys
import os

print("=" * 60)
print("DIAGNÓSTICO PROFUNDO - pyttsx3 / SAPI do Windows")
print("=" * 60)

try:
    import pyttsx3
except ImportError as e:
    print(f"[ERRO] pyttsx3 não instalado: {e}")
    sys.exit(1)

# Teste A: Inicializar com driver específico (sapi5)
print("\n[TESTE A] Inicializar com driver 'sapi5'...")
try:
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    print("  -> Engine inicializado com sucesso")
except Exception as e:
    print(f"  -> ERRO: {e}")
    sys.exit(1)

# Teste B: Listar vozes
print("\n[TESTE B] Vozes disponíveis...")
try:
    voices = engine.getProperty("voices")
    print(f"  -> {len(voices)} voz(es):")
    for i, v in enumerate(voices):
        print(f"     [{i}] {v.name} - {v.id}")
except Exception as e:
    print(f"  -> ERRO: {e}")

# Teste C: Definir voz específica (Maria - português)
print("\n[TESTE C] Definir voz Maria (português)...")
try:
    target_voice = None
    for v in voices:
        if "MARIA" in v.id.upper() or "pt-br" in v.id.lower():
            target_voice = v.id
            break
    if target_voice:
        engine.setProperty("voice", target_voice)
        print(f"  -> Voz definida: {target_voice}")
    else:
        print("  -> Voz Maria não encontrada, usando padrão")
except Exception as e:
    print(f"  -> ERRO: {e}")

# Teste D: Verificar volume e rate
print("\n[TESTE D] Configurações atuais...")
try:
    print(f"     Volume: {engine.getProperty('volume')}")
    print(f"     Rate: {engine.getProperty('rate')}")
    print(f"     Voice: {engine.getProperty('voice')}")
except Exception as e:
    print(f"  -> ERRO: {e}")

# Teste E: Falar texto curto
print("\n[TESTE E] Falar texto curto...")
try:
    engine.say("Teste de voz curta.")
    engine.runAndWait()
    print("  -> Fala concluída sem exceção")
except Exception as e:
    print(f"  -> ERRO ao falar: {e}")

# Teste F: Falar texto longo
print("\n[TESTE F] Falar texto longo (simulação do Ollama)...")
try:
    texto_longo = (
        "A capital do Brasil é Brasília. Essa cidade foi inaugurada como capital em 1960. "
        "O design da cidade foi baseado no conceito de Oscar Niemeyer."
    )
    engine.say(texto_longo)
    engine.runAndWait()
    print("  -> Fala longa concluída sem exceção")
except Exception as e:
    print(f"  -> ERRO ao falar texto longo: {e}")

# Teste G: engine.stop() e falar novamente
print("\n[TESTE G] engine.stop() e falar novamente...")
try:
    engine.stop()
    engine.say("Teste depois do stop.")
    engine.runAndWait()
    print("  -> Fala após stop concluída sem exceção")
except Exception as e:
    print(f"  -> ERRO após stop: {e}")

print("\n" + "=" * 60)
print("DIAGNÓSTICO CONCLUÍDO")
print("=" * 60)
print("Responda: Você ouviu alguma das falas acima? (curta, longa, após stop)")
