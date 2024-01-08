from enum import Enum


AI_ROLE_OPTIONS_EN: list[str] = [
    "",
    "helpful assistant",
    "code assistant",
    "code reviewer",
    "text improver",
    "cinema expert",
    "sport expert",
    "online games expert",
    "food recipes expert",
    "English grammar expert",
    "friendly and helpful teaching assistant",
    "laconic assistant",
    "helpful, pattern-following assistant",
    "translate corporate jargon into plain English",
]

AI_ROLE_OPTIONS_RU: list[str] = [
    "",
    "ассистент, который готов помочь",
    "ассистент программиста",
    "рецензент кода программиста",
    "эксперт по улучшению текста",
    "эксперт по кинематографу",
    "эксперт в области спорта",
    "эксперт в онлайн-играх",
    "эксперт по рецептам блюд",
    "эксперт по английской грамматике",
    "эксперт по русской грамматике",
    "дружелюбный и полезный помощник преподавателя",
    "лаконичный помощник",
    "полезный помощник, следующий шаблонам",
    "переводчик корпоративного жаргона на простой русский",
]

REPO_URL: str = "https://github.com/dKosarevsky/AI-Talks"
README_URL: str = f"{REPO_URL}#readme"
AI_TALKS_URL: str = "https://ai-talks.streamlit.app/"
HEADERS: dict = {"Content-Type": "application/json; charset=utf-8"}
ADMIN_TG: str = "https://t.me/wd4000"

TEMP_KEY: str = "temperature"
TOP_P_KEY: str = "top_p"
MAX_TOKENS_KEY: str = "max_tokens"
PRESENCE_PENALTY_KEY: str = "presence_penalty"
FREQUENCY_PENALTY_KEY: str = "frequency_penalty"
USER_TXT_KEY: str = "user_text"


class AIModels(Enum):
    gpt35_turbo = "gpt-3.5-turbo-1106"
    gpt35_turbo_instruct = "gpt-3.5-turbo-instruct"
    gpt4 = "gpt-4"
    gpt4_32 = "gpt-4-32k"
    gpt4_1106 = "gpt-4-1106-preview"
    gpt4_vision = "gpt-4-vision-preview"
    dalle_3 = "dall-e-3"
