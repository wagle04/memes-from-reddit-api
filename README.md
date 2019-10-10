API created for memes_from_reddit flutter app.

Hosted at: https://memes-from-reddit.herokuapp.com/

To get top pot from specific subreddits:

hit the link: https://memes-from-reddit.herokuapp.com/redditposts <br>
with a post request and body with a format as: <br>

<pre>
{
    "time": "day",
    "limit": 10,
    "subreddits": [
         "tinder",
         "funny",
         "dankmemes"
    ]
}</pre>

where time can be "day","month" or "year" <br>
limit is number of post from specific subreddit<br>
and subreddits is list of subreddits from where you want to get posts. <br>