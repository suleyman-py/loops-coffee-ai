import os
import requests
from config import Config

class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def yanit_uret(self, mesaj):


ai_service = AIService()