class company:
    def __init__(self, name, fixed_value, km_value):
        self.__km_value = name
        self.__fixed_value = fixed_value
        self.__km_value = km_value
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_fixed_value(self, fixed_value):
        self.__fixed_value = fixed_value

    def get_fixed_value(self):
        return self.__fixed_value

    def set_km_value(self, km_value):
        self.__km_value = km_value

    def get_km_value(self):
        return self.__km_value