from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Работа не волк, никто не волк, только волк волк', font_size='24sp')
        layout.add_widget(self.label)
        btn = Button(text='Кнопка не волк')
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(btn)
        return layout
    
    def on_button_press(self, instance):
        self.label.text = 'Волк не кнопка'

if __name__ == '__main__':
    MainApp().run()
