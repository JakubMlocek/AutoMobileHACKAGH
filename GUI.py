import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from json.decoder import JSONDecodeError
from kivy.garden.mapview import MapView
from kivy.uix.image import Image



class CarInfoApp(App):    
    def build(self):
        # load data from json file
        try:
            with open("resources/car_info.json", "r") as f:
                data = json.load(f)
        except JSONDecodeError:
            data = {
                "fuel": "",
                "location": "",
                "oil": "",
                "coolant": ""
            }

        # create layout
        main_grid = GridLayout(cols=1, spacing=10, padding=40)
        label_grid = GridLayout(cols=2, size_hint=(1, 10))

        # create image
        image = Image(source='resources/car.png', size_hint=(4, 12))
        main_grid.add_widget(image)

        # create labels and inputs for car info data
        fuel_label = Label(text="Poziom paliwa:")
        fuel_input = TextInput(text=str(data["fuel"]))
        location_label = Label(text="Aktualna lokalizacja:")
        location_input = TextInput(text=str(data["location"]))
        oil_label = Label(text="Stan oleju:")
        oil_input = TextInput(text=str(data["oil"]))
        coolant_label = Label(text="Stan płynu chłodniczego:")
        coolant_input = TextInput(text=str(data["coolant"]))

        # add widgets to layout
        label_grid.add_widget(fuel_label)
        label_grid.add_widget(fuel_input)
        label_grid.add_widget(location_label)
        label_grid.add_widget(location_input)
        label_grid.add_widget(oil_label)
        label_grid.add_widget(oil_input)
        label_grid.add_widget(coolant_label)
        label_grid.add_widget(coolant_input)

        main_grid.add_widget(label_grid)

        mapview = MapView(zoom=11, lat=50.6394, lon=3.057, size_hint=(4, 15))
        main_grid.add_widget(mapview)

        self.create_button_grid(main_grid)

        return main_grid

    def save_data(self, fuel, location, oil, coolant):
        # create dictionary with car info data
        data = {
            "fuel": fuel,
            "location": location,
            "oil": oil,
            "coolant": coolant
        }

        # save data to json file
        with open("resources/car_info.json", "w") as f:
            json.dump(data, f)

    def create_button_grid(self, main_grid):
        button_grid = GridLayout(cols=3, spacing=10, padding=40, size_hint=(1, 3))
        button1 = Button(text='Przycisk', size_hint=(1, 10))
        button2 = Button(text='Button2')
        button3 = Button(text='Button3')
        button_grid.add_widget(button1)
        button_grid.add_widget(button2)
        button_grid.add_widget(button3)
        main_grid.add_widget(button_grid)


