# Sentiment Analysis and Stock Price Prediction using HuggingFace and SparkML
This is a group project part of which goes on towards satisfying requirements for course project in the Distributed Data Systems course, MSDS 697, as part of the University of San Francisco, MSDS Program. 


## Team Members
- Gurusankar Gopalakrishnan
- Devendra Govil
- Maneel Reddy
- Akshay Pamnani
- Youshi Zhang

## ML Objectives:

1. Scrape reddit posts, financial 10K reports and stock ticker price data using PRAW, PMAW, EDGAR - API, and AlphaVantage.
2. Automate the data pipeline using PySpark, Airflow, MongoDB and GCS.
3. Performing Sentiment Analysis using Pre-trained Models (Hugging Face- FinBERT) on the reddit posts and financial 10K reports.
4. Use sentiment scores and ticker features like EBITDA, 52wk high/lows etc to predict Stock Prices.


## Install
- We recommend creating a new conda environment using the environment.yml file present in the repo.


## Citation
- This repo relies on the edgar api crawler repo available at this location: https://github.com/nlpaueb/edgar-crawler . 


The citation bibtex is as below:

```
@inproceedings{loukas-etal-2021-edgar,
    title = "{EDGAR}-{CORPUS}: Billions of Tokens Make The World Go Round",
    author = "Loukas, Lefteris  and
      Fergadiotis, Manos  and
      Androutsopoulos, Ion  and
      Malakasiotis, Prodromos",
    booktitle = "Proceedings of the Third Workshop on Economics and Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.econlp-1.2",
    pages = "13--18",
}
```
The whole paper is present here: [https://arxiv.org/abs/2109.14394](https://arxiv.org/abs/2109.14394)


## License
Please see the [GNU General Public License v3.0](https://github.com/nlpaueb/edgar-crawler/blob/main/LICENSE)
