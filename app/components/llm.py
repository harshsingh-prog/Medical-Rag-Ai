from langchain_openai import ChatOpenAI
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

import os

logger = get_logger(__name__)


def load_llm():
    try:
        logger.info("Loading OpenAI LLM")

        llm = ChatOpenAI(
            model="gpt-4o-mini",   # ✅ Best choice for RAG
            temperature=0.3,
            max_tokens=512,
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        logger.info("OpenAI LLM loaded successfully")
        return llm

    except Exception as e:
        error_message = CustomException("Failed to load OpenAI LLM", e)
        logger.error(str(error_message))
        raise error_message
