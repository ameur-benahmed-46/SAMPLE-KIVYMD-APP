from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

Window.size = (360, 640)

# شحن ملفات التصميم
Builder.load_file("accueil.kv")
Builder.load_file("details.kv")

class AccueilScreen(Screen):
    def open_category(self, title, problems_list):
        # الوصول إلى شاشة التفاصيل وتحديث بياناتها قبل الانتقال
        details_screen = self.manager.get_screen('details_screen')
        details_screen.category_title = title
        details_screen.problems = problems_list
        # الانتقال إلى صفحة التفاصيل
        self.manager.current = 'details_screen'

class DetailsScreen(Screen):
    # متغيرات ممررة ديناميكياً لتحديث واجهة KV
    category_title = StringProperty("")
    problems = ListProperty([])

    def go_back(self):
        self.manager.current = 'accueil_screen'

class DiagApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        
        sm = ScreenManager()
        sm.add_widget(AccueilScreen(name='accueil_screen'))
        sm.add_widget(DetailsScreen(name='details_screen'))
        return sm

if __name__ == '__main__':
    DiagApp().run()