from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
Answer the following medical question in 2–3 lines maximum
using ONLY the information provided in the context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""


def create_qa_chain():
    try:
        logger.info("Loading vector store for context")
        db = load_vector_store()

        if db is None:
            raise CustomException("Vector store not present or empty")

        retriever = db.as_retriever(search_kwargs={"k": 1})

        logger.info("Loading LLM (OpenAI)")
        llm = load_llm()   # ✅ OpenAI LLM, no HF args

        if llm is None:
            raise CustomException("LLM not loaded")

        prompt = ChatPromptTemplate.from_template(CUSTOM_PROMPT_TEMPLATE)

        qa_chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        logger.info("Successfully created the Medical QA chain")
        return qa_chain

    except Exception as e:
        error_message = CustomException("Failed to make QA chain", e)
        logger.error(str(error_message))
        raise error_message
