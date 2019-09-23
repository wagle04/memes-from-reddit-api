from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import json
import requests
import praw

app = Flask(__name__)
api = Api(app)


class RedditPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('time',
                        type=str,
                        required=True, help='time missing')

    parser.add_argument('limit',
                        type=int,
                        required=True, help='limit missing')

    parser.add_argument('subreddits',
                        type=list,
                        required=True,
                        help='list of subreddit missing')

    def post(self):
        data = RedditPost.parser.parse_args()

        time = data['time']
        limit = data['limit']
        list_of_subreddit = data['subreddits']
        
        print(time)
        print(limit)
        print(list_of_subreddit)

        list_of_all_post = []
        if len(list_of_subreddit[0]) != 0:
            for s in list_of_subreddit:
                subreddit = reddit.subreddit(s)
                all_posts = subreddit.top(time, limit=limit)
                for post in all_posts:
                    url = (post.url)
                    is_image = False
                    if(str(url[-3:]) == "jpg" or str(url[-3:]) == "png"):
                        is_image = True
                    if is_image:
                        list_of_all_post.append(
                            [str(subreddit), post.url, post.title])

            print(list_of_all_post)
            return jsonify(list_of_all_post)
        else:
            return {"message":"error"},400


api.add_resource(RedditPost, '/redditposts')

reddit = praw.Reddit(client_id='AJmL9uQjacx_8A',
                     client_secret='gq8wQA6JzfZDHuiMI09dciduy8Q',
                     user_agent='redditinsta')


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1>"


app.debug = True
app.run()

# if __name__=='__main__':
#     app.run(port=5000,debug=True)
