Sentiment Analysis on Movie Reviews
===================================

As Mentioned Earlier...This is a go at Machine learning (Sentiment Analysis on Movie Reveiws) to take my mind off of my inability to code ... *Oh the sadness*

It's written for Python 3.3 and it's based on [`scikit-learn`](http://scikit-learn.org/) and [`nltk`](http://www.nltk.org/).


Problem description
-----------------

This project presents a chance to benchmark the sentiment-analysis ideas on the [Rotten Tomatoes](http://www.rottentomatoes.com/) dataset. I thought it was best to label phrases on a scale of five values: negative, somewhat negative, neutral, somewhat positive, positive.

Some examples:

 - **4** (positive): _"They works spectacularly well... A shiver-inducing, nerve-rattling ride."_
 - **3** (somewhat positive): _"rooted in a sincere performance by the title character undergoing midlife crisis"_
 - **2** (neutral): _"Its everything you would expect -- but nothing more."_
 - **1** (somewhat negative): _"But it does not leave you with much."_
 - **0** (negative): _"The movies progression into rambling incoherence gives new meaning to the phrase fatal script error."_

So the goal of the project is to produce an algorithm to classify phrases into these categories. 
