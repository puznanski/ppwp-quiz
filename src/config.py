import os
from dotenv import load_dotenv
from llm_gemini import GeminiLLM
from llm_openai import OpenAILLM

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")


def get_llm():
    if LLM_PROVIDER == "openai":
        return OpenAILLM(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
        )
    else:
        return GeminiLLM(
            api_key=os.getenv("GEMINI_API_KEY"),
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            temperature=float(os.getenv("GEMINI_TEMPERATURE", 0.7)),
            top_p=float(os.getenv("GEMINI_TOP_P", 0.9)),
            top_k=int(os.getenv("GEMINI_TOP_K", 40)),
        )
