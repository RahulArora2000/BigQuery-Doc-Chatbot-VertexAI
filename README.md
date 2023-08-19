# BigQuery Documentation Chatbot using Vertex AI and Langchain

This repository contains code that utilizes Google Cloud's Vertex AI Language Model (LLM) and the Langchain framework to build a chatbot that can provide answers from the official BigQuery documentation for various queries. The chatbot uses the Vertex AI LLM to generate responses and leverages Langchain's capabilities for document loading, text splitting, embeddings, and vector stores to enhance its functionality.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt //Just conatin Langchain and GCP credential
```

3. Set up Google Cloud credentials:

Replace `"supply-chain-twin-349311-5efed3f5c999 (1).json"` with the path to your Google Cloud service account credentials JSON file in the following line of the code:

```python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path/to/your/credentials.json"
```

## Usage

1. Run the script:

```bash
python bigdata.py
```

2. The chatbot will prompt you to enter a question related to BigQuery. For example:

```
Enter your question about BigQuery: how to create a view in BigQuery
```

3. The chatbot will process your question and provide a relevant answer sourced from the official BigQuery documentation.

## Code Structure

- `chatbot.py`: The main script that sets up and runs the chatbot.
- `langchain/`: A directory containing Langchain framework components used in the chatbot.
- `langchain/embeddings.py`: Defines VertexAI embeddings.
- `langchain/text_splitter.py`: Defines the CharacterTextSplitter class for document splitting.
- `langchain/document_loaders.py`: Defines the WebBaseLoader class for loading web documents.
- `langchain/vectorstores.py`: Defines the FAISS class for creating vector stores.
- `langchain/chains.py`: Defines the RetrievalQA class for building retrieval chains.
- `langchain/llms.py`: Defines the VertexAI class for using the Vertex AI LLM.
- `langchain/agents.py`: Defines AgentType, Tool, and initialize_agent functions for creating the chatbot agent.

## Tools

The chatbot has a set of predefined tools that allow users to interact with the BigQuery documentation effectively:

- **big_data**: Empowers seamless understanding of BigQuery. Enter queries on view creation, BigQuery insights, and more. This tool acts as your gateway to clear explanations for complex concepts and procedures within the expansive realm of BigQuery documentation.

## Example

You can interact with the chatbot using the provided code. Customize the tools, prompts, and interactions based on your preferences and needs.

---

Feel free to modify, enhance, and extend the functionality of this chatbot according to your requirements. If you have any questions or need further assistance, don't hesitate to ask!