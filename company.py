from product import product
class company:
    def __init__(self, name, fixed_value, km_value, heavy_load_fixed_value = None, heavy_load_km_value = None, lightweight_load_threshold = None):
        self.__name = name
        self.__fixed_value = fixed_value
        self.__km_value = km_value
        self.__heavy_load_fixed_value = heavy_load_fixed_value
        self.__heavy_load_km_value = heavy_load_km_value
        self.__lightweight_load_threshold = lightweight_load_threshold
    
    def calculate_budget(self, product):
        if self.__heavy_load_fixed_value is not None and product.get_weight() > self.__lightweight_load_threshold:
            return self.__heavy_load_fixed_value + (product.get_weight() * product.get_distance() * self.__heavy_load_km_value)
        else:
            return self.__fixed_value + (product.get_weight() * product.get_distance() * self.__km_value)

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
    
    def set_heavy_load_fixed_value(self, heavy_load_fixed_value):
        self.__heavy_load_fixed_value = heavy_load_fixed_value

    def get_heavy_load_fixed_value(self):
        return self.__heavy_load_fixed_value
    
    def set_lightweight_load_threshold(self, lightweight_load_threshold):
        self.__lightweight_load_threshold = lightweight_load_threshold

    def get_lightweight_load_threshold(self):
        return self.__lightweight_load_threshold

    def set_heavy_load_km_value(self, heavy_load_km_value):
        self.__heavy_load_km_value = heavy_load_km_value

    def get_heavy_load_km_value(self):
        return self.__heavy_load_km_value