# SO-ARM101 Imitation Learning & Teleoperation

This repository contains the software pipeline for teleoperating and training a 5-DoF SO-ARM101 robotic manipulator to autonomously pick up objects (e.g., a pen) using Imitation Learning. The project bridges low-level Feetech servo control with the Hugging Face LeRobot framework, utilizing an Action Chunking with Transformers (ACT) policy.

Developed following the Physical AI Student Workshop at Tidel Park, Chennai. A full video demonstration will be available on the [Electrojects YouTube Channel](https://www.youtube.com/@Electrojects).

## Hardware Architecture
* **Robotic Arm:** 5-DoF SO-ARM101 Kit + 1 Gripper
* **Actuators:** STS3215 Serial Bus Servos
* **Motor Driver:** Feetech Adapter Board (Half-duplex UART daisy chain)
* **Vision System:** Dual-camera setup (Workspace/Bird's-eye view + End-effector/Wrist view) downscaled to 640x480 at 30 FPS.

## Software Stack
* Python 3.11
* `lerobot` (v0.9.4) for dataset recording and ACT policy training
* `feetech-servo-sdk` for bypassing abstractions to achieve zero-latency `GroupSyncRead` and `GroupSyncWrite` hardware communication.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/so-arm101-imitation-learning.git](https://github.com/YOUR_USERNAME/so-arm101-imitation-learning.git)
   cd so-arm101-imitation-learning