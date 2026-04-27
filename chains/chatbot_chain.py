from langchain_core.runnables.history import RunnableWithMessageHistory
from llm.model import get_llm
from prompts.prompt import get_prompt
from memory.memory import get_session_history
from retriever.loader import load_text_file
from retriever.chunking import split_text
from retriever.embeddings import get_embeddings
from retriever.vectorstore import VectorStore


text = load_text_file("./data/sample.txt")
chunks = split_text(text)
embeddings = get_embeddings(chunks)
vector_store = VectorStore(embeddings, chunks)

def get_chatbot():
    llm = get_llm()
    prompt = get_prompt()
    chain = prompt | llm
    chatbot = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    return chatbot

def get_context(query: str):
    query_embedding = get_embeddings([query])[0]
    results = vector_store.search(query_embedding)
    context = "\n".join(results)
    return context