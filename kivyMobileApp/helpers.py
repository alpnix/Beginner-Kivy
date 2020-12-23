username_helper = """
MDTextField: 
    hint_text: "Enter username"
    pos_hint: {"center_x":0.5,"center_y":0.5}
    helper_text: "enter your user name"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    helper_text_mode: "on_focus"
    size_hint_x:None
    width:300
"""
list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
            #OneLineListItem:
                #text: "Item 1"
            #OneLineListItem:
                #text: "Item 2"
"""
screen_helper = """
ScreenManager:
    id: screen_manager
    HomeScreen:
    PaintScreen:
    
<PaintScreen>:
    name: "paint"
    FloatLayout:
        orientation: "vertical"
        MDIconButton:    
            icon: "arrow-left-drop-circle"
            pos_hint: {"y":0.92}
            on_release: 
                root.manager.current = "home"
                root.manager.transition.direction = "right"
            
                  
<HomeScreen>:
    name: "home"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    elevation: 40
                    
                    MDToolbar:
                        title: "Welcome to NixApp"
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["atom",lambda x: app.empty()]]
                        elevation: 14
                        
                    
                    MDBottomNavigation:
                        
                        MDBottomNavigationItem:
                            name: 'screen1'
                            text: 'Home'
                            icon: 'home'
                            BoxLayout:
                            
                                orientation: "vertical"
                                padding: "13dp"
                                MDLabel: 
                                    #text: "Welcome, this app is created to make your lives easier and more organized"
                                    text: '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla egestas mi lorem, eget egestas augue elementum sed. Aenean id fermentum massa, vitae aliquet tortor. Quisque ac lectus nisi. Sed commodo, ipsum sit amet fermentum laoreet, justo nulla malesuada augue, eget accumsan urna nunc at tortor nunc lakoset.'''
                                    halign: "center"
                                    
                                
                                Image: 
                                    source: "Images\cog.png"
                                MDLabel: 
                                    text: "Still on construction"
                                    halign: "center"
                                    
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'paint'
                            icon: 'pencil-box'
                            BoxLayout:
                                MDLabel: 
                                    text: "This will be a painting screen"
                                    halign: "center"
                            
                    
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'Game'
                            icon: 'gamepad-variant'
                            BoxLayout:
                                MDLabel: 
                                    text: "Some kind of simple yet fun game will be inserted here"
                                    halign: "center"
                                
                        MDBottomNavigationItem:
                            name: 'screen 4'
                            text: 'Calc'
                            icon: 'calculator'
                            BoxLayout:
                                MDLabel: 
                                    text: "There will a screen capable of doing math operations"
                                    halign: "center"
                        
                    #MDBottomAppBar:
                    #    MDToolbar:
                    #        title: "Home"
                    #        left_action_items: [["home",lambda x: app.navigation_draw()]]
                    #        mode: "end"
                    #        type: "top"
                    #        icon: "all-inclusive"
                    #        on_action_button: app.navigation_draw()
                    #        elevation: 0
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                
                MDIconButton:    
                    icon: "arrow-left-drop-circle"
                    pos_hint: {"y":0.92}
                    on_release: nav_drawer.toggle_nav_drawer()
                    
                Image: 
                    source: "Images\hDpB7t.jpg"
                
                MDLabel:
                    text: "Alp Niksarlı"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                
                MDLabel:
                    text: "alp.niksarli@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: "+90 553 017 44 44"
                    font_style: "Caption"    
                    size_hint_y: None
                    height: self.texture_size[1]
                       
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "alpnix"
                            IconLeftWidget:
                                icon: "git"

                        OneLineIconListItem:
                            text: "alpniksarli"
                            IconLeftWidget:
                                icon: "instagram"
                        
                        OneLineIconListItem:
                            text: "Alp Niksarli"
                            IconLeftWidget:
                                icon: "facebook"
  
"""
screen_manager="""
ScreenManager:
    HomeScreen: 
    AboutScreen:

<HomeScreen>:
    name: "home"
    MDRectangleFlatButton:    
        text: "About"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.5}
        on_press: 
            root.manager.current = "about"
            root.manager.transition.direction = "left"


<AboutScreen>:
    BoxLayout:
        name: "about"
        MDRectangleFlatButton:    
            text: "Home"
            halign: "center"
            pos_hint: {"center_x":0.5,"center_y":0.5}
            on_press: 
                root.manager.current = "home"
                root.manager.transition.direction = "right"
    
"""
