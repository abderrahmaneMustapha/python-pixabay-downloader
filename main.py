import os
import time
import glob

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.image import Image

class Interface(Screen):
    search = ObjectProperty(None)
    grid_layout = GridLayout(cols=4,row_force_default=True, row_default_height=40)
    
    def replace(self,string):
        return string.replace(".txt", ".jpg")
    def addtogrid(self,img):
        self.grid_layout.add_widget(Image(source=img))
        print(self.grid_layout)

    def find(self):
        start_time = time.time()
        #get the text from search text input
        search_text = self.search.text

        #find all txt documents in pictures path
        rel_path_text_list = [f for f in glob.glob(r"pictures\\*.txt")]
        
        #get current working directory
        script_dir  = os.path.dirname(os.path.abspath(__file__))

        for rel_path_text in rel_path_text_list:
            #get full path of txt document
            abs_file_path = os.path.join(script_dir, rel_path_text)
           
            #get tags from txt file
            file_tags = open(abs_file_path, 'r').read()
            #search in text file
            if search_text in file_tags:
                abs_image_file_path = self.replace(abs_file_path)
                self.addtogrid( abs_image_file_path)
                print(abs_image_file_path)                
                print('true')
        
        root = self.ids.floatlayout.add_widget(self.grid_layout)
        print(root)
        print("Execution took : "+  str(time.time() - start_time) + " seconds")
  
    

kv = Builder.load_file("my.kv")

class MainApp(App):
    def build(self): 
        return Interface()

MainApp().run()


