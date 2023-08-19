import praw
import pandas as pd
from pandas import Series, DataFrame
from praw.models import MoreComments
import datetime

# Read-only instance
reddit = praw.Reddit(client_id="7HxEnAcoGVby_dN8OBi1cg",
                     client_secret="-WWpb7cnPjrTpkU5YAGHrMQJVuojdA",
                     password="zlz970601",
                     user_agent="testscript by u/lizzhang97",
                     username="lizzhang97",
                     )

post_comments = []
subreddit = reddit.subreddit("scotland")
submissions = subreddit.search("scotland independence", sort="most_comment", time_filter="year", limit=None)

# Sort the search results by comment count
sorted_results = sorted(submissions, key=lambda x: x.num_comments, reverse=True)

# Print the URLs of the matching Reddit posts
count = 0
for link in sorted_results:
        count+=1
        comment_url = f"https://www.reddit.com/r/scotland/comments/{link.id}/"
        submission = reddit.submission(url=comment_url)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            post_comments.append({'comment': comment.body,
                                  'timestamp': comment.created_utc})

print(count)



# creating a dataframe
comments_df = pd.DataFrame(post_comments,
                           columns=['comment', 'timestamp'])
comments_df
comments_df.to_csv("Comments scotland239.csv", index=True)