# Axle
Axle is an open-source, community driven autonomous RC car software. The purpose of this repository is to create an autonomous self-driving 
RC car script written in Python 3. The software has been designed for the Raspberry Pi and utilises OpenCV. The full testing envrionment is
described below.

## Feature List
* Automatic Stop - The car automatically stops when a red object is detected by the camera. (Completed)
* Collision Avoidance - The car automatically stops when it detects an obstacle obstructing it's path. (TBD)

## Library Dependencies
* opencv_python‑3.2.0 
* RPi.GPIO

## Testing Envrionment
The following section will be used to describe the equipment and outcomes of the software being applied in a real-world envrionment.
### Equipment used
* Raspberry Pi 3
* Logitech C170
* x2 L293D - Each L293D driver IC is capable of powering 2 motors. I do realise that there are significant losses associated with this IC and
that there are other far better solutions available such as the A4988.
* Solderless Breadboard
* RC car frame
* 4x Motors
* Several jumper wires
