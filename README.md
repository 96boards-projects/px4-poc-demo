# PX4 + 96Boards SoM Mavlink Demo

This is a PoC demo to show the mavlink communication between PX4-v5x FMU and a 96Boards SoM. The demo is currently limited to showing telemetry data recieved by the 96Boards SoM from the PX4-v5x FMU over Mavlink and overlaying it on a live video feed using FFMPEG. *This code is actively in development and may change drastically over time*

TODO:
- Add more telemetry data
- Test FFMPEG hw Accelaration for RK3399