class Auto:
    def __init__(self, model, max_speed):
        self.model = model
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print("Silnik odpalony")

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print("Silnik zgaszony")
        else:
            print("Zwolnij najpierw")

    def speed_up(self, amount: float):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f"Twoja prędkość to {self.speed}")
        else:
            print("Wpierw odpal silnik")

    def slow_down(self, amount: float):
        self.speed = max(self.speed - amount, 0)
        print(f"Twoja prędkość to {self.speed}")

class Van(Auto):
    def __init__(self, model, max_speed, seats=7):
        self.seats = seats
        super().__init__(model, max_speed * 0.85)

    def speed_up(self, amount: int):
        super().speed_up(amount)


fiat = Auto("Tipo", 240)
fiat.speed_up(200)
print(fiat.model, fiat.speed, fiat.max_speed, fiat.engine)
fiat.start_engine()
fiat.speed_up(200)
fiat.speed_up(200)
fiat.slow_down(230)
fiat.stop_engine()
fiat.slow_down(20)
fiat.stop_engine()

bmw = Van("e621", 160)
lada = Auto("Niva", 70)
print(lada.model, lada.speed, lada.max_speed, lada.engine)
print(bmw.seats)
print(bmw.max_speed)


