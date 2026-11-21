import requests
import voz

URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"
MAX_HISTORY = 6

conversation_history = []

print("=== Assistente local DESTINO ===")
print("Fale com o microfone. Diga 'sair' para encerrar.\n")

voz.speak("Olá, sou o DESTINO. Estou pronto para conversar.")

while True:
    user_message = voz.listen()

    if not user_message:
        continue

    if user_message.lower() == "sair":
        voz.speak("Até logo!")
        break

    conversation_history.append(user_message)

    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]

    full_prompt = "\n".join(conversation_history)

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(URL, json=payload, timeout=60)

    if response.status_code == 200:
        result = response.json()
        ai_text = result.get("response", "Sem resposta")

        conversation_history.append(ai_text)

        voz.speak(ai_text)
    else:
        voz.speak("Desculpe, tive um erro ao processar.")
        print("Erro. Código:", response.status_code)