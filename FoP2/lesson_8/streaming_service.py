from movie import Movie    

class StreamingService:
    def __init__(self,name):
        self._name = name
        self._catalog =  {}# {title: movie_object}

    def get_name(self):
        return self._name
    
    def get_catalog(self):
        return self._catalog
    
    def add_movie(self, movie_object):
        self._catalog[movie_object.get_title()] = movie_object
        
    def delete_movie(self, movie_title):
        if movie_title in self._catalog:
            del self._catalog[movie_title]