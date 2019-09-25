class Pitch:
    '''
    Pitch class to define pitch objects
    '''
    def __init__(self, id,name,category,upvote,downvote,publishedAt):
        self.id = id
        self.name = name
        self.category = category
        self.upvote = upvote
        self.downvote = downvote
        self.publishedAt = publishedAt
        