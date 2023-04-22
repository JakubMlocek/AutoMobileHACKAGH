import json
import folium
import webbrowser
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from json.decoder import JSONDecodeError
from kivy.garden.mapview import MapView



class CarInfoApp(App):    
    def build(self):
        # load data from json file
        try:
            with open("car_info.json", "r") as f:
                data = json.load(f)
        except JSONDecodeError:
            data = {
                "fuel": "",
                "location": "",
                "oil": "",
                "coolant": ""
            }

        # create layout
        layout = GridLayout(cols=1, spacing=1, padding=20)

        title_label = Label(text="AutoMobile")
        layout.add_widget(title_label)

        image = Image(source='car.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(image)


        # create labels and inputs for car info data
        fuel_label = Label(text="Poziom paliwa:", valign='center')
        fuel_input = TextInput(text=str(data["fuel"]), size_hint_y=None, height=50)
        location_label = Label(text="Aktualna lokalizacja:", valign='center')
        location_input = TextInput(text=str(data["location"]), size_hint_y=None, height=50)
        oil_label = Label(text="Stan oleju:", valign='center')
        oil_input = TextInput(text=str(data["oil"]), size_hint_y=None, height=50)
        coolant_label = Label(text="Stan płynu chłodniczego:", valign='center')
        coolant_input = TextInput(text=str(data["coolant"]), size_hint_y=None, height=50)

        # add widgets to layout
        layout.add_widget(fuel_label)
        layout.add_widget(fuel_input)
        layout.add_widget(location_label)
        layout.add_widget(location_input)
        layout.add_widget(oil_label)
        layout.add_widget(oil_input)
        layout.add_widget(coolant_label)
        layout.add_widget(coolant_input)

        # create save button
        save_button = Button(text='Zapisz')
        save_button.bind(on_press=lambda x: self.save_data(fuel_input.text, location_input.text,
                                                          oil_input.text, coolant_input.text))

        # add save button to layout
        layout.add_widget(Label())  # empty label for spacing
        layout.add_widget(save_button)

        mapview = MapView(zoom=11, lat=52.374, lon=4.900)
        layout.add_widget(mapview, rows=4)


        return layout

    def save_data(self, fuel, location, oil, coolant):
        # create dictionary with car info data
        data = {
            "fuel": fuel,
            "location": location,
            "oil": oil,
            "coolant": coolant
        }

        # save data to json file
        with open("car_info.json", "w") as f:
            json.dump(data, f)


if __name__ == '__main__':
    CarInfoApp().run()
