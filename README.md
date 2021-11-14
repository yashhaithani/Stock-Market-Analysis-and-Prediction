# Stock-Market-Analysis-and-Prediction
It is a model for a basic recommendation system which finds out the best 3 companies from the dataset to invest in and predicts a closing price for the opening value.

Model

1. KNN finds the closest examples from dataset in feature space based on opening and gain values.
2. Top 3 classes (companies) are selected.
3. Dataset of these top 3 classes (companies) is queried from the original dataset.
4. Linear Regression is performed with these top 3 classes (companies).

Dataset

Taken from https://www.kaggle.com/rohanrao/nifty50-stock-market-data

1. Based on <= 10% null values in any feature column, dataset of few companies is selected and merged into a single .xlsx and .csv file.
2. New dataset is segmented into 2 parts -
  <i.>  2006-2019 (training examples)
  <ii.> 2020-2021 (testing examples)
