import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from groq import Groq
from datetime import datetime

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

historial = {}

def hablar_con_jarvis(numero, mensaje):
    fecha_actual = datetime.now().strftime("%A, %d de %B de %Y - %H:%M")

    if numero not in historial:
        historial[numero] = []

    historial[numero].append({"role": "user", "content": mensaje})
    mensajes_recientes = historial[numero][-10:]

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""Tu nombre es Jarvis, el asistente personal inteligente de Moisés.
Tu propósito es ser su mano derecha, gestionando su vida, su trabajo y sus conocimientos.

DIRECTIVAS DE OPERACIÓN:
1. GESTIÓN DE RECORDATORIOS: Si Moisés menciona tareas, fechas o eventos, confírmalos como anotados.
2. RESOLUCIÓN DE CONSULTAS: Responde cualquier pregunta con precisión, claridad y veracidad.
3. CANAL WHATSAPP: Usa emojis, párrafos breves y tono elegante pero cercano. 📱
4. EXPERTO TÉCNICO: Ayuda con cualquier tema, desde lo más básico hasta lo más complejo.
5. IDENTIDAD: Llama a Moisés 'Señor' o 'Moisés'. Sé siempre proactivo.

DATOS DEL ENTORNO:
- Fecha y Hora: {fecha_actual}
- Ubicación: Montelíbano, Córdoba, Colombia.
- Usuario: Moisés, experto en automatización y desarrollador de software."""
            }
        ] + mensajes_recientes,
        max_tokens=1024,
        temperature=0.7
    )

    contenido = respuesta.choices[0].message.content
    historial[numero].append({"role": "assistant", "content": contenido})
    return contenido


@app.route("/webhook", methods=["POST"])
def webhook():
    numero = request.form.get("From", "")
    mensaje = request.form.get("Body", "")
    respuesta_jarvis = hablar_con_jarvis(numero, mensaje)
    resp = MessagingResponse()
    resp.message(respuesta_jarvis)
    return str(resp)


@app.route("/")
def home():
    return "🦾 Jarvis está activo y en línea."


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)