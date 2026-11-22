import sys
import subprocess

print("=" * 60)
print("TESTE VIA POWERSHELL - System.Speech.Synthesis")
print("=" * 60)

def falar_powershell(texto):
    """Fala via PowerShell usando System.Speech do .NET"""
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
            print(f"[OK] PowerShell falou: '{texto[:50]}...'")
            return True
        else:
            print(f"[ERRO] PowerShell falhou: {resultado.stderr[:200]}")
            return False
    except Exception as e:
        print(f"[ERRO] Exceção no PowerShell: {e}")
        return False

# Teste 1: Texto curto
print("\n--- TESTE 1: Texto curto ---")
falar_powershell("Olá, sou o destino. Teste via PowerShell.")

# Teste 2: Texto longo
print("\n--- TESTE 2: Texto longo ---")
texto_longo = (
    "A capital do Brasil é Brasília. Essa cidade foi inaugurada como capital em 1960. "
    "O design da cidade foi baseado no conceito de Oscar Niemeyer."
)
falar_powershell(texto_longo)

# Teste 3: Segunda fala
print("\n--- TESTE 3: Segunda fala ---")
falar_powershell("Esta é a segunda fala via PowerShell.")

print("\n" + "=" * 60)
print("TESTE CONCLUÍDO")
print("=" * 60)
print("Responda: Você ouviu alguma das três falas via PowerShell?")
