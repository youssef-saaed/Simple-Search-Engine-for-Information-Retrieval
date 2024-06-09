import pandas as pd
import pyterrier as pt
import os

os.environ["JAVA_HOME"] = r"D:\Program Files\Java\jdk-22"
if not pt.started():
    pt.init()

docs_df = pd.read_csv("../data/documents.csv")

docs_df["docno"] = docs_df["DocID"].astype(str)
indexer = pt.DFIndexer(r"D:\CSAI\Year 2\Semester 2\DSAI 201\Project\UI search engine\index", overwrite=True)
index_ref = indexer.index(docs_df["Content"], docs_df["docno"])
index = pt.IndexFactory.of(index_ref)

tfidf_retriever = pt.BatchRetrieve(index, wmodel = "TF_IDF", controls = {"c": 0.15}, num_results = 100)

def retrieve_results(query: str):
    tfidf_results = tfidf_retriever.search(query)
    results_documents = docs_df[docs_df["docno"].isin(tfidf_results["docno"])]
    return results_documents