from google import genai
from google.genai import types


class GeminiLLM:
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash",
                 temperature: float = 0.7, top_p: float = 0.9, top_k: int = 40):
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=self.temperature,
                top_p=self.top_p,
                top_k=self.top_k,
            )
        )
        return response.text
