#  LDR & Ultrasonic Alarm System (MicroPython / Raspberry Pi Pico W)

This is a beginner-level alarm-style project for learning GPIO control on Raspberry Pi Pico using MicroPython.

### Features
- Uses an LDR (Light Dependent Resistor) to detect darkness
- If it's dark, a white LED turns on
- Then checks distance using ultrasonic sensor (HC-SR04)
- If an object is closer than 20 cm, a buzzer goes off rapidly like an alarm

###  Components Used
- Raspberry Pi Pico W
- LDR + 10kΩ resistor (voltage divider)
- White LED + 220Ω resistor
- Buzzer (active)
- HC-SR04 Ultrasonic sensor
- Breadboard + jumper wires

###  Purpose
This project is not a real alarm system.  
Its main purpose is to **learn**:
- Analog reading (LDR via ADC)
- Digital input/output (LED, buzzer)
- Timing with `time_pulse_us`
- Condition-based logic

### 📷 Circuit Preview
(You can insert a picture of your breadboard later)

### 📄 main.py
> Contains full source code with comments and modular functions.
