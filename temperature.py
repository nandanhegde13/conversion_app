class temp(object):

    def __init__(self, from_value, to_value, temp_value):
        self.from_value = from_value
        self.to_value = to_value
        self.temp_value = temp_value

    def c_to_c(self, temperature):
        return temperature

    def c_to_k(self, temperature):
        return temperature + 273.15

    def c_to_f(self, temperature):
        return (temperature * (9 / 5)) + 32

    def k_to_c(self, temperature):
        return temperature - 273.15

    def k_to_k(self, temperature):
        return temperature

    def k_to_f(self, temperature):
        return (temperature - 273.15) * 9 / 5 + 32

    def f_to_c(self, temperature):
        return (temperature - 32) * 5 / 9

    def f_to_k(self, temperature):
        return (temperature - 32) * 5 / 9 + 273.15

    def f_to_f(self, temperature):
        return temperature

    def get_unit(self):

        if self.from_value == "Celsius" and self.to_value == "Celsius":
            final_value = self.c_to_c(self.temp_value)

        elif self.from_value == "Celsius" and self.to_value == "Kelvin":
            final_value = self.c_to_k(self.temp_value)

        elif self.from_value == "Celsius" and self.to_value == "Fahrenheit":
            final_value = self.c_to_f(self.temp_value)

        elif self.from_value == "Kelvin" and self.to_value == "Kelvin":
            final_value = self.k_to_k(self.temp_value)

        elif self.from_value == "Kelvin" and self.to_value == "Celsius":
            final_value = self.k_to_c(self.temp_value)

        elif self.from_value == "Kelvin" and self.to_value == "Fahrenheit":
            final_value = self.k_to_f(self.temp_value)

        elif self.from_value == "Fahrenheit" and self.to_value == "Fahrenheit":
            final_value = self.f_to_f(self.temp_value)

        elif self.from_value == "Fahrenheit" and self.to_value == "Celsius":
            final_value = self.f_to_c(self.temp_value)

        elif self.from_value == "Fahrenheit" and self.to_value == "Kelvin":
            final_value = self.f_to_k(self.temp_value)

        return final_value
