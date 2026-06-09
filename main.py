from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Привет, Android!', font_size='24sp')
        layout.add_widget(self.label)
        btn = Button(text='Нажми меня')
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(btn)
        return layout
    
    def on_button_press(self, instance):
        self.label.text = 'Кнопка нажата!'

if __name__ == '__main__':
    MainApp().run()
