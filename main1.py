class Display:
    def __init__(self, resolution):
        self.resolution = resolution
        self.brightness = 50

    def show_resolution(self):
        return f"Display Resolution: {self.resolution}"

    def change_resolution(self, new_resolution):
        self.resolution = new_resolution
        return f"Changed Display Resolution to: {self.resolution}"

    def adjust_brightness(self, value):
        self.brightness = value
        return f"Changed Brightness to: {self.brightness}"


class Processor:
    def __init__(self, speed):
        self.speed = speed
        self.temperature = 40

    def show_speed(self):
        return f"Processor Speed: {self.speed} GHz"

    def check_temperature(self):
        return f"Current Temperature: {self.temperature}°C"

    def overclock(self):
        self.speed += 0.5
        self.temperature += 5
        return f"Overclocked! New Speed: {self.speed} GHz, New Temperature: {self.temperature}°C"

class Computer(Processor, Display):
    def __init__(self, resolution, speed, brand):
        Display.__init__(self, resolution)
        Processor.__init__(self, speed)
        self.brand = brand

    def show_info(self):
        return f"Brand: {self.brand}, {self.show_speed()}, {self.show_resolution()}, {self.check_temperature()}, Brightness: {self.brightness}"
my_computer = Computer(1080, 3.5, "Lenovo")
print(my_computer)
print(my_computer.show_info())
print(my_computer.change_resolution(1440))
print(my_computer.adjust_brightness(70))
print(my_computer.overclock())
print(my_computer.check_temperature())