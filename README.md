# IoTproject
An IoT project for SKEL 4213 on waste management system using ESP 8266 with HC-SR04 ultrasonic sensor to obtain the required data.
## IoT Waste Management System 🗑️ 
### Problem Statement

*The availability of garbage bins spaces are always unavailable during the weekend at the college. This is beacuse of the cleaners are not working during the weekends and this leads to accumulated of rubbish that are not collected. Because of this, the residents do not know where to throw their rubbish and end up leaving it outside of the overflowing rubbish bin.* 

<strong><ins>Our Solution</ins></strong>

An IoT application to automate the manual checking rubbish bins that is already full or not, and pass the information to a dashboard where users could locate any available bins that are available.

<strong><ins>Use Case Diagram</ins></strong>

<p align="center">
<img src="Images/case_diagram.png">
</p>

### System Architecture

Below are the general overview of the system architecture for our IoT waste management system. For this project we will be using **ESP 8266** as our microcontroller device and it will be connected to **HC-SR04** ultrasonic sensor to obtain the capacity level of rubbish bins. The device will communicate using **HTTP** data protocol transmission and it will send the data to a **REST-API** implemented in **Flask** before later on hosted by **Heroku** Cloud platform and finally display the data on our simple dashboard app which we will be build using **Figma**. 

<img src="Images/system_arc.png">

### Hardware
<strong><ins>ESP 8266</ins></strong>

<img src="Images/esp8266.png" width="173" height="308">

<strong><ins>HC-SR04</ins></strong>

<img src="Images/hc_sr04.jpg" width="256" height="197">

<strong><ins>Circuit Diagram</ins></strong>

<img src="https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2021/06/ESP8266-Ultrasonic-Sensor-Wiring-Fritzing-Diagram.png?w=738&quality=100&strip=all&ssl=1" width="318" height="258">

<strong>Code Sample</strong>

<details>
  <summary>Please Click Me</summary>

  ```
//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034


long duration;
float distanceCm;

const int trigPin = 12;
const int echoPin = 14;

void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
}

void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance
  distanceCm = (duration * SOUND_VELOCITY/2)-1;
  
  // Prints the distance on the Serial Monitor
  Serial.print("Distance (cm): ");
  Serial.println(distanceCm);

  delay(1000);
}
  ```
</details>


### Cloud Platform

The following [video](https://youtu.be/mI5fn9AS04o) shows the process on how to deploy an application using Heroku. This is the [link](https://iot-waste-v2.herokuapp.com/) to the website in the video.
 
### Dashboard

<p align="center">

<img src="Images/1. Sign In Page.png" width="227" height="465">
<img src="Images/2. Sign Up Page.png" width="227" height="465">
<img src="Images/3. Select College Page.png" width="227" height="465">
<img src="Images/4. Select Block Page.png" width="227" height="465">
<img src="Images/5. Status Page.png" width="227" height="465">

</p>


## MILESTONE 3

The following [video](https://youtu.be/7Tu39UT9mWg) shows the process on how we send data from our device to our web server using http protocol. This is the [link](https://sampah-app.herokuapp.com/) to the our web server hosted by Heroku as shown in the video.

## MILESTONE 4

The following [video](https://youtu.be/7Tu39UT9mWg) shows the process on how we save the data from our IoT device to a dashboard and visualize the data on a dashboard. The database that we used for our porject is PostgreSQL due to its simplicity to deploy with  heroku. Grafana was used for the visualization of the data in the database as shown in the video. 

## MILESTONE 5

The following [video](https://youtu.be/7Tu39UT9mWg) shows the explanation in detail about milestone 5 which is the UI Improvement. The layout of the improve UI has being change slightly appopriate to the comments of the app user. The changes includes a time-series graph and more sophisicated real-time data refresh. The user comments are as below:

- app too simple and bland
- need to know specific time the rubbish can is full
- the app keeps refreshing making it too buggy