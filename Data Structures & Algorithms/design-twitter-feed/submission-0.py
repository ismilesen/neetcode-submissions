class Twitter:

    def __init__(self):
        #list of users with a list of tweets
        #list of users with list of following
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        #self.followMap[1].add(2)
        #self.tweetmap[1].append(2)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #if user inside tweet map then add to its tweets.
        #if not then add the user and its tweet. Key = user and values are tweets in hashmap
        #everytime we post a tweet we add user to followmap and tweetmap if not in there
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #if user not in the tweetmap or followmap then null
        #if user in tweetmap but no following then null
        #return as many tweets as followers limited to 10
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        #if followee not in tweetmap and followmap then null
        #if user in tweetmap and followmap we can add user to followees list
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if followee not in tweetmap and followmap then null
        #if user in tweetmap and followmap and following then we can remove user to followees list
        self.followMap[followerId].discard(followeeId)
        
