import requests
import os
#put your api key here login in this url and get a one https://pixabay.com/api/docs/
API_KEY = "8553111-12bcee0ed6a0d9dc010b69e27"

#pixabay url to search for images
URL = "https://pixabay.com/api/"

CATEGORY = "sports"
IMAGE_TYPE = "photos"
QUERY = "out"

# get request safe search enabled
SEARCH_URL = URL + "?key=" + API_KEY +"&q="+ QUERY + "&image_type=" + IMAGE_TYPE + "&category=" + CATEGORY + "&safesearch=true" +  "&order=latest"
request = requests.get(url =  SEARCH_URL)
data  = request.json();

url_links = []
i=0
#getting images url from pixabay
for image in data['hits']:
    url_links.append(tuple((image["webformatURL"],image['tags'])))
    print(image["webformatURL"])
    i+=1
    if(i > 2):
        break

#downloade images to myProjects/pixabay_downloader/pictures
index = 0
for image, tags in url_links:
    index+=1
    print(tags)
    request = requests.get(image, allow_redirects=False)
    filename = "35"+str(index)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rel_path_image = r"pictures\\" + filename +  ".jpg"  
    rel_path_text =  r"pictures\\" + filename +  ".txt"   
    abs_file_path_image = os.path.join(script_dir, rel_path_image)
    abs_file_path_text = os.path.join(script_dir, rel_path_text)
    open(abs_file_path_image, 'wb').write(request.content)
    open(abs_file_path_text, 'w+').write(tags)


#references 
#https://www.learnthinkimplement.com/post-pixabay-scraper/
#https://www.geeksforgeeks.org/python-os-path-dirname-method/
#https://stackoverflow.com/questions/3561691/python-syntaxerror-eol-while-scanning-string-literal
#https://pythonprogramming.net/python-3-os-module/




