#!/usr/bin/env python3

from typing import Optional
from .quectelSerial import QuectelSerial


class QuectelGnssATCommands:
    def __init__(
        self, p_port: str = "/dev/ttyUSB1", p_baudrate: int = 115200, p_timeout: int = 1
    ):
        """
        Quectel modem AT commands.
        """
        self.serialPort = QuectelSerial(p_port, p_baudrate, p_timeout)

    def open(self):
        """
        Open the serial connection.
        """
        self.serialPort.open()

    def sendCommand(self, p_command: str) -> tuple[bool, list[str]]:
        """
        Send an AT command to the modem and return the response.

        :param p_command: AT command to send.
        :type p_command: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """

        return self.serialPort.sendCommand(p_command)

    def close(self):
        """
        Close the serial connection.
        """
        self.serialPort.close()

    def freeAtCommand(self, p_command: str):
        """
        Free AT command.

        :param p_command: AT command to free.
        :type p_command: str
        """
        return self.sendCommand(p_command)

    def configureGnss2201ConfigureOutputPortOfNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2201: output port of NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="outport"')

    def configureGnss2201ConfigureOutputPortOfNmeaSentencesWrite(
        self, p_out_port: str
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2201: output port of NMEA sentences.

        :param p_out_port: String type. Configure the output port of NMEA sentences:

                    - **"none"**:  Close NMEA sentence output
                    - **"usbnmea"**:   Output via USB NMEA port
                    - **"uartdebug"**: Output via debug UART port
        :type p_out_port: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="outport","{p_out_port}"')

    def configureGnss2202EnableDisableAcquisitionOfNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2202: enable/disable acquisition of NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="nmeasrc"')

    def configureGnss2202EnableDisableAcquisitionOfNmeaSentencesWrite(
        self, p_nmea_src: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2202: enable/disable acquisition of NMEA sentences.

        :param p_nmea_src:  Integer type. If enabled, original NMEA sentences can be acquired via
                            AT+QGPSGNMEA. Meanwhile, sentences are outputted via the AT port as a return value:

                            - **0**: Disable
                            - **1**: Enablee
        :type p_nmea_src: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="nmeasrc",{p_nmea_src}')

    def configureGnss2203ConfigureOutputTypeOfGpsNmeaRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2203: Read the output type of GPS NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gpsnmeatype"')

    def configureGnss2203ConfigureOutputTypeOfGpsNmeaWrite(
        self, p_gps_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2203: Configure the output type of GPS NMEA sentences.

        :param p_gps_nmea_type:  Integer type. Configure the output type of GPS NMEA sentences:

                                - **0**: Disable
                                - **1**: GPGGA
                                - **2**: GPRMC
                                - **4**: GPGSV
                                - **8**: GPGSA
                                - **16**: GPVTG
                                - **31**: All the five types of sentences

        :type p_gps_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gpsnmeatype",{p_gps_nmea_type}')

    def configureGnss2204ConfigureOutputTypeOfGlonassNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2204: Read the output type of GLONASS NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="glnmeatype"')

    def configureGnss2204ConfigureOutputTypeOfGlonassNmeaSentencesWrite(
        self, p_glonass_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2204: Configure the output type of GLONASS NMEA sentences.

        :param p_glonass_nmea_type: Integer type. Configure output type of GLONASS NMEA sentences in ORed:

                        - **0**: Disable
                        - **1**: GLGSV
                        - **2**: GNGSA
                        - **4**: GNGNS

        :type p_glonass_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="glonassnmeatype",{p_glonass_nmea_type}')

    def configureGnss2205ConfigureOutputTypeOfGalileoNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2205: Read the output type of Galileo NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="galileonmeatype"')

    def configureGnss2205ConfigureOutputTypeOfGalileoNmeaSentencesWrite(
        self, p_galileo_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2205: Configure the output type of Galileo NMEA sentences.

        :param p_galileo_nmea_type: Integer type. Configure output type of Galileo NMEA sentences in ORed:

                        - **0**: Disable
                        - **1**: GAGSV

        :type p_galileo_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="galileonmeatype",{p_galileo_nmea_type}')

    def configureGnss2206ConfigureOutputTypeOfBeidouNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2206: Read the output type of Beidou NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="beidounmeatype"')

    def configureGnss2206ConfigureOutputTypeOfBeidouNmeaSentencesWrite(
        self, p_beidou_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2206: Configure the output type of Beidou NMEA sentences.

        :param p_beidou_nmea_type: Integer type. Configure output type of Beidou NMEA sentences in ORed:

                            - **0**: Disable
                            - **1**: PQGSA
                            - **2**: PQGSV

        :type p_beidou_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="beidounmeatype",{p_beidou_nmea_type}')

    def configureGnss2207ConfigureSupportedGnssConstellationsRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2207: Read the supported GNSS constellations.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gnssconfig"')

    def configureGnss2207ConfigureSupportedGnssConstellationsWrite(
        self, p_gnss_config: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 2207: Configure the supported GNSS constellations.

        :param p_gnss_config: Integer type. Supported GNSS constellations. GPS is always ON:

                        - **0**: GLONASS OFF/BeiDou OFF/Galileo OFF
                        - **1**: GLONASS ON/BeiDou ON/Galileo ON
                        - **2**: GLONASS ON/BeiDou ON/Galileo OFF
                        - **3**: GLONASS ON/BeiDou OFF/Galileo ON
                        - **4**: GLONASS ON/BeiDou OFF/Galileo OFF
                        - **5**: GLONASS OFF/BeiDou ON/Galileo ON
                        - **6**: GLONASS OFF/BeiDou OFF/Galileo ON
                        - **7**: GLONASS OFF/BeiDou ON/Galileo OFF

        :type p_gnss_config: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gnssconfig",{p_gnss_config}')


import click


@click.group()
@click.pass_context
@click.option(
    "--port",
    "-p",
    default="/dev/ttyUSB2",
    help="Serial port to use.",
    show_default=True,
)
@click.option(
    "--baudrate", "-b", default=115200, help="Baudrate to use.", show_default=True
)
@click.option(
    "--timeout",
    "-t",
    default=1,
    help="Timeout for serial communication.",
    show_default=True,
)
def main(ctx, port, baudrate, timeout):
    """CLI for interacting with the Quectel modem via AT commands."""
    ctx.ensure_object(dict)
    client = QuectelGnssATCommands(port, baudrate, timeout)
    ctx.obj["client"] = client


@main.command("free-at-command")
@click.pass_context
@click.option(
    "--command",
    "-c",
    type=str,
    required=True,
    help="AT command to free.",
)
def free_at_command(ctx, c: str):
    """Free AT command."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.freeAtCommand(c)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def configure_gnss(ctx):
    """Configure GNSS 2201."""
    pass


@configure_gnss.group()
@click.pass_context
def configure_output_port_of_nmea_sentences(ctx):
    """Configure output port of NMEA sentences."""
    pass


@configure_output_port_of_nmea_sentences.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the output port of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss2201ConfigureOutputPortOfNmeaSentencesRead()
    print(response if status else "Error")
    client.close()


@configure_output_port_of_nmea_sentences.command("write")
@click.pass_context
@click.option(
    "--out-port",
    "-o",
    type=str,
    required=True,
    help="""
Configure the output port of NMEA sentences:

                    - **"none"**:  Close NMEA sentence output
                    - **"usbnmea"**:   Output via USB NMEA port
                    - **"uartdebug"**: Output via debug UART port
""",
)
def write(ctx, o: str):  # type: ignore[reportRedeclaration]
    """Write the output port of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss2201ConfigureOutputPortOfNmeaSentencesWrite(
        o
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def enable_disable_acquisition_of_nmea_sentences(ctx):
    """Enable/disable acquisition of NMEA sentences."""
    pass


@enable_disable_acquisition_of_nmea_sentences.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the acquisition of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2202EnableDisableAcquisitionOfNmeaSentencesRead()
    )
    print(response if status else "Error")
    client.close()


@enable_disable_acquisition_of_nmea_sentences.command("write")
@click.pass_context
@click.option(
    "--nmea-src",
    "-n",
    type=int,
    required=True,
    help="""
If enabled, original NMEA sentences can be acquired via AT+QGPSGNMEA. Meanwhile, sentences are outputted via the AT port as a return value:

                            - **0**: Disable
                            - **1**: Enablee
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write the acquisition of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2202EnableDisableAcquisitionOfNmeaSentencesWrite(n)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_output_type_of_gps_nmea(ctx):
    """Configure output type of GPS NMEA."""
    pass


@configure_output_type_of_gps_nmea.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the output type of GPS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss2203ConfigureOutputTypeOfGpsNmeaRead()
    print(response if status else "Error")
    client.close()


@configure_output_type_of_gps_nmea.command("write")
@click.pass_context
@click.option(
    "--gps-nmea-type",
    "-g",
    type=int,
    required=True,
    help="""
Configure the output type of GPS NMEA sentences:

                                - **0**: Disable
                                - **1**: GPGGA
                                - **2**: GPRMC
                                - **4**: GPGSV
                                - **8**: GPGSA
                                - **16**: GPVTG
                                - **31**: All the five types of sentences     
""",
)
def write(ctx, g: int):  # type: ignore[reportRedeclaration]
    """Write the output type of GPS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss2203ConfigureOutputTypeOfGpsNmeaWrite(g)
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_output_type_of_glonass_nmea_sentences(ctx):
    """Configure output type of GLONASS NMEA."""
    pass


@configure_output_type_of_glonass_nmea_sentences.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the output type of GLONASS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2204ConfigureOutputTypeOfGlonassNmeaSentencesRead()
    )
    print(response if status else "Error")
    client.close()


@configure_output_type_of_glonass_nmea_sentences.command("write")
@click.pass_context
@click.option(
    "--glonass-nmea-type",
    "-g",
    type=int,
    required=True,
    help="""
Configure output type of GLONASS NMEA sentences in ORed:

                        - **0**: Disable
                        - **1**: GLGSV
                        - **2**: GNGSA
                        - **4**: GNGNS
""",
)
def write(ctx, g: int):  # type: ignore[reportRedeclaration]
    """Write the output type of GLONASS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2204ConfigureOutputTypeOfGlonassNmeaSentencesWrite(g)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_output_type_of_galileo_nmea_sentences(ctx):
    """Configure output type of Galileo NMEA."""
    pass


@configure_output_type_of_galileo_nmea_sentences.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the output type of Galileo NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2205ConfigureOutputTypeOfGalileoNmeaSentencesRead()
    )
    print(response if status else "Error")
    client.close()


@configure_output_type_of_galileo_nmea_sentences.command("write")
@click.pass_context
@click.option(
    "--galileo-nmea-type",
    "-g",
    type=int,
    required=True,
    help="""
Configure output type of Galileo NMEA sentences in ORed:

                        - **0**: Disable
                        - **1**: GAGSV
""",
)
def write(ctx, g: int):  # type: ignore[reportRedeclaration]
    """Write the output type of Galileo NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2205ConfigureOutputTypeOfGalileoNmeaSentencesWrite(g)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_output_type_of_beidou_nmea_sentences(ctx):
    """Configure output type of Beidou NMEA."""
    pass


@configure_output_type_of_beidou_nmea_sentences.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the output type of Beidou NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2206ConfigureOutputTypeOfBeidouNmeaSentencesRead()
    )
    print(response if status else "Error")
    client.close()


@configure_output_type_of_beidou_nmea_sentences.command("write")
@click.pass_context
@click.option(
    "--beidou-nmea-type",
    "-b",
    type=int,
    required=True,
    help="""
Configure output type of Beidou NMEA sentences in ORed:

                            - **0**: Disable
                            - **1**: PQGSA
                            - **2**: PQGSV
""",
)
def write(ctx, b: int):  # type: ignore[reportRedeclaration]
    """Write the output type of Beidou NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2206ConfigureOutputTypeOfBeidouNmeaSentencesWrite(b)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_supported_gnss_constellations(ctx):
    """Configure supported GNSS constellations."""
    pass


@configure_supported_gnss_constellations.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the supported GNSS constellations."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2207ConfigureSupportedGnssConstellationsRead()
    )
    print(response if status else "Error")
    client.close()


@configure_supported_gnss_constellations.command("write")
@click.pass_context
@click.option(
    "--gnss-config",
    "-g",
    type=int,
    required=True,
    help="""
Supported GNSS constellations. GPS is always ON:

                        - **0**: GLONASS OFF/BeiDou OFF/Galileo OFF
                        - **1**: GLONASS ON/BeiDou ON/Galileo ON
                        - **2**: GLONASS ON/BeiDou ON/Galileo OFF
                        - **3**: GLONASS ON/BeiDou OFF/Galileo ON
                        - **4**: GLONASS ON/BeiDou OFF/Galileo OFF
                        - **5**: GLONASS OFF/BeiDou ON/Galileo ON
                        - **6**: GLONASS OFF/BeiDou OFF/Galileo ON
                        - **7**: GLONASS OFF/BeiDou ON/Galileo OFF
""",
)
def write(ctx, g: int):  # type: ignore[reportRedeclaration]
    """Write the supported GNSS constellations."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss2207ConfigureSupportedGnssConstellationsWrite(g)
    )
    print(response if status else "Error")
    client.close()


if __name__ == "__main__":
    main()
