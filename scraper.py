import praw

reddit = praw.Reddit(client_id='v2N8VC1ujIgDLg', \
                     client_secret='B5gdYh_sP74tPOQhFdviwE1Brko', \
                     user_agent='scraper_188', \
                     username='ACCOUNT', \
                     password='PASSWORD')

def scrape(subreddits):

    for sub in subreddits:
        print('Fetching from ', sub)
        subreddit = reddit.subreddit(sub)

        top_subreddit = subreddit.top(limit=1000)

        with open('top'+sub+'.txt', 'w') as f:
            for submission in top_subreddit:
                f.write(submission.title+'\n')

if __name__ == '__main__':
    
    subreddits = ['AskReddit', 'AskWomen', 'AskMen']
    scrape(subreddits)