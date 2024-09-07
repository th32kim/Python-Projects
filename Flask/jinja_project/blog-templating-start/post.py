import requests

class Post:
    def __init__(self):
        self.blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
        self.blog_data = requests.get(self.blog_url)
        self.data = self.blog_data.json()
    
    def return_content(self, order):
        self.id = order
        for d in self.data:
            if d['id'] == self.id:
                self.body = d['body']
                self.title = d['title']
                return {'body':self.body, 'title': self.title}