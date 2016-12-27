#!/usr/bin/python2
import twitter
apiTwitter = twitter.Api(consumer_key="sNbr6JF5MKBGCyYFv80NoW8lE", consumer_secret="pTwfMrlGHOZCbTc8LF1sFTDA9XwJnrQha6Avol7i17feDzo2ie", access_token_key="94489055-KDgQiLZYkPwmRvWuIUFYX7Y594sq35Bl6m20bdf4n", access_token_secret="G7JnBSfeUkevqsJqSYgEtsMuJN52FUO6OQ9HMTtQgZAMV")
tw_query = raw_input("What's the Trending Topic you want to search: ")
query = apiTwitter.GetSearch(tw_query, count=20)
for result in query:
    print "Tweet: %s " %(result.text)
    print "Creation date: %s " %(result.created_at)
    print "Favs count: %d " %(result.favorite_count)
    print "Language: %s " %(result.lang)
    print "Retweets count: %d " %(result.retweet_count)
    print "Account: %s " %(result.user.screen_name)
    print "\n"
