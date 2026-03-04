from langchain_community.vectorstores import Chroma

def create_vectorstore(docs, embeddings):

    vectordb = Chroma.from_texts(
        texts=[d["content"] for d in docs],
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vectordb