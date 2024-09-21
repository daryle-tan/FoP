class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def get_title(self):
        return self._title
    
    def get_genre(self):
        return self._genre
    
    def get_director(self):
        return self._director
    
    def get_year(self):
        return self._year