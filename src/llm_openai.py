from openai import OpenAI


class OpenAILLM:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini",
                 temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        return response.choices[0].message.content
