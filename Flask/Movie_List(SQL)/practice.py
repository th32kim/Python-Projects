import requests
API_KEY="d8f3fcce2702229a56caeddc9b191896"
MOVIE_DETAIL_API = "https://api.themoviedb.org/3/movie/"
response = requests.get(url=f'{MOVIE_DETAIL_API}/{550}',params={'api_key':API_KEY,'language':'en-US'})
data = response.json()

print(data)