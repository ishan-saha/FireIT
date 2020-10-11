#include "DHT.h"
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define DHTTYPE DHT22
#define DHTPIN 4

DHT dht(DHTPIN,DHTTYPE);
/* Put your SSID & Password */
const char* ssid = "FireIT";  // Enter SSID here
const char* password = "<@FireIT@1.1#>";  //Enter Password here
const char* MAC = WiFi.macAddress();

/* Put IP Address details */
IPAddress local_ip(10,0,15,1);
IPAddress gateway(10,0,15,1);
IPAddress subnet(255,0,0,0);

ESP8266WebServer server(80);

void setup()
{
  WiFi.softAP(ssid, password,5,true);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);

  Serial.begin(115200);
  server.on("/", handle_OnConnect);
  server.onNotFound(handle_OnConnect);
  server.begin();
  dht.begin();
}

void loop()
{
  server.handleClient();
  
}

void handle_OnConnect() 
{
  Serial.println("Sending data to the client in form of JSON");
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  server.send(200, "text/html", SendHTML(t,h)); 
}

String SendHTML(float t, float h)
{
  delay(100);
  Serial.println(t);
  Serial.println(h);
  String body="{\"Temperature\":\""+String(t)+"\",\"Humidity\":\""+String(h)+"\",\"MAC\":\""+String(MAC)+"\"}";
  return body;
}
