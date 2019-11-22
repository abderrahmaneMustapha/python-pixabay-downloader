import os
import time
import glob

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class Interface(Screen):
    search = ObjectProperty(None)
    pass

kv = Builder.load_file("my.kv")

class MainApp(App):
    def build(self): 
        return Interface()

MainApp().run()

"""
start_time = time.time()

rel_path_text_list = [f for f in glob.glob(r"pictures\\*.txt")]

script_dir  = os.path.dirname(os.path.abspath(__file__))
for rel_path_text in rel_path_text_list:
    abs_file_path = os.path.join(script_dir, rel_path_text)
    file_tags = open(abs_file_path, 'r').read()
    if "man" in file_tags:
        print(abs_file_path)
        print('true')
print("Execution took : "+  str(time.time() - start_time) + " seconds")
"""

