class SpaceAge:
    def __init__(self, seconds):
        # 31,557,600 is the amount of seconds for a year on Earth
        self.years_on_earth = seconds / 31557600

    def on_earth(self):
        return round(self.years_on_earth, 2)

    def on_mercury(self):
        # 0.2408467 is the orbital period in earth years of mercury
        years = self.years_on_earth / 0.2408467
        return round(years, 2)

    def on_venus(self):
        # 0.61519726 is the orbital period in earth years of mercury
        years = self.years_on_earth / 0.61519726
        return round(years, 2)
    
    def on_mars(self):
        # 1.8808158 is the orbital period in earth years of mercury
        years = self.years_on_earth / 1.8808158
        return round(years, 2)

    def on_jupiter(self):
        # 11.862615 is the orbital period in earth years of mercury
        years = self.years_on_earth / 11.862615
        return round(years, 2)
    
    def on_saturn(self):
        # 29.447498 is the orbital period in earth years of mercury
        years = self.years_on_earth / 29.447498
        return round(years, 2)

    def on_uranus(self):
        # 84.016846 is the orbital period in earth years of mercury
        years = self.years_on_earth / 84.016846
        return round(years, 2)

    def on_neptune(self):
        # 164.79132 is the orbital period in earth years of mercury
        years = self.years_on_earth / 164.79132
        return round(years, 2)