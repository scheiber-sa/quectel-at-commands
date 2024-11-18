#!/usr/bin/env python3

from typing import Optional
from quectelatcommands.quectelSerial import QuectelSerial


class QuectelModemATCommands:
    def __init__(
        self, p_port: str = "/dev/ttyUSB2", p_baudrate: int = 115200, p_timeout: int = 1
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

    def generalCommands201DisplayProductIdentificationInformation(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 201: Display product identification information.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATI")

    def generalCommands202RequestManufacturerIdentification(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 202: Request manufacturer identification.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+GMI")

    def generalCommands203RequestTaModelIdentification(self) -> tuple[bool, list[str]]:
        """
        General commands 203: Request TA model identification.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+GMM")

    def generalCommands204RequestTaRevisionIdentificationSoftwareRelease(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 204: Request TA revision identification of software release.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+GMR")

    def generalCommands205RequestManufacturerIdentification(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 205: Request manufacturer identification.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGMI")

    def generalCommands206RequestModelIdentification(self) -> tuple[bool, list[str]]:
        """
        General commands 206: Request model identification.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGMM")

    def generalCommands207RequestTaRevisionIdentificationOfSoftwareRelease(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 207: Request TA revision identification of software release.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGMR")

    def generalCommands208RequestIMEI(self) -> tuple[bool, list[str]]:
        """
        General commands 208: Request IMEI.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+GSN")

    def generalCommands209InternationalMobileEquipmentIdentity(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 209: International Mobile Equipment Identity.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGSN")

    def generalCommands210ResetAtCommandSettingsToFactoryDefaults(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 210: Reset AT command settings to factory defaults.

        :param p_value: Integer type. Range: 0–1 :

            - **0**:           Reset AT command settings to factory defaults.
            - **1**:           Reset AT command settings to factory defaults and reset the device.

        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT&F{p_value}")

    def generalCommands211DisplayCurrentConfiguration(self) -> tuple[bool, list[str]]:
        """
        General commands 211: Display current configuration.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT&V")

    def generalCommands212StoreCurrentParametersToUserDefinedProfile(
        self, p_profileNb: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 212: Store current parameters to user-defined profile.

        :param p_profileNb: Integer type. Range: 0–9.
        :type p_profileNb: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT&W{p_profileNb}")

    def generalCommands213SetAllCurrentParametersToUserDefinedProfile(
        self, p_profileNb: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 213: Set all current parameters to user-defined profile.

        :param p_profileNb: Integer type. Range: 0–9.
        :type p_profileNb: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATZ{p_profileNb}")

    def generalCommands214SetResultCodePresentationMode(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 214: Set result code presentation mode.

        :param p_n: Integer type. Range: 0–1:

            - **0**:       Disable result code presentation.
            - **1**:       Enable result code presentation.
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATQ{p_n}")

    def generalCommands215SetResponseFormat(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 215: Set response format.

        :param p_value: Integer type. Range: 0–1:

            - **0**:       Numeric response format.
            - **1**:       Verbose response format.
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATV{p_value}")

    def generalCommands216SetCommandEchoMode(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 216: Set command echo mode.

        :param p_value: Integer type. Range: 0–1:

            - **0**:       Disable command echo.
            - **1**:       Enable command echo.
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATE{p_value}")

    def generalCommands217SetCommandLineTerminationCharacterRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 217: Set command line termination character.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATS3?")

    def generalCommands217SetCommandLineTerminationCharacterWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 217: Set command line termination character.

        :param p_n: Integer type. Range: 0–127.
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATS3={p_n}")

    def generalCommands218SetResponseFormattingCharacterRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 218: Set response formatting character.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATS4?")

    def generalCommands218SetResponseFormattingCharacterWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 218: Set response formatting character.

        :param p_n: Integer type. Range: 0–127.
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATS4={p_n}")

    def generalCommands219SetCommandLineEditingCharacterRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        General commands 219: Set command line editing character.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATS5?")

    def generalCommands219SetCommandLineEditingCharacterWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 219: Set command line editing character.

        :param p_n: Integer type. Range: 0–127.
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """

        return self.sendCommand(f"ATS5={p_n}")

    def generalCommands220SetConnectResultFormatAndMonitorCallInProgress(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 220: Set connect result format and monitor call in progress.

        :param p_value: Integer type. Range: 0–4:

            - **0**:       CONNECT result code returned only. Dial tone and busy detection are both disabled.
            - **1**:       CONNECT<text> result code returned only. Dial tone and busy detection are both disabled.
            - **2**:       CONNECT<text> result code returned. Dial tone detection is enabled, while busy detection is disabled.
            - **3**:       CONNECT<text> result code returned. Dial tone detection is disabled, while busy detection is enabled.
            - **4**:       CONNECT<text> result code returned. Both dial tone and busy detection are both enabled.
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATX{p_value}")

    def generalCommands221SetPhoneFunctionalityRead(self) -> tuple[bool, list[str]]:
        """
        General commands 221: Set phone functionality.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CFUN?")

    def generalCommands221SetPhoneFunctionalityWrite(
        self, p_fun: int, p_rst: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 221: Set phone functionality.

        :param p_fun: Integer type. Range: 0–5:

            - **0**:       Minimum functionality
            - **1**:       Full functionality
            - **3**:       Disable the ME from receiving RF signals
            - **4**:       Disable the ME from both transmitting and receiving RF signals
            - **5**:       Disable (U)SIM
        :type p_fun: int
        :param p_rst: Integer type. Range: 0–1:

            - **0**:       Do not reset the ME before setting it to <fun> functionality level.(This is the default setting when <rst> is not given.)
            - **1**:       Reset the ME. The device is fully functional after the reset. This value is available only for <fun> = 1.
        :type p_rst: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        command = f"AT+CFUN={p_fun}"
        if p_rst is not None:
            command += f",{p_rst}"
        return self.sendCommand(command)

    def generalCommands222ErrorMessageFormatRead(self) -> tuple[bool, list[str]]:
        """
        General commands 222: Error message format.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CMEE?")

    def generalCommands222ErrorMessageFormatWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 222: Error message format.

        :param p_n: Integer type. Range: 0–2:

            - **0**:       Disable result code
            - **1**:       Enable result code with numeric values
            - **2**:       Enable result code with verbose values
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CMEE={p_n}")

    def generalCommands223SelectCharacterSetRead(self) -> tuple[bool, list[str]]:
        """
        General commands 223: Select character set.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSCS?")

    def generalCommands223SelectCharacterSetWrite(
        self, p_chset: str
    ) -> tuple[bool, list[str]]:
        """
        General commands 223: Select character set.

        :param p_chset: String type. Character set:

            - **"GSM"** :  GSM default alphabet
            - **"IRA"** :  International reference Alphabet
            - **"UCS2"** :  UCS2 alphabet
        :type p_chset: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CSCS="{p_chset}"')

    def generalCommands224ConfigureUrcIndicationRead(self) -> tuple[bool, list[str]]:
        """
        General commands 224: Configure URC indication.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QURCCFG='urcport'")

    def generalCommands224ConfigureUrcIndicationWrite(
        self, p_urc_port: Optional[str] = None
    ) -> tuple[bool, list[str]]:
        """
        General commands 224: Configure URC indication.

        :param p_urc_port: String type. Set URC output port:

            - **"usbat"** :  USB AT port
            - **"usbmodem"** :  USB modem port
            - **"uart1"** :  Main UART port
        :type p_urc_port: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        command = "AT+QURCCFG"
        if p_urc_port is not None:
            command += f'="urcport","{p_urc_port}"'
        return self.sendCommand(command)

    def generalCommands225TerminatePppConnection(
        self, p_option: int
    ) -> tuple[bool, list[str]]:
        """
        General commands 225: Terminate PPP connection.

        :param p_option: Integer type. The operation about dropping PPP connection:

            - **0**:       Hang up PPP connection without sending TERM REQ frame to peer.
            - **1**:       Hang up PPP connection and automatically send TERM REQ frame to peer.
            - **2**:       Hang up PPP connection with sending TERM REQ frame to peer.
        :type p_option: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QPPPDROP={p_option}")

    def serialInterfaceControlCommands301SetDcdFunctionMode(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        Serial interface control commands 301: Set DCD function mode.

        :param p_value: Integer type. Determines how the state of circuit (DCD) relates to the detection of received line signal from the distant end:

            - **0**:       DCD function is always ON
            - **1**:       DCD function is ON only in the presence of data carrier
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT&C{p_value}")

    def serialInterfaceControlCommands302SetDtrFunctionMode(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        Serial interface control commands 302: Set DTR function mode.

        :param p_value: Integer type. Determines the behavior of the DTR signal:

            - **0**:       TA ignores status on DTR
            - **1**:       Low→High on DTR: Change to command mode while remaining the connected call
            - **2**:       Low→High on DTR: Disconnect data call and change to command mode. When DTR is at high level, auto-answer function is disabled
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT&D{p_value}")

    def serialInterfaceControlCommands303SetTeTaLocalDataFlowControlRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Serial interface control commands 303: Set TE-TA local data flow control.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+IFC?")

    def serialInterfaceControlCommands303SetTeTaLocalDataFlowControlWrite(
        self, p_dce_by_dte: int, p_dte_by_dce: int
    ) -> tuple[bool, list[str]]:
        """
        Serial interface control commands 303: Set TE-TA local data flow control.

        :param p_dce_by_dte: Integer type. Specifies the method that will be used by TE when receiving data from TA:

            - **0**:       None
            - **2**:       RTS flow control
        :type p_dce_by_dte: int
        :param p_dte_by_dce: Integer type. Specifies the method that will be used by TA when receiving data from TE:

            - **0**:       None
            - **2**:       CTS flow control
        :type p_dte_by_dce: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+IFC={p_dce_by_dte},{p_dte_by_dce}")

    def serialInterfaceControlCommands304SetTeTaFixedLocalRateRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Serial interface control commands 304: Set TE-TA fixed local rate.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+IPR?")

    def serialInterfaceControlCommands304SetTeTaFixedLocalRateWrite(self, p_rate: int):
        """
        Serial interface control commands 304: Set TE-TA fixed local rate.

        :param p_rate: Integer type. Baud rate per second on the serial port. Unit: bps:

            - **0** :       Adaptive baud rate
            - **4800**
            - **9600**
            - **19200**
            - **38400**
            - **57600**
            - **115200**
            - **230400**
            - **460800**
            - **921600**
        :type p_rate: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+IPR={p_rate}")

    def statusControlCommands40100QueryMobileEquipmentActivityStatus(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40100: Query mobile equipment activity status.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CPAS")

    def statusControlCommands40200ReportExtendedError(self) -> tuple[bool, list[str]]:
        """
        Status control commands 40200: Report extended error.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CEER")

    def statusControlCommands40300ConfigureExtendedSettings(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40300: Configure extended settings.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QCFG=?")

    def statusControlCommands40301ConfigureGprsAttachMode(
        self, p_attach_mode: int, p_effect: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40301: Configure GPRS attach mode.

        :param p_attach_mode: Integer type. The mode to attach GRPS when UE is powered on:

            - **0**:       Manual attach
            - **1**:       Auto attach
        :type p_attach_mode: int
        :param p_effect: Integer format. When to take effect:

            - **0**:       Take effect after UE reboots (currently not supported)
            - **1**:       Take effect immediately
        :type p_effect: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='gprsattach',{p_attach_mode},{p_effect}")

    def statusControlCommands40302ConfigureNetworkSearchMode(
        self, p_scan_mode: int
    ) -> tuple[bool, list[str]]:
        """
        CStatus control commands 40302: Configure network search mode.

        :param p_scan_mode: Integer type. Network searching mode:

            - **0**:       Automatic (LTE/WCDMA/GSM)
            - **1**:       GSM only
            - **2**:       WCDMA only
            - **3**:       LTE only
        :type p_scan_mode: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='nwscanmode',{p_scan_mode}")

    def statusControlCommands40303ConfigureNetworkSearchingSequence(
        self, p_scanseq: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40303: Configure network searching sequence.

        :param p_scanseq: Integer type. Network searching sequence:

            - **0**:       Automatic (LTE/WCDMA/GSM)
            - **1**:       GSM only
            - **2**:       WCDMA only
            - **3**:       LTE only
            - **4**:       GSM/WCDMA/LTE
            - **5**:       WCDMA/GSM/LTE
            - **6**:       LTE/WCDMA
            - **7**:       LTE/GSM
            - **8**:       WCDMA/LTE
            - **9**:       WCDMA/GSM
            - **10**:      GSM/LTE
            - **11**:      GSM/WCDMA
            - **12**:      LTE/WCDMA/GSM
        :type p_scanseq: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='nwscanseq',{p_scanseq}")

    def statusControlCommands40304ConfigureRelevantFunctionsInRoamingState(
        self, p_roam_modeex: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40304: Configure relevant functions in roaming state.

        :param p_roam_modeex: Integer type. Roaming operating mode. Range: 0–3:

            - **0**:       Normal operating mode, unlimited service
            - **Bit 1**:   Disable dial-up internet access function when UE is in roaming state
            - **Bit 2**:   Disable voice call function when UE is in roaming state
        :type p_roam_modeex: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='roamserviceex',{p_roam_modeex}")

    def statusControlCommands40305ConfigureServiceDomain(
        self, p_service: int, p_effect: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40305: Configure service domain.

        :param p_service: Integer type. Service domain of UE:

            - **0**:       CS only
            - **1**:       PS only
            - **2**:       CS & PS
        :type p_service: int
        :param p_effect: Integer format. When to take effect:

            - **0**:       Take effect after UE reboots (currently not supported)
            - **1**:       Take effect immediately
        :type p_effect: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='servicedomain',{p_service},{p_effect}")

    def statusControlCommands40306ConfigureBand(
        self, p_bandval: int, p_ltebandval: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40306: Configure band.

        :param p_bandval: Integer type. A hexadecimal value that specifies the GSM and WCDMA frequency band:

            - **0x00**:           No change
            - **0x01**:           GSM900
            - **0x02**:           GSM1800
            - **0x10**:           WCDMA 2100
            - **0x20**:           WCDMA 1900
            - **0x40**:           WCDMA 850
            - **0x80**:           WCDMA 900
            - **0xFFFF** :         Any frequency band
        :type p_bandval: int
        :param p_ltebandval: Integer type. A hexadecimal value that specifies the LTE frequency band:

            - **0x1**: (CM_BAND_PREF_LTE_EUTRAN_BAND1)                     LTE B1
            - **0x2**: (CM_BAND_PREF_LTE_EUTRAN_BAND2)                     LTE B2
            - **0x4**: (CM_BAND_PREF_LTE_EUTRAN_BAND3)                     LTE B3
            - **0x8**: (CM_BAND_PREF_LTE_EUTRAN_BAND4)                     LTE B4
            - **0x10**: (CM_BAND_PREF_LTE_EUTRAN_BAND5)                    LTE B5
            - **0x40**: (CM_BAND_PREF_LTE_EUTRAN_BAND7)                    LTE B7
            - **0x80**: (CM_BAND_PREF_LTE_EUTRAN_BAND8)                    LTE B8
            - **0x80000**: (CM_BAND_PREF_LTE_EUTRAN_BAND20)                LTE B20
            - **0x8000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND28)              LTE B28
            - **0x40000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND31)             LTE B31
            - **0x200000000**:(CM_BAND_PREF_LTE_EUTRAN_BAND34)             LTE B34
            - **0x2000000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND38)           LTE B38
            - **0x4000000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND39)           LTE B39
            - **0x8000000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND40)           LTE B40
            - **0x10000000000**: (CM_BAND_PREF_LTE_EUTRAN_BAND41)          LTE B41
            - **0x20000000000000000** : (CM_BAND_PREF_LTE_EUTRAN_BAND66)    LTE B66
            - **0x800000000000000000** : (CM_BAND_PREF_LTE_EUTRAN_BAND72)   LTE B72
            - **0x7FFFFFFFFFFFFFFFF** : (CM_BAND_PREF_ANY)                  Any frequency band
        :type p_ltebandval: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='band',{p_bandval},0x{p_ltebandval:X}")

    def statusControlCommands40307SpecifyRiBehaviorWhenOtherUrcsArePresented(
        self, p_typeRI: str, p_pulse_duration: int, p_pulse_count: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40307: Specify RI behavior when other URCs are presented.

        :param p_typeRI: String type. RI behavior when URCs are presented:

            - **"off"** :       No change. Ring indicator keeps inactive
            - **"pulse"** :     Pulse. Pulse width determined by <pulse_duration>
        :type p_typeRI: str
        :param p_pulse_duration: Integer type. The width of pulse. This parameter is effect only when <typeRI> is''pulse''. Range: 5–2000. Default value: 120. Unit: ms.
        :type p_pulse_duration: int
        :param p_pulse_count: Integer type. The count of pulse. This parameter is only meaningful when <typeRI> is ''pulse''. The interval time between two pulses is equal to <pulse_duration>. Range: 1–5. Default value: 1. Unit: s.
        :type p_pulse_count: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+QCFG="urc/ri/other","{p_typeRI}",{p_pulse_duration},{p_pulse_count}'
        )

    def statusControlCommands40308SetDelayTimeOfUrcIndication(
        self, p_time: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40308: Set delay time of URC indication.

        :param p_time: Integer type. Set the delay time of URC indication when ring indicator pulse starts. Range: 0–120. Unit: ms:

           - **0** :       No delay.
        :type p_time: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='urcdelay',{p_time}")

    def statusControlCommands40309EnableDisableUrcCacheFunction(
        self, p_enable: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40309: Enable/disable URC cache function.

        :param p_enable: Integer type. Enable/disable URC cache function:

            - **0** :       Disable URC cache function.
            - **1** :       Enable URC cache function.
        :type p_enable: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='urc/cache',{p_enable}")

    def statusControlCommands40310ConfigureTheNetworkCardTypeInterface(
        self, p_net: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40310: Configure the network card type interface.

        :param p_net: Integer type. The protocol of net port:

            - **1** :       ECM interface
            - **3** :       RNIDS interface
        :type p_net: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='usbnet',{p_net}")

    def statusControlCommands40311EnableDisableThePppTermFrameSending(
        self, p_flag: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40311: Enable/disable the PPP TERM frame sending.

        :param p_flag: Integer type:

            - **0** :       Disable TERM frame sending when hang up PPP by module itself.
            - **1** :       Enable TERM frame sending when hang up PPP by module itself.
        :type p_flag: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='ppp/termframe',{p_flag}")

    def statusControlCommands40312EnableDisableAirplaneModeControlViaW_DISABLE(
        self, p_enable: int, p_status: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40312: Enable/disable airplane mode control via W_DISABLE#.

        :param p_enable: Integer type. Enable/disable the airplane mode control via W_DISABLE# pin:

            - **0** :       Disable the airplane mode control via W_DISABLE# pin
            - **1** :       Enable the airplane mode control via W_DISABLE# pin. The module enters airplane mode when W_DISABLE# pin is active and exit airplane mode when it is inactive. AT+CFUN=1 is not allowed to be used to enable the module to exit airplane mode when the W_DISABLE# pin is active. Unsolicited result code +QIND: airplanestatus,<status> is reported when the status of W_DISABLE# pin changes
        :type p_enable: int
        :param p_status: Integer type:

            - **0** :       Exit airplane mode
            - **1** :       Enter airplane mode
        :type p_status: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='airplanecontrol',{p_enable},{p_status}")

    def statusControlCommands40313RingLineBehaviorOfRing(
        self, p_typeRI: str, p_pulse_duration: int, p_pulse_count: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40313: Ring line behavior of ring.

        :param p_typeRI: String type. The behavior of the ring line when URCs are presented:

            - **"off"** :       No change. Ring line keeps inactive.
            - **"pulse"** :     Pulse. Pulse width is determined by <pulse_duration>
        :type p_typeRI: str
        :param p_pulse_duration: Integer type. The width of pulse. This parameter is meaningful only when <typeRI> is ''pulse''. If this parameter is not needed, you can set it to null. Range: 5–2000. Default value: 120. Unit: ms.
        :type p_pulse_duration: int
        :param p_pulse_count: Integer type. The count of pulse. This parameter is meaningful only when <typeRI> is ''pulse''. The interval time between two pulse is equal to <pulse_duration>. Range: 1–5. Default value: 1.
        :type p_pulse_count: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+QCFG="urc/ri/ring","{p_typeRI}",{p_pulse_duration},{p_pulse_count}'
        )

    def statusControlCommands40314RiSignalOutputCarrier(
        self, p_ri_signal_type: str
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40314: RI signal output carrier.

        :param p_ri_signal_type: String type. RI signal output carrier.

            **"respective"**: The ring indicator behaves on the port where URC is presented.

            For example:

                - If a URC is presented on the UART port, it is a physical ring indicator.
                - If the URC is presented on the USB port, it is a virtual ring indicator.
                - If the URC is presented on the USB AT port, and the port does not support a ring indicator,
                    there will be no ring indicator.

            Use ``AT+QURCCFG="urcport"`` to get the port on which URC is presented.

            **"physical"**: Regardless of which port URC is presented on, only the physical ring indicator is used.

        :type p_ri_signal_type: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QCFG="risignaltype","{p_ri_signal_type}"')

    def statusControlCommands40315ConfigureBaudRate(
        self, p_ipr: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40315: Configure baud rate.

        :param p_ipr: Integer type. Baud rate per second on the serial port. Unit: bps:

            - **4800**
            - **9600**
            - **19200**
            - **38400**
            - **57600**
            - **115200**
            - **230400**
            - **460800**
            - **921600**
        :type p_ipr: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='uart2ipr',{p_ipr}")

    def statusControlCommands40316ConfigureWorkingModeOfNic(
        self, p_nat: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40316: Configure working mode of NIC.

        :param p_nat: Integer type. The working mode of NIC:

            - **0** :       Routing mode
            - **1** :       NIC mode
        :type p_nat: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='nat',{p_nat}")

    def statusControlCommands40317ConfigureImsFunction(
        self, p_ims_conf: int, p_voltecap: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40317: Configure IMS function.

        :param p_ims_conf: Integer type. IMS function configuration:

            - **0** :       IMS function is not configured
            - **1** :       Enable IMS function
            - **2** :       Disable IMS function
        :type p_ims_conf: int
        :param p_voltecap: Integer type. Whether VoLTE is supported:

            - **0** :       VoLTE is not supported
            - **1** :       VoLTE is supported
        :type p_voltecap: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='ims', {p_ims_conf},{p_voltecap}")

    def statusControlCommands40318ConfigureConnectionExpirationTimeInHttpFota(
        self, p_timeout: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40318: Configure connection expiration time in HTTP FOTA.

        :param p_timeout: Integer type. The connection expiration time in HTTP FOTA download. Range: 10–180. Default value: 60. Unit: second.
        :type p_timeout: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCFG='fota/times',{p_timeout}")

    def statusControlCommands40400ControlUrcIndication(
        self, p_urctype: str, p_enable: int, p_savetonvram: int
    ) -> tuple[bool, list[str]]:
        """
        Status control commands 40400: Control URC indication.

        :param p_urctype: String type. The type of URC:

            - **"all"** :           Main switch of all URCs. Default is ON.
            - **"csq"** :           Indication of signal strength and channel bit error rate change (similar to AT+CSQ). Default is OFF. If this configuration is ON, present: +QIND: "csq",<rssi>,<ber>
            - **"datastatus"** :    Indication of data service status. Default is OFF. If this configuration is ON, present: +QIND: "datastatus",<suspended>,<reason> <reason> is number format as below: 0 SUSPEND_NO_CAUSE 1 SUSPEND_BY_RAU_ATTACH 2 SUSPEND_BY_LAU 3 SUSPEND_BY_TAU 4 SUSPEND_BY_CS_SERVICE 5 SUSPEND_BY_DS_OPERATION 6 SUSPEND_BY_POWERUP
            - **"mode"** :          Indication of network main mode and sub mode. Default is OFF. If this configuration is ON, present: ^MODE:<main_mode>,<sub_mode> <main_mode> is an integer type listed as below: 0 SYSINFO_SYSTEMO_MODE_NO_SERVICE 1 SYSINFO_SYSTEMO_MODE_RESERVED_1 2 SYSINFO_SYSTEMO_MODE_RESERVED_2 3 SYSINFO_SYSTEMO_MODE_GSM_GPRS 5 SYSINFO_SYSTEMO_MODE_WCDMA 17 SYSINFO_SYSTEMO_MODE_LTE <sub_mode> is an integer type listed as below: 0 SYSINFO_SYSTEMO_SUBMODE_NO_SERVICE 1 SYSINFO_SYSTEMO_SUBMODE_GSM 3 SYSINFO_SYSTEMO_SUBMODE_GSM_EGPRS 5 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSDPA 6 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSUPA 7 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSPA 8 SYSINFO_SYSTEMO_SUBMODE_UTRAN 17 SYSINFO_SYSTEMO_SUBMODE_EUTRAN
            - **"smsfull"** :       SMS storage full indication. Default is OFF. If this configuration is ON, present: +QIND: "smsfull",<storage>
            - **"smsincoming"** :   Incoming message indication. Default is ON. Related URC list: +CMTI, +CMT, +CDS
            - **"act"** :           Indication of network access technology change. Default is OFF. If this configuration is ON, present: +QIND: "act",<actvalue> <actvalue> is string format. The values are as below: ''GSM'' ''EGPRS'' ''WCDMA'' ''HSDPA'' ''HSUPA'' ''HSDPA&HSUPA'' ''LTE'' ''UNKNOWN'' The examples of URC are as below: +QIND: "act","HSDPA&HSUPA" +QIND: "act","UNKNOWN" The description of ''act'' is as below: 1. If module does not register on network, <actvalue> would be ''UNKNOWN''. 2. If this configuration is ON, the URC of "act" will be reported immediately. Only when the network access technology changes, a new URC will be reported.
            - **"sqi"** :           Indication of reference signal receiving power, reference signal receiving quality and signal to interference plus noise ratio change. Default is OFF. If this configuration is ON, present: +QIND: "SQI",<RSRP>,<RSRQ>,<SINR> <RSRP> Integer type. Reference signal receiving power. Unit: dBm. (See 3GPP 36.214 Chapter 5.1.1). <RSRQ> Integer type. Reference signal receiving quality. Unit: dB. (See 3GPP 36.214 Chapter 5.1.3). <SINR> Integer type. Signal to interference plus noise ratio. Range: -20–30. Unit: dB.
            - **"phonebook"** :     Incoming phonebook indication. Default is ON. Related URC list: +QIND: PB DONE
            - **"ring"** :          Incoming call indication. Default is ON. Related URC list: RING
            - **"nocarrier"** :     Incoming hang up call indication. Default is ON. Related URC list: NO CARRIER
        :type p_urctype: str
        :param p_enable: Integer type. URC indication is ON or OFF:

            - **0** :       OFF
            - **1** :       ON
        :type p_enable: int
        :param p_savetonvram: Integer type. Save the configuration to NVRAM:

            - **0** :       Do not save the configuration to NVRAM
            - **1** :       Save the configuration to NVRAM
        :type p_savetonvram: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QINDCFG="{p_urctype}",{p_enable},{p_savetonvram}')

    def simRelatedCommands501RequestInternationalMobileSubscriberIdentity(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 501: Request International Mobile Subscriber Identity.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CIMI")

    def simRelatedCommands502FacilityLock(
        self, p_fac: str, p_mode: int, p_passwd: str, p_class: int, p_status: int
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 502: Facility lock.

        :param p_fac: String type. The facility to lock:

            - **"SC"** :        (U)SIM (lock SIM/UICC card installed in the currently selected card slot)
            - **"AO"** :        BAOC (Bar All Outgoing Calls) (see 3GPP TS 22.088 clause 1)
            - **"OI"** :        BOIC (Bar Outgoing International Calls) (see 3GPP TS 22.088 clause 1)
            - **"OX"** :        BOIC-exHC (Bar Outgoing International Calls except to Home Country) (see 3GPP TS 22.088 clause 1)
            - **"AI"** :        BAIC (Bar All Incoming Calls) (see 3GPP TS 22.088 clause 2)
            - **"IR"** :        BIC-Roam (Bar Incoming Calls when Roaming outside the home country) (see 3GPP TS 22.088 clause 2)
            - **"AB"** :        All Barring services (see 3GPP TS 22.030) (applicable only for <mode>=0)
            - **"AG"** :        All outgoing barring services (see 3GPP TS 22.030) (applicable only for <mode>=0)
            - **"AC"** :        All incoming barring services (see 3GPP TS 22.030) (applicable only for <mode>=0)
            - **"FD"** :        (U)SIM card or active application in the UICC (GSM or USIM) fixed dialing memory feature (If PIN2 authentication has not been done during the current session, PIN2 is required as <passwd>)
            - **"PF"** :        Lock Phone to the very first inserted SIM/UICC card (also referred in the present document as PH-FSIM) (MT asks password when other SIM/UICC cards are inserted)
            - **"PN"** :        Network Personalization (see 3GPP TS 22.022)
            - **"PU"** :        Network Subset Personalization (see 3GPP TS 22.022)
            - **"PP"** :        Service Provider Personalization (see 3GPP TS 22.022)
            - **"PC"** :        Corporate Personalization (see 3GPP TS 22.022)
        :type p_fac: str
        :param p_mode: Integer type. The mode of the facility lock:

            - **0** :       Unlock
            - **1** :       Lock
            - **2** :       Query status
        :type p_mode: int
        :param p_passwd: String type. Password.
        :type p_passwd: str
        :param p_class: Integer type. The class of the facility lock:

            - **1** :       Voice
            - **2** :       Data
            - **4** :       FAX
            - **7** :       All telephony except SMS
            - **8** :       Short message service
            - **16** :      Data circuit synchronization
            - **32** :      Data circuit asynchronization
        :type p_class: int
        :param p_status: Integer type. The status of the facility lock:

            - **0** :       Off
            - **1** :       On
        :type p_status: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CLCK="{p_fac}",{p_mode},"{p_passwd}",{p_class},{p_status}'
        )

    def simRelatedCommands503EnterPin(
        self, p_code: str, p_pin: str, p_newpin: str
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 503: Enter PIN.

        :param p_code: String type. The code of the SIM card:

            - **"READY"**
            - **"SIM PIN"**
            - **"SIM PUK"**
            - **"SIM PIN2"**
            - **"SIM PUK2"**
            - **"PH-NET PIN"**
            - **"PH-NET PUK"**
            - **"PH-NETSUB PIN"**
            - **"PH-NETSUB PUK"**
            - **"PH-SP PIN"**
            - **"PH-SP PUK"**
            - **"PH-CORP PIN"**
            - **"PH-CORP PUK"**
        :type p_code: str
        :param p_pin: String type. The PIN of the SIM card.
        :type p_pin: str
        :param p_newpin: String type. A new password required if the requested code is a PUK.
        :type p_newpin: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CPIN="{p_code}","{p_pin}","{p_newpin}"')

    def simRelatedCommands504ChangePassword(
        self, p_fac: str, p_pwdlength: int, p_oldpwd: str, p_newpwd: str
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 504: Change password.

        :param p_fac: String type. The facility to lock:

                    - **"SC"**: (U)SIM (lock SIM/UICC card)
                    - **"AO"**: BAOC (Bar All Outgoing Calls, see 3GPP TS 22.088 clause 1)
                    - **"OI"**: BOIC (Bar Outgoing International Calls, see 3GPP TS 22.088 clause 1)
                    - **"OX"**: BOIC-exHC (Bar Outgoing International Calls except to Home Country, see 3GPP TS 22.088 clause 1)
                    - **"AI"**: BAIC (Bar All Incoming Calls, see 3GPP TS 22.088 clause 2)
                    - **"IR"**: BIC-Roam (Bar Incoming Calls when Roaming outside the home country, see 3GPP TS 22.088 clause 2)
                    - **"AB"**: All barring services (see 3GPP TS 22.030, applicable only for <mode>=0)
                    - **"AG"**: All outgoing barring services (see 3GPP TS 22.030, applicable only for <mode>=0)
                    - **"AC"**: All incoming barring services (see 3GPP TS 22.030, applicable only for <mode>=0)
                    - **"P2"**: (U)SIM PIN2
        :type p_fac: str

        :param p_pwdlength: Integer type. Maximum length of password.
        :type p_pwdlength: int

        :param p_oldpwd: String type. Password specified for the facility from the user interface or with command.
        :type p_oldpwd: str

        :param p_newpwd: String type. New password.
        :type p_newpwd: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CPWD="{p_fac}",{p_pwdlength},"{p_oldpwd}","{p_newpwd}"'
        )

    def simRelatedCommands505GenericUsimAccess(
        self, p_length: int, p_command: str
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 505: Generic (U)SIM access.

        :param p_length: Integer type. Length of <command> or <response> string.
        :type p_length: int
        :param p_command: String type. Command transferred by the MT to the (U)SIM in the format as described in 3GPP TS 51.011.
        :type p_command: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CRSM={p_length},"{p_command}"')

    def simRelatedCommands506RestrictedUsimAccess(
        self,
        p_command: int,
        p_filed: int,
        p_p1: int,
        p_p2: int,
        p_p3: int,
        p_data: int,
        p_pathId: int,
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 506: Restricted (U)SIM access.

        :param p_command: Integer type. (U)SIM command number:

            - **176** :     READ BINARY
            - **178** :     READ RECORD
            - **192** :     GET RESPONSE
            - **214** :     UPDATE BINARY
            - **220** :     UPDATE RECORD
            - **242** :     STATUS
        :type p_command: int
        :param p_filed: Integer type. Identifier for an elementary data file on (U)SIM, if used by <command>.
        :type p_filed: int
        :param p_p1: Integer type. Parameters transferred by the MT to the (U)SIM. These parameters are mandatory for every command, except GET RESPONSE and STATUS. The values are described in 3GPP TS 51.011. Information which shall be written to the (U)SIM (hexadecimal character format; see AT+CSCS).
        :type p_p1: int
        :param p_p2: Integer type. Parameters transferred by the MT to the (U)SIM. These parameters are mandatory for every command, except GET RESPONSE and STATUS. The values are described in 3GPP TS 51.011. Information which shall be written to the (U)SIM (hexadecimal character format; see AT+CSCS).
        :type p_p2: int
        :param p_p3: Integer type. Parameters transferred by the MT to the (U)SIM. These parameters are mandatory for every command, except GET RESPONSE and STATUS. The values are described in 3GPP TS 51.011. Information which shall be written to the (U)SIM (hexadecimal character format; see AT+CSCS).
        :type p_p3: int
        :param p_data: Integer type. Information which shall be written to the (U)SIM (hexadecimal character format; see AT+CSCS).
        :type p_data: int
        :param p_pathId: Integer type. The directory path of an elementary file on a UICC in hexadecimal format.
        :type p_pathId: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f"AT+CRSM={p_command},{p_filed},0x{p_p1:X},0x{p_p2:X},0x{p_p3:X},0x{p_data:X},0x{p_pathId:X}"
        )

    def simRelatedCommands507ShowIccid(self) -> tuple[bool, list[str]]:
        """
        Sim related commands 507: Show ICCID.


        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QCCID")

    def simRelatedCommands508DisplayPinRemainderCounterRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 508: Display PIN remainder counter.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QPINC?")

    def simRelatedCommands508DisplayPinRemainderCounterWrite(
        self, p_facility: str
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 508: Display PIN remainder counter.

        :param p_facility: String type. The facility to lock:

            - **"SC"** :        (U)SIM PIN
            - **"P2"** :        (U)SIM PIN2
        :type p_facility: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QPINC="{p_facility}"')

    def simRelatedCommands509QueryInitializationStatusOfUsimCard(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 509: Query initialization status of (U)SIM card.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QINISTAT")

    def simRelatedCommands510UsimCardDetectionRead(self) -> tuple[bool, list[str]]:
        """
        Sim related commands 510: (U)SIM card detection.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QSIMDET?")

    def simRelatedCommands510UsimCardDetectionWrite(
        self, p_enable: int, p_insert_level: int
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 510: (U)SIM card detection.

        :param p_enable: Integer type. Enable or disable (U)SIM card detection:

            - **0** :       Disable
            - **1** :       Enable
        :type p_enable: int
        :param p_insert_level: Integer type. The level of (U)SIM detection pin when a (U)SIM card is inserted:

            - **0** :       Low level
            - **1** :       High level
        :type p_insert_level: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QSIMDET={p_enable},{p_insert_level}")

    def simRelatedCommands511UsimCardInsertionStatusReportRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 511: (U)SIM card insertion status report.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QSIMSTAT?")

    def simRelatedCommands511UsimCardInsertionStatusReportWrite(self, p_enable: int):
        """
        Sim related commands 511: (U)SIM card insertion status report.

        :param p_enable: Integer type. Enable or disable (U)SIM card insertion status report:

            - **0** :       Disable
            - **1** :       Enable
        :type p_enable: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QSIMSTAT={p_enable}")

    def simRelatedCommands512SelectUsimCardRead(self) -> tuple[bool, list[str]]:
        """
        Sim related commands 512: Select (U)SIM card.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QDSIM")

    def simRelatedCommands512SelectUsimCardWrite(
        self, p_sim_id: int
    ) -> tuple[bool, list[str]]:
        """
        Sim related commands 512: Select (U)SIM card.

        :param p_sim_id: Integer type. (U)SIM card ID:

            - **0** :       SIM1
            - **1** :       SIM2
        :type p_sim_id: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QDSIM={p_sim_id}")

    def networkServiceCommands601OperatorSelectionRead(self) -> tuple[bool, list[str]]:
        """
        Network service commands 6010: Operator selection read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+COPS?")

    def networkServiceCommands601OperatorSelectionWrite(
        self, p_mode: int, p_format: int, p_operator: str, p_act: int
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 6010: Operator selection write.

        :param p_mode: Integer type. The mode of the operator selection:

            - **0** :       Automatic mode. <oper> field is ignored
            - **1** :       Manual operator selection. <oper> field shall be present and <Act> optionally
            - **2** :       Manually deregister from network
            - **3** :       Set only <format> (for AT+COPS? Read Command), and do not attempt registration/deregistration (<oper> and <Act> fields are ignored). This value is invalid in the response of Read Command.
            - **4** :       Manual/automatic selection. <oper> field shall be presented. If manual selection fails, automatic mode (<mode>=0) is entered
        :type p_mode: int
        :param p_format: Integer type. The format of the operator:

            - **0** :       Long format alphanumeric <oper> which can be up to 16 characters long
            - **1** :       Short format alphanumeric <oper>
            - **2** :       Numeric <oper>. GSM location area identification number
        :type p_format: int
        :param p_operator: String type. Operator in format as per <format>.
        :type p_operator: str
        :param p_act: Integer type. Access technology selected:

            - **0** :       GSM
            - **2** :       UTRAN
            - **3** :       GSM W/EGPRS
            - **4** :       UTRAN W/HSDPA
            - **5** :       UTRAN W/HSUPA
            - **6** :       UTRAN W/HSDPA and HSUPA
            - **7** :       E-UTRAN
            - **8** :       UTRAN HSPA+
        :type p_act: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+COPS={p_mode},{p_format},"{p_operator}",{p_act}')

    def networkServiceCommands602DomainNetworkRegistrationStatusRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 602: Domain network registration status read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CREG?")

    def networkServiceCommands602DomainNetworkRegistrationStatusWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 602: Domain network registration status write.

        :param p_n: Integer type. The mode of the network registration unsolicited result code:

            - **0** :       Disable network registration unsolicited result code
            - **1** :       Enable network registration unsolicited result code: +CREG: <stat>
            - **2** :       Enable network registration unsolicited result code with location information: +CREG: <stat>[,<lac>,<ci>[,<Act>]]
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CREG={p_n}")

    def networkServiceCommands603SignalQualityReport(self) -> tuple[bool, list[str]]:
        """
        Network service commands 603: Signal quality report.


        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSQ")

    def networkServiceCommands604PreferredOperatorListRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 604: Preferred operator list read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CPOL?")

    def networkServiceCommands604PreferredOperatorListWrite(
        self,
        p_index: int,
        p_format: int,
        p_oper: str,
        p_gsm: int,
        p_gsm_compact: int,
        p_utran: int,
        p_e_utran: int,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 604: Preferred operator list write.

        :param p_index: Integer type. The order number of operator in the (U)SIM preferred operator list.
        :type p_index: int
        :param p_format: Integer type:

            - **0** :       Long format alphanumeric <oper>
            - **1** :       Short format alphanumeric <oper>
            - **2** :       Numeric <oper>
        :type p_format: int
        :param p_oper: String type. <format> indicates the format is alphanumeric or numeric (see AT+COPS).
        :type p_oper: str
        :param p_gsm: Integer type. GSM access technology:

            - **0** :       Access technology is not selected
            - **1** :       Access technology is selected
        :type p_gsm: int
        :param p_gsm_compact: Integer type. GSM compact access technology:

            - **0** :       Access technology is not selected
            - **1** :       Access technology is selected
        :type p_gsm_compact: int
        :param p_utran: Integer type. UTRAN access technology:

            - **0** :       Access technology is not selected
            - **1** :       Access technology is selected
        :type p_utran: int
        :param p_e_utran: Integer type. E-UTRAN access technology:

            - **0** :       Access technology is not selected
            - **1** :       Access technology is selected
        :type p_e_utran: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CPOL={p_index},{p_format},"{p_oper}",{p_gsm},{p_gsm_compact},{p_utran},{p_e_utran}'
        )

    def networkServiceCommands605ReadOperatorNames(self) -> tuple[bool, list[str]]:
        """
        Network service commands 605: Read operator names.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+COPN")

    def networkServiceCommands606AutomaticTimeZoneUpdateRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 606: Automatic time zone update read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CTZU?")

    def networkServiceCommands606AutomaticTimeZoneUpdateWrite(
        self, p_onoff: int
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 606: Automatic time zone update write.

        :param p_onoff: Integer type. The mode of automatic time zone update:

            - **0** :       Disable automatic time zone update via NITZ.
            - **1** :       Enable automatic time zone update via NITZ and update GMT time to URC
            - **3** :       Enable automatic time zone update via NITZ and update LOCAL time to RTC
        :type p_onoff: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CTZU={p_onoff}")

    def networkServiceCommands607TimeZoneReportingRead(self) -> tuple[bool, list[str]]:
        """
        Network service commands 607: Time zone reporting read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CTZR?")

    def networkServiceCommands607TimeZoneReportingWrite(
        self, p_reporting: int
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 607: Time zone reporting write.

        :param p_reporting: Integer type. The mode of time zone reporting:

            - **0** :       Disable time zone reporting of changed event
            - **1** :       Enable time zone reporting of changed event by unsolicited result code: +CTZV: <tz>
            - **2** :       Enable extended time zone reporting by unsolicited result code: +CTZE: <tz>,<dst>,<time>
        :type p_reporting: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CTZR={p_reporting}")

    def networkServiceCommands608ObtainTheLatestTimeSynchronizedThroughNetwork(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 608: Obtain the latest time synchronized through network.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QLTS")

    def networkServiceCommands609QueryNetworkInformation(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Network service commands 609: Query network information.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QNWINFO")

    def callRelatedCommands701AnswerAnIncomingCall(self) -> tuple[bool, list[str]]:
        """
        Call related commands 701: Answer an incoming call.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATA")

    def callRelatedCommands702MobileOriginatedCallToDialANumber(
        self, p_n: str, p_mgsm: str
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 702: Mobile originated call to dial a number.

        :param p_n: String of dialing digits and optionally V.25ter modifiers.
            Dialing digits: 0–9, \\*, #, +, A, B, C
            Following V.25ter modifiers are ignored: ,(comma), T, P, !, W, @
        :type p_n: str
        :param p_mgsm: String of GSM modifiers:

            - **I** :   Activate CLIR (Disable presentation of own number to the called party)
            - **i** :   Deactivate CLIR (Enable presentation of own number to the called party)
            - **G** :   Activate closed user group invocation for this call only
            - **g** :   Deactivate closed user group invocation for this call only
        :type p_mgsm: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'ATD"{p_n}""{p_mgsm}";')

    def callRelatedCommands703ConnectedLineIdentificationPresentationRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 703: Connected line identification presentation read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+COLP?")

    def callRelatedCommands703ConnectedLineIdentificationPresentationWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 703: Connected line identification presentation write.

        :param p_n: Integer type. Sets/shows the result code presentation status in the TA:

            - **0** :       Disable
            - **1** :       Enable
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+COLP={p_n}")

    def callRelatedCommands704DisconnectExistingConnection(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 704: Disconnect existing connection.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATH")

    def callRelatedCommands705HangUpVoiceCall(self) -> tuple[bool, list[str]]:
        """
        Call related commands 705: Hang up voice call.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CHUP")

    def callRelatedCommands706SwitchFromDataModeToCommandMode(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 706: Switch from data mode to command mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("+++")

    def callRelatedCommands707SwitchFromCommandModeToDataMode(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 707: Switch from command mode to data mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATO")

    def callRelatedCommands708SetNumberOfRingsBeforeAutomaticAnsweringRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 708: Set number of rings before automatic answering read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("ATS0")

    def callRelatedCommands708SetNumberOfRingsBeforeAutomaticAnsweringWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 708: Set number of rings before automatic answering write.

        :param p_n: Integer type. This parameter setting determines the number of rings before automatic answering:

            - **0** :       Automatic answering is disabled
            - **1–255** :   Enable automatic answering on the ring number specified
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"ATS0={p_n}")

    def callRelatedCommands709ListCurrentCallsOfMe(self) -> tuple[bool, list[str]]:
        """
        Call related commands 709: List current calls of ME.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CLCC")

    def callRelatedCommands710CallStatusIndicationRead(self) -> tuple[bool, list[str]]:
        """
        Call related commands 710: Call status indication read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT^DSCI?")

    def callRelatedCommands710CallStatusIndicationWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Call related commands 710: Call status indication write.

        :param p_n: Integer type. The mode of the call status indication:

            - **0** :       Disable call status indication
            - **1** :       Enable call status indication
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT^DSCI={p_n}")

    def phonebookCommands801SubscriberNumber(self) -> tuple[bool, list[str]]:
        """
        Phonebook commands 801: Subscriber number.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CNUM")

    def phonebookCommands802FindPhonebookEntries(
        self, p_findtext: str
    ) -> tuple[bool, list[str]]:
        """
        Phonebook commands 802: Find phonebook entries.

        :param p_findtext: String type field of maximum length <tlength> in current TE character set specified by AT+CSCS.
        :type p_findtext: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CPBF="{p_findtext}"')

    def phonebookCommands803ReadPhonebookEntries(
        self, p_index: int
    ) -> tuple[bool, list[str]]:
        """
        Phonebook commands 803: Read phonebook entries.

        :param p_index: Integer type. Value in the range of location numbers of phonebook memory.
        :type p_index: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CPBR={p_index}")

    def phonebookCommands804SelectPhonebookMemoryStorageRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Phonebook commands 804: Select phonebook memory storage read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CPBS?")

    def phonebookCommands804SelectPhonebookMemoryStorageWrite(
        self, p_storage: str
    ) -> tuple[bool, list[str]]:
        """
        Phonebook commands 804: Select phonebook memory storage write.

        :param p_storage: String type:

            - **"SM"** :              (U)SIM phonebook
            - **"DC"** :              ME dialed calls list (AT+CPBW may not be applicable to this storage)
            - **"FD"** :              (U)SIM fix dialing-phone book (AT+CPBW operation need the authority of PIN2)
            - **"LD"** :              (U)SIM last-dialing-phone book (AT+CPBW may not be applicable to this storage)
            - **"EN"** :              (U)SIM (or ME) emergency number (AT+CPBW may not be applicable to this storage)
            - **"ON"** :              (U)SIM own numbers (MSISDNs) list
            - **"AP"** :              Selected application phonebook. If a UICC with an active USIM application is present, the application phonebook, DFPHONEBOOK under ADFUSIM is selected
            - **"SDN"** :             Service Dialing Number
        :type p_storage: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CPBS="{p_storage}"')

    def phonebookCommands805WritePhonebookEntry(
        self, p_index: int, p_number: str, p_type: int, p_text: str
    ) -> tuple[bool, list[str]]:
        """
        Phonebook commands 805: Write phonebook entry.

        :param p_index: Integer type. Value in the range of location numbers of phonebook memory. If <index> is not given, the first free entry will be used. If <index> is given as the only parameter, the phonebook entry specified by location is deleted.
        :type p_index: int
        :param p_number: String type. Phone number in format specified by <type>.
        :type p_number: str
        :param p_type: Integer type. Type of address of octet (see 3GPP TS 24.008 subclause 10.5.4.7 for details):

            - **129** :             Unknown type (IDSN format)
            - **145** :             International number type (ISDN format)
            - **161** :             National type
        :type p_type: int
        :param p_text: String type field of maximum length <tlength> in current TE character set specified by AT+CSCS.
        :type p_text: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CPBW={p_index},"{p_number}",{p_type},"{p_text}"')

    def shortMessageServiceCommands901SelectMessageServiceRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 901: Select message service read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSMS?")

    def shortMessageServiceCommands901SelectMessageServiceWrite(
        self, p_service: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 901: Select message service write.

        :param p_service: Integer type. Type of message service:

            - **0** :       3GPP TS 23.040 and 3GPP TS 23.041 (the syntax of SMS AT commands is compatible with 3GPP TS 27.005 Phase 2 version 4.7.0; Phase 2+ features which do not require new command syntax may be supported, e.g. correct routing of messages with new Phase 2+ data coding schemes)
            - **1** :       3GPP TS 23.040 and 3GPP TS 23.041 (the syntax of SMS AT commands is compatible with 3GPP TS 27.005 Phase 2+ version; the requirement of <service> setting 1 is mentioned under corresponding command descriptions)
        :type p_service: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CSMS={p_service}")

    def shortMessageServiceCommands902MessageFormatRead(self) -> tuple[bool, list[str]]:
        """
        Short message service commands 902: Message format read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CMGF?")

    def shortMessageServiceCommands902MessageFormatWrite(
        self, p_mode: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 902: Message format write.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CMGF={p_mode}")

    def shortMessageServiceCommands903ServiceCenterAddressRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 903: Service center address read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSCA?")

    def shortMessageServiceCommands903ServiceCenterAddressWrite(
        self, p_sca: str, p_tosca: str
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 903: Service center address write.

        :param p_sca: Service center address. 3GPP TS 24.011 RP SC address Address-Value field in string format; BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007). The type of address is given by <tosca>.
        :type p_sca: str
        :param p_tosca: Type of service center address. 3GPP TS 24.011 RP SC address Type-of-Address octet in integer format (default see <toda>).
        :type p_tosca: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CSCA="{p_sca}","{p_tosca}"')

    def shortMessageServiceCommands904PreferredMessageStorageRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 904: Preferred message storage read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CPMS?")

    def shortMessageServiceCommands904PreferredMessageStorageWrite(
        self, p_mem1: str, p_mem2: str, p_mem3: str
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 904: Preferred message storage write.

        :param p_mem1: Messages to be read and deleted from this memory storage:

            - **"SM"** :            (U)SIM message storage
            - **"ME"** :            Mobile equipment message storage
        :type p_mem1: str
        :param p_mem2: Messages will be written and sent to this memory storage:

            - **"SM"** :            (U)SIM message storage
            - **"ME"** :            Mobile equipment message storage
        :type p_mem2: str
        :param p_mem3: Received messages will be placed in this memory storage if routing to PC is not set (AT+CNMI):

            - **"SM"** :            (U)SIM message storage
            - **"ME"** :            Mobile equipment message storage
        :type p_mem3: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CPMS="{p_mem1}","{p_mem2}","{p_mem3}"')

    def shortMessageServiceCommands905DeleteMessage(
        self, p_index: int, p_delflag: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 905: Delete message.

        :param p_index: Integer type. Value in the range of location numbers supported by the associated memory.
        :type p_index: int
        :param p_delflag: Integer type:

            - **0** :       Delete the message specified in <index>
            - **1** :       Delete all read messages from <mem1> storage
            - **2** :       Delete all read messages from <mem1> storage and sent mobile originated messages
            - **3** :       Delete all read messages, sent and unsent mobile originated messages from <mem1> storage
            - **4** :       Delete all messages from <mem1> storage
        :type p_delflag: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CMGD={p_index},{p_delflag}")

    def shortMessageServiceCommands906ListMessagesGetAll(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 906: List messages get all.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CMGL")

    def shortMessageServiceCommands906ListMessagesQuery(
        self, p_stat: str
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 906: List messages query.

        :param p_stat: String type. In text mode:

            - **"REC UNREAD"** :        Received unread messages
            - **"REC READ"** :          Received read messages
            - **"STO UNSENT"** :        Stored unsent messages
            - **"STO SENT"** :          Stored sent messages
            - **"ALL"** :               All messages
        :type p_stat: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CMGL="{p_stat}"')

    def shortMessageServiceCommands907ReadMessage(
        self, p_index: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 907: Read message.

        :param p_index: Integer type. Value in the range of location numbers supported by the associated memory.
        :type p_index: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CMGR={p_index}")

    def shortMessageServiceCommands908SendMessagesTextMode(
        self, p_da: str, p_toda: int, p_text: str
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 908: Send messages text mode.

        :param p_da: Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007). The type of address is given by <toda>.
        :type p_da: str
        :param p_toda: Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet in integer format.
        :type p_toda: int
        :param p_text: String type. Message content.
        :type p_text: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CMGS="{p_da}",{p_toda}\r{p_text}\x1A')

    def shortMessageServiceCommands908SendMessagesPduMode(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 908: Send messages PDU mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return False, ["Not implemented"]

    def shortMessageServiceCommands909SendMoreMessagesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 909: Send more messages read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CMMS?")

    def shortMessageServiceCommands909SendMoreMessagesWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 909: Send more messages write.

        :param p_n: Integer type:

            - **0** :       Feature disabled
            - **1** :       Keep enabled until the time between the response of the latest message send command (AT+CMGS, AT+CMSS, etc.) and the next send command exceeds 1–5 seconds (the exact value is up to ME implementation), and then ME shall close the link and TA switches <n> back to 0 automatically.
            - **2** :       Feature enabled (If the time between the response of the latest message send command and the next send command exceeds 1-5 seconds (the exact value is up to ME implementation), ME shall close the link but TA will not switch <n> back to 0 automatically).
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CMMS={p_n}")

    def shortMessageServiceCommands910WriteMessageToMemoryTextMode(
        self,
        p_da: str,
        p_oa: str,
        p_tooa: int,
        p_toda: int,
        p_stat: str,
        p_text: str,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 910: Write message to memory text mode.

        :param p_da: Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007). The type of address is given by <toda>.
        :type p_da: str
        :param p_oa: Originating address. 3GPP TS 23.040 TP-Originating-Address Address-Value field in string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007). The type of address is given by <tooa>.
        :type p_oa: str
        :param p_tooa: Type of originating address. 3GPP TS 24.011 TP-Originating-Address Type-of-Address octet in integer format.
        :type p_tooa: int
        :param p_toda: Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet in integer format.
        :type p_toda: int
        :param p_stat: PDU mode        Text mode       Explanation:

            - **0** :               **"REC UNREAD"** :  Received unread messages
            - **1** :               **"REC READ"** :  Received read messages
            - **2** :               **"STO UNSENT"** :  Stored unsent messages
            - **3** :               **"STO SENT"** :  Stored sent messages
            - **4** :               **"ALL** :  All messages
        :type p_stat: str
        :param p_text: String type. Message content.
        :type p_text: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CMGW="{p_da}/{p_oa}",{p_tooa}/{p_toda},"{p_stat}"\r{p_text}\x1A'
        )

    def shortMessageServiceCommands910WriteMessageToMemoryPduMode(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 910: Write message to memory PDU mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return False, ["Not implemented"]

    def shortMessageServiceCommands911SendMessageFromStorage(
        self, p_index: int, p_da: str, p_toda: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 911: Send message from storage.

        :param p_index: Integer type. Value in the range of location numbers supported by the associated memory.
        :type p_index: int
        :param p_da: Destination Address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS command in 3GPP TS 27.007). The type of address is given by <toda>.
        :type p_da: str
        :param p_toda: Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet in integer format.
        :type p_toda: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CMSS={p_index},"{p_da}",{p_toda}')

    def shortMessageServiceCommands912NewMessageAcknowledgementToUeTeExecute(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 912: New message acknowledgement to UE/TE execute.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CNMA")

    def shortMessageServiceCommands912NewMessageAcknowledgementToUeTeWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 912: New message acknowledgement to UE/TE write.

        :param p_n: Integer type:

            - **0** :       Command operates similarly as in text mode
            - **1** :       Send positive (RP-ACK) acknowledgement to the network. Accepted only in PDU mode
            - **2** :       Send negative (RP-ERROR) acknowledgement to the network. Accepted only in PDU mode
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CNMA={p_n}")

    def shortMessageServiceCommands913SmsEventReportingConfigurationRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 913: SMS event reporting configuration read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CNMI?")

    def shortMessageServiceCommands913SmsEventReportingConfigurationWrite(
        self, p_mode: int, p_mt: int, p_bm: int, p_ds: int, p_bfr: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 913: SMS event reporting configuration write.

        :param p_mode: Integer type:

            - **0** :       Buffer unsolicited result codes in the TA. If TA result code buffer is full, indications can be buffered in some other place or the oldest indications may be discarded and replaced with the new received indications.
            - **1** :       Discard indication and reject new received message unsolicited result codes when TA-TE link is reserved (e.g. in on-line data mode). Otherwise forward them directly to the TE.
            - **2** :       Buffer unsolicited result codes in the TA when TA-TE link is reserved (e.g. in data mode) and flush them to the TE after reservation. Otherwise forward them directly to the TE.
        :type p_mode: int
        :param p_mt: Integer type. The rules for storing received SMS depend on its data coding scheme (see GPPTS 23.038) and preferred memory storage (AT+CPMS) setting, and the value is:

            - **0** :       No SMS-DELIVER indications are routed to the TE
            - **1** :       If SMS-DELIVER is stored into ME/TA, indication of the memory location is routed to the TE by using unsolicited result code: +CMTI: <mem>,<index>
            - **2** :       SMS-DELIVERs (except class 2) are routed directly to the TE using unsolicited result code: +CMT: [<alpha>],<length><CR><LF><pdu> (PDU mode enabled) or +CMT:<oa>,[<alpha>],<scts>[,<tooa>,<fo>,<pid>,<dcs>,<sca>,<tosca>,<length>]<CR><LF><data> (text mode enabled; about the parameters in italics, see AT+CSDH) or ^HCMT: <oa>,<scts>,<lang>,<fmt>,<length>,<prt>,<prv>,<type>,<stat><CR><LF><data> (text mode for CDMA SMS). Class 2 messages result in indication as defined in <mt>=1
            - **3** :       Class 3 SMS-DELIVERs are routed directly to TE by using unsolicited result codes defined in <mt>=2. Messages of other classes result in indication as defined in <mt>=1
        :type p_mt: int
        :param p_bm: Integer type. The rules for storing received CBMs depend on its data coding scheme (see 3GPP TS 23.038) and the setting of Select CBM Types (AT+CSCB), and the value is:

            - **0** :       No CBM indications are routed to the TE
            - **2** :       New CBMs are routed directly to the TE using unsolicited result code: +CBM:   <length><CR><LF><pdu>   (PDU mode); or +CBM: <sn>,<mid>,<dcs>,<page>,<pages><CR><LF><data> (text mode)
        :type p_bm: int
        :param p_ds: Integer type:

            - **0** :       No SMS-STATUS-REPORTs are routed to the TE
            - **1** :       SMS-STATUS-REPORTs are routed to the TE using unsolicited result code: +CDS: <length><CR><LF><pdu> (PDU mode) +CDS: <fo>,<mr>,[<ra>],[<tora>],<scts>,<dt>,<st> (text mode)
            - **2** :       If SMS-STATUS-REPORT is stored into ME/TA, indication of the memory location is routed to the TE using unsolicited result code: +CDSI: <mem>,<index>
        :type p_ds: int
        :param p_bfr: Integer type:

            - **0** :       TA buffer of unsolicited result codes defined within this command is flushed to the TE when <mode> 1 or 2 is entered (OK response shall be given before flushing the codes)
            - **1** :       TA buffer of unsolicited result codes defined within this command is cleared when <mode> 1 or 2 is entered
        :type p_bfr: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CNMI={p_mode},{p_mt},{p_bm},{p_ds},{p_bfr}")

    def shortMessageServiceCommands914SelectCellBroadcastMessageTypesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 914: Select cell broadcast message types read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSCB?")

    def shortMessageServiceCommands914SelectCellBroadcastMessageTypesWrite(
        self, p_mode: int, p_mids: str, p_dcss: str
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 914: Select cell broadcast message types write.

        :param p_mode: Integer type:

            - **0** :       Message types specified in <mids> and <dcss> are accepted
            - **1** :       Message types specified in <mids> and <dcss> are not accepted
        :type p_mode: int
        :param p_mids: String type. All different possible combinations of CBM message identifiers (see <mid>), e.g. “0,1,5,320-478,922”.
        :type p_mids: str
        :param p_dcss: String type. All different possible combinations of CBM data coding schemes (see <dcs>) (default is empty string), e.g. “0-3,5”.
        :type p_dcss: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CSCB={p_mode},"{p_mids}","{p_dcss}"')

    def shortMessageServiceCommands915ShowSmsTextModeParametersRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 915: Show SMS text mode parameters read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSDH?")

    def shortMessageServiceCommands915ShowSmsTextModeParametersWrite(
        self, p_show: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 915: Show SMS text mode parameters write.

        :param p_show: Integer type:

            - **0** :       Do not show header values defined in commands +CSCA, +CSMP (<sca>, <tosca>, <fo>, <vp>, <pid>, <dcs>) and <length>, <toda> or <tooa> in +CMT, +CMGL, +CMGR result codes for SMS-DELIVERs and SMS-SUBMITs in text mode
            - **1** :       Show the values in result codes
        :type p_show: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CSDH={p_show}")

    def shortMessageServiceCommands916SetSmsTextModeParametersRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 916: Set SMS text mode parameters read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CSMP?")

    def shortMessageServiceCommands916SetSmsTextModeParametersWrite(
        self, p_fo: int, p_vp: int, p_pid: int, p_dcs: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 916: Set SMS text mode parameters write.

        :param p_fo: First octet. Depending on the command or result code: First octet of 3GPP TS 23.040 SMS-DELIVER, SMS-SUBMIT (default 17), SMS-STATUS-REPORT, SMS-COMMAND in integer format. If a valid value has been entered once, parameter can be omitted.
        :type p_fo: int
        :param p_vp: Validity period. Depending on SMS-SUBMIT <fo> setting: 3GPP TS 23.040 TP-Validity-Period either in integer format or in time-string format (see <dt>). Default value: 167.
        :type p_vp: int
        :param p_pid: Protocol identifier. 3GPP TS 23.040 TP-Protocol-Identifier in integer format (default 0).
        :type p_pid: int
        :param p_dcs: Data coding scheme. Depending on the command or result code: 3GPP TS 23.038 SMS Data Coding Scheme (default 0), or Cell Broadcast Data Coding Scheme in integer format.
        :type p_dcs: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CSMP={p_fo},{p_vp},{p_pid},{p_dcs}")

    def shortMessageServiceCommands917SendConcatenatedMessagesTextMode(
        self,
        p_da: str,
        p_toda: int,
        p_uid: int,
        p_msg_seg: int,
        p_msg_total: int,
        p_text: str,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 917: Send concatenated messages text mode.

        :param p_da: Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007). The type of address is given by <toda>.
        :type p_da: str
        :param p_toda: Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet in integer format.
        :type p_toda: int
        :param p_uid: Integer type. Message identification in the user data header (UDH). Range: 0-255. This parameter is defined and inputted by the user. All segments of a same concatenated message must have the same <uid>. Different concatenated messages should have different <uid>.
        :type p_uid: int
        :param p_msg_seg: Integer type. Sequence number of a concatenated message. Range: 0–7. <msg_seg>=0 means: ignore the
            value and regard it as a non-concatenated message.
        :type p_msg_seg: int
        :param p_msg_total: Integer type. The total number of the segments of one concatenated message. Range: 0–7. <msg_total>=0 or 1 means: ignore the value and regard it as a non-concatenated message.
        :type p_msg_total: int
        :param p_text: String type. Message content.
        :type p_text: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+QCMGS="{p_da}",{p_toda},{p_uid},{p_msg_seg},{p_msg_total}\r{p_text}\x1A'
        )

    def shortMessageServiceCommands917SendConcatenatedMessagesPduMode(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 917: Send concatenated messages PDU mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return False, ["Not implemented"]

    def shortMessageServiceCommands918ReadConcatenatedMessages(
        self, p_index: int
    ) -> tuple[bool, list[str]]:
        """
        Short message service commands 918: Read concatenated messages.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCMGR={p_index}")

    def packetDomainCommands1001AttachmentDetachmentOfPsRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1001 attachment detachment of PS read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGATT?")

    def packetDomainCommands1001AttachmentDetachmentOfPsWrite(
        self, p_state: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1001 attachment detachment of PS write.

        :param p_state: Integer type. Indicates the state of PS attachment:

            - **0** :       Detached
            - **1** :       Attached
            - Other values are reserved and will result in an ERROR response to the Write Command
        :type p_state: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGATT={p_state}")

    def packetDomainCommands1002DefinePdpContextRead(self) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1002 define PDP context read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGDCONT?")

    def packetDomainCommands1002DefinePdpContextWrite(
        self,
        p_cid: int,
        p_pdp_type: str,
        p_apn: str,
        p_pdp_addr: str,
        p_data_comp: int,
        p_head_comp: int,
        p_ipv4_addr_alloc: int,
        p_request_type: int,
        p_p_cscf_discovery: int,
        p_im_cn_signalling_flag_ind: int,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1002 define PDP context write.

        :param p_cid: PDP context identifier. Range: 1–15. A numeric parameter which specifies a particular PDP context definition. The parameter is local to the TE-MT interface and is used in other PDP context-related commands. The range of permitted values (minimum value=1) is returned by the test form of the command.
        :type p_cid: int
        :param p_pdp_type: Packet data protocol type, a string parameter which specifies the type of packet data protocol:

            - **"IP"** :            Internet Protocol (IETF STD 5)
            - **"PPP"** :           Point to Point Protocol (IETF STD 51).
            - **"IPV6"** :          Internet Protocol, version 6
            - **"IPV4V6"** :        Virtual <PDP_type> introduced to handle dual IP stack UE capability
        :type p_pdp_type: str
        :param p_apn: Access point name, a string parameter that is a logical name used to select the GGSN or the external packet data network. If the value is null or omitted, then the subscription value will be requested.
        :type p_apn: str
        :param p_pdp_addr: A string parameter identifies the MT in the address space applicable to the PDP. If the value is null or omitted, then a value may be provided by the TE during the PDP startup procedure or, failing that, a dynamic address will be requested. The allocated address may be read using the AT+CGPADDR command.
        :type p_pdp_addr: str
        :param p_data_comp: A numeric parameter that controls PDP data compression (applicable for SNDCP only) (see 3GPP TS 44.065):

            - **0** :       Off (Default if value is omitted)
            - **1** :       On (Manufacturer preferred compression)
            - **2** :       V.42bis
            - **3** :       V.44 (Not supported currently)
        :type p_data_comp: int
        :param p_head_comp: A numeric parameter that controls PDP header compression (see 3GPP TS 44.065 and 3GPP TS 25.323):

            - **0** :       Off
            - **1** :       On
            - **2** :       RFC1144
            - **3** :       RFC2507
            - **4** :       RFC3095
        :type p_head_comp: int
        :param p_ipv4_addr_alloc: Numeric type. Control how the MT/TA requests to get the IPv4 address information:

            - **0** :       IPv4 address allocated through NAS signalling
            - **1** :       IPv4 address allocated through DHCP
        :type p_ipv4_addr_alloc: int
        :param p_request_type: Numeric type. Indicate the type of PDP context activation request for the PDP context.Please see 3GPP TS 24.301 (subclause 6.5.1.2) and 3GPP TS 24.008 (subclause10.5.6.17). If the initial PDP context is supported (subclause 10.1.0), it is not allowed toassign <cid>=0 for emergency bearer services. According to 3GPP TS 24.008(subclause 4.2.4.2.2 and 4.2.5.1.4) and 3GPP TS 24.301 (subclause 5.2.2.3.3 and5.2.3.2.2), a separate PDP context must be established for emergency bearer services.
        :type p_request_type: int
        :param p_p_cscf_discovery: Numeric type. Affect how the MT/TA requests to get the P-CSCF address, (see 3GPP TS 24.229 annex B and L):

            - **0** :       Preference of P-CSCF address discovery not affected by AT+CGDCONT
            - **1** :       Preference of P-CSCF address discovery through NAS signaling
            - **2** :       Preference of P-CSCF address discovery through DHCP
        :type p_p_cscf_discovery: int
        :param p_im_cn_signalling_flag_ind: Numeric type. Indicates to the network whether the PDP context is for IM CN subsystem-related signaling only or not:

            - **0** :       UE indicates that the PDP context is not for IM CN subsystem-related signaling only
            - **1** :       UE indicates that the PDP context is for IM CN subsystem-related signaling only
        :type p_im_cn_signalling_flag_ind: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CGDCONT={p_cid},"{p_pdp_type}","{p_apn}","{p_pdp_addr}",{p_data_comp},{p_head_comp},{p_ipv4_addr_alloc},{p_request_type},{p_p_cscf_discovery},{p_im_cn_signalling_flag_ind}'
        )

    def packetDomainCommands1003QualityOfServiceProfileRequestedRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1003 quality of service profile requested read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGQREQ?")

    def packetDomainCommands1003QualityOfServiceProfileRequestedWrite(
        self,
        p_cid: int,
        p_precedence: int,
        p_delay: int,
        p_reliability: int,
        p_peak: int,
        p_mean: int,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1003 quality of service profile requested write.

        :param p_cid: A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT command)
        :type p_cid: int
        :param p_precedence: A numeric parameter which specifies the precedence class:

            - **0** :       Network subscribed value
            - **1** :       High Priority. Service commitments shall be maintained ahead of precedence classes 2 and 3
            - **2** :       Normal priority. Service commitments shall be maintained ahead of precedence class 3
            - **3** :       Low priority. Service commitments shall be maintained
        :type p_precedence: int
        :param p_delay: A numeric parameter which specifies the delay class. This parameter defines the end-to-end transfer delay incurred in the transmission of SDUs through the network:

            - **0** :       Network subscribed value
        :type p_delay: int
        :param p_reliability: A numeric parameter which specifies the reliability class:

            - **0** :       Network subscribed value
            - **1** :       Non real-time traffic, error-sensitive application that cannot cope with data loss
            - **2** :       Non real-time traffic, error-sensitive application that can cope with infrequent data loss
            - **3** :       Non real-time traffic, error-sensitive application that can cope with data loss,GMM/SM, and SMS
            - **4** :       Real-time traffic, error-sensitive application that can cope with data loss
            - **5** :       Real-time traffic, error non-sensitive application that can cope with data loss
        :type p_reliability: int
        :param p_peak: A numeric parameter which specifies the peak throughput class, in octets per second:

            - **0** :       Network subscribed value
            - **1** :       Up to 1 000 (8 kbit/s)
            - **2** :       Up to 2 000 (16 kbit/s)
            - **3** :       Up to 4 000 (32 kbit/s)
            - **4** :       Up to 8 000 (64 kbit/s)
            - **5** :       Up to 16 000 (128 kbit/s)
            - **6** :       Up to 32 000 (256 kbit/s)
            - **7** :       Up to 64 000 (512 kbit/s)
            - **8** :       Up to 128 000 (1024 kbit/s)
            - **9** :       Up to 256 000 (2048 kbit/s)
        :type p_peak: int
        :param p_mean: A numeric parameter which specifies the mean throughput class, in octets per hour:

            - **0** :       Network subscribed value
            - **1** :       100 (~0.22 bit/s)
            - **2** :       200 (~0.44 bit/s)
            - **3** :       500 (~1.11 bit/s)
            - **4** :       1 000 (~2.2 bit/s)
            - **5** :       2 000 (~4.4 bit/s)
            - **6** :       5 000 (~11.1 bit/s)
            - **7** :       10 000 (~22 bit/s)
            - **8** :       20 000 (~44 bit/s)
            - **9** :       50 000 (~111 bit/s)
            - **10** :      100 000 (~0.22 kbit/s)
            - **11** :      200 000 (~0.44 kbit/s)
            - **12** :      500 000(~1.11 kbit/s)
            - **13** :      1000 000 (~2.2 kbit/s)
            - **14** :      2 000 000 (~4.4 kbit/s)
            - **15** :      5 000 000 (~11.1 kbit/s)
            - **16** :      10 000 000 (~22 kbit/s)
            - **17** :      20 000 000 (~44 kbit/s)
            - **18** :      50 000 000 (~111 kbit/s)
            - **31** :      Best effort
        :type p_mean: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f"AT+CGQREQ={p_cid},{p_precedence},{p_delay},{p_reliability},{p_peak},{p_mean}"
        )

    def packetDomainCommands1004QualityOfServiceProfileMinimumAcceptableRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1004 quality of service profile minimum acceptable read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGQMIN?")

    def packetDomainCommands1004QualityOfServiceProfileMinimumAcceptableWrite(
        self,
        p_cid: int,
        p_precedence: int,
        p_delay: int,
        p_reliability: int,
        p_peak: int,
        p_mean: int,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1004 quality of service profile minimum acceptable write.

        :param p_cid: A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT command)
        :type p_cid: int
        :param p_precedence: A numeric parameter which specifies the precedence class:

            - **0** :       Network subscribed value
            - **1** :       High Priority. Service commitments shall be maintained ahead of precedence classes 2 and 3
            - **2** :       Normal priority. Service commitments shall be maintained ahead of precedence class 3
            - **3** :       Low priority. Service commitments shall be maintained
        :type p_precedence: int
        :param p_delay: A numeric parameter which specifies the delay class. This parameter defines the end-to-end transfer delay incurred in the transmission of SDUs through the network:

            - **0** :       Network subscribed value
        :type p_delay: int
        :param p_reliability: A numeric parameter which specifies the reliability class:

            - **0** :       Network subscribed value
            - **1** :       Non real-time traffic, error-sensitive application that cannot cope with data loss
            - **2** :       Non real-time traffic, error-sensitive application that can cope with infrequent data loss
            - **3** :       Non real-time traffic, error-sensitive application that can cope with data loss,GMM/SM, and SMS
            - **4** :       Real-time traffic, error-sensitive application that can cope with data loss
            - **5** :       Real-time traffic, error non-sensitive application that can cope with data loss
        :type p_reliability: int
        :param p_peak: A numeric parameter which specifies the peak throughput class, in octets per second:

            - **0** :               Network subscribed value
            - **1** :               Up to 1 000 (8 kbit/s)
            - **2** :               Up to 2 000 (16 kbit/s)
            - **3** :               Up to 4 000 (32 kbit/s)
            - **4** :               Up to 8 000 (64 kbit/s)
            - **5** :               Up to 16 000 (128 kbit/s)
            - **6** :               Up to 32 000 (256 kbit/s)
            - **7** :               Up to 64 000 (512 kbit/s)
            - **8** :               Up to 128 000 (1024 kbit/s)
            - **9** :               Up to 256 000 (2048 kbit/s)
        :type p_peak: int
        :param p_mean: A numeric parameter which specifies the mean throughput class, in octets per hour:

            - **0** :               Network subscribed value
            - **1** :               100 (~0.22 bit/s)
            - **2** :               200 (~0.44 bit/s)
            - **3** :               500 (~1.11 bit/s)
            - **4** :               1 000 (~2.2 bit/s)
            - **5** :               2 000 (~4.4 bit/s)
            - **6** :               5 000 (~11.1 bit/s)
            - **7** :               10 000 (~22 bit/s)
            - **8** :               20 000 (~44 bit/s)
            - **9** :               50 000 (~111 bit/s)
            - **10** :              100 000 (~0.22 kbit/s)
            - **11** :              200 000 (~0.44 kbit/s)
            - **12** :              500 000(~1.11 kbit/s)
            - **13** :              1000 000 (~2.2 kbit/s)
            - **14** :              2 000 000 (~4.4 kbit/s)
            - **15** :              5 000 000 (~11.1 kbit/s)
            - **16** :              10 000 000 (~22 kbit/s)
            - **17** :              20 000 000 (~44 kbit/s)
            - **18** :              50 000 000 (~111 kbit/s)
            - **31** :              Best effort
        :type p_mean: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f"AT+CGQMIN={p_cid},{p_precedence},{p_delay},{p_reliability},{p_peak},{p_mean}"
        )

    def packetDomainCommands1005QualityOfServiceProfile3gRequestedRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1005 quality of service profile 3g requested read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGEQREQ?")

    def packetDomainCommands1005QualityOfServiceProfile3gRequestedWrite(
        self,
        p_cid: int,
        p_traffic_class: int,
        p_max_bitrate_ul: int,
        p_max_bitrate_dl: int,
        p_guaranteed_bitrate_ul: int,
        p_guaranteed_bitrate_dl: int,
        p_delivery_order: int,
        p_max_sdu_size: int,
        p_sdu_error_ratio: str,
        p_residual_bit_error_ratio: str,
        p_delivery_of_err_sdu: int,
        p_transfer_delay: int,
        p_traffic_handling_priority: int,
        p_source_statistics_descriptor: int,
        p_signalling_indication: int,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1005 quality of service profile 3g requested write.

        :param p_cid: PDP context identifier, a numeric parameter which specifies a particular PDP context definition.
                    The parameter is local to the TE-MT interface and is used in other PDP context-related commands.
                    The range of permitted values (minimum value=1) is returned by the test form of the command.
        :type p_cid: int

        :param p_traffic_class: Integer type. Indicates the type of application for which the UMTS bearer service is optimized:
                                (see 3GPP TS 24.008 subclause 10.5.6.5). If specified as conversational or streaming, then
                                the Guaranteed and Maximum bitrate parameters should also be provided:

                                - **0** : - Conversational
                                - **1** : - Streaming
                                - **2** : - Interactive
                                - **3** : - Background
                                - **4** : - Subscribed value
        :type p_traffic_class: int

        :param p_max_bitrate_ul: Integer type. Indicates the maximum number of kbits/s delivered to UMTS (up-link traffic) at a SAP.
                                Range: 0–256000:

                                - **0** : - Subscribed value
                                - **0–64** : Values in the ranges:
                                - **64–568** : (multiple of 8)
                                - **568–8640** : (multiple of 64)
                                - **8640–16000** : (multiple of 100)
                                - **16000–128000** : (multiple of 1000)
                                - **128000–256000** : (multiple of 2000)
        :type p_max_bitrate_ul: int

        :param p_max_bitrate_dl: Integer type. Indicates the maximum number of kbits/s delivered by UMTS (down-link traffic) at a SAP.
                                Range: 0–256000.
                                Same format as p_max_bitrate_ul.
        :type p_max_bitrate_dl: int

        :param p_guaranteed_bitrate_ul: Integer type. Indicates the guaranteed number of kbits/s delivered to UMTS (up-link traffic) at a SAP.
                                        Range: 0–256000.
                                        Same format as p_max_bitrate_ul.
        :type p_guaranteed_bitrate_ul: int

        :param p_guaranteed_bitrate_dl: Integer type. Indicates the guaranteed number of kbits/s delivered by UMTS (down-link traffic) at a SAP.
                                        Range: 0–256000.
                                        Same format as p_max_bitrate_ul.
        :type p_guaranteed_bitrate_dl: int

        :param p_delivery_order: Integer type. Indicates the delivery order requested by the UMTS user:

                                - **0** : - Delivery of SDUs in the order of the SDU sequence numbers
                                - **1** : - Delivery of SDUs not guaranteed in the order of the SDU sequence numbers
        :type p_delivery_order: int

        :param p_max_sdu_size: Integer type. Indicates the maximum SDU size requested by the UMTS user. Range: 0–1520.
        :type p_max_sdu_size: int

        :param p_sdu_error_ratio: String type. Indicates the acceptable residual SDU error ratio requested by the UMTS user:

                                - **"0E0"** : - Subscribed value
                                - **"1E1"**
                                - **"1E2"**
                                - **"7E3"**
                                - **"1E3"**
                                - **"1E4"**
                                - **"1E5"**
                                - **"1E6"**
        :type p_sdu_error_ratio: str

        :param p_residual_bit_error_ratio: String type. Indicates the acceptable residual bit error ratio requested by the UMTS user:

                                        - **"0E0"** :     - Subscribed value
                                        - **"1E1"**
                                        - **"7E2"**
                                        - **"1E2"**
                                        - **"1E3"**
                                        - **"1E4"**
                                        - **"1E5"**
                                        - **"1E6"**
        :type p_residual_bit_error_ratio: str

        :param p_delivery_of_err_sdu: Integer type. Indicates the delivery of erroneous SDUs requested by the UMTS user:

                                    - **0** : No detect
                                    - **1** : Erroneous SDUs are delivered
        :type p_delivery_of_err_sdu: int

        :param p_transfer_delay: Integer type. Indicates the transfer delay requested by the UMTS user. Range: 0–400.
        :type p_transfer_delay: int

        :param p_traffic_handling_priority: Integer type. Indicates the traffic handling priority requested by the UMTS user:

                                            - **0** :  Subscribe:
                                            - **1**
                                            - **2**
                                            - **3**
        :type p_traffic_handling_priority: int

        :param p_source_statistics_descriptor: Integer type. Indicates the source statistics descriptor requested by the UMTS user:

                                            - **0** :  Characteristics of SDUs is unknown
                                            - **1** :  Characteristics of SDUs correspond to a speech source
        :type p_source_statistics_descriptor: int

        :param p_signalling_indication: Integer type. Indicates the signalling indication requested by the UMTS user:

                                        - **0** : - PDP context is not optimized for signaling
                                        - **1** : - PDP context is optimized for signaling
        :type p_signalling_indication: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CGEQREQ={p_cid},{p_traffic_class},{p_max_bitrate_ul},{p_max_bitrate_dl},{p_guaranteed_bitrate_ul},{p_guaranteed_bitrate_dl},{p_delivery_order},{p_max_sdu_size},"{p_sdu_error_ratio}","{p_residual_bit_error_ratio}",{p_delivery_of_err_sdu},{p_transfer_delay},{p_traffic_handling_priority},{p_source_statistics_descriptor},{p_signalling_indication}'
        )

    def packetDomainCommands1006QualityOfServiceProfile3gMinimumAcceptableRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1006 quality of service profile 3g minimum acceptable read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGEQMIN?")

    def packetDomainCommands1006QualityOfServiceProfile3gMinimumAcceptableWrite(
        self,
        p_cid: int,
        p_traffic_class: int,
        p_max_bitrate_ul: int,
        p_max_bitrate_dl: int,
        p_guaranteed_bitrate_ul: int,
        p_guaranteed_bitrate_dl: int,
        p_delivery_order: int,
        p_max_sdu_size: int,
        p_sdu_error_ratio: str,
        p_residual_bit_error_ratio: str,
        p_delivery_of_err_sdu: int,
        p_transfer_delay: int,
        p_traffic_handling_priority: int,
        p_source_statistics_descriptor: int,
        p_signalling_indication: int,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1005 quality of service profile 3g requested write.

        :param p_cid: PDP context identifier, a numeric parameter which specifies a particular PDP context definition.
                    The parameter is local to the TE-MT interface and is used in other PDP context-related commands.
                    The range of permitted values (minimum value=1) is returned by the test form of the command.
        :type p_cid: int

        :param p_traffic_class: Integer type. Indicates the type of application for which the UMTS bearer service is optimized
                                (see 3GPP TS 24.008 subclause 10.5.6.5). If the parameter is specified as conversational or streaming, then
                                the Guaranteed and Maximum bitrate parameters should also be provided:

                                - **0** :       Conversational
                                - **1** :       Streaming
                                - **2** :       Interactive
                                - **3** :       Background
                                - **4** :       Subscribed value
        :type p_traffic_class: int

        :param p_max_bitrate_ul: Integer type. Indicates the maximum number of kbits/s delivered to UMTS (up-link traffic) at a SAP.
                                Range: 0–256000:

                                - **0** :       Subscribed value
                                - **0–64**
                                - **64–568** :      (value needs to be a multiple of 8)
                                - **568–8640** :    (value needs to be a multiple of 64)
                                - **8640–16000** :  (value needs to be a multiple of 100)
                                - **16000–128000** : (value needs to be a multiple of 1000)
                                - **128000–256000** : (value needs to be a multiple of 2000)
        :type p_max_bitrate_ul: int

        :param p_max_bitrate_dl: Integer type. Indicates the maximum number of kbits/s delivered by UMTS (down-link traffic) at a SAP.
                                Range: 0–256000.
                                Same format as p_max_bitrate_ul.
        :type p_max_bitrate_dl: int

        :param p_guaranteed_bitrate_ul: Integer type. Indicates the guaranteed number of kbits/s delivered to UMTS (up-link traffic) at a SAP (provided that there is data to deliver).
                                        Range: 0–256000.
                                        Same format as p_max_bitrate_ul.
        :type p_guaranteed_bitrate_ul: int

        :param p_guaranteed_bitrate_dl: Integer type. Indicates the guaranteed number of kbits/s delivered by UMTS (down-link traffic) at a SAP (provided that there is data to deliver).
                                        Range: 0–256000.
                                        Same format as p_max_bitrate_ul.
        :type p_guaranteed_bitrate_dl: int

        :param p_delivery_order: Integer type. Indicates the delivery order requested by the UMTS user:

                                - **0** :       Delivery of SDUs in the order of the SDU sequence numbers
                                - **1** :       Delivery of SDUs not guaranteed in the order of the SDU sequence numbers
        :type p_delivery_order: int

        :param p_max_sdu_size: Integer type. Indicates the maximum SDU size requested by the UMTS user. Range: 0–1520.
        :type p_max_sdu_size: int

        :param p_sdu_error_ratio: String type. Indicates the acceptable residual SDU error ratio requested by the UMTS user:

                                - **"0E0"** :       Subscribed value
                                - **"1E1"**
                                - **"1E2"**
                                - **"7E3"**
                                - **"1E3"**
                                - **"1E4"**
                                - **"1E5"**
                                - **"1E6"**
        :type p_sdu_error_ratio: str

        :param p_residual_bit_error_ratio: String type. Indicates the acceptable residual bit error ratio requested by the UMTS user:

                                        - **"0E0"** :       Subscribed value
                                        - **"1E1"**
                                        - **"7E2"**
                                        - **"1E2"**
                                        - **"1E3"**
                                        - **"1E4"**
                                        - **"1E5"**
                                        - **"1E6"**
        :type p_residual_bit_error_ratio: str

        :param p_delivery_of_err_sdu: Integer type. Indicates the delivery of erroneous SDUs requested by the UMTS user:

                                    - **0** :       No detect
                                    - **1** :       Erroneous SDUs are delivered
        :type p_delivery_of_err_sdu: int

        :param p_transfer_delay: Integer type. Indicates the transfer delay requested by the UMTS user. Range: 0–400.
        :type p_transfer_delay: int

        :param p_traffic_handling_priority: Integer type. Indicates the traffic handling priority requested by the UMTS user:

                                            - **0** :       Subscribed
                                            - **1**
                                            - **2**
                                            - **3**
        :type p_traffic_handling_priority: int

        :param p_source_statistics_descriptor: Integer type. Indicates the source statistics descriptor requested by the UMTS user:

                                            - **0** :       Characteristics of SDUs is unknown
                                            - **1** :       Characteristics of SDUs correspond to a speech source
        :type p_source_statistics_descriptor: int

        :param p_signalling_indication: Integer type. Indicates the signalling indication requested by the UMTS user:

                                        - **0** :       PDP context is not optimized for signaling
                                        - **1** :       PDP context is optimized for signaling
        :type p_signalling_indication: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+CGEQMIN={p_cid},{p_traffic_class},{p_max_bitrate_ul},{p_max_bitrate_dl},{p_guaranteed_bitrate_ul},{p_guaranteed_bitrate_dl},{p_delivery_order},{p_max_sdu_size},"{p_sdu_error_ratio}","{p_residual_bit_error_ratio}",{p_delivery_of_err_sdu},{p_transfer_delay},{p_traffic_handling_priority},{p_source_statistics_descriptor},{p_signalling_indication}'
        )

    def packetDomainCommands1007ActivateDeactivatePdpContextRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1007 activate deactivate PDP context read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGACT?")

    def packetDomainCommands1007ActivateDeactivatePdpContextWrite(
        self, p_state: int, p_cid: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1007 activate deactivate PDP context write.

        :param p_state: Indicates the state of PDP context activation:

            - **0** :       Deactivated
            - **1** :       Activated
            - **Other values** : are reserved and will result in an ERROR response to the Write Command
        :type p_state: int
        :param p_cid: A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT)
        :type p_cid: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGACT={p_state},{p_cid}")

    def packetDomainCommands1008EnterDataState(
        self, p_l2p: str, p_cid: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1008 enter data state.

        :param p_l2p: The layer 2 protocol to be used between the TE and MT:

            - **PPP** : (Point to Point protocol) for a PDP such as IP
            - **Other values** : are not supported and will result in an ERROR response to the execution command
        :type p_l2p: str
        :param p_cid: The particular PDP context definition (see AT+CGDCONT)
        :type p_cid: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CGDATA="{p_l2p}",{p_cid}')

    def packetDomainCommands1009ShowPdpAddress(
        self, p_cid: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1009 show PDP address.

        :param p_cid: A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT command)
        :type p_cid: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGPADDR={p_cid}")

    def packetDomainCommands1010GprsMobileStationClassRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1010 GPRS mobile station class read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGCLASS?")

    def packetDomainCommands1010GprsMobileStationClassWrite(
        self, p_class: str
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1010 GPRS mobile station class write.

        :param p_class: String type. GPRS mobile class (Functionality in descending order).
            "A" Class-A mode of operation (A/Gb mode), or CS/PS mode of operation (Iu mode)
            (highest mode of operation)
        :type p_class: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CGCLASS="{p_class}"')

    def packetDomainCommands1011PsDomainNetworkRegistrationStatusRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1011 PS domain network registration status read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGREG?")

    def packetDomainCommands1011PsDomainNetworkRegistrationStatusWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1011 PS domain network registration status write.

        :param p_n: Integer type:

            - **0** :       Disable network registration unsolicited result code
            - **1** :       Enable network registration unsolicited result code +CGREG: <stat>
            - **2** :       Enable network registration and location information unsolicited result code +CGREG: <stat>[,<lac>,<ci>[,<Act>]]
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGREG={p_n}")

    def packetDomainCommands1012PacketDomainEventReportingRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1012 packet domain event reporting read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGEREP?")

    def packetDomainCommands1012PacketDomainEventReportingWrite(
        self, p_mode: int, p_bfr: int
    ):
        """
        Packet domain commands 1012 packet domain event reporting write.

        :param p_mode: Integer type:

            - **0** :       Buffer unsolicited result codes in the MT; if MT result code buffer is full, the oldest ones can be discarded. No codes are forwarded to the TE.
            - **1** :       Discard unsolicited result codes when MT-TE link is reserved (e.g. in on-line data mode), otherwise forward them directly to the TE.
            - **2** :       Buffer unsolicited result codes in the MT when MT-TE link is reserved (e.g. in on-line data mode) and flush them to the TE when MT-TE link becomes available. Otherwise forward them directly to the TE.
        :type p_mode: int
        :param p_bfr: Integer type:

            - **0** :       MT buffer of unsolicited result codes defined within this command is cleared when <mode> 1 or 2 is entered.
            - **1** :       MT buffer of unsolicited result codes defined within this command is flushed to the TE when <mode> 1 or 2 is entered (OK response shall be given before flushing the codes).
        :type p_bfr: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGEREP={p_mode},{p_bfr}")

    def packetDomainCommands1013SelectServiceForMoSmsMessagesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1013 select service for MO SMS messages read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CGSMS?")

    def packetDomainCommands1013SelectServiceForMoSmsMessagesWrite(
        self, p_service: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1013 select service for MO SMS messages write.

        :param p_service: Integer type. Service or service preference to be used:

            - **0** : GPRS
            - **1** : Circuit switch
            - **2** : GPRS preferred (use circuit switched if GPRS not available)
            - **3** : Circuit switch preferred (use GPRS if circuit switch not available)

        :type p_service: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CGSMS={p_service}")

    def packetDomainCommands1014EpsNetworkRegistrationStatusRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1014 EPS network registration status read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CEREG?")

    def packetDomainCommands1014EpsNetworkRegistrationStatusWrite(self, p_n: int):
        """
        Packet domain commands 1014 EPS network registration status write.

        :param p_n: Integer type:

            - **0** :       Disable network registration unsolicited result code
            - **1** :       Enable network registration unsolicited result code +CEREG: <stat>
            - **2** :       Enable network registration and location information unsolicited result code +CEREG: <stat>[,<tac>,<ci>[,<Act>]]
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+CEREG={p_n}")

    def packetDomainCommands1015PacketDataCounterRead(self) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1015 packet data counter read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QGDCNT?")

    def packetDomainCommands1015PacketDataCounterWrite(
        self, p_op: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1015 packet data counter write.

        :param p_op: Integer type. The operation for data counter:

                    - **"0"** : : Reset the data counter.
                    - **"1"** : : Save the results of the data counter to NV.

                    *If the results need to be automatically saved, see AT+QAUGDCNT.*
        :type p_op: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGDCNT={p_op}")

    def packetDomainCommands1016AutoSavePacketDataCounterRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1016 auto save packet data counter read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QAUGDCNT?")

    def packetDomainCommands1016AutoSavePacketDataCounterWrite(
        self, p_value: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1016 auto save packet data counter write.

        :param p_value: Integer type. The time-interval for AT+QGDCNT to save results to NV automatically. If it
            is set to 0, auto-save feature would be disabled. Range: 0, 30–65535. Default value: 0. Unit: second.
        :type p_value: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QAUGDCNT={p_value}")

    def packetDomainCommands1017ConnectUsbNetcardToNetworkRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1017 connect USB netcard to network read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QNETDEVCTL?")

    def packetDomainCommands1017ConnectUsbNetcardToNetworkWrite(
        self, p_type: int, p_cid: int, p_urc_en: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1017 connect USB netcard to network write.

        :param p_type: Integer type. The type of the network connection:

            - **0** :       Disconnect the network connection.
            - **1** :       Connect the network connection.

        :type p_type: int
        :param p_cid: Integer type. The PDP context identifier.
        :type p_cid: int

        :param p_urc_en: Integer type. Whether to enable the URC +QNETDEVSTATUS: <status> showing the netcard status:

            - **0** :       Disable the URC.
            - **1** :       Enable the URC.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QNETDEVCTL={p_type},{p_cid},{p_urc_en}")

    def packetDomainCommands1018ConfigureResponseFormatOfAtCeerIn2g4gRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1018 configure response format of AT+CEER in 2G/4G read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QCEERCATCFG?")

    def packetDomainCommands1018ConfigureResponseFormatOfAtCeerIn2g4gWrite(
        self, p_mode: int
    ) -> tuple[bool, list[str]]:
        """
        Packet domain commands 1018 configure response format of AT+CEER in 2G/4G write.

        :param p_mode: Integer type. Return format of AT+CEER:

            - **0** : The return format of AT+CEER is +CEER: <text>
            - **1** : The return format of AT+CEER is +CEER: <category>,<cause>,<description>

        :type p_mode: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QCEERCATCFG={p_mode}")

    def hardwareRelatedCommands1101PowerOff(self, p_n: int):
        """
        Hardware related commands 1101 power off.

        :param p_n: Integer type:

            - **0** :       Immediately power down
            - **1** :       Normal power down
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QPOWD={p_n}")

    def hardwareRelatedCommands1102ClockRead(self) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1102 clock read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CCLK?")

    def hardwareRelatedCommands1102ClockWrite(
        self, p_time: str
    ) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1102 clock write.

        :param p_time: String type. The format is “yy/MM/dd,hh:mm:ss±zz”, indicating year (two last digits), month,
            day, hour, minutes, seconds and time zone (indicates the difference, expressed in quarters of an hour,
            between the local time and GMT; range: -48 to +56), e.g. May 6th, 1994, 22:10:00 GMT+2 hours equals to
            “94/05/06,22:10:00+08”.
        :param p_time: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+CCLK="{p_time}"')

    def hardwareRelatedCommands1103EnableDisableSleepModeRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1103 enable disable sleep mode read.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QSCLK?")

    def hardwareRelatedCommands1103EnableDisableSleepModeWrite(
        self, p_n: int
    ) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1103 enable disable sleep mode write.

        :param p_n: Integer type:

            - **0** :       Disable
            - **1** :       Enable. It is controlled by DTR pin and WAKEUP_IN pin.
        :type p_n: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QSCLK={p_n}")

    def hardwareRelatedCommands1104QueryReadBatteryChargeInformation(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1104 query read battery charge information.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+CBC")

    def hardwareRelatedCommands1105ReadAdcValue(self, p_port) -> tuple[bool, list[str]]:
        """
        Hardware related commands 1105 read ADC value.

        :param p_port: Integer type. Channel number of the ADC:

            - **0** :       ADC Channel 0
            - **1** :       ADC Channel 1
        :type p_port: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QADC={p_port}")


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
    client = QuectelModemATCommands(port, baudrate, timeout)
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
def free_at_command(ctx, command: str):
    """Free AT command."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.freeAtCommand(command)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def general_command(ctx):
    """Group for general AT commands."""
    pass


@general_command.command("display-product-id")
@click.pass_context
def display_product_id(ctx):
    """Display Product Identification Information."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands201DisplayProductIdentificationInformation()
    )
    print(response if status else "Error")
    client.close()


@general_command.command("request-manufacturer-id")
@click.pass_context
def request_manufacturer_id(ctx):
    """Request Manufacturer Identification."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands202RequestManufacturerIdentification()
    print(response if status else "Error")
    client.close()


@general_command.command("request-ta-model-id")
@click.pass_context
def request_ta_model_id(ctx):
    """Request TA Model Identification."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands203RequestTaModelIdentification()
    print(response if status else "Error")
    client.close()


@general_command.command("request-software-version")
@click.pass_context
def request_software_version(ctx):
    """Request TA Revision Identification of Software Release"""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands204RequestTaRevisionIdentificationSoftwareRelease()
    )
    print(response if status else "Error")
    client.close()


@general_command.command("request-manufacturer-idenfication")
@click.pass_context
def request_manufacturer_idenfication(ctx):
    """Request Manufacturer Identification."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands205RequestManufacturerIdentification()
    print(response if status else "Error")
    client.close()


@general_command.command("request-model-id")
@click.pass_context
def request_model_id(ctx):
    """Request Model Identification."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands206RequestModelIdentification()
    print(response if status else "Error")
    client.close()


@general_command.command("display-ta-revision-identification-of-software-release")
@click.pass_context
def display_ta_revision_identification_of_software_release(ctx):
    """Request TA Revision Identification of Software Release."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands207RequestTaRevisionIdentificationOfSoftwareRelease()
    )
    print(response if status else "Error")
    client.close()


@general_command.command("request-imei")
@click.pass_context
def request_imei(ctx):
    """Request International Mobile Equipment Identity (IMEI)."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands208RequestIMEI()
    print(response if status else "Error")
    client.close()


@general_command.command("request-international-mobile-equipment-identity")
@click.pass_context
def request_international_mobile_equipment_identity(ctx):
    """Request International Mobile Equipment Identity."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands209InternationalMobileEquipmentIdentity()
    print(response if status else "Error")
    client.close()


@general_command.command("reset-at-command-settings-to-factory-defaults")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="0 Reset all AT command settings to factory defaults.",
)
def reset_at_command_settings_to_factory_defaults(ctx, n: int):
    """Reset AT Command Settings to Factory Defaults"""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands210ResetAtCommandSettingsToFactoryDefaults(
        n
    )
    print(response if status else "Error")
    client.close()


@general_command.command("display-current-configuration")
@click.pass_context
def display_current_configuration(ctx):
    """Display Current Configuration."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands211DisplayCurrentConfiguration()
    print(response if status else "Error")
    client.close()


@general_command.command("store-current-parameters-to-user-defined-profile")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="Profile number to store current parameters.",
)
def store_current_parameters_to_user_defined_profile(ctx, n: int):
    """Store Current Parameters to User Defined Profile."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands212StoreCurrentParametersToUserDefinedProfile(n)
    )
    print(response if status else "Error")
    client.close()


@general_command.command("set-all-current-parameters-to-user-defined-profile")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="Profile number to store current parameters.",
)
def set_all_current_parameters_to_user_defined_profile(ctx, n: int):
    """Set All Current Parameters to User Defined Profile."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands213SetAllCurrentParametersToUserDefinedProfile(n)
    )
    print(response if status else "Error")
    client.close()


@general_command.command("set-result-code-presentation-mode")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="0 TA transmits result code. 1 Result codes are suppressed and not transmitted.",
)
def set_result_code_presentation_mode(ctx, n: int):
    """Set Result Code Presentation Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands214SetResultCodePresentationMode(n)
    print(response if status else "Error")
    client.close()


@general_command.command("set-response-format")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="0 Information response: <text><CR><LF> Short result code format: <numeric code><CR> 1 Information response: <CR><LF><text><CR><LF> Long result code format: <CR><LF><verbose code><CR><LF>",
)
def set_response_format(ctx, n: int):
    """Set Response Format."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands215SetResponseFormat(n)
    print(response if status else "Error")
    client.close()


@general_command.command("set-command-echo-mode")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="0 Command echo disabled. 1 Command echo enabled.",
)
def set_command_echo_mode(ctx, n: int):
    """Set Command Echo Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands216SetCommandEchoMode(n)
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def set_command_line_termination_character(ctx):
    """Commands related to setting the command line termination character."""
    pass


@set_command_line_termination_character.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read command line termination character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands217SetCommandLineTerminationCharacterRead()
    print(response if status else "Error")
    client.close()


@set_command_line_termination_character.command()
@click.option(
    "-n",
    type=int,
    default=13,
    show_default=True,
    help="Command line termination character. Range: 0–127. (Default 13 = <CR>)",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write command line termination character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands217SetCommandLineTerminationCharacterWrite(
        n
    )
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def set_response_formatting_character(ctx):
    """Commands related to setting the response formatting character."""
    pass


@set_response_formatting_character.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read response formatting character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands218SetResponseFormattingCharacterRead()
    print(response if status else "Error")
    client.close()


@set_response_formatting_character.command()
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=10,
    show_default=True,
    help="Response formatting character. Range: 0–127. (Default 10 = <LF>)",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write response formatting character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands218SetResponseFormattingCharacterWrite(n)
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def set_command_line_editing_character(ctx):
    """Commands related to setting the command line editing character."""
    pass


@set_command_line_editing_character.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read command line editing character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands219SetCommandLineEditingCharacterRead()
    print(response if status else "Error")
    client.close()


@set_command_line_editing_character.command()
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=8,
    show_default=True,
    help="Command line editing character. Range: 0–127. (Default 8 = <Backspace>)",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write command line editing character."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands219SetCommandLineEditingCharacterWrite(n)
    print(response if status else "Error")
    client.close()


@general_command.command("set-connect-result-format-and-monitor-call-in-progress")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help="0 CONNECT result code returned only. Dial tone and busy detection are both disabled. 1 CONNECT<text> result code returned only. Dial tone and busy detection are both disabled. 2 CONNECT<text> result code returned. Dial tone detection is enabled, while busy detection is disabled. 3 CONNECT<text> result code returned. Dial tone detection is disabled, while busy detection is enabled. 4 CONNECT<text> result code returned. Both dial tone and busy detection are both enabled.",
)
def set_connect_result_format_and_monitor_call_in_progress(ctx, n: int):
    """Set Connect Result Format and Monitor Call in Progress."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.generalCommands220SetConnectResultFormatAndMonitorCallInProgress(n)
    )
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def set_phone_functionality(ctx):
    """Commands related to setting the phone functionality."""
    pass


@set_phone_functionality.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read phone functionality."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands221SetPhoneFunctionalityRead()
    print(response if status else "Error")
    client.close()


@set_phone_functionality.command()
@click.pass_context
@click.option(
    "-f",
    type=int,
    default=0,
    show_default=True,
    help=f"0 Minimum functionality \n1 Full functionality \n3 Disable the ME from receiving RF signals \n4 Disable the ME from both transmitting and receiving RF signals \n5 Disable (U)SIM",
)
@click.option(
    "-r",
    type=int,
    help=f"0 Do not reset the ME before setting it to <fun> functionality level.(This is the default setting when <rst> is not given.) \n1 Reset the ME. The device is fully functional after the reset. This value is available only for <fun> = 1.",
)
def write(ctx, f: int, r: int):  # type: ignore[reportRedeclaration]
    """Write phone functionality."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands221SetPhoneFunctionalityWrite(f, r)
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def error_message_format(ctx):
    """Commands related to setting the error message format."""
    pass


@error_message_format.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read error message format."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands222ErrorMessageFormatRead()
    print(response if status else "Error")
    client.close()


@error_message_format.command()
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help=f"0 Disable result code \n1 Enable result code with numeric values \n2 Enable result code with verbose values",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write error message format."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands222ErrorMessageFormatWrite(n)
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def select_character_set(ctx):
    """Commands related to setting the character set."""
    pass


@select_character_set.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read character set."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands223SelectCharacterSetRead()
    print(response if status else "Error")
    client.close()


@select_character_set.command()
@click.pass_context
@click.option(
    "-chset",
    type=str,
    default="GSM",
    show_default=True,
    help=f'"GSM" GSM default alphabet \n"IRA" International reference Alphabet \n"UCS2" UCS2 alphabet',
)
def write(ctx, chset: str):  # type: ignore[reportRedeclaration]
    """Write character set."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands223SelectCharacterSetWrite(chset)
    print(response if status else "Error")
    client.close()


@general_command.group()
@click.pass_context
def configure_urc_indication(ctx):
    """Commands related to configuring URC indication."""
    pass


@configure_urc_indication.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read URC indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands224ConfigureUrcIndicationRead()
    print(response if status else "Error")
    client.close()


@configure_urc_indication.command()
@click.pass_context
@click.option(
    "-urc_port",
    type=str,
    help=f'"usbat" USB AT port \n"usbmodem" USB modem port \n"uart1" Main UART port',
)
def write(ctx, urc_port: str):  # type: ignore[reportRedeclaration]
    """Write URC indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands224ConfigureUrcIndicationWrite(urc_port)
    print(response if status else "Error")
    client.close()


@general_command.command("terminate-ppp-connection")
@click.pass_context
@click.option(
    "-op",
    type=int,
    default=0,
    show_default=True,
    help=f"0 Hang up PPP connection without sending TERM REQ frame to peer. \n1 Hang up PPP connection and automatically send TERM REQ frame to peer. \n2 Hang up PPP connection with sending TERM REQ frame to peer.",
)
def terminate_ppp_connection(ctx, op: int):
    """Terminate PPP Connection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.generalCommands225TerminatePppConnection(op)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def serial_interface_control(ctx):
    """Group for serial interface control commands."""
    pass


@serial_interface_control.command("set-dcd-function-mode")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help=f"0 DCD function is always ON \n1 DCD function is ON only in the presence of data carrier",
)
def set_dcd_function_mode(ctx, n: int):
    """Set DCD Function Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.serialInterfaceControlCommands301SetDcdFunctionMode(n)
    print(response if status else "Error")
    client.close()


@serial_interface_control.command("set-dtr-function-mode")
@click.pass_context
@click.option(
    "-n",
    type=int,
    default=0,
    show_default=True,
    help=f"0 TA ignores status on DTR \n1 Low→High on DTR: Change to command mode while remaining the connected call \n2 Low→High on DTR: Disconnect data call and change to command mode. When DTR is at high level, auto-answer function is disabled",
)
def set_dtr_function_mode(ctx, n: int):
    """Set DTR Function Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.serialInterfaceControlCommands302SetDtrFunctionMode(n)
    print(response if status else "Error")
    client.close()


@serial_interface_control.group()
@click.pass_context
def set_te_ta_local_data_flow_control(ctx):
    """Commands related to setting the TE-TA local data flow control."""
    pass


@set_te_ta_local_data_flow_control.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read TE-TA local data flow control."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.serialInterfaceControlCommands303SetTeTaLocalDataFlowControlRead()
    )
    print(response if status else "Error")
    client.close()


@set_te_ta_local_data_flow_control.command()
@click.pass_context
@click.option(
    "-dce_by_dte",
    type=int,
    default=0,
    show_default=True,
    help=f"0 None \n2 RTS flow control",
)
@click.option(
    "-dte_by_dce",
    type=int,
    default=0,
    show_default=True,
    help=f"0 None \n2 CTS flow control",
)
def write(ctx, dce_by_dte: int, dte_by_dce: int):  # type: ignore[reportRedeclaration]
    """Write TE-TA local data flow control."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.serialInterfaceControlCommands303SetTeTaLocalDataFlowControlWrite(
            dce_by_dte, dte_by_dce
        )
    )
    print(response if status else "Error")
    client.close()


@serial_interface_control.group()
@click.pass_context
def set_te_ta_fixed_local_rate(ctx):
    """Commands related to setting the TE-TA fixed local rate."""
    pass


@set_te_ta_fixed_local_rate.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read TE-TA fixed local rate."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.serialInterfaceControlCommands304SetTeTaFixedLocalRateRead()
    )
    print(response if status else "Error")
    client.close()


@set_te_ta_fixed_local_rate.command()
@click.pass_context
@click.option(
    "-rate",
    type=int,
    default=0,
    show_default=True,
    help=f"0 (Adaptive baud rate) \n4800 \n9600 \n19200 \n38400 \n57600 \n115200 \n230400 \n460800 \n921600",
)
def write(ctx, rate: int):  # type: ignore[reportRedeclaration]
    """Write TE-TA fixed local rate."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.serialInterfaceControlCommands304SetTeTaFixedLocalRateWrite(rate)
    )
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def status_control_commands(ctx):
    """Group for status control commands."""
    pass


@status_control_commands.command("query-mobile-equipe-activity-status")
@click.pass_context
def query_mobile_equipe_activity_status(ctx):
    """Query Mobile Equipement Activity Status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40100QueryMobileEquipmentActivityStatus()
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("report-Extended-Error")
@click.pass_context
def report_extended_error(ctx):
    """Report Extended Error."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40200ReportExtendedError()
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-extended-settings")
@click.pass_context
def configure_extended_settings(ctx):
    """Configure Extended Settings."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40300ConfigureExtendedSettings()
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-gprs-attach-mode")
@click.pass_context
@click.option(
    "--attach_mode",
    "-m",
    type=int,
    required=True,
    help=f"0 Manual attach \n1 Auto attach",
)
@click.option(
    "--effect",
    "-e",
    type=int,
    required=True,
    help=f"0 Take effect after UE reboots (currently not supported) \n1 Take effect immediately",
)
def configure_gprs_attach_mode(ctx, attach_mode: int, effect: int):
    """Configure GPRS Attach Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40301ConfigureGprsAttachMode(
        attach_mode, effect
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-network-search-mode")
@click.pass_context
@click.option(
    "--scan_mode",
    "-m",
    type=int,
    required=True,
    help=f"0 Automatic (LTE/WCDMA/GSM) \n1 GSM only \n2 WCDMA only \n3 LTE only",
)
def configure_network_search_mode(ctx, scan_mode: int):
    """Configure Network Search Mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40302ConfigureNetworkSearchMode(
        scan_mode
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-network-serching-sequence")
@click.pass_context
@click.option(
    "--scanseq",
    "-s",
    type=int,
    required=True,
    help="""
0                   Automatic (LTE/WCDMA/GSM)
1                   GSM only
2                   WCDMA only
3                   LTE only
4                   GSM/WCDMA/LTE
5                   WCDMA/GSM/LTE
6                   LTE/WCDMA
7                   LTE/GSM
8                   WCDMA/LTE
9                   WCDMA/GSM
10                  GSM/LTE
11                  GSM/WCDMA
12                  LTE/WCDMA/GSM
""",
)
def configure_network_serching_sequence(ctx, scanseq: int):
    """Configure Network Searching Sequence."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40303ConfigureNetworkSearchingSequence(scanseq)
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-relevant-functions-in-roaming-state")
@click.pass_context
@click.option(
    "--roam_modeex",
    "-m",
    type=int,
    required=True,
    help="""
<roam_modeex>       Integer type. Roaming operating mode. Range: 0–3. Default value: 0. Each bit corresponds to a feature. Set the bit to 1 indicates enabling the corresponding function.
0                   Normal operating mode, unlimited service
Bit 1               Disable dial-up internet access function when UE is in roaming state
Bit 2               Disable voice call function when UE is in roaming state
                    The above reports can be combined at will.
""",
)
def configure_relevant_functions_in_roaming_state(ctx, roam_modeex: int):
    """Configure Relevant Functions in Roaming State."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40304ConfigureRelevantFunctionsInRoamingState(
            roam_modeex
        )
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-service-domain")
@click.pass_context
@click.option(
    "--service",
    "-s",
    type=int,
    required=True,
    help="""
0                   CS only
1                   PS only
2                   CS & PS
""",
)
@click.option(
    "--effect",
    "-e",
    type=int,
    required=True,
    help="""
<effect>            Integer format. When to take effect
0                   Take effect after UE reboots (currently not supported)
1                   Take effect immediately
""",
)
def configure_service_domain(ctx, service: int, effect: int):
    """Configure Service Domain."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40305ConfigureServiceDomain(
        service, effect
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-band")
@click.pass_context
@click.option(
    "--band",
    "-b",
    type=int,
    required=True,
    help="""
00000000            No change
00000001            GSM900
00000002            GSM1800
00000010            WCDMA 2100
00000020            WCDMA 1900
00000040            WCDMA 850
00000080            WCDMA 900
0000FFFF            Any frequency band
""",
)
@click.option(
    "--ltebandval",
    "-l",
    type=int,
    required=True,
    help="""
0x1 (CM_BAND_PREF_LTE_EUTRAN_BAND1)                     LTE B1
0x2 (CM_BAND_PREF_LTE_EUTRAN_BAND2)                     LTE B2
0x4 (CM_BAND_PREF_LTE_EUTRAN_BAND3)                     LTE B3
0x8 (CM_BAND_PREF_LTE_EUTRAN_BAND4)                     LTE B4
0x10 (CM_BAND_PREF_LTE_EUTRAN_BAND5)                    LTE B5
0x40 (CM_BAND_PREF_LTE_EUTRAN_BAND7)                    LTE B7
0x80 (CM_BAND_PREF_LTE_EUTRAN_BAND8)                    LTE B8
0x80000 (CM_BAND_PREF_LTE_EUTRAN_BAND20)                LTE B20
0x8000000 (CM_BAND_PREF_LTE_EUTRAN_BAND28)              LTE B28
0x40000000 (CM_BAND_PREF_LTE_EUTRAN_BAND31)             LTE B31
0x200000000(CM_BAND_PREF_LTE_EUTRAN_BAND34)             LTE B34
0x2000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND38)           LTE B38
0x4000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND39)           LTE B39
0x8000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND40)           LTE B40
0x10000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND41)          LTE B41
0x20000000000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND66)    LTE B66
0x800000000000000000 (CM_BAND_PREF_LTE_EUTRAN_BAND72)   LTE B72
0x7FFFFFFFFFFFFFFFF (CM_BAND_PREF_ANY)                  Any frequency band
""",
)
def configure_band(ctx, band: int, ltebandval: int):
    """Configure Band."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40306ConfigureBand(band, ltebandval)
    print(response if status else "Error")
    client.close()


@status_control_commands.command("specify-ri-behavior-when-urc-are-present")
@click.pass_context
@click.option(
    "--type_ri",
    "-t",
    type=str,
    required=True,
    help="""
"off"               No change. Ring indicator keeps inactive
"pulse"             Pulse. Pulse width determined by <pulse_duration    
""",
)
@click.option(
    "--pulse_duration",
    "-p",
    type=int,
    required=True,
    help="""
The width of pulse. This parameter is effect only when <typeRI> is''pulse''. Range: 5–2000. Default value: 120. Unit: ms.
""",
)
@click.option(
    "--pulse_count",
    "-c",
    type=int,
    required=True,
    help="""
The count of pulse. This parameter is only meaningful when <typeRI> is ''pulse''.
The interval time between two pulses is equal to <pulse_duration>. Range: 1–5. Default value: 1. Unit: s.
""",
)
def specify_ri_behavior_when_urc_are_present(
    ctx, type_ri: str, pulse_duration: int, pulse_count: int
):
    """Specify RI Behavior When URC Are Present."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40307SpecifyRiBehaviorWhenOtherUrcsArePresented(
            type_ri, pulse_duration, pulse_count
        )
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("delay-time-of-urc-indication")
@click.pass_context
@click.option(
    "--time",
    "-t",
    type=int,
    required=True,
    help="""
Set the delay time of URC indication when ring indicator pulse starts.RI behavior when URCs are presented. Range: 0–120. Unit: ms.
0                   No delay.
""",
)
def delay_time_of_urc_indication(ctx, time: int):
    """Delay Time of URC Indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40308SetDelayTimeOfUrcIndication(
        time
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("enable-disable-urc-cache-function")
@click.pass_context
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
0                   Disable URC cache function.
1                   Enable URC cache function.
""",
)
def enable_disable_urc_cache_function(ctx, enable: int):
    """Enable Disable URC Cache Function."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40309EnableDisableUrcCacheFunction(
        enable
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-the-network-card-type-interface")
@click.pass_context
@click.option(
    "--net" "-n",
    type=int,
    required=True,
    help="""
1                   ECM interface
3                   RNIDS interface
""",
)
def configure_the_network_card_type_interface(ctx, net: int):
    """Configure the Network Card Type Interface."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40310ConfigureTheNetworkCardTypeInterface(net)
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("enable-disable--the-ppp-term--frame-sending")
@click.pass_context
@click.option(
    "--flag" "-f",
    type=int,
    required=True,
    help="""
0                   Disable TERM frame sending when hang up PPP by module itself.
1                   Enable TERM frame sending when hang up PPP by module itself.    
""",
)
def enable_disable_the_ppp_term_frame_sending(ctx, flag: int):
    """Enable Disable the PPP Term Frame Sending."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40311EnableDisableThePppTermFrameSending(flag)
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("enable-disable-airplane-mode-control-via-wdisable")
@click.pass_context
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
0                   Disable the airplane mode control via W_DISABLE# pin
1                   Enable the airplane mode control via W_DISABLE# pin. The module enters airplane mode when W_DISABLE# pin is active and exit airplane mode when it is inactive. AT+CFUN=1 is not allowed to be used to enable the module to exit airplane mode when the W_DISABLE# pin is active. Unsolicited result code +QIND: airplanestatus,<status> is reported when the status of W_DISABLE# pin changes
""",
)
@click.option(
    "--status",
    "-s",
    type=int,
    required=True,
    help="""
0                   Exit airplane mode
1                   Enter airplane mode
""",
)
def enable_disable_airplane_mode_control_via_wdisable(ctx, enable: int, status: int):
    """Enable Disable Airplane Mode Control via W_DISABLE."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40312EnableDisableAirplaneModeControlViaW_DISABLE(
            enable, status
        )
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("ring-line-behavior-of-ring")
@click.pass_context
@click.option(
    "--type_ri",
    "-t",
    type=str,
    required=True,
    help="""
"off"               No change. Ring line keeps inactive.
"pulse"             Pulse. Pulse width is determined by <pulse_duration>
""",
)
@click.option(
    "--pulse_duration",
    "-p",
    type=int,
    required=True,
    help="""
The width of pulse. This parameter is meaningful only when <typeRI> is ''pulse''. If this parameter is not needed, you can set it to null. Range: 5–2000.
Default value: 120. Unit: ms.
""",
)
@click.option(
    "--pulse_count",
    "-c",
    type=int,
    required=True,
    help="""
he count of pulse. This parameter is meaningful only when <typeRI>
is ''pulse''. The interval time between two pulse is equal to <pulse_duration>.
Range: 1–5. Default value: 1.    
""",
)
def ring_line_behavior_of_ring(
    ctx, type_ri: str, pulse_duration: int, pulse_count: int
):
    """Ring Line Behavior of Ring."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40313RingLineBehaviorOfRing(
        type_ri, pulse_duration, pulse_count
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("ri-signal-output-carrier")
@click.pass_context
@click.option(
    "--ri-signal-type",
    "-t",
    type=str,
    required=True,
    help="""
"respective"        The ring indicator behaves on the port where URC is presented. For
                    example, if a URC is presented on UART port, it is physical ring
                    indicator. If the URC is presented on USB port, it is virtual ring
                    indicator. If the URC is presented on USB AT port, and the port does
                    not support ring indicator, then there will be no ring indicator.
                    AT+QURCCFG="urcport" can get the port on which URC is
                    presented.
"physical"          No matter which port URC is presented on, URC only causes the
                    behavior of physical ring indicator.    
""",
)
def ri_signal_output_carrier(ctx, ri_signal_type: str):
    """RI Signal Output Carrier."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40314RiSignalOutputCarrier(
        ri_signal_type
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-baud-rate")
@click.pass_context
@click.option(
    "--ipr",
    "-r",
    type=int,
    required=True,
    help="""
4800
9600
19200
38400
57600
115200
230400
460800
921600
""",
)
def configure_baud_rate(ctx, ipr: int):
    """Configure Baud Rate."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40315ConfigureBaudRate(ipr)
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-working-mode-of-nic")
@click.pass_context
@click.option(
    "--nat",
    "-n",
    type=int,
    required=True,
    help="""
0               Routing mode
1               NIC mode    
""",
)
def configure_working_mode_of_nic(ctx, nat: int):
    """Configure Working Mode of NIC."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40316ConfigureWorkingModeOfNic(nat)
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-ims-function")
@click.pass_context
@click.option(
    "--ims-conf",
    "-i",
    type=int,
    required=True,
    help="""
0               IMS function is not configured
1               Enable IMS function
2               Disable IMS function
""",
)
@click.option(
    "--volte-cap",
    "-v",
    type=int,
    required=True,
    help="""
0               VoLTE is not supported
1               VoLTE is supported
""",
)
def configure_ims_function(ctx, ims_conf: int, volte_cap: int):
    """Configure IMS Function."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40317ConfigureImsFunction(
        ims_conf, volte_cap
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("configure-connection-expiration-time-in-http-fota")
@click.pass_context
@click.option(
    "--timeout",
    "-t",
    type=int,
    required=True,
    help="""
The connection expiration time in HTTP FOTA download.
Range: 10–180. Default value: 60. Unit: second.
""",
)
def configure_connection_expiration_time_in_http_fota(ctx, timeout: int):
    """Configure Connection Expiration Time in HTTP FOTA."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.statusControlCommands40318ConfigureConnectionExpirationTimeInHttpFota(
            timeout
        )
    )
    print(response if status else "Error")
    client.close()


@status_control_commands.command("control-urc-indication")
@click.pass_context
@click.option(
    "--urc-type",
    "-u",
    type=str,
    required=True,
    help="""
"all"               Main switch of all URCs. Default is ON.
"csq"               Indication of signal strength and channel bit error rate change (similar to
                    AT+CSQ). Default is OFF. If this configuration is ON, present:
                    +QIND: "csq",<rssi>,<ber>
"datastatus"        Indication of data service status. Default is OFF. If this configuration
                    is ON, present:
                    +QIND: "datastatus",<suspended>,<reason>
                    <reason> is number format as below:
                    0 SUSPEND_NO_CAUSE
                    1 SUSPEND_BY_RAU_ATTACH
                    2 SUSPEND_BY_LAU
                    3 SUSPEND_BY_TAU
                    4 SUSPEND_BY_CS_SERVICE
                    5 SUSPEND_BY_DS_OPERATION
                    6 SUSPEND_BY_POWERUP
"mode"              Indication of network main mode and sub mode. Default is OFF. If this
                    configuration is ON, present:
                    ^MODE:<main_mode>,<sub_mode>
                    <main_mode> is an integer type listed as below:
                    0 SYSINFO_SYSTEMO_MODE_NO_SERVICE
                    1 SYSINFO_SYSTEMO_MODE_RESERVED_1
                    2 SYSINFO_SYSTEMO_MODE_RESERVED_2
                    3 SYSINFO_SYSTEMO_MODE_GSM_GPRS
                    5 SYSINFO_SYSTEMO_MODE_WCDMA
                    17 SYSINFO_SYSTEMO_MODE_LTE
                    <sub_mode> is an integer type listed as below:
                    0 SYSINFO_SYSTEMO_SUBMODE_NO_SERVICE
                    1 SYSINFO_SYSTEMO_SUBMODE_GSM
                    3 SYSINFO_SYSTEMO_SUBMODE_GSM_EGPRS
                    5 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSDPA
                    6 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSUPA
                    7 SYSINFO_SYSTEMO_SUBMODE_UTRAN_HSPA
                    8 SYSINFO_SYSTEMO_SUBMODE_UTRAN
                    17 SYSINFO_SYSTEMO_SUBMODE_EUTRAN
"smsfull"           SMS storage full indication. Default is OFF. If this configuration is ON,
                    present:
                    +QIND: "smsfull",<storage>
"smsincoming"       Incoming message indication. Default is ON. Related URC list:
                    +CMTI, +CMT, +CDS
"act"               Indication of network access technology change. Default is OFF. If this
                    configuration is ON, present:
                    +QIND: "act",<actvalue>
                    <actvalue> is string format. The values are as below:
                    ''GSM''
                    ''EGPRS''
                    ''WCDMA''
                    ''HSDPA''
                    ''HSUPA''
                    ''HSDPA&HSUPA''
                    ''LTE''
                    ''UNKNOWN''
                    The examples of URC are as below:
                    +QIND: "act","HSDPA&HSUPA"
                    +QIND: "act","UNKNOWN"
                    The description of ''act'' is as below:
                    1. If module does not register on network, <actvalue> would be
                    ''UNKNOWN''.
                    2. If this configuration is ON, the URC of "act" will be reported
                    immediately. Only when the network access technology changes,
                    a new URC will be reported.
"sqi"               Indication of reference signal receiving power, reference signal receiving
                    quality and signal to interference plus noise ratio change. Default is OFF.
                    If this configuration is ON, present:
                    +QIND: "SQI",<RSRP>,<RSRQ>,<SINR>
                    <RSRP>
                    Integer type. Reference signal receiving power. Unit: dBm.
                    (See 3GPP 36.214 Chapter 5.1.1).
                    <RSRQ>
                    Integer type. Reference signal receiving quality. Unit: dB.
                    (See 3GPP 36.214 Chapter 5.1.3).
                    <SINR>
                    Integer type. Signal to interference plus noise ratio.
                    Range: -20–30. Unit: dB.
"phonebook"         Incoming phonebook indication. Default is ON. Related URC list:
                    +QIND: PB DONE
"ring"              Incoming call indication. Default is ON. Related URC list:
                    RING
"nocarrier"         Incoming hang up call indication. Default is ON. Related URC list:
                    NO CARRIER    
""",
)
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
0                   OFF
1                   ON
""",
)
@click.option(
    "--savetonvram",
    "-s",
    type=int,
    required=True,
    help="""
0                   Not save
1                   Save
""",
)
def control_urc_indication(ctx, urc_type: str, enable: int, savetonvram: int):
    """Control URC Indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.statusControlCommands40400ControlUrcIndication(
        urc_type, enable, savetonvram
    )
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def sim_related_commands(ctx):
    """Group for SIM related commands."""
    pass


@sim_related_commands.command("request-international-mobile-subscriber-identity")
@click.pass_context
def request_international_mobile_subscriber_identity(ctx):
    """Request International Mobile Subscriber Identity."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.simRelatedCommands501RequestInternationalMobileSubscriberIdentity()
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("facility-lock")
@click.pass_context
@click.option(
    "--facility",
    "-f",
    type=str,
    required=True,
    help="""
''SC''
(U)SIM (lock SIM/UICC card installed in the currently selected card slot)
(SIM/UICC asks password in MT power-up and when this lock command
issued).
''AO''
BAOC (Bar All Outgoing Calls) (see 3GPP TS 22.088 clause 1).
''OI''
BOIC (Bar Outgoing International Calls) (see 3GPP TS 22.088 clause 1).
''OX''
BOIC-exHC (Bar Outgoing International Calls except to Home Country) (see
3GPP TS 22.088 clause 1).
''AI''
BAIC (Bar All Incoming Calls) (see 3GPP TS 22.088 clause 2).
''IR''
BIC-Roam (Bar Incoming Calls when Roaming outside the home country) (see
3GPP TS 22.088 clause 2).
''AB''
All Barring services (see 3GPP TS 22.030) (applicable only for <mode>=0).
''AG''
All outgoing barring services (see 3GPP TS 22.030) (applicable only for
<mode>=0).
''AC''
All incoming barring services (see 3GPP TS 22.030) (applicable only for
<mode>=0).
''FD''
(U)SIM card or active application in the UICC (GSM or USIM) fixed dialing
memory feature (If PIN2 authentication has not been done during the current
session, PIN2 is required as <passwd>).
''PF''
Lock Phone to the very first inserted SIM/UICC card (also referred in the present
document as PH-FSIM) (MT asks password when other SIM/UICC cards are
inserted).
''PN''
Network Personalization (see 3GPP TS 22.022).
''PU''
Network Subset Personalization (see 3GPP TS 22.022).
''PP''
Service Provider Personalization (see 3GPP TS 22.022).
''PC''
Corporate Personalization (see 3GPP TS 22.022).
""",
)
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""                        
0 Unlock
1 Lock
2 Query status
""",
)
@click.option(
    "--passwd",
    "-p",
    type=str,
    required=True,
    help="password",
)
@click.option(
    "--clas",
    "-c",
    type=int,
    required=True,
    help="""
1   Voice
2   Data
4   FAX
7   All telephony except SMS
8   Short message service
16  Data circuit synchronization
32  Data circuit asynchronization
""",
)
@click.option(
    "--status",
    "-s",
    type=int,
    required=True,
    help="""
0   Off
1   On    
""",
)
def facility_lock(ctx, facility: str, mode: int, passwd: str, clas: int, status: int):
    """Facility Lock."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands502FacilityLock(
        facility, mode, passwd, clas, status
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("enter-pin")
@click.pass_context
@click.option(
    "--code",
    "-c",
    type=str,
    required=True,
    help="""
READY
SIM PIN
SIM PUK
SIM PIN2
SIM PUK2
PH-NET PIN
PH-NET PUK
MT is not pending for any password
MT is waiting for (U)SIM PIN to be given
MT is waiting for (U)SIM PUK to be given
MT is waiting for (U)SIM PIN2 to be given
MT is waiting for (U)SIM PUK2 to be given
MT is waiting for network personalization password to be given
MT is waiting for network personalization unblocking password
to be given
PH-NETSUB PIN
MT is waiting for network subset personalization password to
be given
PH-NETSUB PUK
MT is waiting for network subset personalization unblocking
password to be given
PH-SP PIN
MT is waiting for service provider personalization password to
be given
PH-SP PUK
MT is waiting for service provider personalization unblocking
password to be given
PH-CORP PIN
MT is waiting for corporate personalization password to be given
PH-CORP PUK
MT is waiting for corporate personalization unblocking password
to be given      
""",
)
@click.option(
    "--pin",
    "-p",
    type=str,
    required=True,
    help="""
The PIN of the SIM card.Password. If the requested password is a PUK, such as (U)SIM PUK1,
PH-FSIM PUK or other passwords, then <pin> must be followed by <newpin>.    
""",
)
@click.option(
    "--newpin",
    "-n",
    type=str,
    required=True,
    help="""
A new password required if the requested code is a PUK.
""",
)
def enter_pin(ctx, code: str, pin: str, newpin: str):
    """Enter PIN."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands503EnterPin(code, pin, newpin)
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("change-password")
@click.pass_context
@click.option(
    "--fac",
    "-f",
    type=str,
    required=True,
    help="""
''SC''      (U)SIM (lock SIM/UICC card) (SIM/UICC asks password in MT power-up and
            when this lock command is issued)
''AO''      BAOC (Bar All Outgoing Calls, see 3GPP TS 22.088 clause 1)
''OI'       BOIC (Bar Outgoing International Calls, see 3GPP TS 22.088 clause 1)
''OX''      BOIC-exHC (Bar Outgoing International Calls except to Home Country, see
            3GPP TS 22.088 clause 1)
''AI'       BAIC (Bar All Incoming Calls, see 3GPP TS 22.088 clause 2)
''IR''      BIC-Roam (Bar Incoming Calls when Roaming outside the home country,
            see 3GPP TS 22.088 clause 2)
''AB''      All barring services (see 3GPP TS 22.030, applicable only for <mode>=0)
''AG''      All outgoing barring services (see 3GPP TS 22.030, applicable only for
            <mode>=0)
''AC'       All incoming barring services (see 3GPP TS 22.030, applicable only for
            <mode>=0)
''P2''      (U)SIM PIN2
""",
)
@click.option(
    "--pwdlength",
    "-l",
    type=int,
    required=True,
    help="""
Maximum length of password.
""",
)
@click.option(
    "--oldpwd",
    "-o",
    type=str,
    required=True,
    help="""
Password specified for the facility from the user interface or with command.
""",
)
@click.option("--newpwd", "-n", type=str, required=True, help="""New password.""")
def change_password(ctx, fac: str, pwdlength: int, oldpwd: str, newpwd: str):
    """Change Password."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands504ChangePassword(
        fac, pwdlength, oldpwd, newpwd
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("generic-usim-access")
@click.pass_context
@click.option(
    "--length",
    "-l",
    type=int,
    required=True,
    help="""Length of <command> or <response> string.""",
)
@click.option(
    "--command",
    "-c",
    type=str,
    required=True,
    help="""Command transferred by the MT to the (U)SIM in the format as described in 3GPP TS 51.011.""",
)
def generic_usim_access(ctx, length: int, command: str):
    """Generic USIM Access."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands505GenericUsimAccess(length, command)
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("restricted-usim-access")
@click.pass_context
@click.option(
    "--command",
    "-c",
    type=int,
    required=True,
    help="""
176     READ BINARY
178     READ RECORD
192     GET RESPONSE
214     UPDATE BINARY
220     UPDATE RECORD
242     STATUS
""",
)
@click.option(
    "--filed",
    "-f",
    type=int,
    required=True,
    help="""Identifier for an elementary data file on (U)SIM, if used by <command>.""",
)
@click.option(
    "-p1",
    type=int,
    required=True,
    help="""
Parameters transferred by the MT to the (U)SIM. These
parameters are mandatory for every command, except GET RESPONSE and
STATUS. The values are described in 3GPP TS 51.011.
Information which shall be written to the (U)SIM (hexadecimal character
format; see AT+CSCS).
""",
)
@click.option(
    "-p2",
    type=int,
    required=True,
    help="""
Parameters transferred by the MT to the (U)SIM. These
parameters are mandatory for every command, except GET RESPONSE and
STATUS. The values are described in 3GPP TS 51.011.
Information which shall be written to the (U)SIM (hexadecimal character
format; see AT+CSCS).
""",
)
@click.option(
    "-p3",
    type=int,
    required=True,
    help="""
Parameters transferred by the MT to the (U)SIM. These
parameters are mandatory for every command, except GET RESPONSE and
STATUS. The values are described in 3GPP TS 51.011.
Information which shall be written to the (U)SIM (hexadecimal character
format; see AT+CSCS).
""",
)
@click.option(
    "--data",
    "-d",
    type=int,
    required=True,
    help="""
Information which shall be written to the (U)SIM (hexadecimal character
format; see AT+CSCS).
""",
)
@click.option(
    "--path-id",
    "-i",
    type=int,
    required=True,
    help="""
The directory path of an elementary file on a UICC in hexadecimal format.
""",
)
def restricted_usim_access(
    ctx, command: int, filed: int, p1: int, p2: int, p3: int, data: int, path_id: int
):
    """Restricted USIM Access."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands506RestrictedUsimAccess(
        command, filed, p1, p2, p3, data, path_id
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("show-iccid")
@click.pass_context
def show_iccid(ctx):
    """Show ICCID."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands507ShowIccid()
    print(response if status else "Error")
    client.close()


@sim_related_commands.group()
@click.pass_context
def display_pin_remainder_counter(ctx):
    """Group for display pin remainder counter."""
    pass


@display_pin_remainder_counter.command("display-pin-remainder-counter")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Display PIN remainder counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands508DisplayPinRemainderCounterRead()
    print(response if status else "Error")
    client.close()


@display_pin_remainder_counter.command("reset-pin-remainder-counter")
@click.pass_context
@click.option(
    "--facility",
    "-f",
    type=str,
    required=True,
    help="""
''SC''      (U)SIM PIN
''P2''      (U)SIM PIN2
""",
)
def write(ctx, facility: str):  # type: ignore[reportRedeclaration]
    """Reset PIN remainder counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands508DisplayPinRemainderCounterWrite(
        facility
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.command("query-initialization-status-of-usim-card")
@click.pass_context
def query_initialization_status_of_usim_card(ctx):
    """Query Initialization Status of USIM Card."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands509QueryInitializationStatusOfUsimCard()
    print(response if status else "Error")
    client.close()


@sim_related_commands.group()
@click.pass_context
def usim_card_detection(ctx):
    """Group for USIM card detection."""
    pass


@usim_card_detection.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read USIM card detection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands510UsimCardDetectionRead()
    print(response if status else "Error")
    client.close()


@usim_card_detection.command()
@click.pass_context
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
Enable or disable (U)SIM card detection
0   Disable
1   Enable    
""",
)
@click.option(
    "--insert-level",
    "-i",
    type=int,
    required=True,
    help="""
The level of (U)SIM detection pin when a (U)SIM card is inserted
                            0   Low level
                            1   High level
""",
)
def write(ctx, enable: int, insert_level: int):  # type: ignore[reportRedeclaration]
    """Write USIM card detection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands510UsimCardDetectionWrite(
        enable, insert_level
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.group()
@click.pass_context
def usim_card_insertion_status_report(ctx):
    """Group for USIM card insertion status report."""
    pass


@usim_card_insertion_status_report.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read USIM card insertion status report."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands511UsimCardInsertionStatusReportRead()
    print(response if status else "Error")
    client.close()


@usim_card_insertion_status_report.command()
@click.pass_context
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
Integer type. Enable or disable (U)SIM card insertion status report. If it is enabled,
when (U)SIM card is removed or inserted, the URC +QSIMSTAT:
<enable>,<inserted_status> will be reported.
0       Disable
1       Enable
""",
)
def write(ctx, enable: int):  # type: ignore[reportRedeclaration]
    """Write USIM card insertion status report."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands511UsimCardInsertionStatusReportWrite(
        enable
    )
    print(response if status else "Error")
    client.close()


@sim_related_commands.group()
@click.pass_context
def select_usim_card(ctx):
    """Group for select USIM card."""
    pass


@select_usim_card.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read select USIM card."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands512SelectUsimCardRead()
    print(response if status else "Error")
    client.close()


@select_usim_card.command()
@click.pass_context
@click.option(
    "--sim-id",
    "-s",
    type=int,
    required=True,
    help="""
Integer type. (U)SIM card ID.
0 SIM1
1 SIM2
""",
)
def write(ctx, sim_id: int):  # type: ignore[reportRedeclaration]
    """Write select USIM card."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.simRelatedCommands512SelectUsimCardWrite(sim_id)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def network_service_commands(ctx):
    """Group for network services commands."""
    pass


@network_service_commands.group()
@click.pass_context
def operators_selection(ctx):
    """Group for operator selection."""
    pass


@operators_selection.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read operator selection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands601OperatorSelectionRead()
    print(response if status else "Error")
    client.close()


@operators_selection.command()
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
0               Automatic mode. <oper> field is ignored
1               Manual operator selection. <oper> field shall be present and <Act> optionally
2               Manually deregister from network
3               Set only <format> (for AT+COPS? Read Command), and do not attempt
                registration/deregistration (<oper> and <Act> fields are ignored). This value is
                invalid in the response of Read Command.
4               Manual/automatic selection. <oper> field shall be presented. If manual selection
                fails, automatic mode (<mode>=0) is entered
""",
)
@click.option(
    "--format",
    "-f",
    type=int,
    required=True,
    help="""
0               Automatic mode. <oper> field is ignored
1               Manual operator selection. <oper> field shall be present and <Act> optionally
2               Manually deregister from network
3               Set only <format> (for AT+COPS? Read Command), and do not attempt
                registration/deregistration (<oper> and <Act> fields are ignored). This value is
                invalid in the response of Read Command.
4               Manual/automatic selection. <oper> field shall be presented. If manual selection
                fails, automatic mode (<mode>=0) is entered    
""",
)
@click.option(
    "--oper",
    "-o",
    type=str,
    required=True,
    help="""
String type. Operator in format as per <format>.
""",
)
@click.option(
    "--act",
    "-a",
    type=int,
    required=True,
    help="""
        0               GSM
        2               UTRAN
        3               GSM W/EGPRS
        4               UTRAN W/HSDPA
        5               UTRAN W/HSUPA
        6               UTRAN W/HSDPA and HSUPA
        7               E-UTRAN
        8               UTRAN HSPA+
""",
)
def write(ctx, mode: int, format: int, oper: str, act: int):  # type: ignore[reportRedeclaration]
    """Write operator selection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands601OperatorSelectionWrite(
        mode, format, oper, act
    )
    print(response if status else "Error")
    client.close()


@network_service_commands.group()
@click.pass_context
def domain_network_registration_status(ctx):
    """Group for domain network registration status."""
    pass


@domain_network_registration_status.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read domain network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.networkServiceCommands602DomainNetworkRegistrationStatusRead()
    )
    print(response if status else "Error")
    client.close()


@domain_network_registration_status.command()
@click.pass_context
@click.option(
    "--enable",
    "-e",
    type=int,
    required=True,
    help="""
0               Disable network registration unsolicited result code
1               Enable network registration unsolicited result code: +CREG: <stat>
2               Enable network registration unsolicited result code with location information:
                +CREG: <stat>[,<lac>,<ci>[,<Act>]]    
""",
)
def write(ctx, enable: int):  # type: ignore[reportRedeclaration]
    """Write domain network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.networkServiceCommands602DomainNetworkRegistrationStatusWrite(enable)
    )
    print(response if status else "Error")
    client.close()


@network_service_commands.command("signal-quality-report")
@click.pass_context
def signal_quality_report(ctx):
    """Signal Quality Report."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands603SignalQualityReport()
    print(response if status else "Error")
    client.close()


@network_service_commands.group()
@click.pass_context
def preferred_operator_list(ctx):
    """Group for preferred operator list."""
    pass


@preferred_operator_list.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read preferred operator list."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands604PreferredOperatorListRead()
    print(response if status else "Error")
    client.close()


@preferred_operator_list.command()
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="""
Integer type. The order number of operator in the (U)SIM preferred operator list
""",
)
@click.option(
    "--format",
    "-f",
    type=int,
    required=True,
    help="""
0                   Long format alphanumeric <oper>
1                   Short format alphanumeric <oper>
2                   Numeric <oper>
""",
)
@click.option(
    "--oper",
    "-o",
    type=str,
    required=True,
    help="""
String type. <format> indicates the format is alphanumeric or numeric (see
AT+COPS).
""",
)
@click.option(
    "--gsm",
    "-g",
    type=int,
    required=True,
    help="""
0                   Access technology is not selected
1                   Access technology is selected    
""",
)
@click.option(
    "--gsm-compact",
    "-c",
    type=int,
    required=True,
    help="""
0                   Access technology is not selected
1                   Access technology is selected
""",
)
@click.option(
    "--utran",
    "-u",
    type=int,
    required=True,
    help="""
0                   Access technology is not selected
1                   Access technology is selected    
""",
)
@click.option(
    "--e-utran",
    "-e",
    type=int,
    required=True,
    help="""
0                   Access technology is not selected
1                   Access technology is selected
""",
)
def write(  # type: ignore[reportRedeclaration]
    ctx,
    index: int,
    format: int,
    oper: str,
    gsm: int,
    gsm_compact: int,
    utran: int,
    e_utran: int,
):
    """Write preferred operator list."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands604PreferredOperatorListWrite(
        index, format, oper, gsm, gsm_compact, utran, e_utran
    )
    print(response if status else "Error")
    client.close()


@network_service_commands.command("read-operator-names")
@click.pass_context
def read_operator_names(ctx):
    """Read Operator Names."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands605ReadOperatorNames()
    print(response if status else "Error")
    client.close()


@network_service_commands.group()
@click.pass_context
def automatic_time_zone_update(ctx):
    """Group for automatic time zone update."""
    pass


@automatic_time_zone_update.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read automatic time zone update."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands606AutomaticTimeZoneUpdateRead()
    print(response if status else "Error")
    client.close()


@automatic_time_zone_update.command()
@click.pass_context
@click.option(
    "--onoff",
    "-o",
    type=int,
    required=True,
    help="""
0                   Disable automatic time zone update via NITZ.
1                   Enable automatic time zone update via NITZ and update GMT time to URC
3                   Enable automatic time zone update via NITZ and update LOCAL time to RTC    
""",
)
def write(ctx, onoff: int):  # type: ignore[reportRedeclaration]
    """Write automatic time zone update."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands606AutomaticTimeZoneUpdateWrite(
        onoff
    )
    print(response if status else "Error")
    client.close()


@network_service_commands.group()
@click.pass_context
def time_zone_reporting(ctx):
    """Group for time zone reporting."""
    pass


@time_zone_reporting.command()
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read time zone reporting."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands607TimeZoneReportingRead()
    print(response if status else "Error")
    client.close()


@time_zone_reporting.command()
@click.pass_context
@click.option(
    "--reporting",
    "-r",
    type=int,
    required=True,
    help="""
0                   Disable time zone reporting of changed event
1                   Enable time zone reporting of changed event by unsolicited result code:
                    +CTZV: <tz>
2                   Enable extended time zone reporting by unsolicited result code:
                    +CTZE: <tz>,<dst>,<time>   
""",
)
def write(ctx, reporting: int):  # type: ignore[reportRedeclaration]
    """Write time zone reporting."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands607TimeZoneReportingWrite(reporting)
    print(response if status else "Error")
    client.close()


@network_service_commands.command("obtain-the-latest-time-synchronized-through-network")
@click.pass_context
def obtain_the_latest_time_synchronized_through_network(ctx):
    """Obtain the latest time synchronized through network."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.networkServiceCommands608ObtainTheLatestTimeSynchronizedThroughNetwork()
    )
    print(response if status else "Error")
    client.close()


@network_service_commands.command("query-network-information")
@click.pass_context
def query_network_information(ctx):
    """Query Network Information."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.networkServiceCommands609QueryNetworkInformation()
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def call_related_commands(ctx):
    """Group for call related commands."""
    pass


@call_related_commands.command("answer-an-incoming-call")
@click.pass_context
def answer_an_incoming_call(ctx):
    """Answer an incoming call."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands701AnswerAnIncomingCall()
    print(response if status else "Error")
    client.close()


@call_related_commands.command("mobile-originated-call-to-dial-a-number")
@click.pass_context
@click.option(
    "--number",
    "-n",
    type=str,
    required=True,
    help="""
String of dialing digits and optionally V.25ter modifiers.
Dialing digits: 0–9, * , #, +, A, B, C
Following V.25ter modifiers are ignored: ,(comma), T, P, !, W, @
""",
)
@click.option(
    "--mgsm",
    "-m",
    type=str,
    required=True,
    help="""
I               Activate CLIR (Disable presentation of own number to the called party)
i               Deactivate CLIR (Enable presentation of own number to the called party)
G               Activate closed user group invocation for this call only
g               Deactivate closed user group invocation for this call only    
""",
)
def mobile_originated_call_to_dial_a_number(ctx, number: str, mgsm: str):
    """Mobile originated call to dial a number."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands702MobileOriginatedCallToDialANumber(
        number, mgsm
    )
    print(response if status else "Error")
    client.close()


@call_related_commands.group("connected-line-identification-presentation")
@click.pass_context
def connected_line_identification_presentation(ctx):
    """Group for connected line identification presentation."""
    pass


@connected_line_identification_presentation.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read connected line identification presentation."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.callRelatedCommands703ConnectedLineIdentificationPresentationRead()
    )
    print(response if status else "Error")
    client.close()


@connected_line_identification_presentation.command("write")
@click.pass_context
@click.option(
    "-n",
    type=int,
    required=True,
    help="""
0               Disable
1               Enable
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write connected line identification presentation."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.callRelatedCommands703ConnectedLineIdentificationPresentationWrite(n)
    )
    print(response if status else "Error")
    client.close()


@call_related_commands.command("disconnect-existing-connection")
@click.pass_context
def disconnect_existing_connection(ctx):
    """Disconnect existing connection."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands704DisconnectExistingConnection()
    print(response if status else "Error")
    client.close()


@call_related_commands.command("hang-up-voice-call")
@click.pass_context
def hang_up_voice_call(ctx):
    """Hang up voice call."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands705HangUpVoiceCall()
    print(response if status else "Error")
    client.close()


@call_related_commands.command("switch-from-data-mode-to-command-mode")
@click.pass_context
def switch_from_data_mode_to_command_mode(ctx):
    """Switch from data mode to command mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands706SwitchFromDataModeToCommandMode()
    print(response if status else "Error")
    client.close()


@call_related_commands.command("switch-from-command-mode-to-data-mode")
@click.pass_context
def switch_from_command_mode_to_data_mode(ctx):
    """Switch from command mode to data mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands707SwitchFromCommandModeToDataMode()
    print(response if status else "Error")
    client.close()


@call_related_commands.group()
@click.pass_context
def set_number_of_rings_before_automatic_answering(ctx):
    """Group for set number of rings before automatic answering."""
    pass


@set_number_of_rings_before_automatic_answering.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read set number of rings before automatic answering."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.callRelatedCommands708SetNumberOfRingsBeforeAutomaticAnsweringRead()
    )
    print(response if status else "Error")
    client.close()


@set_number_of_rings_before_automatic_answering.command("write")
@click.pass_context
@click.option(
    "-n",
    type=int,
    required=True,
    help="""
0               Automatic answering is disabled
1–255           Enable automatic answering on the ring number specified
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write set number of rings before automatic answering."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.callRelatedCommands708SetNumberOfRingsBeforeAutomaticAnsweringWrite(n)
    )
    print(response if status else "Error")
    client.close()


@call_related_commands.command("list-current-calls-of-me")
@click.pass_context
def list_current_calls_of_me(ctx):
    """List current calls of ME."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands709ListCurrentCallsOfMe()
    print(response if status else "Error")
    client.close()


@call_related_commands.group()
@click.pass_context
def call_status_indication(ctx):
    """Group for call status indication."""
    pass


@call_status_indication.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read call status indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands710CallStatusIndicationRead()
    print(response if status else "Error")
    client.close()


@call_status_indication.command("write")
@click.pass_context
@click.option(
    "-n",
    type=int,
    required=True,
    help="""
0               DSCI not provisioned
1               DSCI provisioned    
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write call status indication."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.callRelatedCommands710CallStatusIndicationWrite(n)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def phonebook_commands(ctx):
    """Group for phonebook commands."""
    pass


@phonebook_commands.command("subscriber-number")
@click.pass_context
def subscriber_number(ctx):
    """Subscriber Number."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands801SubscriberNumber()
    print(response if status else "Error")
    client.close()


@phonebook_commands.command("find-phonebook-entries")
@click.pass_context
@click.option(
    "--findtext",
    "-f",
    type=str,
    required=True,
    help="""
String type field of maximum length <tlength> in current TE character set specified by
AT+CSCS.
""",
)
def find_phonebook_entries(ctx, findtext: str):
    """Find Phonebook Entries."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands802FindPhonebookEntries(findtext)
    print(response if status else "Error")
    client.close()


@phonebook_commands.command("read_phonebook_entries")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="Index of the phonebook entry to read.",
)
def read_phonebook_entries(ctx, index: int):
    """Read Phonebook Entries."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands803ReadPhonebookEntries(index)
    print(response if status else "Error")
    client.close()


@phonebook_commands.group()
@click.pass_context
def select_phonebook_memory_storage(ctx):
    """Group for select phonebook memory storage."""
    pass


@select_phonebook_memory_storage.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read select phonebook memory storage."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands804SelectPhonebookMemoryStorageRead()
    print(response if status else "Error")
    client.close()


@select_phonebook_memory_storage.command("write")
@click.pass_context
@click.option(
    "--storage",
    "-s",
    type=str,
    required=True,
    help="""
''SM''              (U)SIM phonebook
''DC''              ME dialed calls list (AT+CPBW may not be applicable to this storage)
''FD''              (U)SIM fix dialing-phone book (AT+CPBW operation need the authority of PIN2)
''LD''              (U)SIM last-dialing-phone book (AT+CPBW may not be applicable to this
                    storage)
''EN''              (U)SIM (or ME) emergency number (AT+CPBW may not be applicable to this
                    storage)
''ON''              (U)SIM own numbers (MSISDNs) list
''AP''              Selected application phonebook. If a UICC with an active USIM application is
                    present, the application phonebook, DFPHONEBOOK under ADFUSIM is selected
''SDN''             Service Dialing Number    
""",
)
def write(ctx, storage: str):  # type: ignore[reportRedeclaration]
    """Write select phonebook memory storage."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands804SelectPhonebookMemoryStorageWrite(
        storage
    )
    print(response if status else "Error")
    client.close()


@phonebook_commands.command("write-phonebook-entry")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="""
Integer type. Value in the range of location numbers of phone book memory. If <index>
is not given, the first free entry will be used. If <index> is given as the only parameter,
the phonebook entry specified by location is deleted.
""",
)
@click.option(
    "--number",
    "-n",
    type=str,
    required=True,
    help="""
String type. Phone number in format specified by <type>.
""",
)
@click.option(
    "--type",
    "-y",
    type=int,
    required=True,
    help="""
Integer type. Type of address of octet (see 3GPP TS 24.008 subclause 10.5.4.7 for
details).
""",
)
@click.option(
    "--text",
    "-t",
    type=int,
    required=True,
    help="""
String type field of maximum length <tlength> in current TE character set specified by
AT+CSCS.
""",
)
def write_phonebook_entry(ctx, index: int, number: str, type: int, text: str):
    """Write Phonebook Entry."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.phonebookCommands805WritePhonebookEntry(
        index, number, type, text
    )
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def short_message_service_commands(ctx):
    """Group for short message service commands."""
    pass


@short_message_service_commands.group()
@click.pass_context
def select_message_service(ctx):
    """Group for select message service."""
    pass


@select_message_service.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read select message service."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands901SelectMessageServiceRead()
    print(response if status else "Error")
    client.close()


@select_message_service.command("write")
@click.pass_context
@click.option(
    "--service",
    "-s",
    type=int,
    required=True,
    help="""
0   3GPP TS 23.040 and 3GPP TS 23.041 (the syntax of SMS AT commands is
    compatible with 3GPP TS 27.005 Phase 2 version 4.7.0; Phase 2+ features
    which do not require new command syntax may be supported, e.g. correct
    routing of messages with new Phase 2+ data coding schemes)
1   3GPP TS 23.040 and 3GPP TS 23.041 (the syntax of SMS AT commands is
    compatible with 3GPP TS 27.005 Phase 2+ version; the requirement of
    <service> setting 1 is mentioned under corresponding command    
""",
)
def write(ctx, service: int):  # type: ignore[reportRedeclaration]
    """Write select message service."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands901SelectMessageServiceWrite(
        service
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def message_format(ctx):
    """Group for message format."""
    pass


@message_format.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read message format."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands902MessageFormatRead()
    print(response if status else "Error")
    client.close()


@message_format.command("write")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
0                   PDU mode
1                   Text mode    
""",
)
def write(ctx, mode: int):  # type: ignore[reportRedeclaration]
    """Write message format."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands902MessageFormatWrite(mode)
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def service_center_address(ctx):
    """Group for service center address."""
    pass


@service_center_address.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read service center address."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands903ServiceCenterAddressRead()
    print(response if status else "Error")
    client.close()


@service_center_address.command("write")
@click.pass_context
@click.option(
    "--sca",
    "-s",
    type=str,
    required=True,
    help="""
Service center address. 3GPP TS 24.011 RP SC address Address-Value field in string
format; BCD numbers (or GSM 7 bit default alphabet characters) are converted to
characters of the currently selected TE character set (see AT+CSCS in 3GPP TS
27.007). The type of address is given by <tosca>. 
""",
)
@click.option(
    "--tosca",
    "-t",
    type=str,
    required=True,
    help="""
Type of service center address. 3GPP TS 24.011 RP SC address Type-of-Address
octet in integer format (default see <toda>). 
""",
)
def write(ctx, sca: str, tosca: str):  # type: ignore[reportRedeclaration]
    """Write service center address."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands903ServiceCenterAddressWrite(
        sca, tosca
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def preferred_message_storage(ctx):
    """Group for preferred message storage."""
    pass


@preferred_message_storage.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read preferred message storage."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands904PreferredMessageStorageRead()
    )
    print(response if status else "Error")
    client.close()


@preferred_message_storage.command("write")
@click.pass_context
@click.option(
    "-mem1",
    type=str,
    required=True,
    help="""
''SM''          (U)SIM message storage
''ME''          Mobile equipment message storage    
""",
)
@click.option(
    "-mem2",
    type=str,
    required=True,
    help="""
''SM''          (U)SIM message storage
''ME''          Mobile equipment message storage    
""",
)
@click.option(
    "-mem3",
    type=str,
    required=True,
    help="""
''SM''          (U)SIM message storage
''ME''          Mobile equipment message storage    
""",
)
def write(ctx, mem1: str, mem2: str, mem3: str):  # type: ignore[reportRedeclaration]
    """Write preferred message storage."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands904PreferredMessageStorageWrite(
            mem1, mem2, mem3
        )
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.command("delete-message")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="Value in the range of location numbers supported by the associated memory.",
)
@click.option(
    "--delflag",
    "-d",
    type=int,
    required=True,
    help="""
0               Delete the message specified in <index>
1               Delete all read messages from <mem1> storage
2               Delete all read messages from <mem1> storage and sent mobile originated messages
3               Delete all read messages, sent and unsent mobile originated messages from <mem1> storage
4               Delete all messages from <mem1> storage  
""",
)
def delete_message(ctx, index: int, delflag: int):
    """Delete Message."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands905DeleteMessage(
        index, delflag
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def list_messages(ctx):
    """Group for list messages."""
    pass


@list_messages.command("get-all")
@click.pass_context
def get_all(ctx):
    """Get all messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands906ListMessagesGetAll()
    print(response if status else "Error")
    client.close()


@list_messages.command("query")
@click.pass_context
@click.option(
    "--stat",
    "-s",
    type=str,
    required=True,
    help="""
''REC UNREAD''      Received unread messages
''REC READ''        Received read messages
''STO UNSENT''      Stored unsent messages
''STO SENT''        Stored sent messages
''ALL''             All messages
Integer type. In PDU mode:
0                   Received unread messages
1                   Received read messages
2                   Stored unsent messages
3                   Stored sent messages
4                   All messages   
""",
)
def query(ctx, stat: str):
    """Query messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands906ListMessagesQuery(stat)
    print(response if status else "Error")
    client.close()


@short_message_service_commands.command("read-message")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="""Value in the range of location numbers supported by the associated memory.""",
)
def read_message(ctx, index: int):
    """Read message."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands907ReadMessage(index)
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def send_messages(ctx):
    """Group for send messages."""
    pass


@send_messages.command("text-mode")
@click.pass_context
@click.option(
    "--da",
    "-d",
    type=str,
    required=True,
    help="""
Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in
string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to
characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007).
The type of address is given by <toda>.
""",
)
@click.option(
    "--toda",
    "-t",
    type=int,
    required=True,
    help="""
Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet
in integer format.
""",
)
@click.option("--text", "-x", type=str, required=True, help="""SMS Text""")
def text_mode(ctx, da: str, toda: int, text: str):  # type: ignore[reportRedeclaration]
    """Send messages in text mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands908SendMessagesTextMode(
        da, toda, text
    )
    print(response if status else "Error")
    client.close()


@send_messages.command("pdu-mode")
@click.pass_context
def pdu_mode(ctx):  # type: ignore[reportRedeclaration]
    """Send messages in PDU mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands908SendMessagesPduMode()
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def send_more_messages(ctx):
    """Group for send more messages."""
    pass


@send_more_messages.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read send more messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands909SendMoreMessagesRead()
    print(response if status else "Error")
    client.close()


@send_more_messages.command("write")
@click.pass_context
@click.option(
    "-n",
    type=int,
    required=True,
    help="""
0           Feature disabled
1           Keep enabled until the time between the response of the latest message send
            command (AT+CMGS, AT+CMSS, etc.) and the next send command exceeds 1–5
            seconds (the exact value is up to ME implementation), and then ME shall close the
            link and TA switches <n> back to 0 automatically.
2           Feature enabled (If the time between the response of the latest message send
            command and the next send command exceeds 1-5 seconds (the exact value is up to
            ME implementation), ME shall close the link but TA will not switch <n> back to 0
            automatically).
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write send more messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands909SendMoreMessagesWrite(n)
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def write_message_to_memory(ctx):
    """Group for write message to memory."""
    pass


@write_message_to_memory.command("text-mode")
@click.pass_context
@click.option(
    "-da",
    type=str,
    required=True,
    help="""
Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in
string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to
characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007).
The type of address is given by <toda>.    
""",
)
@click.option(
    "-oa",
    type=str,
    required=True,
    help="""
Originating address. 3GPP TS 23.040 TP-Originating-Address Address-Value field in
string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to
characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007).
The type of address is given by <tooa>.    
""",
)
@click.option(
    "-tooa",
    type=int,
    required=True,
    help="""
Type of originating address. 3GPP TS 24.011 TP-Originating-Address Type-of-Address
octet in integer format.   
""",
)
@click.option(
    "-toda",
    type=int,
    required=True,
    help="""
Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet
in integer format.
""",
)
@click.option(
    "--stat",
    "-s",
    type=str,
    required=True,
    help="""
Text mode       Explanation
''REC UNREAD''  Received unread messages
''REC READ''    Received read messages
''STO UNSENT''  Stored unsent messages
''STO SENT''    Stored sent messages
''ALL''         All messages    
""",
)
@click.option(
    "--text",
    "-x",
    type=str,
    required=True,
    help="Message content.",
)
def text_mode(ctx, da: str, oa: str, tooa: int, toda: int, stat: str, text: str):  # type: ignore[reportRedeclaration]
    """Write message to memory in text mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands910WriteMessageToMemoryTextMode(
            da, oa, tooa, toda, stat, text
        )
    )
    print(response if status else "Error")
    client.close()


@write_message_to_memory.command("pdu-mode")
@click.pass_context
def pdu_mode(ctx):  # type: ignore[reportRedeclaration]
    """Write message to memory in PDU mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands910WriteMessageToMemoryPduMode()
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.command("send-message-from-storage")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="""
Value in the range of location numbers supported by the associated memory.
""",
)
@click.option(
    "-da",
    type=str,
    required=True,
    help="""
Destination Address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in
string format. BCD numbers (or GSM 7 bit default alphabet characters) are
converted to characters of the currently selected TE character set (see AT+CSCS
command in 3GPP TS 27.007). The type of address is given by <toda>.   
""",
)
@click.option(
    "-toda",
    type=int,
    required=True,
    help="""
Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address
octet in integer format.   
""",
)
def send_message_from_storage(ctx, index: int, da: str, toda: int):
    """Send message from storage."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands911SendMessageFromStorage(
        index, da, toda
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def new_message_acknowledgement_to_ue_te(ctx):
    """Group for new message acknowledgement to UE TE."""
    pass


@new_message_acknowledgement_to_ue_te.command("execute")
@click.pass_context
def execute(ctx):  # type: ignore[reportRedeclaration]
    """Execute new message acknowledgement to UE TE."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands912NewMessageAcknowledgementToUeTeExecute()
    )
    print(response if status else "Error")
    client.close()


@new_message_acknowledgement_to_ue_te.command("write")
@click.pass_context
@click.option(
    "-n",
    type=int,
    required=True,
    help="""
0           Command operates similarly as in text mode
1           Send positive (RP-ACK) acknowledgement to the network. Accepted only in PDU mode
2           Send negative (RP-ERROR) acknowledgement to the network. Accepted only in PDU mode
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write new message acknowledgement to UE TE."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands912NewMessageAcknowledgementToUeTeWrite(n)
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def sms_event_reporting_configuration(ctx):
    """Group for SMS event reporting configuration."""
    pass


@sms_event_reporting_configuration.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read SMS event reporting configuration."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands913SmsEventReportingConfigurationRead()
    )
    print(response if status else "Error")
    client.close()


@sms_event_reporting_configuration.command("write")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
0               Buffer unsolicited result codes in the TA. If TA result code buffer is full, indications can
                be buffered in some other place or the oldest indications may be discarded and
                replaced with the new received indications.
1               Discard indication and reject new received message unsolicited result codes when
                TA-TE link is reserved (e.g. in on-line data mode). Otherwise forward them directly to
                the TE.
2               Buffer unsolicited result codes in the TA when TA-TE link is reserved (e.g. in data
                mode) and flush them to the TE after reservation. Otherwise forward them directly to
                the TE.
<mt>            Integer type. The rules for storing received SMS depend on its data coding scheme (see
                GPPTS 23.038) and preferred memory storage (AT+CPMS) setting, and the value is:
0               No SMS-DELIVER indications are routed to the TE
1               If SMS-DELIVER is stored into ME/TA, indication of the memory location is routed to
                the TE by using unsolicited result code: +CMTI: <mem>,<index>
2               SMS-DELIVERs (except class 2) are routed directly to the TE using unsolicited
                result code: +CMT: [<alpha>],<length><CR><LF><pdu> (PDU mode enabled) or
                +CMT:<oa>,[<alpha>],<scts>[,<tooa>,<fo>,<pid>,<dcs>,<sca>,<tosca>,<length>]
                <CR><LF><data> (text mode enabled; about the parameters in italics, see
                AT+CSDH) or ^HCMT: <oa>,<scts>,<lang>,<fmt>,<length>,<prt>,<prv>,<type>,
                <stat><CR><LF><data> (text mode for CDMA SMS). Class 2 messages result in
                indication as defined in <mt>=1
3               Class 3 SMS-DELIVERs are routed directly to TE by using unsolicited result codes
                defined in <mt>=2. Messages of other classes result in indication as defined in
                <mt>=1   
""",
)
@click.option(
    "--mt",
    "-t",
    type=int,
    required=True,
    help="""
The rules for storing received SMS depend on its data coding scheme (see
GPPTS 23.038) and preferred memory storage (AT+CPMS) setting, and the value is:
0               No SMS-DELIVER indications are routed to the TE
1               If SMS-DELIVER is stored into ME/TA, indication of the memory location is routed to
                the TE by using unsolicited result code: +CMTI: <mem>,<index>
2               SMS-DELIVERs (except class 2) are routed directly to the TE using unsolicited
                result code: +CMT: [<alpha>],<length><CR><LF><pdu> (PDU mode enabled) or
                +CMT:<oa>,[<alpha>],<scts>[,<tooa>,<fo>,<pid>,<dcs>,<sca>,<tosca>,<length>]
                <CR><LF><data> (text mode enabled; about the parameters in italics, see
                AT+CSDH) or ^HCMT: <oa>,<scts>,<lang>,<fmt>,<length>,<prt>,<prv>,<type>,
                <stat><CR><LF><data> (text mode for CDMA SMS). Class 2 messages result in
                indication as defined in <mt>=1
3               Class 3 SMS-DELIVERs are routed directly to TE by using unsolicited result codes
                defined in <mt>=2. Messages of other classes result in indication as defined in
                <mt>=1
""",
)
@click.option(
    "--bm",
    "-b",
    type=int,
    required=True,
    help="""
The rules for storing received CBMs depend on its data coding scheme (see
3GPP TS 23.038) and the setting of Select CBM Types (AT+CSCB), and the value is:
0               No CBM indications are routed to the TE
2               New CBMs are routed directly to the TE using unsolicited result code:
                +CBM:   <length><CR><LF><pdu>   (PDU mode); or
                +CBM: <sn>,<mid>,<dcs>,<page>,<pages><CR><LF><data> (text mode)   
""",
)
@click.option(
    "--ds",
    "-d",
    type=int,
    required=True,
    help="""
0               No SMS-STATUS-REPORTs are routed to the TE
1               SMS-STATUS-REPORTs are routed to the TE using unsolicited result code:
                +CDS: <length><CR><LF><pdu> (PDU mode)
                +CDS: <fo>,<mr>,[<ra>],[<tora>],<scts>,<dt>,<st> (text mode)
2               If SMS-STATUS-REPORT is stored into ME/TA, indication of the memory location
                is routed to the TE using unsolicited result code:
                +CDSI: <mem>,<index>   
""",
)
@click.option(
    "--bfr",
    "-f",
    type=int,
    required=True,
    help="""
0               TA buffer of unsolicited result codes defined within this command is flushed to
                the TE when <mode> 1 or 2 is entered (OK response shall be given before flushing
                the codes)
1               TA buffer of unsolicited result codes defined within this command is cleared when
                <mode> 1 or 2 is entered                    
""",
)
def write(ctx, mode: int, mt: int, bm: int, ds: int, bfr: int):  # type: ignore[reportRedeclaration]
    """Write SMS event reporting configuration."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands913SmsEventReportingConfigurationWrite(
            mode, mt, bm, ds, bfr
        )
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def select_cell_broadcast_message_types(ctx):
    """Group for select cell broadcast message types."""
    pass


@select_cell_broadcast_message_types.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read select cell broadcast message types."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands914SelectCellBroadcastMessageTypesRead()
    )
    print(response if status else "Error")
    client.close()


@select_cell_broadcast_message_types.command("write")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
0               Message types specified in <mids> and <dcss> are accepted
1               Message types specified in <mids> and <dcss> are not accepted
""",
)
@click.option(
    "--mids",
    "-i",
    type=str,
    required=True,
    help="""
All different possible combinations of CBM message identifiers (see <mid>), e.g. “0,1,5,320-478,922”.    
""",
)
@click.option(
    "--dcss",
    "-d",
    type=str,
    required=True,
    help="""
All different possible combinations of CBM data coding schemes (see <dcs>) (default is empty string), e.g. “0-3,5”.    
""",
)
def write(ctx, mode: int, mids: str, dcss: str):  # type: ignore[reportRedeclaration]
    """Write select cell broadcast message types."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands914SelectCellBroadcastMessageTypesWrite(
            mode, mids, dcss
        )
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def show_sms_text_mode_parameters(ctx):
    """Group for show SMS text mode parameters."""
    pass


@show_sms_text_mode_parameters.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read show SMS text mode parameters."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands915ShowSmsTextModeParametersRead()
    )
    print(response if status else "Error")
    client.close()


@show_sms_text_mode_parameters.command("write")
@click.pass_context
@click.option(
    "--show",
    "-s",
    type=int,
    required=True,
    help="""
0               Do not show header values defined in commands +CSCA, +CSMP (<sca>,
                <tosca>, <fo>, <vp>, <pid>, <dcs>) and <length>, <toda> or <tooa> in +CMT,
                +CMGL, +CMGR result codes for SMS-DELIVERs and SMS-SUBMITs in text mode
1               Show the values in result codes    
""",
)
def write(ctx, show: int):  # type: ignore[reportRedeclaration]
    """Write show SMS text mode parameters."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands915ShowSmsTextModeParametersWrite(show)
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def set_sms_text_mode_parameters(ctx):
    """Group for set SMS text mode parameters."""
    pass


@set_sms_text_mode_parameters.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read set SMS text mode parameters."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands916SetSmsTextModeParametersRead()
    )
    print(response if status else "Error")
    client.close()


@set_sms_text_mode_parameters.command("write")
@click.pass_context
@click.option(
    "-fo",
    type=int,
    required=True,
    help="""
First octet. Depending on the command or result code: First octet of 3GPP TS 23.040
SMS-DELIVER, SMS-SUBMIT (default 17), SMS-STATUS-REPORT, SMS-COMMAND in
integer format. If a valid value has been entered once, parameter can be omitted.   
""",
)
@click.option(
    "-vp",
    type=int,
    required=True,
    help="""
Validity period. Depending on SMS-SUBMIT <fo> setting: 3GPP TS 23.040 TP-Validity-
Period either in integer format or in time-string format (see <dt>). Default value: 167.   
""",
)
@click.option(
    "-pid",
    type=int,
    required=True,
    help="""
Protocol identifier. 3GPP TS 23.040 TP-Protocol-Identifier in integer format. Default value: 0.
""",
)
@click.option(
    "-dcs",
    type=int,
    required=True,
    help="""
Data coding scheme. Depending on the command or result code: 3GPP TS 23.038
SMS Data Coding Scheme (default 0), or Cell Broadcast Data Coding Scheme in
integer format.
""",
)
def write(ctx, fo: int, vp: int, pid: int, dcs: int):  # type: ignore[reportRedeclaration]
    """Write set SMS text mode parameters."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands916SetSmsTextModeParametersWrite(
            fo, vp, pid, dcs
        )
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.group()
@click.pass_context
def send_concatenated_messages(ctx):
    """Group for send concatenated messages."""
    pass


@send_concatenated_messages.command("text-mode")
@click.pass_context
@click.option(
    "--da",
    "-d",
    type=str,
    required=True,
    help="""
Destination address. 3GPP TS 23.040 TP-Destination-Address Address-Value field in
string format. BCD numbers (or GSM 7 bit default alphabet characters) are converted to
characters of the currently selected TE character set (see AT+CSCS in 3GPP TS 27.007).
The type of address is given by <toda>.
""",
)
@click.option(
    "--toda",
    "-t",
    type=int,
    required=True,
    help="""
Type of recipient address. 3GPP TS 24.011 TP-Recipient-Address Type-of-Address octet
in integer format.
""",
)
@click.option(
    "--uid",
    "-u",
    type=int,
    required=True,
    help="""
Message identification in the user data header (UDH). Range: 0-255. This parameter is defined and inputted by the user. All segments of a same
concatenated message must have the same <uid>. Different concatenated
messages should have different <uid>.
""",
)
@click.option(
    "--msgseg",
    "-m",
    type=int,
    required=True,
    help="""
Sequence number of a concatenated message. Range: 0–7.
<msg_seg>=0 means: ignore the value and regard it as a non-concatenated message.
""",
)
@click.option(
    "--msgtotal",
    "-o",
    type=int,
    required=True,
    help="""
The total number of the segments of one concatenated message.
Range: 0–7. <msg_total>=0 or 1 means: ignore the value and regard it as a non-concatenated message.
""",
)
@click.option("--text", "-x", type=str, required=True, help="SMS Text")
def text_mode(ctx, da: str, toda: int, uid: int, msgseg: int, msgtotal: int, text: str):
    """Send concatenated messages in text mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands917SendConcatenatedMessagesTextMode(
            da, toda, uid, msgseg, msgtotal, text
        )
    )
    print(response if status else "Error")
    client.close()


@send_concatenated_messages.command("pdu-mode")
@click.pass_context
def pdu_mode(ctx):
    """Send concatenated messages in PDU mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.shortMessageServiceCommands917SendConcatenatedMessagesPduMode()
    )
    print(response if status else "Error")
    client.close()


@short_message_service_commands.command("read-concatenated-messages")
@click.pass_context
@click.option(
    "--index",
    "-i",
    type=int,
    required=True,
    help="Value in the range of location numbers supported by the associated memory.",
)
def read_concatenated_messages(ctx, index: int):
    """Read concatenated messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.shortMessageServiceCommands918ReadConcatenatedMessages(
        index
    )
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def packet_domain_commands(ctx):
    """Group for packet domain commands."""
    pass


@packet_domain_commands.group()
@click.pass_context
def attachment_detachment_of_ps_read(ctx):
    """Group for attachment detachment of PS read."""
    pass


@attachment_detachment_of_ps_read.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read attachment detachment of PS read."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1001AttachmentDetachmentOfPsRead()
    print(response if status else "Error")
    client.close()


@attachment_detachment_of_ps_read.command("write")
@click.pass_context
@click.option(
    "--state",
    "-s",
    type=int,
    required=True,
    help="""
0               Detached
1               Attached
Other values are reserved and will result in an ERROR response to the Write Command  
""",
)
def write(ctx, state: int):  # type: ignore[reportRedeclaration]
    """Write attachment detachment of PS read."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1001AttachmentDetachmentOfPsWrite(
        state
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def define_pdp_context(ctx):
    """Group for define PDP context."""
    pass


@define_pdp_context.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read define PDP context."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1002DefinePdpContextRead()
    print(response if status else "Error")
    client.close()


@define_pdp_context.command("write")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
<cid>               PDP context identifier. Range: 1–15. A numeric parameter which specifies a particular
                    PDP context definition. The parameter is local to the TE-MT interface and is used in
                    other PDP context-related commands. The range of permitted values (minimum
                    value=1) is returned by the test form of the command.
""",
)
@click.option(
    "--pdptype" "-p",
    type=str,
    required=True,
    help="""
Packet data protocol type, a string parameter which specifies the type of packet data protocol.
''IP''              Internet Protocol (IETF STD 5)
''PPP''             Point to Point Protocol (IETF STD 51).
''IPV6''            Internet Protocol, version 6
""",
)
@click.option(
    "--apn",
    "-a",
    type=str,
    required=True,
    help="""
Access point name, a string parameter that is a logical name used to select the GGSN
or the external packet data network. If the value is null or omitted, then the
subscription value will be requested.    
""",
)
@click.option(
    "--dpaddr" "-d",
    type=str,
    required=True,
    help="""
A string parameter identifies the MT in the address space applicable to the PDP. If the
value is null or omitted, then a value may be provided by the TE during the PDP startup
procedure or, failing that, a dynamic address will be requested. The allocated address
may be read using the AT+CGPADDR command.
""",
)
@click.option(
    "--datacomp",
    "-c",
    type=int,
    required=True,
    help="""
A numeric parameter that controls PDP data compression (applicable for SNDCP
only) (see 3GPP TS 44.065).
0                   Off (Default if value is omitted)
1                   On (Manufacturer preferred compression)
2                   V.42bis
3                   V.44 (Not supported currently)
""",
)
@click.option(
    "--headcomp",
    "-h",
    type=int,
    required=True,
    help="""
A numeric parameter that controls PDP header compression (see 3GPP TS 44.065
and 3GPP TS 25.323).
0                   Off
1                   On
2                   RFC1144
3                   RFC2507
4                   RFC3095   
""",
)
@click.option(
    "--ipv4addralloc",
    "-i",
    type=int,
    required=True,
    help="""
Control how the MT/TA requests to get the IPv4 address information.
0                   IPv4 address allocated through NAS signalling
1                   IPv4 address allocated through DHCP
""",
)
@click.option(
    "--requesttype",
    "-r",
    type=int,
    required=True,
    help="""
Indicate the type of PDP context activation request for the PDP context.
Please see 3GPP TS 24.301 (subclause 6.5.1.2) and 3GPP TS 24.008 (subclause
10.5.6.17). If the initial PDP context is supported (subclause 10.1.0), it is not allowed to
assign <cid>=0 for emergency bearer services. According to 3GPP TS 24.008
(subclause 4.2.4.2.2 and 4.2.5.1.4) and 3GPP TS 24.301 (subclause 5.2.2.3.3 and
5.2.3.2.2), a separate PDP context must be established for emergency bearer services. 
""",
)
@click.option(
    "--pcscfdiscovery",
    "-p",
    type=int,
    required=True,
    help="""
Affect how the MT/TA requests to get the P-CSCF
address, (see 3GPP TS 24.229 annex B and L).
0                   Preference of P-CSCF address discovery not affected by AT+CGDCONT
1                   Preference of P-CSCF address discovery through NAS signaling
2                   Preference of P-CSCF address discovery through DHCP
""",
)
@click.option(
    "--imcnsignallingflagind",
    "-i",
    type=int,
    required=True,
    help="""
Indicates to the network whether the PDP context is
for IM CN subsystem-related signaling only or not.
0                   UE indicates that the PDP context is not for IM CN subsystem-related signaling only
1                   UE indicates tha
""",
)
def write(ctx, cid: int, pdptype: str, apn: str, dpaddr: str, datacomp: int, headcomp: int, ipv4addralloc: int, requesttype: int, pcscfdiscovery: int, imcnsignallingflagind: int):  # type: ignore[reportRedeclaration]
    """Write define PDP context."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1002DefinePdpContextWrite(
        cid,
        pdptype,
        apn,
        dpaddr,
        datacomp,
        headcomp,
        ipv4addralloc,
        requesttype,
        pcscfdiscovery,
        imcnsignallingflagind,
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def quality_of_service_profile_requested(ctx):
    """Group for quality of service profile requested."""
    pass


@quality_of_service_profile_requested.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read quality of service profile requested."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1003QualityOfServiceProfileRequestedRead()
    )
    print(response if status else "Error")
    client.close()


@quality_of_service_profile_requested.command("write")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT command)
""",
)
@click.option(
    "--precedence",
    "-p",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the precedence class.
0               Network subscribed value
1               High Priority. Service commitments shall be maintained ahead of precedence
            classes 2 and 3
2               Normal priority. Service commitments shall be maintained ahead of
            precedence class 3
3               Low priority. Service commitments shall be maintained
""",
)
@click.option(
    "--delay",
    "-d",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the delay class. This parameter defines the
end-to-end transfer delay incurred in the transmission of SDUs through the network.        
For the details, see Table 5.
0               Network subscribed valu     
""",
)
@click.option(
    "--reliability",
    "-r",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the reliability class
0               Network subscribed value
1               Non real-time traffic, error-sensitive application that cannot cope with data loss
2               Non real-time traffic, error-sensitive application that can cope with infrequent data loss
3               Non real-time traffic, error-sensitive application that can cope with data loss,GMM/SM, and SMS
4               Real-time traffic, error-sensitive application that can cope with data loss
5               Real-time traffic, error non-sensitive application that can cope with data loss 
""",
)
@click.option(
    "--peak",
    "-k",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the peak throughput class, in octets per second.
0               Network subscribed value
1               Up to 1 000 (8 kbit/s)
2               Up to 2 000 (16 kbit/s)
3               Up to 4 000 (32 kbit/s)
4               Up to 8 000 (64 kbit/s)
5               Up to 16 000 (128 kbit/s)
6               Up to 32 000 (256 kbit/s)
7               Up to 64 000 (512 kbit/s)
8               Up to 128 000 (1024 kbit/s)
9               Up to 256 000 (2048 kbit/s)
""",
)
@click.option(
    "--mean",
    "-m",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the mean throughput class, in octets per hour.
0               Network subscribed value
1               100 (~0.22 bit/s)
2               200 (~0.44 bit/s)
3               500 (~1.11 bit/s)
4               1 000 (~2.2 bit/s)
5               2 000 (~4.4 bit/s)
6               5 000 (~11.1 bit/s)
7               10 000 (~22 bit/s)
8               20 000 (~44 bit/s)
9               50 000 (~111 bit/s)
10              100 000 (~0.22 kbit/s)
11              200 000 (~0.44 kbit/s)
12              500 000(~1.11 kbit/s)
13              1000 000 (~2.2 kbit/s)
14              2 000 000 (~4.4 kbit/s)
15              5 000 000 (~11.1 kbit/s)
16              10 000 000 (~22 kbit/s)
17              20 000 000 (~44 kbit/s)
18              50 000 000 (~111 kbit/s)
31              Best effort     
""",
)
def write(ctx, cid: int, precedence: int, delay: int, reliability: int, peak: int, mean: int):  # type: ignore[reportRedeclaration]
    """Write quality of service profile requested."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1003QualityOfServiceProfileRequestedWrite(
            cid, precedence, delay, reliability, peak, mean
        )
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def quality_of_service_profile_minimum_acceptable(ctx):
    """Group for quality of service profile minimum acceptable."""
    pass


@quality_of_service_profile_minimum_acceptable.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read quality of service profile minimum acceptable."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1004QualityOfServiceProfileMinimumAcceptableRead()
    )
    print(response if status else "Error")
    client.close()


@quality_of_service_profile_minimum_acceptable.command("write")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT command)
""",
)
@click.option(
    "--precedence",
    "-p",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the precedence class.
0               Network subscribed value
1               High Priority. Service commitments shall be maintained ahead of precedence
            classes 2 and 3
2               Normal priority. Service commitments shall be maintained ahead of
            precedence class 3
3               Low priority. Service commitments shall be maintained
""",
)
@click.option(
    "--delay",
    "-d",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the delay class. This parameter defines the
end-to-end transfer delay incurred in the transmission of SDUs through the network.        
For the details, see Table 5.
0               Network subscribed valu     
""",
)
@click.option(
    "--reliability",
    "-r",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the reliability class
0               Network subscribed value
1               Non real-time traffic, error-sensitive application that cannot cope with data loss
2               Non real-time traffic, error-sensitive application that can cope with infrequent data loss
3               Non real-time traffic, error-sensitive application that can cope with data loss,GMM/SM, and SMS
4               Real-time traffic, error-sensitive application that can cope with data loss
5               Real-time traffic, error non-sensitive application that can cope with data loss 
""",
)
@click.option(
    "--peak",
    "-k",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the peak throughput class, in octets per second.
0               Network subscribed value
1               Up to 1 000 (8 kbit/s)
2               Up to 2 000 (16 kbit/s)
3               Up to 4 000 (32 kbit/s)
4               Up to 8 000 (64 kbit/s)
5               Up to 16 000 (128 kbit/s)
6               Up to 32 000 (256 kbit/s)
7               Up to 64 000 (512 kbit/s)
8               Up to 128 000 (1024 kbit/s)
9               Up to 256 000 (2048 kbit/s)
""",
)
@click.option(
    "--mean",
    "-m",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies the mean throughput class, in octets per hour.
0               Network subscribed value
1               100 (~0.22 bit/s)
2               200 (~0.44 bit/s)
3               500 (~1.11 bit/s)
4               1 000 (~2.2 bit/s)
5               2 000 (~4.4 bit/s)
6               5 000 (~11.1 bit/s)
7               10 000 (~22 bit/s)
8               20 000 (~44 bit/s)
9               50 000 (~111 bit/s)
10              100 000 (~0.22 kbit/s)
11              200 000 (~0.44 kbit/s)
12              500 000(~1.11 kbit/s)
13              1000 000 (~2.2 kbit/s)
14              2 000 000 (~4.4 kbit/s)
15              5 000 000 (~11.1 kbit/s)
16              10 000 000 (~22 kbit/s)
17              20 000 000 (~44 kbit/s)
18              50 000 000 (~111 kbit/s)
31              Best effort     
""",
)
def write(ctx, cid: int, precedence: int, delay: int, reliability: int, peak: int, mean: int):  # type: ignore[reportRedeclaration]
    """Write quality of service profile minimum acceptable."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1004QualityOfServiceProfileMinimumAcceptableWrite(
            cid, precedence, delay, reliability, peak, mean
        )
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def quality_of_service_profile3g_requested(ctx):
    """Group for quality of service profile 3G requested."""
    pass


@quality_of_service_profile3g_requested.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read quality of service profile 3G requested."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1005QualityOfServiceProfile3gRequestedRead()
    )
    print(response if status else "Error")
    client.close()


@quality_of_service_profile3g_requested.command("write")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
PDP context identifier, a numeric parameter which specifies a
particular PDP context definition. The parameter is local to the TE-
MT interface and is used in other PDP context-related commands.
The range of permitted values (minimum value=1) is returned by
the test form of the command.
""",
)
@click.option(
    "--trafficclass",
    "-t",
    type=int,
    required=True,
    help="""
Indicates the type of application for which the UMTS
bearer service is optimized (see 3GPP TS 24.008 subclause
10.5.6.5). If the parameter is specified as conversational or
streaming, then the Guaranteed and Maximum bitrate parameters
should also be provided.
0                               Conversational
1                               Streaming
2                               Interactive
3                               Background
4                               Subscribed value
""",
)
@click.option(
    "--maxbitrateul",
    "-u",
    type=int,
    required=True,
    help="""
Indicates the maximum number of kbits/s delivered to
UMTS (up-link traffic) at a SAP. As an example, a bit rate of
32 kbit/s would be specified as ‘32’
(e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--maxbitratedl",
    "-d",
    type=int,
    required=True,
    help="""
Indicates the maximum number of kbits/s delivered by
UMTS (down-link traffic) at a SAP. As an example, a bitrate of
32 kbit/s would be specified as ‘32’
(e.g. AT+CGEQREQ=…,32, …).
Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--guaranteedbitrateul",
    "-g",
    type=int,
    required=True,
    help="""
Indicates the guaranteed number of kbits/s delivered
to UMTS (up-link traffic) at a SAP (provided that there is data to
deliver). As an example, a bitrate of 32 kbit/s would be specified as
‘32’ (e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--guaranteedbitratedl",
    "-l",
    type=int,
    required=True,
    help="""
Indicates the guaranteed number of kbits/s delivered
by UMTS (down-link traffic) at a SAP (provided that there is data to
deliver). As an example, a bitrate of 32 kbit/s would be specified as
‘32’ (e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--deliveryorder",
    "-o",
    type=int,
    required=True,
    help="""
Indicates whether the UMTS bearer shall provide in-
sequence SDU delivery or not (see 3GPP TS 24.008 subclause
10.5.6.5).
0                               No
1                               Yes
2                               Subscribed value
""",
)
@click.option(
    "--maxsdusize",
    "-s",
    type=int,
    required=True,
    help="""
(1,2,3,…) indicates the maximum allowed SDU size in
octets. If the parameter is set to ‘0’ the subscribed value will be
requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed value
10–520                          (Value needs to be divisible by 10 without remainder)
1520
""",
)
@click.option(
    "--sduerrorratio",
    "-e",
    type=str,
    required=True,
    help="""
Indicates the target value for the fraction of SDUs lost
or detected as erroneous. SDU error ratio is defined only for
conforming traffic. The value is specified as ‘mEe’. As an example a
target SDU error ratio of 5 × 10-3 would be specified as "5E3" (e.g.
AT+CGEQREQ=…,"5E3",…).
"0E0"                                   Subscribed value
"1E1"
"1E2"
"7E3"
"1E3"
"1E4"
"1E5"
"1E6"
""",
)
@click.option(
    "--residualbiterrorratio",
    "-r",
    type=str,
    required=True,
    help="""
Indicates the target value for the undetected bit error
ratio in the delivered SDUs. If no error detection is requested,
Residual bit error ratio indicates the bit error ratio in the delivered
SDUs. The value is specified as “mEe”. As an example, a target
residual bit error ratio of 5 × 10-3 would be specified as "5E3" (e.g.
AT+CGEQREQ=…,"5E3",…).
"0E0"                           Subscribed value
"5E2"
"1E2"
"5E3"
"4E3"
"1E3"
"1E4"
"1E5"
"1E6"
"6E8"
""",
)
@click.option(
    "--deliveryoferrsdu",
    "-f",
    type=int,
    required=True,
    help="""
Indicates whether SDUs detected as erroneous shall
be delivered or not (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               No
1                               Yes
2                               No detect
3                               Subscribed value
""",
)
@click.option(
    "--transferdelay",
    "-t",
    type=int,
    required=True,
    help="""
(0,1,2,…) indicates the targeted time between request
to transfer an SDU at one SAP to its delivery at the other SAP, in
milliseconds. If the parameter is set to ‘0’ the subscribed value will
be requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed value
100–150                         (value needs to be divisible by 10 without remainder)
200–950                         (value needs to be divisible by 50 without remainder)
1000–4000                       (value needs to be divisible by 100 without remainder)
""",
)
@click.option(
    "--traffichandlingpriority",
    "-h",
    type=int,
    required=True,
    help="""
(1,2,3,…) specifies the relative importance for handling
of all SDUs belonging to the UMTS bearer compared to the SDUs
of other bearers. If the parameter is set to ‘0’ the subscribed value
will be requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed
1
2
3
""",
)
@click.option(
    "--sourcestatisticsdescriptor",
    "-s",
    type=int,
    required=True,
    help="""
Specifies characteristics of the source of the submitted
SDUs for a PDP context.
0                               Characteristics of SDUs is unknown
1                               Characteristics of SDUs correspond to a speech source
""",
)
@click.option(
    "--signallingindication",
    "-i",
    type=int,
    required=True,
    help="""
Indicates signaling content of submitted SDUs for a
PDP context.
0                               PDP context is not optimized for signaling
1                               PDP context is optimized for signaling
""",
)
def write(  # type: ignore[reportRedeclaration]
    ctx,
    cid: int,
    trafficclass: int,
    maxbitrateul: int,
    maxbitratedl: int,
    guaranteedbitrateul: int,
    guaranteedbitratedl: int,
    deliveryorder: int,
    maxsdusize: int,
    sduerrorratio: str,
    residualbiterrorratio: str,
    deliveryoferrsdu: int,
    transferdelay: int,
    traffichandlingpriority: int,
    sourcestatisticsdescriptor: int,
    signallingindication: int,
):
    """Write quality of service profile 3G requested."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1005QualityOfServiceProfile3gRequestedWrite(
            cid,
            trafficclass,
            maxbitrateul,
            maxbitratedl,
            guaranteedbitrateul,
            guaranteedbitratedl,
            deliveryorder,
            maxsdusize,
            sduerrorratio,
            residualbiterrorratio,
            deliveryoferrsdu,
            transferdelay,
            traffichandlingpriority,
            sourcestatisticsdescriptor,
            signallingindication,
        )
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def quality_of_service_profile3g_minimum_acceptable(ctx):
    """Group for quality of service profile 3G minimum acceptable."""
    pass


@quality_of_service_profile3g_minimum_acceptable.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read quality of service profile 3G minimum acceptable."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1006QualityOfServiceProfile3gMinimumAcceptableRead()
    )
    print(response if status else "Error")
    client.close()


@quality_of_service_profile3g_minimum_acceptable.command("write")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
PDP context identifier, a numeric parameter which specifies a
particular PDP context definition. The parameter is local to the TE-
MT interface and is used in other PDP context-related commands.
The range of permitted values (minimum value=1) is returned by
the test form of the command.
""",
)
@click.option(
    "--trafficclass",
    "-t",
    type=int,
    required=True,
    help="""
Indicates the type of application for which the UMTS
bearer service is optimized (see 3GPP TS 24.008 subclause
10.5.6.5). If the parameter is specified as conversational or
streaming, then the Guaranteed and Maximum bitrate parameters
should also be provided.
0                               Conversational
1                               Streaming
2                               Interactive
3                               Background
4                               Subscribed value
""",
)
@click.option(
    "--maxbitrateul",
    "-u",
    type=int,
    required=True,
    help="""
Indicates the maximum number of kbits/s delivered to
UMTS (up-link traffic) at a SAP. As an example, a bit rate of
32 kbit/s would be specified as ‘32’
(e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--maxbitratedl",
    "-d",
    type=int,
    required=True,
    help="""
Indicates the maximum number of kbits/s delivered by
UMTS (down-link traffic) at a SAP. As an example, a bitrate of
32 kbit/s would be specified as ‘32’
(e.g. AT+CGEQREQ=…,32, …).
Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--guaranteedbitrateul",
    "-g",
    type=int,
    required=True,
    help="""
Indicates the guaranteed number of kbits/s delivered
to UMTS (up-link traffic) at a SAP (provided that there is data to
deliver). As an example, a bitrate of 32 kbit/s would be specified as
‘32’ (e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--guaranteedbitratedl",
    "-l",
    type=int,
    required=True,
    help="""
Indicates the guaranteed number of kbits/s delivered
by UMTS (down-link traffic) at a SAP (provided that there is data to
deliver). As an example, a bitrate of 32 kbit/s would be specified as
‘32’ (e.g. AT+CGEQREQ=…,32, …). Range: 0–256000.
0                               Subscribed value
0–64
64–568                          (value needs to be a multiple of 8)
568–8640                        (value needs to be a multiple of 64)
8640–16000                      (value needs to be a multiple of 100)
16000–128000                    (value needs to be a multiple of 1000)
128000–256000                   (value needs to be a multiple of 2000)
""",
)
@click.option(
    "--deliveryorder",
    "-o",
    type=int,
    required=True,
    help="""
Indicates whether the UMTS bearer shall provide in-
sequence SDU delivery or not (see 3GPP TS 24.008 subclause
10.5.6.5).
0                               No
1                               Yes
2                               Subscribed value
""",
)
@click.option(
    "--maxsdusize",
    "-s",
    type=int,
    required=True,
    help="""
(1,2,3,…) indicates the maximum allowed SDU size in
octets. If the parameter is set to ‘0’ the subscribed value will be
requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed value
10–520                          (Value needs to be divisible by 10 without remainder)
1520
""",
)
@click.option(
    "--sduerrorratio",
    "-e",
    type=str,
    required=True,
    help="""
Indicates the target value for the fraction of SDUs lost
or detected as erroneous. SDU error ratio is defined only for
conforming traffic. The value is specified as ‘mEe’. As an example, a
target SDU error ratio of 5 × 10-3 would be specified as "5E3" (e.g.
AT+CGEQREQ=…,"5E3",…).
"0E0"                           Subscribed value
"1E2"
"7E3"
"1E3"
"1E4"
"1E5"
"1E6"
"1E1"
""",
)
@click.option(
    "--residualbiterrorratio",
    "-r",
    type=str,
    required=True,
    help="""
Indicates the target value for the undetected bit error
ratio in the delivered SDUs. If no error detection is requested,
Residual bit error ratio indicates the bit error ratio in the delivered
SDUs. The value is specified as “mEe”. As an example, a target
residual bit error ratio of 5 × 10-3 would be specified as "5E3" (e.g.
AT+CGEQREQ=…,"5E3",…).
"0E0"                           Subscribed value
"5E2"
"1E2"
"5E3"
"4E3"
"1E3"
"1E4"
"1E5"
"1E6"
"6E8"
""",
)
@click.option(
    "--deliveryoferrsdu",
    "-f",
    type=int,
    required=True,
    help="""
Indicates whether SDUs detected as erroneous shall
be delivered or not (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               No
1                               Yes
2                               No detect
3                               Subscribed value
""",
)
@click.option(
    "--transferdelay",
    "-t",
    type=int,
    required=True,
    help="""
(0,1,2,…) indicates the targeted time between request
to transfer an SDU at one SAP to its delivery at the other SAP, in
milliseconds. If the parameter is set to ‘0’ the subscribed value will
be requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed value
100–150                         (value needs to be divisible by 10 without remainder)
200–950                         (value needs to be divisible by 50 without remainder)
1000–4000                       (value needs to be divisible by 100 without remainder)
""",
)
@click.option(
    "--traffichandlingpriority",
    "-h",
    type=int,
    required=True,
    help="""
(1,2,3,…) specifies the relative importance for handling
of all SDUs belonging to the UMTS bearer compared to the SDUs
of other bearers. If the parameter is set to ‘0’ the subscribed value
will be requested (see 3GPP TS 24.008 subclause 10.5.6.5).
0                               Subscribed
1
2
3
""",
)
@click.option(
    "--sourcestatisticsdescriptor",
    "-s",
    type=int,
    required=True,
    help="""
Specifies characteristics of the source of the submitted
SDUs for a PDP context.
0                               Characteristics of SDUs is unknown
1                               Characteristics of SDUs correspond to a speech source
""",
)
@click.option(
    "--signallingindication",
    "-i",
    type=int,
    required=True,
    help="""
Indicates signaling content of submitted SDUs for a
PDP context.
0                               PDP context is not optimized for signaling
1                               PDP context is optimized for signaling
""",
)
def write(  # type: ignore[reportRedeclaration]
    ctx,
    cid: int,
    trafficclass: int,
    maxbitrateul: int,
    maxbitratedl: int,
    guaranteedbitrateul: int,
    guaranteedbitratedl: int,
    deliveryorder: int,
    maxsdusize: int,
    sduerrorratio: str,
    residualbiterrorratio: str,
    deliveryoferrsdu: int,
    transferdelay: int,
    traffichandlingpriority: int,
    sourcestatisticsdescriptor: int,
    signallingindication: int,
):
    """Write quality of service profile 3G minimum acceptable."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1006QualityOfServiceProfile3gMinimumAcceptableWrite(
            cid,
            trafficclass,
            maxbitrateul,
            maxbitratedl,
            guaranteedbitrateul,
            guaranteedbitratedl,
            deliveryorder,
            maxsdusize,
            sduerrorratio,
            residualbiterrorratio,
            deliveryoferrsdu,
            transferdelay,
            traffichandlingpriority,
            sourcestatisticsdescriptor,
            signallingindication,
        )
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def activate_deactivate_pdp_context(ctx):
    """Group for activate deactivate PDP context."""
    pass


@activate_deactivate_pdp_context.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read activate deactivate PDP context."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1007ActivateDeactivatePdpContextRead()
    print(response if status else "Error")
    client.close()


@activate_deactivate_pdp_context.command("write")
@click.pass_context
@click.option(
    "--state",
    "-s",
    type=int,
    required=True,
    help="""
Indicates the state of PDP context activation
0                   Deactivated
1                   Activated
Other values are reserved and will result in an ERROR response to the Write Command
""",
)
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
A numeric parameter which specifies a particular PDP context definition (see AT+CGDCONT)
""",
)
def write(ctx, state: int, cid: int):  # type: ignore[reportRedeclaration]
    """Write activate deactivate PDP context."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1007ActivateDeactivatePdpContextWrite(
        state, cid
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.command("enter-data-state")
@click.pass_context
@click.option(
    "--l2p",
    "-l",
    type=str,
    required=True,
    help="""
The layer 2 protocol to be used between the TE and MT:
PPP (Point to Point protocol) for a PDP such as IP
Other values are not supported and will result in an ERROR response to the execution
command
""",
)
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
The particular PDP context definition (see AT+CGDCONT)
""",
)
def enter_data_state(ctx, l2p: str, cid: int):
    """Enter data state."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1008EnterDataState(l2p, cid)
    print(response if status else "Error")
    client.close()


@packet_domain_commands.command("show-pdp-address")
@click.pass_context
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
The particular PDP context definition (see AT+CGDCONT)
""",
)
def show_pdp_address(ctx, cid: int):
    """Show PDP address."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1009ShowPdpAddress(cid)
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def gprs_mobile_station_class(ctx):
    """Group for GPRS mobile station class."""
    pass


@gprs_mobile_station_class.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read GPRS mobile station class."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1010GprsMobileStationClassRead()
    print(response if status else "Error")
    client.close()


@gprs_mobile_station_class.command("write")
@click.pass_context
@click.option(
    "--gprsclass",
    "-c",
    type=str,
    required=True,
    help="""
GPRS mobile class (Functionality in descending order).
"A" Class-A mode of operation (A/Gb mode), or CS/PS mode of operation (Iu mode)
(highest mode of operation)
""",
)
def write(ctx, gprsclass: str):  # type: ignore[reportRedeclaration]
    """Write GPRS mobile station class."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1010GprsMobileStationClassWrite(
        gprsclass
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def ps_domain_network_registration_status(ctx):
    """Group for PS domain network registration status."""
    pass


@ps_domain_network_registration_status.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read PS domain network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1011PsDomainNetworkRegistrationStatusRead()
    )
    print(response if status else "Error")
    client.close()


@ps_domain_network_registration_status.command("write")
@click.pass_context
@click.option(
    "--n",
    "-n",
    type=int,
    required=True,
    help="""
0           Disable network registration unsolicited result code
1           Enable network registration unsolicited result code +CGREG: <stat>
2           Enable network registration and location information unsolicited result code +CGREG: <stat>[,<lac>,<ci>[,<Act>]]
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write PS domain network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1011PsDomainNetworkRegistrationStatusWrite(n)
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def packet_domain_event_reporting(ctx):
    """Group for packet domain event reporting."""
    pass


@packet_domain_event_reporting.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read packet domain event reporting."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1012PacketDomainEventReportingRead()
    print(response if status else "Error")
    client.close()


@packet_domain_event_reporting.command("write")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
0               Buffer unsolicited result codes in the MT; if MT result code buffer is full, the oldest
                ones can be discarded. No codes are forwarded to the TE.
1               Discard unsolicited result codes when MT-TE link is reserved (e.g. in on-line data
                mode), otherwise forward them directly to the TE.
2               Buffer unsolicited result codes in the MT when MT-TE link is reserved (e.g. in
                on-line data mode) and flush them to the TE when MT-TE link becomes available.
                Otherwise forward them directly to the TE.
""",
)
@click.option(
    "--bfr",
    "-b",
    type=int,
    required=True,
    help="""
0               MT buffer of unsolicited result codes defined within this command is cleared when
                <mode> 1 or 2 is entered.
1               MT buffer of unsolicited result codes defined within this command is flushed to the
                TE when <mode> 1 or 2 is entered (OK response shall be given before flushing
                the codes).
""",
)
def write(ctx, mode: int, bfr: int):  # type: ignore[reportRedeclaration]
    """Write packet domain event reporting."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1012PacketDomainEventReportingWrite(
        mode, bfr
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def select_service_for_mo_sms_messages(ctx):
    """Group for select service for MO SMS messages."""
    pass


@select_service_for_mo_sms_messages.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read select service for MO SMS messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1013SelectServiceForMoSmsMessagesRead()
    )
    print(response if status else "Error")
    client.close()


@select_service_for_mo_sms_messages.command("write")
@click.pass_context
@click.option(
    "--service",
    "-s",
    type=int,
    required=True,
    help="""    
Service or service preference to be used
0                   GPRS
1                   Circuit switch
2                   GPRS preferred (use circuit switched if GPRS not available)
3                   Circuit switch preferred (use GPRS if circuit switched not available)
""",
)
def write(ctx, service: int):  # type: ignore[reportRedeclaration]
    """Write select service for MO SMS messages."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1013SelectServiceForMoSmsMessagesWrite(service)
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def eps_network_registration_status(ctx):
    """Group for EPS network registration status."""
    pass


@eps_network_registration_status.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read EPS network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1014EpsNetworkRegistrationStatusRead()
    print(response if status else "Error")
    client.close()


@eps_network_registration_status.command("write")
@click.pass_context
@click.option(
    "--n",
    "-n",
    type=int,
    required=True,
    help="""
0               Disable network registration unsolicited result code
1               Enable network registration unsolicited result code +CEREG: <stat>
2               Enable network registration and location information unsolicited result code
                +CEREG: <stat>[,<tac>,<ci>[,<Act>]]
                """,
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write EPS network registration status."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1014EpsNetworkRegistrationStatusWrite(
        n
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def packet_data_counter(ctx):
    """Group for packet data counter."""
    pass


@packet_data_counter.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read packet data counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1015PacketDataCounterRead()
    print(response if status else "Error")
    client.close()


@packet_data_counter.command("write")
@click.pass_context
@click.option(
    "--op",
    "-o",
    type=int,
    required=True,
    help="""
The operation about data counter
0               Reset the data counter
1               Save the results of data counter to NV
                If the results need to be automatically saved, see AT+QAUGDCNT.    
""",
)
def write(ctx, op: int):  # type: ignore[reportRedeclaration]
    """Write packet data counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1015PacketDataCounterWrite(op)
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def auto_save_packet_data_counter(ctx):
    """Group for auto save packet data counter."""
    pass


@auto_save_packet_data_counter.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read auto save packet data counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1016AutoSavePacketDataCounterRead()
    print(response if status else "Error")
    client.close()


@auto_save_packet_data_counter.command("write")
@click.pass_context
@click.option(
    "--value",
    "-v",
    type=int,
    required=True,
    help="""
The time-interval for AT+QGDCNT to save results to NV automatically. If it
is set to 0, auto-save feature would be disabled. Range: 0, 30–65535. Default value: 0.
Unit: second.
""",
)
def write(ctx, value: int):  # type: ignore[reportRedeclaration]
    """Write auto save packet data counter."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1016AutoSavePacketDataCounterWrite(
        value
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def connect_usb_netcard_to_network(ctx):
    """Group for connect USB netcard to network."""
    pass


@connect_usb_netcard_to_network.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read connect USB netcard to network."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1017ConnectUsbNetcardToNetworkRead()
    print(response if status else "Error")
    client.close()


@connect_usb_netcard_to_network.command("write")
@click.pass_context
@click.option(
    "--type",
    "-t",
    type=int,
    required=True,
    help="""
The type of the network connection.
0                   Disconnect the network connection.
1                   Connect the network connection.    
""",
)
@click.option(
    "--cid",
    "-c",
    type=int,
    required=True,
    help="""
The PDP context identifier.    
""",
)
@click.option(
    "--urc-en",
    "-u",
    type=int,
    required=True,
    help="""
Whether to enable the URC +QNETDEVSTATUS: <status> showing the netcard status:

            - **0** :       Disable the URC.
            - **1** :       Enable the URC.
""",
)
def write(ctx, type: int, cid: int, urc_en: int):  # type: ignore[reportRedeclaration]
    """Write connect USB netcard to network."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.packetDomainCommands1017ConnectUsbNetcardToNetworkWrite(
        type, cid, urc_en
    )
    print(response if status else "Error")
    client.close()


@packet_domain_commands.group()
@click.pass_context
def configure_response_format_of_at_ceer_in2g4g(ctx):
    """Group for configure response format of AT+CEER in 2G/4G."""
    pass


@configure_response_format_of_at_ceer_in2g4g.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read configure response format of AT+CEER in 2G/4G."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1018ConfigureResponseFormatOfAtCeerIn2g4gRead()
    )
    print(response if status else "Error")
    client.close()


@configure_response_format_of_at_ceer_in2g4g.command("write")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
Return format of AT+CEER.
        0           The return format of AT+CEER is +CEER: <text>
        1           The return format of AT+CEER is +CEER: <category>,<cause>,<description>
""",
)
def write(ctx, mode: int):  # type: ignore[reportRedeclaration]
    """Write configure response format of AT+CEER in 2G/4G."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.packetDomainCommands1018ConfigureResponseFormatOfAtCeerIn2g4gWrite(mode)
    )
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def hardware_related_commands(ctx):
    """Group for hardware related commands."""
    pass


@hardware_related_commands.command("power-off")
@click.pass_context
@click.option(
    "--n",
    "-n",
    type=int,
    required=True,
    help="""
0               Immediately power down
1               Normal power down    
""",
)
def power_off(ctx, n: int):
    """Power off."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1101PowerOff(n)
    print(response if status else "Error")
    client.close()


@hardware_related_commands.group()
@click.pass_context
def clock(ctx):
    """Group for clock."""
    pass


@clock.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read clock."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1102ClockRead()
    print(response if status else "Error")
    client.close()


@clock.command("write")
@click.pass_context
@click.option(
    "--time",
    "-t",
    type=str,
    required=True,
    help="""
The format is “yy/MM/dd,hh:mm:ss±zz”, indicating year (two last digits), month,
day, hour, minutes, seconds and time zone (indicates the difference, expressed in quarters
of an hour, between the local time and GMT; range: -48 to +56), e.g. May 6th, 1994, 22:10:00
GMT+2 hours equals to “94/05/06,22:10:00+08”.
""",
)
def write(ctx, time: str):  # type: ignore[reportRedeclaration]
    """Write clock."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1102ClockWrite(time)
    print(response if status else "Error")
    client.close()


@hardware_related_commands.group()
@click.pass_context
def enable_disable_sleep_mode(ctx):
    """Group for enable disable sleep mode."""
    pass


@enable_disable_sleep_mode.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read enable disable sleep mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1103EnableDisableSleepModeRead()
    print(response if status else "Error")
    client.close()


@enable_disable_sleep_mode.command("write")
@click.pass_context
@click.option(
    "--n",
    "-n",
    type=int,
    required=True,
    help="""
0           Disable
1           Enable. It is controlled by DTR pin and WAKEUP_IN pin.
""",
)
def write(ctx, n: int):  # type: ignore[reportRedeclaration]
    """Write enable disable sleep mode."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1103EnableDisableSleepModeWrite(n)
    print(response if status else "Error")
    client.close()


@hardware_related_commands.command("query-read-battery-charge-information")
@click.pass_context
def query_read_battery_charge_information(ctx):
    """Query read battery charge information."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.hardwareRelatedCommands1104QueryReadBatteryChargeInformation()
    )
    print(response if status else "Error")
    client.close()


@hardware_related_commands.command("read-adc-value")
@click.pass_context
@click.option(
    "--port",
    "-p",
    type=int,
    required=True,
    help="""
Channel number of the ADC.
0               ADC Channel 0
1               ADC Channel 1
""",
)
def read_adc_value(ctx, port: int):
    """Read ADC value."""
    client: QuectelModemATCommands = ctx.obj["client"]
    client.open()
    status, response = client.hardwareRelatedCommands1105ReadAdcValue(port)
    print(response if status else "Error")
    client.close()


if __name__ == "__main__":
    main()
