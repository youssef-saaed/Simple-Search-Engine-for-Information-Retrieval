# Simple Search Engine for Information Retrieval

This repository hosts the implementation of a Simple Search Engine designed for efficient information retrieval. The project encompasses several stages from data collection to evaluation, ensuring a comprehensive approach to search and retrieval.

## Data Collection

- **CISI Test Collection**: After exploring various test collections, the CISI test collection was chosen for its relevance and comprehensiveness.
- **Parsing to CSV**: Documents, qrels, and topics files were parsed and stored in CSV format for ease of handling and processing.

## Preprocessing

- **Text Processing Function**: A specialized function was created to perform tokenization, case folding, stemming, and removing stopwords using the `nltk` library.
- **Application**: This preprocessing function was applied to all documents to standardize and prepare the data for indexing.

## Indexing

- **DFIndexer**: Utilized DFIndexer to construct an index for the document corpus.
- **Word-Document Dictionary**: Created a dictionary where each word is associated with a set of documents containing that word.
- **Frequency Dictionary**: Formulated a secondary dictionary mapping each word to another dictionary that records the frequency of the word in each document.

## Query Processing

- **Preprocessing Queries**: User queries are preprocessed using the same function applied to documents.
- **TF-IDF Weighting**: Employed TF-IDF weighting to retrieve relevant results for user queries.

## Query Expansion

- **RM3 Model**: Expanded user queries using the RM3 model to enhance the search results.
- **ELMo Re-ranking**: Re-ranked the result documents using ELMo embedding to improve the relevance of the retrieved documents.

## User Interface (UI)

- **Flask Web App**: Developed a simple Flask web application with two pages: one featuring a search bar and button, and another to display the search results.
- **Performance Metrics**: The UI shows the number of documents retrieved and the time taken for the search process.

## Evaluation

- **Search Engine Assessment**: Evaluated the search engine's performance using the qrels and topics parsed during the data collection stage.