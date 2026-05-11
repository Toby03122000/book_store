class Film:
    
    def __init__(self, id, title, release_year, image_url):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.image_url = image_url
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Film({self.id}, {self.title}, {self.release_year}, {self.image_url})"