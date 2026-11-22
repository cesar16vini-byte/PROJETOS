import datetime
import requests
import voz

URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"
MAX_HISTORY = 6
USAR_NAME = "César"

conversation_history = []


def comando_local(mensage):
    texto = mensage.lower().strip()

    if texto in ("que horas são", "qual é a hora", "hora agora"):
        agora = datetime.datetime.now()
        return f"São {agora.hour} horas e {agora.minute} minutos."

    if texto in ("quem é você", "qual é o seu nome"):
        return "Eu sou o DESTINO, seu assistente local de voz."

    if texto in ("sair", "encerrar", "tchau", "desligar", "encerrar processo"):
        return "SAIR"

    # Não é um comando conhecido
    return None


print("=== Assistente local DESTINO ===")
print("Fale com o microfone. Diga 'sair' para encerrar.\n")

voz.speak("Olá, sou o DESTINO. Estou pronto para conversar.")

while True:
    user_message = voz.listen()

    if not user_message:
        continue

    resposta_local = comando_local(user_message)
    if resposta_local is not None:
        if resposta_local == "SAIR":
            voz.speak("Até logo!")
            break
        voz.speak(resposta_local)
        continue

    conversation_history.append(user_message)

    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]

    full_prompt = "\n".join(conversation_history)

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(URL, json=payload, timeout=60)
    except Exception as e:
        voz.speak("Desculpe, não consegui me conectar ao Ollama.")
        continue

    if response.status_code == 200:
        result = response.json()
        ai_text = result.get("response", "Sem resposta")

        if not ai_text or ai_text.strip() == "":
            ai_text = "Desculpe, não tive resposta para isso."

        conversation_history.append(ai_text)

        try:
            voz.speak(ai_text)
        except Exception:
            voz.speak("Desculpe, tive um erro ao falar.")
    else:
        voz.speak("Desculpe, tive um erro ao processar.")
        print("Erro. Código:", response.status_code)
