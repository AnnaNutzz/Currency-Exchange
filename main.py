from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Pastel background color
Window.clearcolor = (0.92, 0.95, 1, 1)  # soft pastel blue

# Conversion rate
INR_TO_VND = 299  # 1 INR = 299 VND
VND_TO_INR = 1 / INR_TO_VND


class CurrencyConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [30, 50]
        self.spacing = 25

        # Title
        self.label = Label(
            text="VND -> INR Converter",
            font_size="32sp",
            bold=True,
            color=(0.2, 0.3, 0.6, 1),  # navy-ish
            size_hint=(1, 0.2)
        )
        self.add_widget(self.label)

        # VND input
        self.vnd_input = TextInput(
            hint_text="Enter amount in VND",
            multiline=False,
            font_size="20sp",
            size_hint=(1, 0.12),
            halign="center",
            padding=[10, 20],  # more padding inside
            background_normal="",  # remove default texture
            background_color=(1, 1, 1, 1),  # clean white box
            foreground_color=(0.2, 0.2, 0.2, 1),  # dark grey text
            cursor_color=(0.3, 0.5, 0.7, 1)  # pastel blue cursor
        )
        self.vnd_input.bind(size=self._update_text_padding)
        self.add_widget(self.vnd_input)

        # Convert button
        self.convert_button = Button(
            text="Convert",
            font_size="22sp",
            background_normal="",  # remove default button texture
            background_color=(0.6, 0.85, 0.7, 1),  # pastel green
            color=(0.1, 0.2, 0.1, 1),  # dark green text
            size_hint=(1, 0.12)
        )
        self.convert_button.bind(on_press=self.convert_currency)
        self.add_widget(self.convert_button)

        # Result label
        self.result = Label(
            text="Result will appear here",
            font_size="24sp",
            color=(0.7, 0.2, 0.4, 1),  # pastel pink text
            size_hint=(1, 0.2)
        )
        self.add_widget(self.result)

        # Info label (conversion rate)
        self.info = Label(
            text=f"1 INR ≈ {INR_TO_VND} VND",
            font_size="20sp",
            color=(0.2, 0.4, 0.6, 1),  # bluish-grey
            size_hint=(1, 0.1)
        )
        self.add_widget(self.info)

    def _update_text_padding(self, instance, value):
        """Keep text horizontally centered in TextInput."""
        instance.text_size = (instance.width, None)

    def convert_currency(self, instance):
        try:
            vnd_amount = float(self.vnd_input.text.replace(",", ""))
            inr_amount = vnd_amount * VND_TO_INR
            self.result.text = f"{vnd_amount:,.0f} VND ≈ {inr_amount:.2f} INR"
        except ValueError:
            self.result.text = "Please enter a valid number!"


class ConverterApp(App):
    def build(self):
        return CurrencyConverter()


if __name__ == "__main__":
    ConverterApp().run()
