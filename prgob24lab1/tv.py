class TV:
    def __init__(self, tv_name, max_channel, current_channel, max_volume, current_volume):

        self.tv_name = tv_name
        self.max_channel = max_channel
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.current_volume = current_volume

    def volume_up(self):
        if self.current_volume < self.max_volume:
            self.current_volume += 1
        else:
            print("Volume is already at maximum")

    def volume_down(self):
        if self.current_volume > 0:
            self.current_volume -= 1
        else:
            print("Volume is already at minimum")

    def change_channel(self, new_channel):
        if 1 <= new_channel <= self.max_channel:
            self.current_channel = new_channel
        else:
            print(f"Invalid channel. Channel must be between 1 and {self.max_channel}.")


    
    def __str__(self) -> str:
        return f"TV name: {self.tv_name}\nVolume: {self.current_volume}/{self.max_volume}\nChannel: {self.current_channel}/{self.max_channel}"
    
    def str_for_file(self) -> str:
        return f"{self.tv_name},{self.max_channel},{self.current_channel},{self.max_volume},{self.current_volume}"
        
    