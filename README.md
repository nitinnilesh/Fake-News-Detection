# Fake-News-Detection

Course Project of IRE M-18

## Dataset Used:

We scraped the fake data from [Faking News](fakingnews.com) of various categories which is as follows
  - India,
  - Politics,
  - Entertainment,
  - Technology
We have a total of 299 samples of both real and fake news.

## Model

We have trained an LSTM model followed by dense layer. GloVe embedding of 300 dimensions has been used. RMSProp Optimizer is used with binary cross entropy loss. We ran it for 10 epochs.
