from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", 
         "You are a {role}.\n"
         "Use the following context to answer the question.\n"
         "If the context is not relevant, answer based on your knowledge.\n\n"
         "Context:\n{context}"
        ),

        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])