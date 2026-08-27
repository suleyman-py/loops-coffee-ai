import os
import requests
from config import Config

class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def yanit_uret(self, mesaj):
        if not self.api_key:
            return "Sistem şu an demo modunda. Lütfen API anahtarınızı kontrol edin."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": Config.BUSINESS_CONTEXT},
                {"role": "user", "content": mesaj}
            ]
        }

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            print(f"--- GROQ STATUS CODE: {response.status_code} ---")
            print(f"--- GROQ RESPONSE: {response.text} ---")
            
            data = response.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            print(f"--- AI SERVICE HATA DETAYI: {e} ---")
            return "Üzgünüm, şu an bağlantı kuramıyorum. Lütfen daha sonra tekrar deneyin."

ai_service = AIService()