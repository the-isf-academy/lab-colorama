from django.db import models
from django.urls import reverse
from colors_app.validators import color_channel_validator

class Color(models.Model):
    name = models.CharField(max_length=50)
    red = models.IntegerField(validators=[color_channel_validator])
    green = models.IntegerField(validators=[color_channel_validator])
    blue = models.IntegerField(validators=[color_channel_validator])

    def hex_code(self):
        """Returns a hex representation of the color like #00ff00 (green) suitable for CSS.
        """
        return '#' + ''.join([self.int2hex(self.red), self.int2hex(self.green), self.int2hex(self.blue)])

    def int2hex(self, int_value):
        "Converts an integer value like 15 to a two-digit hex string like 0b"
        return hex(int_value)[2:].zfill(2)

    def inverted(self, name=None):
        """Returns a new color which is the 'opposite' of this one. 
        A color is defined by red, green, and blue values, each ranging from
        0-255. If a color's red, green, and blue values are (x, y, z), the 
        opposite color's values are (255-x, 255-y, 255-z). For example, white is 
        (255, 255, 255), so its opposite, black, is (0, 0, 0). 
        """
        if name is None:
            name = self.name + ' inverted'
        return Color(name=name, red=255-self.red, green=255-self.green, blue=255-self.blue)

    def tinted(self, ratio=0.3, name=None):
        """Returns a new color, a tinted (more white) version of this one.
        As with inverted, the math is pretty simple--for each channel, just
        move its value closer to 255 (white).
        """
        if name is None:
            name = self.name + " tinted {}%".format(ratio * 100)
        return Color(name=name, 
            red=255-self.red, green=255-self.green, blue=255-self.blue)
