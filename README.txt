Quadruped Robot project by Daniel Wirick 12-7-14

This is a small 4 legged servo bot.
There are 2 degrees of freedom on each leg which are servo driven.
Servos are controlled by an Arduino Nano which in turn receives instruction through its UART port
A MPU6050 is also on-board to assist with navigation and attitude in rough terrain
The MPU6050 is attached to the Arduino Nano

Currently I have an Olinuxino IMX255 sending instruction to the Arduino UART and a HC-05 bluetooth adapter to connect to the Olinuxino

Python code runs on the Olinuxino

Arduino code runs on Arduino Nano (obvious I hope :)

Current chassis was laser cut from 6mm plywood
