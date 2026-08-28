# VISIO-SAFE

### Offline AI Assistive Vision System for Visually Impaired People

> "เปลี่ยนสิ่งที่กล้องมองเห็น ให้กลายเป็นสิ่งที่ผู้ใช้รับรู้ได้"
> *Turning what the camera sees into information the user can perceive.*

---

## สารบัญ / Table of Contents

- [ภาษาไทย](#ภาษาไทย)
- [English](#english)

---

<a id="ภาษาไทย"></a>
## ภาษาไทย

### เกี่ยวกับโครงการ

**VISIO-SAFE** คือโครงงานอุปกรณ์ช่วยเหลือผู้พิการทางสายตา ซึ่งนำเทคโนโลยี **Artificial Intelligence (AI), Computer Vision** และ **Distance Sensors** มาทำงานร่วมกัน เพื่อตรวจจับสิ่งกีดขวางและแจ้งเตือนผู้ใช้งานผ่านเสียงและแรงสั่นสะเทือน

ระบบออกแบบภายใต้แนวคิด **Offline-First** ทำให้การประมวลผลหลักสามารถทำงานภายในอุปกรณ์ได้โดยไม่ต้องพึ่งพาอินเทอร์เน็ต โครงการนี้มีเป้าหมายเพื่อศึกษาการประยุกต์ใช้ AI และ Embedded Systems ในการเพิ่มความสะดวกและความปลอดภัยในการเดินทางของผู้พิการทางสายตา

### เป้าหมายของโครงการ

| ลำดับ | เป้าหมาย |
|---|---|
| 1 | ตรวจจับสิ่งกีดขวางที่อยู่ด้านหน้าผู้ใช้งาน |
| 2 | ระบุตำแหน่งของสิ่งกีดขวาง (ซ้าย / กลาง / ขวา) |
| 3 | ประเมินระยะห่างระหว่างผู้ใช้กับสิ่งกีดขวาง |
| 4 | ประเมินระดับความเสี่ยงของสถานการณ์ |
| 5 | แจ้งเตือนผ่านเสียงและแรงสั่นสะเทือน |
| 6 | รองรับการทำงานแบบ Offline |
| 7 | ลดการพึ่งพาอินเทอร์เน็ตและ Cloud |
| 8 | ศึกษาการประยุกต์ใช้ AI เพื่อช่วยเหลือผู้พิการ |

### หลักการทำงาน

```
Camera → AI Object Detection → Object Position → Distance Measurement
   → Risk Analysis → Voice + Vibration Alert → User
```

**1. Camera** — เก็บภาพจากสภาพแวดล้อมด้านหน้าของผู้ใช้งาน

**2. AI Object Detection** — วิเคราะห์ภาพเพื่อค้นหาวัตถุ เช่น คน เก้าอี้ โต๊ะ รถ ประตู และสิ่งกีดขวางอื่น ๆ ที่โมเดลสามารถตรวจจับได้

**3. Object Position** — วิเคราะห์ตำแหน่งของวัตถุในภาพ แบ่งเป็น `LEFT` / `CENTER` / `RIGHT` เพื่อแจ้งเตือนทิศทางของสิ่งกีดขวาง

**4. Distance Measurement** — ใช้ Distance Sensor วัดระยะห่างระหว่างอุปกรณ์กับสิ่งกีดขวาง

| ระยะ | ระดับ |
|---|---|
| มากกว่า 200 ซม. | ปลอดภัย (SAFE) |
| 100–200 ซม. | เฝ้าระวัง (WARNING) |
| น้อยกว่า 100 ซม. | เสี่ยงสูง (HIGH RISK) |

*ค่าระยะจริงสามารถปรับตามผลการทดลองของโครงการ*

**5. Risk Analysis** — นำข้อมูลจาก AI และ Distance Sensor มาประเมินร่วมกัน

```
Object     = Chair
Position   = Center
Distance   = 45 cm
──────────────────────
Risk Level = HIGH
```

**6. Alert System** — เมื่อพบความเสี่ยง ระบบจะแจ้งเตือนผ่านเสียงและแรงสั่นสะเทือน เช่น *"ระวัง มีสิ่งกีดขวางด้านหน้า"* หรือ *"สิ่งกีดขวางด้านซ้าย"*

### โครงสร้างระบบ

```
                         VISIO-SAFE
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                   │
        Camera          Distance Sensor       Control
           │                  │                   │
           └──────────────────┼───────────────────┘
                              │
                         Processing
                              │
              ┌───────────────┴───────────────┐
              │                                │
       Object Detection                 Risk Analysis
              │                                │
              └───────────────┬────────────────┘
                              │
                        Alert System
                     ┌────────┴────────┐
                     │                 │
                  Audio           Vibration
```

### เทคโนโลยีที่ใช้

**Software**
- Python
- OpenCV
- YOLO / Object Detection Model
- Text-to-Speech
- Raspberry Pi OS *(สำหรับ Prototype Hardware)*

**Hardware**
- Raspberry Pi
- Camera
- Ultrasonic / Distance Sensor
- Vibration Motor
- Speaker
- Push Button
- Battery / Power Bank

*Hardware สามารถเปลี่ยนแปลงได้ตามรุ่นต้นแบบและงบประมาณของโครงการ*

### การประมวลผลแบบ Offline และความเป็นส่วนตัว

VISIO-SAFE ออกแบบภายใต้แนวคิด **Offline Processing** โดยประมวลผลข้อมูลภายในอุปกรณ์แทนการส่งภาพขึ้น Cloud ซึ่งมีข้อดีดังนี้:

- ไม่จำเป็นต้องมีอินเทอร์เน็ตสำหรับฟังก์ชันหลัก
- ลดการส่งข้อมูลภาพออกจากอุปกรณ์
- ลดการพึ่งพาเซิร์ฟเวอร์ภายนอก
- สามารถใช้งานในพื้นที่ไม่มี Wi-Fi ได้

### การประเมินประสิทธิภาพ

| การทดสอบ | สิ่งที่วัด |
|---|---|
| ตรวจจับเก้าอี้ | Detection Accuracy |
| ตรวจจับคน | Detection Accuracy |
| ตรวจจับสิ่งกีดขวาง | Detection Rate |
| วัดระยะ | Distance Error |
| แจ้งเตือน | Response Time |
| ระบุตำแหน่ง | Direction Accuracy |

```
Accuracy (%) = (จำนวนครั้งที่ตรวจถูกต้อง ÷ จำนวนครั้งที่ทดสอบทั้งหมด) × 100
```

ผลการทดสอบจริงจะถูกบันทึกและนำเสนอในรูปแบบตารางและกราฟ

### ข้อจำกัด

VISIO-SAFE เป็น **Prototype สำหรับการศึกษาและการแข่งขัน** และมีข้อจำกัดดังนี้:

- ประสิทธิภาพของ AI ขึ้นอยู่กับโมเดลและ Hardware ที่ใช้
- การตรวจจับอาจผิดพลาดในสภาพแสงที่ไม่เหมาะสม
- Distance Sensor อาจมีความคลาดเคลื่อนกับพื้นผิวบางประเภท
- วัตถุบางชนิดอาจไม่อยู่ในข้อมูลที่โมเดลเคยเรียนรู้
- ระบบไม่ควรใช้แทนไม้เท้าหรืออุปกรณ์ช่วยเหลือทางการแพทย์/วิชาชีพ

**ผู้ใช้งานควรใช้อุปกรณ์ช่วยเหลือมาตรฐานร่วมกับระบบเสมอ**

### สถานะโครงการ

- [ ] Research
- [ ] System Design
- [ ] AI Prototype
- [ ] Computer Vision
- [ ] Distance Detection
- [ ] Risk Analysis
- [ ] Voice Alert
- [ ] Vibration Alert
- [ ] Hardware Prototype
- [ ] Field Testing

### Roadmap

**Phase 1 — AI Prototype**
- [x] ศึกษาแนวคิดระบบ
- [ ] ติดตั้ง Python
- [ ] ทดลอง OpenCV
- [ ] ทดลอง Object Detection
- [ ] ทดสอบ Webcam

**Phase 2 — Intelligent Detection**
- [ ] Object Position
- [ ] Distance Measurement
- [ ] Risk Score
- [ ] Voice Alert

**Phase 3 — Hardware**
- [ ] Raspberry Pi
- [ ] Camera
- [ ] Distance Sensors
- [ ] Vibration System
- [ ] Speaker
- [ ] Portable Power

**Phase 4 — Testing**
- [ ] Accuracy Test
- [ ] Distance Test
- [ ] Response Time Test
- [ ] Real-world Simulation
- [ ] User Experience Evaluation

### ทีมพัฒนา

**Project:** VISIO-SAFE
**Category:** Assistive Technology / Artificial Intelligence / Embedded System

Developed as a student innovation project.

### Disclaimer

VISIO-SAFE เป็นต้นแบบเพื่อการศึกษาและการพัฒนานวัตกรรม ไม่ใช่อุปกรณ์ทางการแพทย์ และไม่ควรใช้เป็นระบบนำทางเพียงอย่างเดียวในสถานการณ์จริงที่มีความเสี่ยงสูง

---

<a id="english"></a>
## English

### About

**VISIO-SAFE** is an assistive technology prototype designed to help visually impaired people detect obstacles in their surrounding environment. The system combines **Artificial Intelligence (AI), Computer Vision**, and **Distance Sensors** to detect nearby objects, estimate their position and distance, analyze potential risks, and provide feedback through voice and vibration alerts.

VISIO-SAFE follows an **Offline-First** design philosophy, allowing core processing to run locally without requiring an internet connection.

### Objectives

| # | Objective |
|---|---|
| 1 | Detect obstacles in front of the user |
| 2 | Identify obstacle positions (left, center, right) |
| 3 | Estimate the distance to detected obstacles |
| 4 | Analyze potential danger levels |
| 5 | Provide voice and vibration alerts |
| 6 | Support offline operation |
| 7 | Reduce dependency on cloud services |
| 8 | Explore the application of AI in assistive technology |

### System Workflow

```
Camera → AI Object Detection → Object Position → Distance Measurement
   → Risk Analysis → Voice + Vibration Alert → User
```

**1. Camera** — Captures the environment in front of the user.

**2. AI Object Detection** — Analyzes the camera feed to detect objects such as people, chairs, tables, vehicles, doors, and other objects supported by the detection model.

**3. Object Position** — Classifies detected objects into approximate directions: `LEFT` / `CENTER` / `RIGHT`.

**4. Distance Measurement** — A distance sensor measures the approximate distance between the device and an obstacle.

| Distance | Level |
|---|---|
| > 200 cm | SAFE |
| 100–200 cm | WARNING |
| < 100 cm | HIGH RISK |

*Thresholds can be adjusted based on experimental results.*

**5. Risk Analysis** — Combines AI detection and distance data to estimate potential risk.

```
Object     = Chair
Position   = Center
Distance   = 45 cm
──────────────────────
Risk Level = HIGH
```

**6. Alert System** — Provides feedback through voice and vibration, e.g. *"Obstacle detected ahead"* or *"Obstacle on the left."*

### System Architecture

```
                         VISIO-SAFE
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                   │
        Camera          Distance Sensor       Control
           │                  │                   │
           └──────────────────┼───────────────────┘
                              │
                         Processing
                              │
              ┌───────────────┴───────────────┐
              │                                │
       Object Detection                 Risk Analysis
              │                                │
              └───────────────┬────────────────┘
                              │
                        Alert System
                     ┌────────┴────────┐
                     │                 │
                  Audio           Vibration
```

### Technologies

**Software**
- Python
- OpenCV
- YOLO / Object Detection Model
- Text-to-Speech
- Raspberry Pi OS *(for the hardware prototype)*

**Hardware**
- Raspberry Pi
- Camera
- Ultrasonic / Distance Sensor
- Vibration Motor
- Speaker
- Push Button
- Battery / Power Bank

*Hardware components may change depending on the prototype version and available budget.*

### Offline Processing & Privacy

VISIO-SAFE is designed with an Offline-First approach. Core processing runs locally on the device instead of sending camera footage to a cloud server:

- No internet required for core functions
- Reduced transmission of camera data
- Less dependency on external servers
- Usable in areas without Wi-Fi

### Performance Evaluation

| Test | Measurement |
|---|---|
| Chair Detection | Detection Accuracy |
| Person Detection | Detection Accuracy |
| Obstacle Detection | Detection Rate |
| Distance Measurement | Distance Error |
| Alert System | Response Time |
| Direction Detection | Direction Accuracy |

```
Accuracy (%) = (Correct Detections ÷ Total Tests) × 100
```

Actual experimental results will be recorded and presented using tables and graphs.

### Limitations

VISIO-SAFE is an **educational and competition prototype** with the following limitations:

- AI performance depends on the selected model and hardware
- Detection may be affected by poor lighting
- Distance sensors may have errors with certain surfaces
- Objects outside the model's training data may not be detected
- The system should not replace standard mobility aids or professional medical equipment

Users should continue to use appropriate standard mobility aids when necessary.

### Project Status

- [ ] Research
- [ ] System Design
- [ ] AI Prototype
- [ ] Computer Vision
- [ ] Distance Detection
- [ ] Risk Analysis
- [ ] Voice Alert
- [ ] Vibration Alert
- [ ] Hardware Prototype
- [ ] Field Testing

### Roadmap

**Phase 1 — AI Prototype**
- [x] Research system concept
- [ ] Install Python
- [ ] Test OpenCV
- [ ] Test Object Detection
- [ ] Test Webcam

**Phase 2 — Intelligent Detection**
- [ ] Object Position
- [ ] Distance Measurement
- [ ] Risk Score
- [ ] Voice Alert

**Phase 3 — Hardware**
- [ ] Raspberry Pi
- [ ] Camera
- [ ] Distance Sensors
- [ ] Vibration System
- [ ] Speaker
- [ ] Portable Power

**Phase 4 — Testing**
- [ ] Accuracy Test
- [ ] Distance Test
- [ ] Response Time Test
- [ ] Real-world Simulation
- [ ] User Experience Evaluation

### Project Information

**Project:** VISIO-SAFE
**Category:** Assistive Technology / Artificial Intelligence / Embedded Systems

Developed as a student innovation project.

### Disclaimer

VISIO-SAFE is an educational prototype and is not a medical device. It should not be relied upon as the sole navigation or safety system in high-risk real-world situations.