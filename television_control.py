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
    def volume_up(self):
        self.volume = (self.volume % 7) + 1
        
    # Volume down control
    def volume_down(self):
        self.volume = (self.volume - 1) % 7 + 1

# Create object for TV1
television_1 = TV(channel = 30, volume = 3)
# Print channel and volume of TV1
print("\n✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾ ﾟ ｡⋆✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾ ﾟ ｡⋆✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾\n")
print("\033[93;1m\nTelevision 1\n\033[0m")
print("\033[38;5;93m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
print("\033[38;5;207m║┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓║\033[0m")
print(f"\033[38;5;218m     tv1's channel is{television_1.get_channel():^5} and volume level is{television_1.get_volume():^5}   \033[0m")
print("\033[38;5;207m║┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛║")
print("\033[38;5;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")

# Create object for TV2
television_2 = TV(channel = 3, volume = 2)
# Print channel and volume of TV2
print("\033[93;1m\nTelevision 2\n\033[0m")
print("\033[38;5;117m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
print("\033[38;5;226m║┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓║\033[0m")
print(f"\033[38;5;156m     tv2's channel is{television_2.get_channel():^5} and volume level is{television_2.get_volume():^5}   \033[0m")
print("\033[38;5;226m║┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛║")
print("\033[38;5;117m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
print("\n✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾ ﾟ ｡⋆✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾ ﾟ ｡⋆✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾\n")

