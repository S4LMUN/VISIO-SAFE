# === main.py === #

import mock_sensor

def start():
    while True:
        print("=== System Start ===")
        danger = mock_sensor.sensor() # will change#
        print(f"Danger Level == {danger}")

        decided(danger)

def decided(danger):
    if danger == 1:
        pass
    elif danger == 2:
        pass
    elif danger == 3:
        pass

if __name__ == "__main__":
    start()
