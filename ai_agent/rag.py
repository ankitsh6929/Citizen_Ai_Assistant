from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    FAISS
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


def build_vector_db():

    loader = PyPDFLoader(
        "knowledge_base/schemes.pdf"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(
        "knowledge_base/faiss_index"
    )

    print(
        "Vector DB Created Successfully!"
    )


if __name__ == "__main__":

    build_vector_db()