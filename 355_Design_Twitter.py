from typing import List
import heapq
class Twitter:
    """
    Design a simplified version of Twitter where users can post tweets,
    follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

    Implement the Twitter class:

    Twitter() Initializes your twitter object.

    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
    Each call to this function will be made with a unique tweetId.

    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
    Each item in the news feed must be posted by users who the user followed or by the user themself. 
    Tweets must be ordered from most recent to least recent.

    void follow(int followerId, int followeeId) The user with ID followerId
    started following the user with ID followeeId.

    void unfollow(int followerId, int followeeId) The user with ID followerId 
    started unfollowing the user with ID followeeId.
    """
    def __init__(self):
        #following dictionary keeps track of users following
        self.followingDict = dict()
        #heapq of tweets
        self.tweets = []
        #timer for heapq
        self.timer = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        #increase timer by 1 for heapq
        self.timer += 1
        #negative timer for maxheap
        heapq.heappush(self.tweets,[-self.timer,tweetId,userId])
        #if user doesn't exist, add user to following dict following self
        if userId not in self.followingDict.keys():
            self.followingDict[userId] = [userId]
    def getNewsFeed(self, userId: int) -> List[int]:
        #if userId is None, return empty feed
        if not userId:
            return []
        #user doesn't exist, add to followingDict and follow self.
        if userId not in self.followingDict.keys():
            self.followingDict[userId] = [userId]
        #create newsFeed list to heapify
        newsFeed = list(self.tweets)
        heapq.heapify(newsFeed)
        #create unique feed to return
        uniqueFeed = []
        #while less than 10 tweets and newsFeed is not empty
        while len(uniqueFeed) < 10 and len(newsFeed) > 0:
            #pop heap
            time,tweetId,tweeter = heapq.heappop(newsFeed)
            #if person who tweeted tweet is in followed by userId, append tweet to uniqueFeed
            if tweeter in self.followingDict[userId]:
                uniqueFeed.append(tweetId)
        return uniqueFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        #append followeeId to followerId
        listOfFollowing = self.followingDict.get(followerId,[followerId])
        listOfFollowing.append(followeeId)
        self.followingDict[followerId] = listOfFollowing
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if not following in first place, do nothing
        if followerId not in self.followingDict.keys():
            return
        #delete followeeId
        if followeeId in self.followingDict[followerId]:
            del(self.followingDict[followerId][self.followingDict[followerId].index(followeeId)])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)