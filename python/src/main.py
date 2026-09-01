# === main.py === #
import mock_voice
import mock_sensor

def start():
    while True:
        print("=== System Start ===")
        danger = mock_sensor.sensor() # will change#
        print(f"Danger Level == {danger}")

        decided(danger)

def decided(danger):
    if danger == 1:
        mock_voice.simple()
    elif danger == 2:
        mock_voice.near()
    elif danger == 3:
        mock_voice.danger()

if __name__ == "__main__":
    start()
