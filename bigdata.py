import os
import sys
import json
from langchain.embeddings import VertexAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import VertexAI
from langchain.agents import AgentType, Tool, initialize_agent

# Set Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "YOUR SERVICE ACCOUNT KEY"

# Initialize VertexAI LLM
llm = VertexAI(model_name="text-bison@001", max_output_tokens=512, temperature=0, top_p=0.8, top_k=40, verbose=True)

def big_data():
    # Load data using WebBaseLoader
    loader = WebBaseLoader("https://cloud.google.com/bigquery/docs/introduction")
    data = loader.load()
    
    # Split documents using CharacterTextSplitter
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1500, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    
    # Initialize VertexAI LLM and embeddings
    llm = VertexAI(model_name="text-bison@001", max_output_tokens=512, temperature=0, top_p=0.8, top_k=40)
    embeddings = VertexAIEmbeddings()
    
    # Create FAISS vector store from documents
    vectorStore_openAI = FAISS.from_documents(docs, embeddings)
    
    # Create RetrievalQA chain
    retrieval_chain = RetrievalQA.from_chain_type(llm, chain_type="refine",
                                                  retriever=vectorStore_openAI.as_retriever(),
                                                  return_source_documents=True)
    
    return retrieval_chain

x = big_data()

# Define tools
tools = [
    Tool(
        name="big_data",
        func=lambda query: x({"query": query}),
        description="Empowering seamless understanding of BigQuery. Enter queries on view creation, BigQuery insights, and more.\
                    Your gateway to clear explanations for complex concepts and procedures within the expansive realm of BigQuery documentation."
    ),
]

# Initialize agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True
)

# Example prompt
prompt = "how to create a view in bigquery"
answer = agent(prompt)

