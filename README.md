# Quectel AT Commands Python Library

A Python library for interacting with Quectel modems and GNSS devices using AT commands. This package provides classes for managing and sending AT commands for modem and GNSS configurations, as well as command-line interfaces (CLIs) for quick access.

---

This package simplifies interaction with Quectel modems and GNSS modules by providing Python classes and CLI tools for managing configurations and sending AT commands.


## Modem source documentation
```
ECx00x&EG800K&EG810M&EG91xN&EG950A Series - AT Commands Manual
LTE Standard Module Series
Version: 1.3
Date: 2024-09-27
Status: Released
```

## Gnss source documentation
```
EC2x&EG9x&EG2x-G&EM05 Series - GNSS Application Note
LTE Standard Module Series
Version: 1.3
Date: 2020-09-04
Status: Released
```

## Source code organization :

Whether for modem or gnss, the class methods are numbered according to the chapters in the documentation.

```python
class QuectelModemATCommands:
    # Extract
    def generalCommands201DisplayProductIdentificationInformation(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 201: Display product identification information.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATI")
```

`generalCommands201DisplayProductIdentificationInformation` is the method name:

-  `generalCommands` is the chapter name in the documentation.
-  `201` corresponds to chapter 2.1 in the documentation.
-  `DisplayProductIdentificationInformation` is the title of the chapter in the documentation : "Display product identification information".


## Installation
Install the package using `pip`:

```bash
pip install quectelatcommands
```

## Usage

This package provides two main classes and corresponding CLI tools:

1. `QuectelModemATCommandsCLI`: For interacting with Quectel modems.
2. `QuectelGnssATCommandsCLI`: For GNSS (Global Navigation Satellite System) configurations.

### Python API

#### QuectelModemATCommands

This class allows you to send AT commands to a Quectel modem for various configurations and operations.

**Example:**

```python
from quectelatcommands import QuectelModemATCommands

# Initialize with default port and baudrate
modem = QuectelModemATCommands("/dev/ttyUSB2", 115200)

# Open connection
modem.open()

# Send a command to display product identification information
status, response = modem.generalCommands201DisplayProductIdentificationInformation()
print(response if status else "Error sending command")

# Close connection
modem.close()
```

**Available Methods in `QuectelModemATCommands`** (Examples):
- `generalCommands201DisplayProductIdentificationInformation`: Displays modem information.
- `packetDomainCommands1015PacketDataCounterWrite`: Configures packet data counters.
- `statusControlCommands40314RiSignalOutputCarrier`: Sets the RI signal output carrier type.

Refer to the class documentation for a full list of available AT commands.

#### QuectelGnssATCommands

This class provides GNSS-specific AT commands for configuring output ports, enabling or disabling NMEA sentence acquisition, and more.

**Example:**

```python
from quectelatcommands import QuectelGnssATCommands

# Initialize with default port and baudrate
gnss = QuectelGnssATCommands("/dev/ttyUSB1", 115200)

# Open connection
gnss.open()

# Configure the output port for NMEA sentences
status, response = gnss.configureGnss2201ConfigureOutputPortOfNmeaSentencesWrite("usbnmea")
print(response if status else "Error sending command")

# Close connection
gnss.close()
```

**Available Methods in `QuectelGnssATCommands`** (Examples):
- `configureGnss2201ConfigureOutputPortOfNmeaSentencesWrite`: Sets the output port for NMEA sentences.
- `configureGnssEnableDisableNmeaSentencesAcquisition`: Enables or disables NMEA sentence acquisition.

Refer to the class documentation for a complete list of available commands.

### Command-Line Interface (CLI)

The package provides two CLI commands, `modem-cli` and `gnss-cli`, for quick command execution without writing a script.

#### Modem CLI (`modem-cli`)


**Example Usage**:

```bash
quectelModemATCommandsCLI --help
```

Output:
```bash
Usage: quectelModemATCommandsCLI [OPTIONS] COMMAND [ARGS]...

  CLI for interacting with the Quectel modem via AT commands.

Options:
  -p, --port TEXT         Serial port to use.  [default: /dev/ttyUSB2]
  -b, --baudrate INTEGER  Baudrate to use.  [default: 115200]
  -t, --timeout INTEGER   Timeout for serial communication.  [default: 1]
  --help                  Show this message and exit.

Commands:
  call-related-commands           Group for call related commands.
  free-at-command                 Free AT command.
  general-command                 Group for general AT commands.
  hardware-related-commands       Group for hardware related commands.
  network-service-commands        Group for network services commands.
  packet-domain-commands          Group for packet domain commands.
  phonebook-commands              Group for phonebook commands.
  serial-interface-control        Group for serial interface control...
  short-message-service-commands  Group for short message service commands.
  sim-related-commands            Group for SIM related commands.
  status-control-commands         Group for status control commands.
```

#### GNSS CLI (`gnss-cli`)


**Example Usage**:

```bash
quectelGnssATCommandsCLI configure-gnss --help
```

Output:
```bash
Usage: quectelGnssATCommandsCLI configure-gnss [OPTIONS] COMMAND [ARGS]...

  Configure GNSS 20201.

Options:
  --help  Show this message and exit.

Commands:
  configure-agnss-positioning-protocols
                                  Configure AGNSS...
  configure-agps-positioning-mode
                                  Configure AGPS...
  configure-nmea-output-frequency
                                  Configure NMEA output...
  configure-odp-mode              Configure ODP mode.
  configure-output-port-of-nmea-sentences
                                  Configure output port...
  configure-output-type-of-beidou-nmea-sentences
                                  Configure output type...
  configure-output-type-of-galileo-nmea-sentences
                                  Configure output type...
  configure-output-type-of-glonass-nmea-sentences
                                  Configure output type...
  configure-output-type-of-gps-nmea
                                  Configure output type...
  configure-plane-mode-used-by-mo-agps-session
                                  Configure plane mode...
  configure-supl-protocol-version
                                  Configure SUPL...
  configure-supported-gnss-constellations
                                  Configure supported...
  enable-disable-acquisition-of-nmea-sentences
                                  Enable/disable...
  enable-disable-dpo-mode         Enable/disable DPO mode.
  enable-disable-gnss-extended-ggsv
                                  Enable/disable GNSS...
  enable-disable-gnss-to-run-automatically
                                  Enable/disable GNSS to...

```


## Requirements

This library requires the following dependencies:
- `pyserial`: For handling serial communication with the Quectel modem/GNSS devices.
- `click`: For building the command-line interfaces.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Additional Information

For more details on the AT commands used by this library, please refer to the official Quectel AT command documentation provided by Quectel for your specific modem or GNSS device model.

## Troubleshooting

If you encounter issues with serial communication:
- Ensure the correct permissions are set on the serial device (e.g., `/dev/ttyUSB2`).
- Verify the serial port and baud rate match those required by your Quectel device.


## Known Limitations
Given the large number of possible AT commands, the classes are not fully tested.
If you find bugs, don't hesitate to correct them by submitting a PR.

