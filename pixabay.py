import requests
import os
#put your api key here login in this url and get a one https://pixabay.com/api/docs/
API_KEY = ""

#pixabay url to search for images
URL = "https://pixabay.com/api/"

CATEGORY = "sports"
IMAGE_TYPE = "photos"

# get request safe search enabled
SEARCH_URL = URL + "?key=" + API_KEY + "&image_type=" + IMAGE_TYPE + "&category=" + CATEGORY + "&safesearch=true"
request = requests.get(url =  SEARCH_URL)
data  = request.json();

url_links = []
i=0
#getting images url from pixabay
for image in data['hits']:
    url_links.append(image["webformatURL"])
    print(image["webformatURL"])
    i+=1
    if(i > 49):
        break;

#downloade images to myProjects/pixabay_downloader/pictures
index = 0
for image in url_links:
    index+=1
    request = requests.get(image, allow_redirects=False)
    filename = "35"+str(index)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rel_path = r"pictures\\" + filename +  ".jpg"  
    abs_file_path = os.path.join(script_dir, rel_path)
    open(abs_file_path, 'wb').write(request.content)


#references 
#https://www.learnthinkimplement.com/post-pixabay-scraper/
#https://www.geeksforgeeks.org/python-os-path-dirname-method/
#https://stackoverflow.com/questions/3561691/python-syntaxerror-eol-while-scanning-string-literal
#https://pythonprogramming.net/python-3-os-module/




