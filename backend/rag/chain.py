from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def build_chain(system_prompt):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Chat History:\n{history}\n\nUser Question:\n{question}"),
        ]
    )

    chain = prompt | llm
    return chain
