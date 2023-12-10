
# NewzifyHub : News Research Tool 📈 
[![LangChain](https://img.shields.io/badge/LangChain-UnstructuredURL%20Loader-blue)](https://langchain.io/) [![OpenAI](https://img.shields.io/badge/OpenAI-Language%20Model-orange)](https://www.openai.com/) [![Streamlit](https://img.shields.io/badge/Streamlit-User%20Interface-green)](https://streamlit.io/) [![FAISS](https://img.shields.io/badge/FAISS-Similarity%20Search-red)](https://github.com/facebookresearch/faiss)

Welcome to NewzifyHub, your go-to news research tool powered by cutting-edge technologies. NewzifyHub seamlessly integrates LangChain's UnstructuredURL Loader and OpenAI's Language Model (LLM) to provide a comprehensive solution for efficient news exploration.

NewzifyHub is a user-friendly news research tool designed for effortless information retrieval. Users can input article URLs and ask questions to receive relevant insights from the stock market and financial domain.

![](NewzifyHub.jpg)

## Features:

- **LangChain Integration:** Utilizing LangChain's UnstructuredURL Loader, NewzifyHub extracts raw text from news articles based on their URLs, ensuring a reliable and consistent data source.

- **OpenAI Language Model:** NewzifyHub leverages OpenAI's powerful Language Model (LLM) for natural language processing, enabling robust interaction through queries and answers.

- **Embedding Vector Construction:** The backend of NewzifyHub constructs embedding vectors using OpenAI's embeddings. This enhances information retrieval by capturing semantic similarities within the data.

- **FAISS Integration:** To enable swift and effective retrieval of relevant information, NewzifyHub incorporates FAISS, a powerful similarity search library. This ensures that users can quickly find the most pertinent news articles based on their queries.

- **Streamlit Frontend:** The user-friendly interface is built using Streamlit, allowing users to effortlessly navigate and explore news content directly through their web browsers.

## How it Works:
1. **URL Loading:** NewzifyHub starts by loading raw text from news articles using LangChain's UnstructuredURL Loader, providing a solid foundation for information extraction.

2. **Embedding Vector Generation:** OpenAI's embeddings are employed to construct meaningful embedding vectors for each article, capturing the essence of the content.

3. **FAISS Search:** The generated embedding vectors are indexed using FAISS, enabling NewzifyHub to perform efficient similarity searches and deliver relevant results quickly.

4. **LLM Interaction:** Users can interact with the Language Model by inputting queries, receiving informative answers, and obtaining source URLs for further exploration.

To get started with NewzifyHub, follow the installation steps and documentation provided in the respective sections.
## Installation

1.Clone this repository to your local machine using:

```bash
  https://github.com/yunus5603/Newzify-News-Research-Tool.git
```

2. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
3.Set up your OpenAI API key by creating a .env file in the project root and adding your API

```bash
  OPENAI_API_KEY=your_api_key_here
```
## Usage/Examples

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- On the sidebar, you can input URLs directly.

- Initiate the data loading and processing by clicking "Process URLs."

- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.

- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.

- The FAISS index will be saved in a local file path in pickle format for future use.
- One can now ask a question and get the answer based on those news articles
- we used following news articles for trainings
  - https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html
  - https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html
  - https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html

## Project Structure

- **main.py:** The main Streamlit application script.
- **requirements.txt:** A list of required Python packages for the project.
- **faiss_store_openai.pkl:** A pickle file to store the FAISS index.
- **.env:** Configuration file for storing your OpenAI API key.
