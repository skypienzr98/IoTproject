# IoTproject
An IoT project for SKEL 4213 on waste management system using ESP 8266 with HC-SR04 ultrasonic sensor to obtain the required data.
## IoT Waste Management System 🗑️ 
### Problem Statement

*The availability of garbage bins spaces are always unavailable during the weekend at the college. This is beacuse of the cleaners are not working during the weekends and this leads to accumulated of rubbish that are not collected. Because of this, the residents do not know where to throw their rubbish and end up leaving it outside of the overflowing rubbish bin.* 

<strong><ins>Our Solution</ins></strong>

An IoT application to automate the manual checking rubbish bins that is already full or not, and pass the information to a dashboard where users could locate any available bins that are available.

### System Architecture

Below are the general overview of the system architecture for our IoT waste management system. For this project we will be using **ESP 8266** as our microcontroller device and it will be connected to **HC-SR04** ultrasonic sensor to obtain the capacity level of rubbish bins. The device will communicate using **MQTT** data protocol transmission and it will send the data to **Mosquitto** broker as the main MQTT broker then to **Heroku** Cloud platform and finally update the data on our simple dashboard app which we will be build using **Figma**. 

<img src="Images/system_arc.png">

### Hardware
<strong>ESP 8266</strong>

<img src="Images/esp8266.png" width="173" height="308">

<strong>HC-SR04</strong>


<img src="Images/hc_sr04.jpg" width="256" height="197">


### Cloud Platform

### Dashboard

<img src="Images/1. Sign In Page.png" width="384" height="216">
<img src="Images/2. Sign Up Page.png" width="384" height="216">
<img src="Images/3. Select College Page.png" width="384" height="216">
<img src="Images/4. Select Block Page.png" width="384" height="216">
<img src="Images/5. Status Page.png" width="384" height="216">