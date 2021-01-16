class RainData:
    def __init__(self, date, tips):
        self.date = date
        self.tips = tips
        self.inches = tips/100

    def __str__(self):
        return f"{self.date}: {self.tips/100}inches"
