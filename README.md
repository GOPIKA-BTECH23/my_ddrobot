# my_ddrobot
A teleop-controlled fire sprinkler AGV robot that allows remote/manual control of a robotic arm and turret, designed for fire suppression applications. Operators can use keyboard commands to position the arm and turret in real time. The system is ROS2-integrated and facilitates safe, responsive actuation for emergency or hazardous environments.

Teleop-Controlled Fire Sprinkler AGV Robot
This project implements a teleoperation system for an Autonomous Guided Vehicle (AGV) equipped with a fire sprinkler arm. It allows remote/manual control of the arm’s position and turret using keyboard commands.

Features
Remote teleoperation for a fire sprinkler robotic arm

Keyboard controls for two arm links and the turret

ROS 2 integration for real-time command and feedback

Project Structure
teleop_arm_control.py: ROS2 node receiving keyboard input and publishing float commands to arm/turret motors

setup.py: Python setup script for ROS2 packaging and installation

Log files (logger_all.log, events.log): For debugging and recording events

report_ROS.pdf: Detailed technical report

Controls
Arm Link 1:
q: Down
w: Up

Arm Link 2:
a: Down
s: Up

Turret:
z: Left
x: Right

Exit:
CTRL+C

Installation
Clone this repository:

bash
git clone https://github.com/yourusername/your_repository_name.git
Navigate to the project folder:

bash
cd your_repository_name
Install the package using ROS2 tools:

bash
ros2 run myddrobot armturretteleop
Requirements
Python 3

ROS 2 (tested with [choose your distro, e.g., Foxy/Humble])

setuptools

[pytest] (for testing)

Usage
Run the teleop node:

bash
python3 teleop_arm_control.py
Use the keyboard controls to operate the arm and turret.

Robot Initialisation and Description  
<img width="1050" height="718" alt="image" src="https://github.com/user-attachments/assets/8ff78088-b7f1-41fa-86ff-fb0281f18b0a" />

Navigation Performance and motion control 

<img width="767" height="329" alt="image" src="https://github.com/user-attachments/assets/15f12a77-b8f6-4d75-9a92-cec9f042d755" />

Sensor feedback and visualisations(1) 
<img width="1218" height="551" alt="image" src="https://github.com/user-attachments/assets/157becd3-6edd-4580-bec4-64206967ac5a" />
Sensor feedback and visualisations(2) 
<img width="1219" height="691" alt="image" src="https://github.com/user-attachments/assets/701145f7-bcf1-4cd3-bacf-c3e3ca6f0266" />
 ROS 2 Integration and TF Management
<img width="897" height="613" alt="image" src="https://github.com/user-attachments/assets/0487a619-e5d5-4019-b97e-06b70212a72b" />
