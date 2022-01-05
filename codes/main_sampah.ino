#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <string>

const int trigPin = 14;
const int echoPin = 12;
uint8 capLevel;
int tank_h =50;

//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034


long duration;
float distanceCm;

const char* ssid = "Qibby";
const char* password = "0123456789";
 
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting...");
  }
 
  Serial.println("Connected successfully.");
}

void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  setup_wifi();
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
  distanceCm = duration * SOUND_VELOCITY/2;
  capLevel = 100 - round((distanceCm/tank_h)*100);

  
  // Prints the distance on the Serial Monitor
  Serial.print("Capacity: ");
  Serial.print(capLevel);
  Serial.println("%");

  if (WiFi.status() != WL_CONNECTED) {
    setup_wifi();
  } else {
    //WiFiClient client;
    HTTPClient http;
 
    http.begin("http://sampah-app.herokuapp.com/");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    String requestData = "capacity=" + String(capLevel) + "&count=" + String(true);
    int httpCode = http.POST(requestData); //Send the request
    String payload = http.getString(); //Get the response payload
    Serial.println(httpCode); //Print HTTP return code
    http.end(); //Close connection
  }
  
  delay(1000);
}
