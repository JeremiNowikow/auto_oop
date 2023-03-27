# auto - model, speed, max_speed, enginem, start engine, stop_engine, speed_up, slow_down


def auto_init(model, max_speed):
    return {"model": model, "speed": 0, "max_speed": max_speed, "engine": False}


def start_engine(car):
    if not car["engine"]:
        car["engine"] = True
        print("Silnik odpalony")

def stop_engine(car):
    if car["speed"] == 0:
        car["engine"] = False
        print("Silnik zgaszony")
    else:
        print("Zwolnij najpierw")

def speed_up(amount:int, car):
    if car["engine"]:
        car["speed"] = min(car["speed"] + amount, car["max_speed"])
        print(f"Twoja prędkość to {car['speed']}")
    else:
        print("Wpierw odpal silnik")

def slow_down(amount: int, car):
    car["speed"] = max(car["speed"] - amount, 0)
    print(f"Twoja prędkość to {car['speed']}")


fiat = auto_init("Tipo", 240)

print(fiat)
speed_up(200, fiat)
start_engine(fiat)
speed_up(220, fiat)
slow_down(210, fiat)
slow_down(50,fiat)
stop_engine(fiat)
print(fiat)
