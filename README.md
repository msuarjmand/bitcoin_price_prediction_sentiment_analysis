# bitcoin_price_prediction_sentiment_analysis
This repository is a source code for the published paper entitled "Bitcoin price prediction based on financial data, technical indicators, and news headlines sentiment analysis using CNN and GRU deep learning algorithms".

# Bitcoin price prediction based on financial data, technical indicators, and news headlines sentiment analysis using CNN and GRU deep learning algorithms

The code repository for "Bitcoin price prediction based on financial data, technical indicators, and news headlines sentiment analysis using CNN and GRU deep learning algorithms" [paper](https://ieeexplore.ieee.org/abstract/document/10454082/) (DCHPC 2024). If you use any content of this repo for your work, please cite the following bib entry:
  
    @inproceedings{
        10454082,
        author={Arjmand, Masoud, and Kazeminia, Saman and Sajedi, Hedieh},
        booktitle={2024 2024 Third International Conference on Distributed Computing and High Performance Computing (DCHPC)}, 
        title={Bitcoin price prediction based on financial data, technical indicators, and news headlines sentiment analysis using CNN and GRU deep learning algorithms}, 
        year={2024},
        pages={1-7},
        doi={10.1109/DCHPC60845.2024.10454082}
    }


## Bitcoin price prediction based on financial data, technical indicators, and news headlines sentiment analysis using CNN and GRU deep learning algorithms

Bitcoin is the leading cryptocurrency with the highest market value among digital currencies. Therefore, predicting the value of Bitcoin can help to understand the entire cryptocurrency market. However, Bitcoin has had a lot of price fluctuations since its inception. In this paper, we will forecast the price of Bitcoin using news headline analysis, technical analysis indicators, and historical financial data. The news headlines used in this article are scraped from the Cointelegraph news website, which contains 3988 news headlines related to Bitcoin between 2/7/2020 and 3/8/2021. A transformer pre-trained model on cryptocurrency-related texts called CryptoBERT, which is a BERT-based sentiment analysis model, has been used to analyze the textual data. Also, a novel hybrid 2DCNN-GRU deep learning model has been used to predict the price. A parameter tuning method based on orthogonal arrays called the Taguchi method was employed to adjust the parameters of this model. Finally, to examine the proposed model’s efficiency, the results were compared with other deep learning models from the literature review that used text data to predict bitcoin prices. The results show that this model outperformed other models in terms of the MAE criterion, while in the other three criteria, namely MSE, RMSE, and MAPE, it still demonstrated good results.

## Prerequisites

The following packages are required to run the code:

- [TensorFlow](https://www.tensorflow.org/resources/libraries-extensions)
- [TensorFlow_Keras](https://www.tensorflow.org/guide/keras)
- [NLTK](https://www.nltk.org/)
- [TA-Lib](https://ta-lib.org/)
- [Transformers](https://huggingface.co/docs/transformers/en/index)
