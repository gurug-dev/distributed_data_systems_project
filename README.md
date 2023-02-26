# Sentiment Analysis and Stock Price Prediction using Knowledge Graphs
This is a group project part of which goes on towards satisfying requirements for course project in the Distributed Data Systems course, MSDS 697, as part of the University of San Francisco, MSDS Program. 

Please note that this is a private repository as of now and access to this repo is limited to the group members and the course instructor/grader. 

## Team Members
- Devendra Govil
- Maneel Reddy
- Gurusankar Gopalakrishnan
- Akshay Pamnani
- Youshi Zhang

## ML Objectives:

1. Performing Sentiment Analysis using Pre-trained Models (Hugging Face- FinBERT)
2. Use sentiment analysis to predict Stock Prices
3. Build Knowledge Graph for US Publicly listed firms
4. Perform Community Detection/ Link Prediction to identify knowledge graph embeddings
5. Use Graph Data Science to augment sentiment scores for related/smaller firms and use them to improve stock market predictions



## Install
- We recommend creating a new conda environment using the environment.yml file present in the repo.


## Citation

- This repo uses class material given by Dr. Diane Woodbridge as part of the MSDS 697 course (part of USFCA MSDS curriculum) for setting up base function utilities as well as environment yaml files.

- This repo (as of this current state) relies heavily on the edgar api crawler repo available at this location: https://github.com/nlpaueb/edgar-crawler


The citation bibtex required by the github is present below:

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
