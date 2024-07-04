from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import TwoLineListItem, MDList
from kivymd.uix.datatables import MDDataTable

screen_helper = """
ScreenManager:
    id: screen_manager
    MenuScreen:
        name: 'menu'
        id: menu_screen
    ProfileScreen:
        name: 'profile'
        id: profile_screen
    SecondScreen:
    	name:'second'
    	id: second_screen
    InfoScreen:
    	name:'info'
    	id: info_screen 
    	

<MenuScreen>:
    MDBoxLayout:
    	pedding : 30
    	orientation:'vertical'
    	md_bg_color: (1,1,1,1)
    MDIcon:
    	icon:"bank"
    	pos_hint: {'center_y':0.4,'center_x':0.9}
    	user_font_size:89
    MDIcon:
    	icon:"cellphone"
    	pos_hint: {'center_y':0.9,'center_x':0.9}
    	user_font_size:89
    MDFloatingActionButton:
    	icon:"brightness-7"
    	pos_hint: {'center_y':0.9,'center_x':0.1}
    	on_press:root.manager.current='info'
    MDRectangleFlatIconButton:
        icon:'phone'
        text:'BANGLADESH'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current='profile'
    MDRectangleFlatIconButton
        text:'International'
        icon:'cellphone'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:root.manager.current='second'
     
    MDTopAppBar:
        title: 'SMH by Mejban'
        type: 'top'
    MDLabel:
        text: 'SMH'
        halign: 'center'
        font_style: 'H1'
        theme_text_color: 'Custom'
        text_color: (0, 1, 1, 1)
<ProfileScreen>:
    MDIcon:
    	icon:'id-card'
    	pos_hint: {'center_y':0.72}
    MDIcon:	
    	icon:'baby'
    	pos_hint: {'center_y':0.82}
    	MDIcon:	
    		icon:'phone'
    		pos_hint: {'center_x':0.4,'center_y':2.8}
    	
        MDIcon:
        	icon:'book'
        	pos_hint:{'center_y':-4}
        MDIcon:
        	icon:'cloud'
        	pos_hint:{'center_y':-6}
        MDIcon:
        	icon:'earth'
        	pos_hint:{'center_y':-8.2}
        MDIcon:
        	icon:'seed'
        	pos_hint:{'center_y':-10.5}
        MDIcon:
        	icon:'cow'
        	pos_hint:{'center_y':-12.5}
        MDIcon:
        	icon:'doctor'
        	pos_hint:{'center_y':-14.5}
    ScrollView:
        MDList:
            TwoLineListItem:
                text: '    National Emergency Number'
                secondary_text:'    999'
            TwoLineListItem:
            	text:'   Women And Chil help line:109'
            ThreeLineListItem:
            	text:'    National ID Card:105'
            TwoLineListItem:
            	text:'    Govt Law Service:16430'
            TwoLineListItem:
            	text:'    Weather Info: 10981'
            TwoLineListItem:
            	text:'    ANY INFORMATION'
            	secondary_text:'    333'
            TwoLineListItem:
            	text:'   Agriculture Call Service:16123'
            TwoLineListItem:
            	text:'   Farmers Call Center'
            	secondary_text:'     3331'
            TwoLineListItem:
            	text:'    Health Care:16263'
            MDRectangleFlatButton:
            	text:'BACK'
            	pos_hint:{'center_x':1,'center_y':1}
            	on_press:root.manager.current='menu'
            	
            	
<SecondScreen>:
    MDBoxLayout:
    	orientation: "vertical"

    MDTopAppBar:
        title: "Emergency Number"
        type: "top"
	MDIcon:
    	icon:'ambulance'
	MDIcon:
    	icon:'alarm-light'
    	icon_color: (0, 0, 1, 1)
    	pos_hint:{'center_x':0.1,'center_y':0.9}
	MDIcon:
    	icon:'fire-truck'
    	pos_hint:{'center_x':0.3,'center_y':0.9}
    MDIcon:
    	icon:'car'
    	pos_hint:{'center_x':0.5 ,'center_y':0.9}
    MDIcon:
    	icon:'phone'
    	pos_hint:{'center_x':0.7 ,'center_y':0.9}
    MDIcon:
    	icon:'ambulance'
    	pos_hint:{'center_x':0.9 ,'center_y':0.9}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.68}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.58}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.48}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.38}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.28}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.18}
    MDIcon
    	icon:'earth'
    	pos_hint:{'center_x':0.1,'center_y':0.11}
    ScrollView:
        MDList:
            TwoLineListItem:
                text: ''
            TwoLineListItem:
                text:''
            OneLineListItem:
            	text:'           EMERGENCY NUMBER'
            	theme_text_color:'Error'
            TwoLineListItem:
            	text:'           INDIA'
            	theme_text_color:'Custom'
            	text_color:(255/255,164/255,0/255,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:122'
                font_style:'Caption'
                
   
   
            TwoLineListItem:
            	text:'           USA'
            	theme_text_color:'Custom'
            	text_color:(0,0,1,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:911'
                font_style:'Caption'
                
            TwoLineListItem:
            	text:'           Singapore'
            	theme_text_color:'Custom'
            	text_color:(1,0,0,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:999'
                font_style:'Caption'
            
            TwoLineListItem:
            	text:'           Maldives'
            	theme_text_color:'Custom'
            	text_color:(0,1,0,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:119'
                font_style:'Caption'
            TwoLineListItem:
            	text:'           Nepal'
            	theme_text_color:'Custom'
            	text_color:(1,0,1,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:100'
                font_style:'Caption'
            TwoLineListItem:
            	text:'           MONGOLIA'
            	theme_text_color:'Custom'
            	text_color:(1,0,0,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:105'
                font_style:'Caption'
            TwoLineListItem:
            	text:'           Pakistan'
            	theme_text_color:'Custom'
            	text_color:(0,1,0,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:911'
                font_style:'Caption'
            TwoLineListItem:
            	text:'           Maxico'
            	theme_text_color:'Custom'
            	text_color:(1,0,1,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:911'
                font_style:'Caption'
                
            TwoLineListItem:
            	text:'           Albania'
            	theme_text_color:'Custom'
            	text_color:(255/255,164/255,0/255,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:129'
                font_style:'Caption' 
            TwoLineListItem:
            	text:'           Armenia'
            	theme_text_color:'Custom'
            	text_color:(255/255,164/255,0/255,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:122'
                font_style:'Caption'
            TwoLineListItem:
            	text:'           Croatia'
            	theme_text_color:'Custom'
            	text_color:(255/255,164/255,0/255,1)
                halign:'center'
            	font_style:'Caption'
               
                secondary_text:'        NUMBER:122'
                font_style:'Caption'
	MDRoundFlatIconButton
    	icon:'arrow-left'
    	text:'back'
    	pos_hint:{'center_x':0.2,'center_y':0.97}
        on_press:root.manager.current='menu'       
                      
<InfoScreen>:
    MDCard:
        size_hint: None, None
        size: dp(280), dp(340)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
    MDRectangleFlatButton:
    	text:'Email:mejbankadir@gmail.com'
    	font_size:37
    	pos_hint:{'center_x':0.5,'center_y':0.53}
    MDFillRoundFlatIconButton:
    	text:'SMH'
    	icon:'android'
    	pos_hint:{'center_x':0.5,'center_y':0.6}
    
    MDRectangleFlatButton:
    	text:'Number:+8801710905705'
    	font_size:37
    	pos_hint:{'center_x':0.5,'center_y':0.45}
    MDRaisedButton:
    	md_bg_color: 1, 0, 1, 1
    	text:'Team Members:'
    	pos_hint:{'center_x':0.5,'center_y':0.39}
    MDRaisedButton:
    	md_bg_color: 1, 0, 1, 1
    	text:'TEAM Ahnaf Bin Zaman '
    	pos_hint:{'center_x':0.5,'center_y':0.35}
    MDRaisedButton:
    	md_bg_color: 1, 0, 1, 1
    	text:'AL-SHAHI '
    	pos_hint:{'center_x':0.5,'center_y':0.32}
    	 
    MDFillRoundFlatIconButton:
        icon:'arrow-left'
        
    	text:'back'
    
        on_press:root.manager.current='menu'         	 
    	
           
"""
    

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class InfoScreen(Screen):
	pass

class SmhApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
       
        return screen

SmhApp().run()