from streaming_service import StreamingService
from movie import Movie

class StreamingGuide:
    def __init__(self):
        self._list_of_streaming_services = []

    def add_streaming_service(self, streaming_service_object):
        self._list_of_streaming_services.append(streaming_service_object)

    def delete_streaming_service(self,name_of_streaming_service):
        for name in self._list_of_streaming_services:
            if name.get_name() == name_of_streaming_service:
                self._list_of_streaming_services.remove(name)
     

    def where_to_watch_movie(self, movie_title):
        result = []
        for streaming_service in self._list_of_streaming_services:
            catalog = streaming_service.get_catalog()
            if movie_title in catalog:
                if len(result) == 0:
                    result.append(f"{movie_title} ({catalog[movie_title].get_year()})")
                    result.append(streaming_service.get_name())
                else:
                    result.append(streaming_service.get_name())
        return result if result else None
    
movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)
print(movie_1)
print(stream_serv_1.get_catalog())
stream_serv_1.delete_movie('Home Alone')
print(stream_serv_1.get_catalog())

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')

print(search_results)
