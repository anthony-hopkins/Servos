# Servos - Raspberry Pi Servo Motor Control

A Python-based servo motor control system designed for the Raspberry Pi, specifically built to control LS-3006 continuous rotation servos for robotic applications. This project provides precise control over servo motors for tasks requiring accurate positioning, gripping, and movement control.

## 🚀 Features

- **Precise Servo Control** - Accurate duty cycle calculations for smooth operation
- **Multiple Movement Modes** - Open, close, precise move, and hold operations
- **Continuous Rotation Support** - Designed for LS-3006 continuous rotation servos
- **Raspberry Pi Integration** - Native GPIO control using RPi.GPIO library
- **Flexible Timing Control** - Customizable duration and duty cycle parameters
- **Safety Features** - GPIO cleanup and kill switch functionality
- **Real-World Applications** - Perfect for robotics, automation, and precision tasks
- **Professional Grade** - Suitable for critical applications requiring exact control

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Raspberry Pi](https://www.raspberrypi.org/) (any model with GPIO pins)
- [Raspberry Pi OS](https://www.raspberrypi.org/software/) (or compatible Linux distribution)
- [Python 3](https://www.python.org/downloads/) (3.6+ recommended)
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) library
- LS-3006 continuous rotation servo motor
- Appropriate power supply and wiring

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Servos
```

### 2. Install Dependencies

```bash
# Install RPi.GPIO library
sudo pip3 install RPi.GPIO

# Or install via apt
sudo apt-get install python3-rpi.gpio
```

### 3. Connect Hardware

Connect your LS-3006 servo to the Raspberry Pi:
- **Signal Wire**: GPIO 18 (Pin 12)
- **Power**: 5V supply (Pin 2 or 4)
- **Ground**: GND (Pin 6)

### 4. Run Basic Operations

```bash
cd LS3006
python3 Rotation.py
```

## 🏗️ Project Structure

```
Servos/
├── LS3006/                     # LS-3006 servo control module
│   ├── Rotation.py             # Main servo control class
│   └── kill_gpios.py           # GPIO cleanup utility
└── README.md                   # This documentation
```

## 🔧 Configuration

### GPIO Pin Configuration

The servo is configured to use:
- **GPIO Mode**: BCM numbering system
- **Control Pin**: GPIO 18 (Pin 12 on physical board)
- **PWM Frequency**: 50 Hz (standard for servos)
- **Duty Cycle Range**: 0-180 (mapped to servo control)

### Servo Specifications

- **Model**: LS-3006 continuous rotation servo
- **Voltage**: 5V DC
- **Control Signal**: PWM (Pulse Width Modulation)
- **Rotation**: Continuous (360° rotation capability)
- **Speed Control**: Variable based on duty cycle

## 📦 Dependencies

### Core Components

- **RPi.GPIO** - Raspberry Pi GPIO control library
- **Python 3** - Runtime environment
- **time** - Built-in Python timing functions
- **sys** - Built-in Python system functions

### Hardware Requirements

- **Raspberry Pi** - Single-board computer
- **LS-3006 Servo** - Continuous rotation servo motor
- **Power Supply** - 5V DC power source
- **Connecting Wires** - Jumper wires for connections

## 🐳 Usage Examples

### Basic Servo Operations

```python
from Rotation import Grip

# Initialize servo control
g = Grip()

# Basic open/close operations
g.start("open")      # Open gripper
g.start("close")     # Close gripper

# Hold with specific pressure
g.hold(5, 130)      # Hold for 5 seconds with duty 130

# Precise movement
g.start("precise", 0.3, 75)  # Move for 0.3 seconds with duty 75
```

### Advanced Control

```python
# Custom duty cycle and duration
g.precise_move(2.0, 90)    # 2 seconds, neutral position
g.hold(10, 150)            # High pressure hold for 10 seconds

# Sequential operations
g.start("open")
time.sleep(1)
g.start("close")
g.hold(3, 120)
```

## 🚀 Development Workflow

### Running the Servo Controller

```bash
# Basic operation
python3 Rotation.py

# Test specific movements
python3 -c "
from Rotation import Grip
g = Grip()
g.start('open')
g.start('close')
"
```

### GPIO Management

```bash
# Clean up GPIO pins
python3 kill_gpios.py

# Check GPIO status
gpio readall
```

### Debugging

```bash
# Monitor GPIO activity
sudo python3 -u Rotation.py

# Check servo connections
gpio -g mode 18 out
gpio -g write 18 1
```

## 🔍 Application Features

### Movement Control

- **Open Operation**: Clockwise rotation for opening gripper
- **Close Operation**: Counter-clockwise rotation for closing
- **Precise Movement**: Custom duration and duty cycle control
- **Hold Function**: Maintains position with specified pressure

### Duty Cycle Calculations

The servo uses the formula:
```
grip_cycle = (duty / 18.0) + 2.0
```

Where:
- **duty**: Input value (0-180 scale)
- **grip_cycle**: Actual PWM duty cycle
- **2.0**: Base offset for servo control

### Timing Control

- **Duration Parameters**: Precise control over movement time
- **Sleep Functions**: Accurate timing using Python's time module
- **Sequential Operations**: Chain multiple movements together

## 🚨 Important Notes

### Safety Considerations

- **Power Requirements**: Ensure adequate power supply for servo
- **GPIO Protection**: Use appropriate voltage levels (3.3V logic)
- **Physical Safety**: Keep hands clear during operation
- **Emergency Stop**: Use kill_gpios.py for immediate shutdown

### Limitations

- **Raspberry Pi Only**: Designed specifically for Raspberry Pi GPIO
- **Single Servo**: Currently controls one servo at a time
- **Fixed Pin**: Hardcoded to GPIO 18 (configurable in code)
- **Continuous Rotation**: Designed for LS-3006 continuous servos

### Best Practices

- **Calibration**: Test duty cycles for your specific servo
- **Power Management**: Use external power supply for servos
- **Error Handling**: Implement proper exception handling
- **GPIO Cleanup**: Always clean up GPIO pins after use

## 🚀 Production Deployment

For production use, consider:

1. **Multiple Servo Support** - Extend for multiple servos
2. **Web Interface** - Add remote control capabilities
3. **Safety Systems** - Implement emergency stop and limits
4. **Logging** - Add comprehensive operation logging
5. **Error Recovery** - Implement fault tolerance and recovery
6. **Calibration Tools** - Add servo calibration utilities

## 🔧 Customization

### Adding New Servo Types

Extend the system for different servo models:

```python
class CustomServo(Grip):
    def __init__(self, pin, frequency=50):
        self.pin = pin
        self.frequency = frequency
        # Custom initialization code
```

### Multiple Servo Control

Modify for controlling multiple servos:

```python
class MultiServo:
    def __init__(self, pins):
        self.servos = [Grip(pin) for pin in pins]
    
    def synchronized_move(self, operation, duration):
        # Control multiple servos simultaneously
```

### Web Interface

Add remote control capabilities:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/servo/<operation>')
def control_servo(operation):
    g = Grip()
    g.start(operation)
    return f"Servo {operation} operation completed"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly on actual hardware
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Servo Control! 🤖**
