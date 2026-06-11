from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class AccueilContent(BoxLayout):
    pass

class DiagnosticContent(BoxLayout):
    pass

# قمنا بتحديث هذه الفئة لإضافة دالة التصفية
class PannesContent(BoxLayout):
    def filtrer_panne(self, nom_panne):
        # مسح القائمة أولاً
        self.ids.list_container.clear_widgets()
        
        # تصفية الحالات الأربعة بالكامل
        if nom_panne == "injection":
            self.ids.list_container.add_widget(self.ids.item_injection)
        elif nom_panne == "turbo":
            self.ids.list_container.add_widget(self.ids.item_turbo)
        elif nom_panne == "fap":
            self.ids.list_container.add_widget(self.ids.item_fap)
        elif nom_panne == "moteur":
            self.ids.list_container.add_widget(self.ids.item_moteur) # الحالة الرابعة المضافة
            
    def afficher_tout(self):
        # إظهار الحالات الأربعة معاً
        self.ids.list_container.clear_widgets()
        self.ids.list_container.add_widget(self.ids.item_injection)
        self.ids.list_container.add_widget(self.ids.item_turbo)
        self.ids.list_container.add_widget(self.ids.item_fap)
        self.ids.list_container.add_widget(self.ids.item_moteur) # الحالة الرابعة المضافة
class GuideContent(BoxLayout):
    pass

class InfosContent(BoxLayout):
    pass

class MainScreen(Screen):
    pass

class DieselCareApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        
        Builder.load_file("accueil_screen.kv")
        Builder.load_file("diagnostic_screen.kv")
        Builder.load_file("pannes_screen.kv")
        Builder.load_file("guide_screen.kv")
        Builder.load_file("infos_screen.kv")
        
        return Builder.load_string('''
MainScreen:
    MDBottomNavigation:
        id: bottom_nav
        panel_color: 0.10, 0.10, 0.10, 1
        text_color_active: 0.12, 0.40, 0.70, 1 # تغيير لون الأيقونة النشطة للأزرق ليتناسق مع الهوية
        text_color_normal: 0.6, 0.6, 0.6, 1

        # 1. تبويب الواجهة الرئيسية
        MDBottomNavigationItem:
            name: "home"
            icon: "home"
            text: "Accueil"
            AccueilContent:

        # 2. تبويب موسوعة الأعطال (مع خاصية الإظهار الكامل عند الضغط)
        MDBottomNavigationItem:
            name: "pannes"
            icon: "car-cog"
            text: "Pannes"
            on_tab_press: pannes_ui.afficher_tout()
            PannesContent:
                id: pannes_ui

        # 3. تبويب مساعد التشخيص الذكي
        MDBottomNavigationItem:
            name: "diagnostic"
            icon: "comment-question"
            text: "Diagnostic"
            DiagnosticContent:

        # 4. تبويب دليل الصيانة الوقائية
        MDBottomNavigationItem:
            name: "guide"
            icon: "book-open-page-variant"
            text: "Guide"
            GuideContent:

        # 5. تبويب حول التطبيق والمعلومات
        MDBottomNavigationItem:
            name: "infos"
            icon: "information"
            text: "Infos"
            InfosContent:
''')

if __name__ == "__main__":
    DieselCareApp().run()