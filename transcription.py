import os
import google.generativeai as genai
from dotenv import load_dotenv

# carrega o .env
load_dotenv()

# Configura o model para a gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# descreve para o modelo como será a conversa
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [genai.upload_file("images.jpeg", mime_type="image/jpeg")],
        }
    ]
)

# Envia para o modelo o que deve ser feito com as informações recebidas
response = chat_session.send_message("Transcreva o que foi escrito acima")
print(response.text)
