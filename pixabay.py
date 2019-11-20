import requests
#put your api key here login in this url and get a one https://pixabay.com/api/docs/
API_KEY = "8553111-12bcee0ed6a0d9dc010b69e27"

#pixabay url to search for images
URL = "https://pixabay.com/api/"

CATEGORY = "sports"
IMAGE_TYPE = "photos"

# get request safe search enabled
SEARCH_URL = URL + "?key=" + API_KEY + "&image_type=" + IMAGE_TYPE + "&category=" + CATEGORY + "&safesearch=true"
request = requests.get(url =  SEARCH_URL)
data  = request.json();

print(data)


