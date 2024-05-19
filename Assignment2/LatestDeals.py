
class LatestDeals:
    def __init__(self, store, item, votes, username, timestamp, category, replies, views, url):
        self.store = store
        self.item = item
        self.votes = votes
        self.username = username
        self.timestamp = timestamp
        self.category = category
        self.replies = replies
        self.views = views
        self.url = url

    def print_info(self):
        print(f"Store: {self.store}")
        print(f"Item: {self.item}")
        print(f"Votes: {self.votes}")
        print(f"Username: {self.username}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Category: {self.category}")
        print(f"Replies: {self.replies}")
        print(f"Views: {self.views}")
        print(f"Url: {self.url}")
        print("-------------------------")

    def print_info_file(self):
        return f"Store: {self.store}\nItem: {self.item} \nVotes: {self.votes} \nUsername: {self.username} \nTimestamp: {self.timestamp} \nCategory: {self.category} \nReplies: {self.replies} \nViews: {self.views} \nUrl: {self.url}\n-------------------------"

    def getcategory(self):
        return self.category


