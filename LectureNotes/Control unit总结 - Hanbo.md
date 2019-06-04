# Control Unit

_Content Included_
1. Intruder Alert - Hanbo
2. Automated Door - Jelly
3. Automated Temperature Control - Helen
4. Automated Speed Control Fan - Charlie
5. Soil Humidity Detector - Mr.нет
6. Pulse Sensor - David X

---

## 1. Intruder Alert
- Sensor Input
  - Vibration Sensor
  - Ultrasonic sensor
  - IR Sensor
- Output Tranducer
  - RED Lightbulbs
  - Buzzer
- Feedback: Niet
  
- Syllabus content:
  > 7.1.2 Outline the uses of microprocessors and sensors input in control systems
  
  > 7.1.3 Evaluate different input devices for the collection of data in specified situations.
  
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
  (Feedback: output that goes back as input of the control system)
  
 **PPT click this:** [Intruder Alert PPT](abc)
 
 ## 2. Automatede Door
 
 - Sensor Input: Ultrasonic sensor(s)
 - Output Tranducer: 2 Servos
 - Feedback: Yes, because the servo status (door open or not) is taken as a input to the control system
 
 - Syllabus content:
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
  > 7.1.5 Describe the role of feedback in a control system
  
 **PPT click this:** [Automated Door PPT](abc)
 
 ## 3. Automated Temperature Control
 
 > What Why How
 
 >> What we need: to control the temperature for an object
 
 >> Why design this: to protect something that need careful temperature control, e.g: medicine, fridge
 
 >> Prototype: control the temperature to be +/- 2 degree celcius of the room temperature
 
 
- Sensor Input: temperature sensor 
- Output Tranducer: 
  - fan that turns on when temperature is too high
  - LED lightbulb that indicates the status of the object (heating, temperature reached, too warm, etc.)
- Feedback: the output (change in temperature) feeds in as input for each cycle

- Syllabus content:
  > 7.1.2 Outline the uses of microprocessors and sensor input in control systems
  
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
  > 7.1.5 Describe the role of feedback in a control system
  
 **PPT click this:** [Automated Temperature Control PPT](abc)
 
 ## 4. Automated Speed Control Fan
 
 > What Why How
 
 >> What: a automated speed-control fan
 
 >> Why: turn on/off fans in order to save energy
 
 >> How: The speed of fan decreases as the distance increases
 
 - Sensor Input: Ultrasonic sensor
 - Output Tranducer: LED light, Fan speed
 - Feedback: not really, because the output doesn't really affect input
 
 - Syllabus content:
  > 7.1.2 Outline the uses of microprocessors and sensor input in control systems
  
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
  > 7.1.5 Describe the role of feedback in a control system
  
 **PPT click this:** [Automated Speed Control Fan PPT](abc)
 
## 5. Soil Humidity Detector

- Why this: prevent plants dying from dehydration
- What I need: detect humidity, alarm when the soil is dry, automated water adder

- Input Sensor: humidity sensor
- Output Tranducer:
  - Buzzer
  - Servo (for adding water)
  - Digital Pipe display (to display the exact humidity)
- Feedback: the water added by turning servo affects the input sensor, which detects the humidity

- Syllabus content:
  > 7.1.2 Outline the uses of microprocessors and sensor input in control systems
  
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
  > 7.1.5 Describe the role of feedback in a control system
  
 **PPT click this:** [Soil Humidity Detector PPT](abc)
 
 ## 6. Pulse Sensor
 
 - Background: pulse sensors (which detects heart beets) are widely used in smart watches and in some phones
 
 - Input Sensor: pulse sensor
 - Output: Image of the pulse displayed in Arduino
 - Feedback: ninet
 
 - Futuer Expectations: Connect it to other sensors and possibly the a network that alerts the medical service provider when something wrong happened
 
 - Syllabus content:
  > 7.1.2 Outline the uses of microprocessors and sensor input in control systems
  
  > 7.1.4 Explain the relationship between a sensor, the processor and an output transducer
  
 **PPT click this:** [Pulse Sensor PPT](abc)
 
