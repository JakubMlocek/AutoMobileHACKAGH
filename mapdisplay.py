import kivy
from kivy.app import App
from kivy.garden.mapview import MapView

kivy.require("1.11.1")


class MapApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=52.374, lon=4.900)
        return mapview


if __name__ == "__main__":
    MapApp().run()
