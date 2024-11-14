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


if __name__ == "__main__":
    main()
