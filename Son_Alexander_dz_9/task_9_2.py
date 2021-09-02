class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_weight(self):
        weight = self.__width * self.__length * 25 * 5
        # print(f'{weight} т')
        return weight


city_road = Road(250, 20)
print(city_road.get_weight())
