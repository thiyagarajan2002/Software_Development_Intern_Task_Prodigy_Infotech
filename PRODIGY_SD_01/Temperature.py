class Temperature:
    def __init__(self,temperature,unit):
        self.temperature=temperature
        self.unit=unit
        self.result={}
        if self.unit=="Degree Celsius":
            self.result["unit 1"]="Fahrenheit"
            self.result["unit 2"]="Kelvin"
            self.result["unit 1 result"]=self.degree_celsius_to_fahrenheit()
            self.result["unit 2 result"]=self.degree_celsius_to_kelvin()
        elif self.unit=="Fahrenheit":
            self.result["unit 1"]="Kelvin"
            self.result["unit 2"]="Degree Celsius"
            self.result["unit 1 result"]=self.fahrenheit_to_kelvin()
            self.result["unit 2 result"]=self.fahrenheit_to_degree_celsius()
        elif self.unit=="Kelvin":
            self.result["unit 1"]="Degree Celsius"
            self.result["unit 2"]="Fahrenheit"
            self.result["unit 1 result"]=self.kelvin_to_degree_celsius()
            self.result["unit 2 result"]=self.kelvin_to_fahrenheit()
        elif self.unit=="":
            self.result["unit 1"]=" "
            self.result["unit 2"]=" "
            self.result["unit 1 result"]=" "
            self.result["unit 2 result"]=" "
            

    def degree_celsius_to_fahrenheit(self):
        return (self.temperature*9/5)+32
    
    def degree_celsius_to_kelvin(self):
        return self.temperature+273.15
    
    def fahrenheit_to_kelvin(self):
        return (self.temperature-32)*5/9+273.15
    
    def fahrenheit_to_degree_celsius(self):
        return (self.temperature-32)*5/9
    
    def kelvin_to_degree_celsius(self):
        return self.temperature-273.15

    def kelvin_to_fahrenheit(self):
        return (self.temperature-273.15)*9/5+32

    def Result(self):
        return self.result


#p=Temperature(32,"Fahrenheit")
#print(p.Result())
