# 🚦 Traffic Control System — Subsystem 4 (Overheight Detection)
*Engineering Smart Systems Project*

## 📌 Project Overview
This project features **Subsystem 4**, the final safety barrier designed to detect overheight vehicles prior to a tunnel entrance. Upon detection, the system automatically triggers warning signals and traffic lights to stop high-clearance vehicles and prevent tunnel collisions.

## ⚡ Key Features & Contributions
* **Real-Time Overheight Detection:** Integrated ultrasonic sensors to continuously measure vehicle height at the tunnel approach.
* **Hardware & Software Integration:** Programmed the control logic in Python using the `PyMata4` library to control an **Arduino Uno** via serial communication.
* **Circuit Design & Hardware Wiring:** Designed and wired sensor inputs and traffic light signal outputs onto physical circuit boards.
* **Incremental Testing & Integration:** Conducted end-to-end testing with neighboring subsystems to ensure zero-latency fail-safe triggers during the final live demonstration.

## 🛠️ Tech Stack & Hardware
* **Language:** Python
* **Microcontroller:** Arduino Uno
* **Libraries:** `PyMata4`
* **Hardware:** Ultrasonic Sensors (HC-SR04), Traffic LED Lights, Signal Conditioning Circuits
