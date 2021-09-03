from itertools import cycle
from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self, selected_color):
        colors = ['red', 'yellow', 'green']
        colors_time = {'red': 7, 'yellow': 2, 'green': 5}
        colors_temp = ['red', 'yellow', 'green']
        for i, color in enumerate(colors):
            if color == selected_color.lower():
                colors[0] = colors_temp[i]
                colors[1] = colors_temp[i-1]
                colors[2] = colors_temp[i-2]
        print(colors)

        colors_priority = cycle(colors)
        for i in colors:
            for color, time in colors_time.items():
                if i == color:
                    t = time
            print(next(colors_priority))
            sleep(t)

        return ''



light = TrafficLight()

# sleep(10)

print(light.running('green'))
