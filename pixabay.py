#excute:  python pixaby.py <query> <category> <number_of_pics <= 200 > <tp_num>
#example: python pixabay.py ball sports 50 35


#references 
#https://www.learnthinkimplement.com/post-pixabay-scraper/
#https://www.geeksforgeeks.org/python-os-path-dirname-method/
#https://pythonprogramming.net/python-3-os-module/
#https://pixabay.com/api/docs/
#https://www.tutorialspoint.com/python/python_command_line_arguments.htm


import requests
import os
import time
import sys

def main(argv):
    # initialize the start time  
    start_time = time.time()
  
    #put your api key here login in this url and get a one https://pixabay.com/api/docs/
    API_KEY = ""

    #pixabay url to search for images
    URL = "https://pixabay.com/api/"

    CATEGORY = str(argv[1])
    IMAGE_TYPE = "photos"
    QUERY = str(argv[0])
    tp_number = str(argv[3])
    #maximum pics  200
    pics_number = int(argv[2])
    if pics_number > 200:
        sys.exit('photos number must be <= 200')
       
    # get request safe search enabled
    SEARCH_URL = URL + "?key=" + API_KEY +"&q="+ QUERY + "&image_type=" + IMAGE_TYPE + "&category=" + CATEGORY + "&safesearch=true" +  "&order=popular" + "&per_page="+str(pics_number)
    request = requests.get(url =  SEARCH_URL)
    data  = request.json()

    url_links = []
    i=0
    print('query :'+ QUERY)
    print('category :'+ CATEGORY)  
    print('number of pictures :'+ str(pics_number) )
    print('tp number :'+ str(tp_number))
    #getting images url from pixabay
    for image in data['hits']:
        print('getting image url........')
        url_links.append(tuple((image["webformatURL"],image['tags'])))
        print(image["webformatURL"])
        i+=1
        if(i > pics_number - 1):
            break

    #downloade images and write tags in txt files to myProjects/pixabay_downloader/pictures
    index = 0
    for image, tags in url_links:
        index+=1
        request = requests.get(image, allow_redirects=False)
        filename = tp_number+str(index)
        script_dir = os.path.dirname(os.path.abspath(__file__))

        print("saving picture: "+filename+".jpg")
        rel_path_image = r"pictures\\" + filename +  ".jpg" 

        print("put tags in "+filename+".txt") 
        print(tags+ "\n")   
        rel_path_text =  r"pictures\\" + filename +  ".txt"   

        abs_file_path_image = os.path.join(script_dir, rel_path_image)
        abs_file_path_text = os.path.join(script_dir, rel_path_text)
        open(abs_file_path_image, 'wb').write(request.content)
        open(abs_file_path_text, 'w+').write(tags)

    #calculate and display execution time
    print("Execution took : "+  str(time.time() - start_time) + " seconds")

if __name__ == "__main__":
   main(sys.argv[1:])


