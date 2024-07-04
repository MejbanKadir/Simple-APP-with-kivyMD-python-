

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.icon import MDIcon


#Main App
class MainApp(MDApp):
	def build(self):
		text= MDLabel(text='Hello' )
		icon = MDIcon(icon="language-python")
		
		return text,icon

#Run/Test
MainApp().run()