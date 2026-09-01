# === sensor.py === #

# r = range
# m = meter
# danger level 1 simple, 2 near, 3 danger 

def sensor():
    sensor_r = 100
    if sensor_r >= 2 < 5:
        return 1

    elif sensor_r >= 1 < 2:
        return 2

    elif sensor_r < 1:
        return 3

    else:
        return None
