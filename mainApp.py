#python
import os
import time
import glob
from datetime import date

#kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput




class Interface(Screen):
    def __init__(self):
        super().__init__()
        self.count_images()
        

    search = ObjectProperty(None)
    def count_images(self):
        total =len(self.findText())
        float_layout = self.ids.label_widget
        images_number = Label(text=str(total),pos_hint= {'right': 1.3,'top': 0.65})
        float_layout.add_widget(images_number)


    def replace(self,string):
        return string.replace(".txt", ".jpg")
    def addtogrid(self,img):
        root = self.ids.gridlayout
        root.add_widget(Image(source=img))
    def no_result(self,count):
        if count == 0:
            self.ids.gridlayout.add_widget(Label(text = 'no result '))
    def add_labels(self,count,time):
        float_layout = self.ids.label_widget
        float_layout.clear_widgets()
    
        images_number = Label(text=str(count), pos_hint={'right':0.94,'top': 0.65} )
        excution_time = Label(text=str(format(float(time), '.5f')),pos_hint= {'right': 0.685,'top': 0.65})
        self.count_images()
    
        float_layout.add_widget(images_number)
        float_layout.add_widget(excution_time)
    
    def create_info_file(self,count,ex_time,query):
        read_f = open('info.txt', 'r')       
        append_f = open('info.txt', 'a')
        string = ""
        if read_f.read():
            string = "%10s%20s%20s%30s\n"%(query,str(format(float(ex_time), '.5f')),str(count),str(date.today()))
            append_f.write(string)
        else:
            string  ="%12s%20s%25s%20s\n"%("query",str("execution time"),str("number of images"),str("date"))
            string += "%10s%20s%20s%30s\n"%(query,str(format(float(ex_time), '.5f')),str(count),str(date.today()))
            
            append_f.write(string)         
    def findText(self):
        return [f for f in glob.glob(r"pictures\\*.txt")]          
    def find(self): 
        self.ids.gridlayout.clear_widgets()   
        start_time = time.time()
        #get the text from search text input
        search_text = self.search.text

        #find all txt documents in pictures path
        rel_path_text_list =self.findText()
       
        
        #get current working directory
        script_dir  = os.path.dirname(os.path.abspath(__file__))
        count = 0
        for rel_path_text in rel_path_text_list:
            #get full path of txt document
            abs_file_path = os.path.join(script_dir, rel_path_text)
           
            #get tags from txt file
            file_tags = open(abs_file_path, 'r').read()
            #search in text file
            if search_text in file_tags:
                abs_image_file_path = self.replace(abs_file_path)
                self.addtogrid(abs_image_file_path)
                print(abs_image_file_path)
                count+=1
                if count == 10 :
                    break;
        self.no_result(count)
        self.add_labels(count,str(time.time() - start_time))                          
        self.create_info_file(count,str(time.time() - start_time),search_text)
  
    

kv = Builder.load_file("my.kv")

class MainApp(App):
    def build(self): 
        return Interface()

MainApp().run()


