from langchain_community.vectorstores import (
    FAISS
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "knowledge_base/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def search_rag(query):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return "\n\n".join(
        [doc.page_content for doc in docs]
    )