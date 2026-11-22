import sys
sys.path.insert(0, "C:/Users/Cesar/Documents/Projetos/DESTINO/DESTINO")
import voz

print("=== TESTE DE ÁUDIO DO DESTINO ===\n")

# Teste 1: Texto curto (comando local)
print("TESTE 1: Texto curto")
voz.speak("Olá, sou o DESTINO. Teste de voz curta.")
print("-> Teste 1 concluído\n")

# Teste 2: Texto longo (como resposta do Ollama)
print("TESTE 2: Texto longo (resposta do Ollama)")
texto_longo = (
    "A capital do Brasil é Brasília. Essa cidade foi inaugurada como capital em 1960, "
    "substituindo a antiga capital, Rio de Janeiro. O design da cidade foi baseado no "
    "conceito de Oscar Niemeyer, um renomado arquiteto brasileiro."
)
voz.speak(texto_longo)
print("-> Teste 2 concluído\n")

# Teste 3: Múltiplas falações em sequência (simula o loop do assistente)
print("TESTE 3: Múltiplas falações em sequência")
voz.speak("Primeira fala.")
voz.speak("Segunda fala.")
voz.speak("Terceira e última fala do teste.")
print("-> Teste 3 concluído\n")

print("=== TODOS OS TESTES CONCLUÍDOS ===")
print("Se você ouviu as três falas acima, o áudio está funcionando perfeitamente.")
