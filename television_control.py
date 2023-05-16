# Start 

# Create a class named TV
class TV:
    # Constructor
    def __init__(self, channel = 1, volume = 1, on = False):
        self.channel = channel
        self.volume = volume
        self.on = on

    # On and Off control
    # on control
    def turn_on(self):
        self.on = True
    # off control
    def turn_off(self):
        self.on = False

    # Get current channel 
    def get_channel(self):
        return self.channel

    # Channel control
    def set_channel(self, number):
        try:
          if (number > 120 or number < 1):
              raise ValueError
          self.channel = number
        except ValueError:
            print("Invalid channel.")

    # Channel up control
    def channel_up(self):
        self.channel = (self.channel) % 120 + 1
    # Channel down control
    def channel_down(self):
        self.channel = (self.channel - 2) % 120 + 1

    # Get current volume
    def get_volume(self):
        return self.volume

    # Volume control
    def set_volume(self, degree):
        try:
            if (degree > 7 or degree < 1):
                raise ValueError
            self.volume = degree
        except:
            print("Invalid volume.")

    # Volume up control

    # Volume down control

# Create object for TV1
# Print channel and volume of TV1

# Create object for TV2
# Print channel and volume of TV2
    


