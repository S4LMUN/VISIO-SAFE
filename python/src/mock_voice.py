# === mock_voice.py === #


class MockVoice:
    """จำลองระบบเสียงพูดของ"""

    def __init__(self):
        self.enabled = True

    def speak(self, message: str):
        """จำลองการพูดข้อความ"""
        if not self.enabled:
            return

        print(f"[VOICE] {message}")

    def alert(self, message: str):
        """จำลองการแจ้งเตือนด้วยเสียง"""
        if not self.enabled:
            return

        print(f"[VOICE ALERT]  {message}")

    def stop(self):
        """หยุดระบบเสียง"""
        self.enabled = False
        print("[VOICE] Voice system stopped")

    def start(self):
        """เปิดระบบเสียง"""
        self.enabled = True
        print("[VOICE] Voice system started")


if __name__ == "__main__":
    voice = MockVoice()

    voice.speak("ระบบ VISIO-SAFE เริ่มทำงานแล้ว")
    voice.alert("ตรวจพบสิ่งกีดขวางด้านหน้า")
