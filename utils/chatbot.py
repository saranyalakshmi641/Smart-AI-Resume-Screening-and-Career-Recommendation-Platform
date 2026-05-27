from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def build_chatbot(vectorstore):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.3
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    class CareerChatbot:

        def invoke(self, query):

            docs = retriever.get_relevant_documents(
                query
            )

            context = "\n".join([
                doc.page_content
                for doc in docs
            ])

            prompt = f"""
            You are an intelligent AI Career Assistant.

            Use the resume context below to answer.

            Resume Context:
            {context}

            User Question:
            {query}

            Give detailed professional answers.
            """

            response = llm.invoke(prompt)

            return {
                "result": response.content
            }

    return CareerChatbot()