# Project 1 Generative Text

Raul Pegan, rpegan@ucsd.edu

## Abstract

Text generation is cool, but there is extra value when there is something that is impacted by the text generation. For this project, I generate Reddit post titles, and post them to Reddit. This way we can see how real humans interact with machine generated content when they are not aware it is machine generated. Sort of illustrating the most genuine interaction between man and machine, a true Turing test. I generated AskReddit, AskMen, and AskWomen titles. Some are very funny, some are very interesting and realistic, and some are actual questions that have been asked before. Of all my attempts to get responses, two threads got several replies (See Results section). This experiment used a GRU-based RNN.

## Files

Training data:
- topAskMen.txt - Top posts retrieved from Reddit's AskMen
- topAskWomen.txt - Top posts retrieved from Reddit's AskWomen
- topAskReddit.txt - Top posts retrieved from Reddit's AskReddit

- project1.ipynb - project code
- scraper.py - script that scrapes reddit and generates the training data

## Results

Results:
- askmenresults.txt - generated post titles for Reddit's AskMen
- askwomenresults.txt - generated post titles for Reddit's AskWomen
- askredditresults.txt - generated post titles for Reddit's AskReddit

Real people's responses:

https://www.reddit.com/r/AskWomen/comments/bdjzue/women_who_decided_not_to_have_a_dog_what_made_you/

https://www.reddit.com/r/AskMen/comments/bdk59k/men_of_reddit_how_do_you_handle_a_friend_that_you/


## Notes

Any implementation details or notes on repeating your work. 

- The scraper requires a `pip install praw`
- I removed my reddit credentials from the script in order to maintain my account's security, so it won't work

## Reference

Project requirements: [doc](https://docs.google.com/document/d/13ueceIyuUc4ATD7B-SFZK641MycFZ57eZ9n1lQ3Y1CM/edit?usp=sharing)
