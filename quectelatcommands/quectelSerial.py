#!/usr/bin/env python3

import serial
import threading
import time


class QuectelSerial:
    def __init__(self, p_port: str, p_baudrate: int, p_timeout: int):
        """
        Initialize the QuectelSerial class.

        :param p_port: Serial port to connect to.
        :type p_port: str
        :param p_baudrate: Baudrate to use.
        :type p_baudrate: int
        :param p_timeout: Timeout for the serial connection.
        :type p_timeout: int
        """
        self.port = p_port
        self.baudrate = p_baudrate
        self.timeout = p_timeout

    def open(self):
        """
        Open the serial connection.
        """
        try:
            self.serial_conn = serial.Serial(
                self.port, self.baudrate, timeout=self.timeout
            )
            self.currentCommand = ""
            self.waitForResponse = False
            self.response = []
            self.receiveThreadAlive = True
            self.receiveThread = threading.Thread(target=self.readResponthThread)
            self.receiveThread.name = "SerialModemReceiveThread"
            self.receiveThread.start()
        except Exception as e:
            print(e)
            self.close()

    def readResponthThread(self):
        """
        Thread to read the response from the modem.
        """
        while self.receiveThreadAlive:
            try:
                line = self.serial_conn.readline().decode().strip()
                if line != "" and self.waitForResponse:
                    if line == "OK" or line == "ERROR":
                        self.waitForResponse = False

                    if line != self.currentCommand and self.waitForResponse == True:
                        self.response.append(line)

            except Exception as e:
                pass

    def sendCommand(self, p_command: str) -> tuple[bool, list[str]]:
        """
        Send an AT command to the modem and return the response.

        :param p_command: AT command to send.
        :type p_command: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """

        status = False
        response = []
        self.response = []
        self.currentCommand = p_command

        self.waitForResponse = True
        self.serial_conn.write((p_command + "\r\n").encode())

        timeout = 2
        while self.waitForResponse and timeout > 0:
            time.sleep(0.1)
            timeout -= 0.1

        if timeout <= 0:
            self.waitForResponse = False

        response = self.response
        if response:
            status = True

        return status, response

    def close(self):
        """
        Close the serial connection.
        """
        self.receiveThreadAlive = False
        self.serial_conn.close()
        self.receiveThread.join()
