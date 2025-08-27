## Data collection
* The data are collected from Alpha Vantage. I gathered daily stock price of AAPL and Nasdaq500. I wanted to find the correlation of AAPL and the date.
* The data are in fine quality, and outliers are important for this study which might indicates the crash day. So the data do not need further cleaning.
* The data are stored as both .csv and .parquet.

## Modeling
* First I find some features of the data. I have tried many types of them and find out that the three days mean and five days delayed data of the aapl stock return are performing best.
* By using the correlation test and other index, it is suggested that the Nasdaq 500 Index cannot help the prediction.
* I seperated the data, and used eighty percent of them to  return to build a linear model to forcast the next day's return, and use the rest forty to test the result.
* The model is under such assumption:

The next day's price is linear with the input;

There are no effect of the macroecnomics;

## Evaluation of the model

The model do not have high accuracy, it is only approximately 44% corrected when predicting the next day's trend.

It is suggested that the model's input and output do not fit a linear correlation. A polynomial regression may result in a higher accuracy.

The test data is not sufficient, more data would result in a better model performance.

More features would be required to improve the model performance.

## Reporting

I have saved the model into the folder and created app.py and app_streamlit.py, users can easily use them to forcast the next day's aapl stock return.