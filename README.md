# downDetec
# Network Connectivity Monitor and Logger

This project aims to create a network connectivity monitor and logger using a microcontroller with network capabilities. The code provided here is written in MicroPython and can be run on compatible devices.

## Overview

The network connectivity monitor and logger continuously checks the connectivity status to a specified network or host and logs any changes in connectivity. It also provides a web interface to view the status log and adjust the refresh rate.

## Features

- Monitors network connectivity status
- Logs status changes with date and time
- Web interface to view status log and adjust refresh rate

## Requirements

- Microcontroller with network capabilities
- MicroPython firmware installed
- Network or host information stored in `.secret.env` file

## Installation

1. Clone or download the code from this repository.
2. Update the `.secret.env` file with your network or host information.
3. Transfer the code to your microcontroller.
4. Run the code using a MicroPython environment.

## Usage

1. Ensure that the microcontroller is connected to the network.
2. Access the web interface by navigating to the IP address of the microcontroller on port 80 in a web browser.
3. The web interface allows you to view the current status log and adjust the refresh rate for monitoring.
4. The status log displays the date and time of each status change, indicating whether the network connectivity is up or down.

## Limitations

- The code provided is a basic implementation and may require modifications or enhancements for specific use cases.
- The maximum refresh rate is 60 seconds, and the minimum is 1 second.
- The status log displays the last 10 status changes.

## Contributions

Contributions to this project are welcome. If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
