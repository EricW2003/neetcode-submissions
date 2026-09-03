import heapq
# heap with max size 10 where i can order by the value 
class Twitter:

    def __init__(self):
        
        # for each individual, I have a queue structure containing his 10 most recent tweets
        # for each individual I have a list of the individuals he follows
        self.dic = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        dic = self.dic
        if userId not in dic:
            heap = []
            heapq.heapify(heap)
            dic[userId] = [heap,set([userId])]

        heap = dic[userId][0]
        heapq.heappush(heap,(self.time,tweetId))
        if len(heap)>10:
            heapq.heappop(heap)
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        dic = self.dic

        if userId not in dic:
            heap = []
            heapq.heapify(heap)
            dic[userId] = [heap,set([userId])]
        follow_list = dic[userId][1]

        tweets = []
        for userId1 in follow_list:
            heap = dic[userId1][0]
            for element in heap:
                tweets.append(element)
        heapq.heapify(tweets)
        while len(tweets)>10:
            heapq.heappop(tweets)
        ans = []
        while tweets:
            element = heapq.heappop(tweets)
            ans.append(element[1])
        ans.reverse()
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        dic = self.dic
        if followerId not in dic:
            heap = []
            heapq.heapify(heap)
            dic[followerId] = [heap,set([followerId])]


        follow_list = dic[followerId][1]
        follow_list.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        dic = self.dic
        if followerId not in dic:
            heap = []
            heapq.heapify(heap)
            dic[followerId] = [heap,set([followerId])]


        follow_list = dic[followerId][1]
        if followeeId in follow_list:
            follow_list.remove(followeeId)