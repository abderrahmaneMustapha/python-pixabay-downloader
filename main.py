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
    search = ObjectProperty(None)
    first = True
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
    
        images_number = Label(text=str(count), pos_hint={'right': 1.14,'top': 0.65} )
        excution_time = Label(text=str(time),pos_hint= {'right': 0.76,'top': 0.65})
    
        float_layout.add_widget(images_number)
        float_layout.add_widget(excution_time)
    
    def create_info_file(self,count,ex_time):
        read_f = open('info.txt', 'r')       
        append_f = open('info.txt', 'a')
        string = ""
        if read_f.read():
            string = str(ex_time)+ " \t \t \t \t "+ str(count) +" \t \t \t \t \t \t "+str(date.today())+"\n"
            append_f.write(string)
        else:
            string  = "execution time \t \t \t \t number of images \t \t \t \t \t \t date \n"
            string += str(ex_time)+ " \t \t \t \t "+ str(count) +" \t \t \t \t \t \t "+str(date.today())+"\n"
            
            append_f.write(string)

            


                  
            
            
            
           
                   
           
           
    def find(self): 
        self.ids.gridlayout.clear_widgets()   
        start_time = time.time()
        #get the text from search text input
        search_text = self.search.text

        #find all txt documents in pictures path
        rel_path_text_list = [f for f in glob.glob(r"pictures\\*.txt")]
        
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
                self.addtogrid( abs_image_file_path)
                print(abs_image_file_path)
                count+=1
        self.no_result(count)
        self.add_labels(count,str(time.time() - start_time))                          
        self.create_info_file(count,str(time.time() - start_time))
  
    

kv = Builder.load_file("my.kv")

class MainApp(App):
    def build(self): 
        return Interface()

MainApp().run()


