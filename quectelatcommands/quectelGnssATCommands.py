#!/usr/bin/env python3

from typing import Optional
from quectelatcommands.quectelSerial import QuectelSerial


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

    def configureGnss20201ConfigureOutputPortOfNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20201: output port of NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="outport"')

    def configureGnss20201ConfigureOutputPortOfNmeaSentencesWrite(
        self, p_out_port: str
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20201: output port of NMEA sentences.

        :param p_out_port: String type. Configure the output port of NMEA sentences:

                    - **"none"**:  Close NMEA sentence output
                    - **"usbnmea"**:   Output via USB NMEA port
                    - **"uartdebug"**: Output via debug UART port
        :type p_out_port: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="outport","{p_out_port}"')

    def configureGnss20202EnableDisableAcquisitionOfNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20202: enable/disable acquisition of NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="nmeasrc"')

    def configureGnss20202EnableDisableAcquisitionOfNmeaSentencesWrite(
        self, p_nmea_src: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20202: enable/disable acquisition of NMEA sentences.

        :param p_nmea_src:  Integer type. If enabled, original NMEA sentences can be acquired via
                            AT+QGPSGNMEA. Meanwhile, sentences are outputted via the AT port as a return value:

                            - **0**: Disable
                            - **1**: Enablee
        :type p_nmea_src: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="nmeasrc",{p_nmea_src}')

    def configureGnss20203ConfigureOutputTypeOfGpsNmeaRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20203: Read the output type of GPS NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gpsnmeatype"')

    def configureGnss20203ConfigureOutputTypeOfGpsNmeaWrite(
        self, p_gps_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20203: Configure the output type of GPS NMEA sentences.

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

    def configureGnss20204ConfigureOutputTypeOfGlonassNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20204: Read the output type of GLONASS NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="glnmeatype"')

    def configureGnss20204ConfigureOutputTypeOfGlonassNmeaSentencesWrite(
        self, p_glonass_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20204: Configure the output type of GLONASS NMEA sentences.

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

    def configureGnss20205ConfigureOutputTypeOfGalileoNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20205: Read the output type of Galileo NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="galileonmeatype"')

    def configureGnss20205ConfigureOutputTypeOfGalileoNmeaSentencesWrite(
        self, p_galileo_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20205: Configure the output type of Galileo NMEA sentences.

        :param p_galileo_nmea_type: Integer type. Configure output type of Galileo NMEA sentences in ORed:

                        - **0**: Disable
                        - **1**: GAGSV

        :type p_galileo_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="galileonmeatype",{p_galileo_nmea_type}')

    def configureGnss20206ConfigureOutputTypeOfBeidouNmeaSentencesRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20206: Read the output type of Beidou NMEA sentences.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="beidounmeatype"')

    def configureGnss20206ConfigureOutputTypeOfBeidouNmeaSentencesWrite(
        self, p_beidou_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20206: Configure the output type of Beidou NMEA sentences.

        :param p_beidou_nmea_type: Integer type. Configure output type of Beidou NMEA sentences in ORed:

                            - **0**: Disable
                            - **1**: PQGSA
                            - **2**: PQGSV

        :type p_beidou_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="beidounmeatype",{p_beidou_nmea_type}')

    def configureGnss20207ConfigureSupportedGnssConstellationsRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20207: Read the supported GNSS constellations.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gnssconfig"')

    def configureGnss20207ConfigureSupportedGnssConstellationsWrite(
        self, p_gnss_config: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20207: Configure the supported GNSS constellations.

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

    def configureGnss20208ConfigureOdpModeRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20208: Read the ODP mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="odpcontrol"')

    def configureGnss20208ConfigureOdpModeWrite(
        self, p_odp_control: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20208: Configure the ODP mode.

        :param p_odp_control: Integer type. Set ODP mode:

                        - **0**: Disable ODP
                        - **1**: Low power mode
                        - **2**: Ready mode

        :type p_odp_control: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="odpcontrol",{p_odp_control}')

    def configureGnss20209EnableDisableDpoModeRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20209: Read the DPO mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="dpoenable"')

    def configureGnss20209EnableDisableDpoModeWrite(
        self, p_dpo_enable: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20209: Configure the DPO mode.

        :param p_dpo_enable: Integer type. Enable/Disable DPO:

                        - **0**: Disable DPO
                        - **1**: Enable DPO with dynamic duty cycle

        :type p_dpo_enable: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="dpoenable",{p_dpo_enable}')

    def configureGnss20210EnableDisableGnssExtendedGgsvRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20210: Read the GNSS extended GGSV.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gsvextnmeatype"')

    def configureGnss20210EnableDisableGnssExtendedGgsvWrite(
        self, gsvext_nmea_type: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20210: Configure the GNSS extended GGSV.

        :param gsvext_nmea_type: Integer type. Enable/Disable extended GGSV:

                        - **0**: Disable extended GGSV
                        - **1**: Display extended GGSV

        :type gsvext_nmea_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="gsvextnmeatype",{gsvext_nmea_type}')

    def configureGnss20211ConfigurePlaneModeUsedByMoAgpsSessionRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20211: Read the plane mode used by MO AGPS session.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="plane"')

    def configureGnss20211ConfigurePlaneModeUsedByMoAgpsSessionWrite(
        self, p_plane: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20211: Configure the plane mode used by MO AGPS session.

        :param p_plane: Integer type. The plane mode used by MO AGPS session:

                        - **0**: User plane without SSL
                        - **1**: User plane with SSL
                        - **2**: Control plane
        :type p_plane: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="plane",{p_plane}')

    def configureGnss20212EnableDisableGnssToRunAutomaticallyRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20212: Read the GNSS to run automatically.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="autogps"')

    def configureGnss20212EnableDisableGnssToRunAutomaticallyWrite(
        self, p_autogps: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20212: Configure the GNSS to run automatically.

        :param p_autogps: Integer type. Enable/disable GNSS to run automatically after the module is powered on:

                    - **0**: Disable GNSS to run automatically
                    - **1**: Enable GNSS to run automatically

        :type p_autogps: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="autogps",{p_autogps}')

    def configureGnss20213ConfigureSuplProtocolVersionRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20213: Read the SUPL protocol version.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="suplver"')

    def configureGnss20213ConfigureSuplProtocolVersionWrite(
        self, p_supl_version: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20213: Configure the SUPL protocol version.

        :param p_supl_version: Integer type. The SUPL protocol version:

                    - **0**: SUPL version 1.0
                    - **1**: SUPL version 2.0

        :type p_supl_version: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="suplver",{p_supl_version}')

    def configureGnss20214ConfigureAgpsPositioningModeRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20214: Read the AGPS positioning mode.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="agpsposmode"')

    def configureGnss20214ConfigureAgpsPositioningModeWrite(
        self, p_agps_posmode: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20214: Configure the AGPS positioning mode.

        :param p_agps_posmode: Integer type. The AGPS positioning mode:

            - **Bit 0**: Standalone
            - **Bit 1**: UP MS-based
            - **Bit 2**: UP MS-assisted
            - **Bit 3**: CP MS-based (2G)
            - **Bit 4**: CP MS-assisted (2G)
            - **Bit 5**: CP UE-based (3G)
            - **Bit 6**: CP UE-assisted (3G)
            - **Bit 7**: UP network measurement report (2G)
            - **Bit 8**: UP MS-based (4G)
            - **Bit 9**: UP MS-assisted (4G)
            - **Bit 10**: CP MS-based (4G)
            - **Bit 11**: CP MS-assisted (4G)
            - **Bit 16**: Enabling of autonomous fallback for SUPL-MSB
            - **Bit 17**: A-GLONASS UP MS-based for 3G
            - **Bit 18**: A-GLONASS UP MS-assisted for 3G
            - **Bit 19**: A-GLONASS CP MS-based for 3G
            - **Bit 20**: A-GLONASS CP MS-assisted for 3G
            - **Bit 21**: A-GLONASS UP MS-based for 4G
            - **Bit 202**: A-GLONASS UP MS-assisted for 4G
            - **Bit 203**: A-GLONASS CP MS-based for 4G
            - **Bit 204**: A-GLONASS CP MS-assisted for 4Ge

        :type p_agps_posmode: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="agpsposmode",{p_agps_posmode}')

    def configureGnss20215ConfigureAgnssPositioningProtocolsRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20215: Read the AGNSS positioning protocols.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="agnssprotocol"')

    def configureGnss20215ConfigureAgnssPositioningProtocolsWrite(
        self, agps_lp: int, p_aglonass_lp: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20215: Configure the AGNSS positioning protocols.

        :param agps_lp: Integer type. A-GPS LPP positioning protocol in ORed. Default: 3:

                        - **1**: User plane LPP
                        - **2**: Control plane LPP

        :type agps_lp: int
        :param p_aglonass_lp: Integer type. A-GLONASS positioning protocol in ORed. Default: 12087:

                        - **1**:       Control plane RRLP
                        - **2**:       Control plane RRC
                        - **4**:       Control plane LPP
                        - **2056**:     User plane RRLP
                        - **10204**:    User plane LPP

        :type p_aglonass_lp: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="agnssprotocol",{agps_lp},{p_aglonass_lp}')

    def configureGnss20216ConfigureNmeaOutputFrequencyRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20216: Read the NMEA output frequency.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="fixfreq"')

    def configureGnss20216ConfigureNmeaOutputFrequencyWrite(
        self, p_freq: int
    ) -> tuple[bool, list[str]]:
        """
        Configure GNSS 20216: Configure the NMEA output frequency.

        :param p_freq: Integer type. NMEA sentence output frequency:

                        - **1**: 1 Hz
                        - **2**: 2 Hz
                        - **5**: 5 Hz
                        - **10**: 10 Hz

        :type p_freq: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSCFG="fixfreq",{p_freq}')

    def gnssGeneralCommands20300DeleteAssistanceData(
        self, pdelete_type: int
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20300: Delete assistance data.

        :param pdelete_type: Integer type. The type of GNSS assistance data to be deleted:

        - **0**: Delete all assistance data. Enforce cold start after starting GNSS.
        - **1**: Do not delete any data. Perform hot start if the conditions are permitted after starting GNSS.
        - **2**: Delete some related data. Perform warm start if the conditions are permitted after starting GNSS.
        - **3**: Delete the gpsOneXTRA assistance data injected into GNSS engine.

        :type pdelete_type: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSDEL={pdelete_type}")

    def gnssGeneralCommands20400TurnOnGnssRead(self) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20400: Turn on GNSS.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QGPS?")

    def gnssGeneralCommands20400TurnOnGnssWrite(
        self,
        p_gnss_mode: int,
        p_fix_maxtime: Optional[int],
        p_fix_maxdist: Optional[int],
        p_fix_count: Optional[int],
        p_fix_rate: Optional[int],
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20400: Turn on GNSS.

        :param p_gnss_mode: Integer type. GNSS working mode:

        - **1**: Stand-alone
        - **2**: MS-based
        - **3**: MS-assisted
        - **4**: Speed-optimal

        :type p_gnss_mode: int
        :param p_fix_maxtime: Integer type. The maximum positioning time, which indicates the response time of
                                            GNSS receiver while measuring the GNSS pseudo range and the upper time limit of
                                            GNSS satellite searching. It also includes the time for demodulating the ephemeris
                                            data and calculating the position. Range: 1–2055. Default: 2055. Unit: second.

        :type p_fix_maxtime: int
        :param p_fix_maxdist: Integer type. Accuracy threshold of positioning. Range: 0–1000. Default: 50. Unit: meter.

        :type p_fix_maxdist: int
        :param p_fix_count: Integer type. Positioning times. Range: 0–1000. Default: 0:

        -**0**: Continuous positioning.
        -**Other values**: Actual positioning times.

        :type p_fix_count: int
        :param p_fix_rate: Integer type. The interval between the first and the second positioning.
                                        Range: 1–65535. Default value: 1. Unit: second.

        :type p_fix_rate: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        if (
            p_fix_maxtime is not None
            and p_fix_maxdist is not None
            and p_fix_count is not None
            and p_fix_rate is not None
        ):
            return self.sendCommand(
                f"AT+QGPS={p_gnss_mode},{p_fix_maxtime},{p_fix_maxdist},{p_fix_count},{p_fix_rate}"
            )
        elif (
            p_fix_maxtime is not None
            and p_fix_maxdist is not None
            and p_fix_count is not None
        ):
            return self.sendCommand(
                f"AT+QGPS={p_gnss_mode},{p_fix_maxtime},{p_fix_maxdist},{p_fix_count}"
            )
        elif p_fix_maxtime is not None and p_fix_maxdist is not None:
            return self.sendCommand(
                f"AT+QGPS={p_gnss_mode},{p_fix_maxtime},{p_fix_maxdist}"
            )
        elif p_fix_maxtime is not None:
            return self.sendCommand(f"AT+QGPS={p_gnss_mode},{p_fix_maxtime}")
        else:
            return self.sendCommand(f"AT+QGPS={p_gnss_mode}")

    def gnssGeneralCommands20500TurnOffGnssRead(self) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20500: Turn off GNSS.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QGPSEND?")

    def gnssGeneralCommands20500TurnOffGnssWrite(self) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20500: Turn off GNSS.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand("AT+QGPSEND")

    def gnssGeneralCommands20600AcquirePositioningInformation(
        self, p_mode: int
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20600: Acquire positioning information.

        :param p_mode: Integer type. Latitude and longitude display format:

                        - **0** <latitude>,<longitude> format: ddmm.mmmmN/S,dddmm.mmmmE/W
                        - **1** <latitude>,<longitude> format: ddmm.mmmmmm,N/S,dddmm.mmmmmm,E/W
                        - **2** <latitude>,<longitude> format: (-)dd.ddddd,(-)ddd.ddddd

        :type p_mode: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSLOC={p_mode}")

    def gnssGeneralCommands20700ConfigureSuplServerUrlRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20700: Read the SUPL server URL.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSSUPLURL?")

    def gnssGeneralCommands20700ConfigureSuplServerUrlWrite(
        self, p_supl_url: str
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20700: Configure the SUPL server URL.

        :param p_supl_url:  String type. SUPL server address. The address format is "URL:port_number" where
                            the “port_number” can be omitted, for example "supl.server.com", "1203.1203.1203.1203",
                            and "supl.server.com:72075". When the “port number” is omitted, the default value
                            (72075) will be used.

        :type p_supl_url: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSSUPLURL={p_supl_url}")

    def gnssGeneralCommands20800InjectSuplCertificateRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20800: Read the SUPL certificate.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSSUPLCA?")

    def gnssGeneralCommands20800InjectSuplCertificateWrite(
        self, p_ca_file_name: str
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20800: Inject the SUPL certificate.

        :param p_ca_file_name: String type. SUPL certificate name.

        :type p_ca_file_name: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSSUPLCA="{p_ca_file_name}"')

    def gnssGeneralCommands20900AcquireNmeaSentences(
        self, p_nmea_type: str
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 20900: Acquire NMEA sentences.

        :param p_nmea_type: String type. String type. NMEA sentence type:

                            - **"GGA"**: Acquire GGA sentence
                            - **"RMC"**: Acquire RMC sentence
                            - **"GSV"**: Acquire GSV sentence
                            - **"GSA"**: Acquire GSA sentence
                            - **"VTG"**: Acquire VTG sentence

        :type p_nmea_type: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSGNMEA="{p_nmea_type}"')

    def gnssGeneralCommands21000EnableDisableGpsOneXtraAssistanceRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 21000: Read the GPS OneXTRA assistance.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSXTRA?")

    def gnssGeneralCommands21000EnableDisableGpsOneXtraAssistanceWrite(
        self, p_xtra_enable: int
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 21000: Enable/disable GPS OneXTRA assistance.

        :param p_xtra_enable: Integer type. Enable/disable gpsOneXTRA Assistance function:

                            - **0**: Disable gpsOneXTRA Assistance
                            - **1**: Enable gpsOneXTRA Assistance

        :type p_xtra_enable: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSXTRA={p_xtra_enable}")

    def gnssGeneralCommands21100InjectGpsOneXtraTime(
        self, p_type: int, p_xtratime: str, p_utc: int, p_force: int, p_uncrtn: int
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 21100: Inject gpsOneXTRA time.

        :param p_type:      Integer type. Type of injecting time:

                                - **0**: Inject XTRA time manually

        :type p_type: int
        :param p_xtratime:  Sting type. Current UTC time.
                            Format: "YYYY/MM/DD,hh:mm:ss". e.g. "2019/01/05,08:30:30".

        :type p_xtratime: str
        :param p_utc:       Integer type. UTC or GPS time that gpsOneXTRA time refers to:

                                - **0**: GPS time
                                - **1**: UTC time (Recommended).

        :type p_utc: int
        :param p_force:     Integer type. Whether to force GNSS to accept the data:

                                    - **0**: Not force GNSS to accept the data
                                    - **1**: Force acceptance of data (Recommended).

        :type p_force: int
        :param p_uncrtn:    Integer type. Uncertainty of time. It indicates the time difference between sending a
                            request to the SNTP server and receiving a response from the SNTP server. Default:
                            3500. Unit: millisecond.

        :type p_uncrtn: int

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(
            f'AT+QGPSXTRATIME={p_type},"{p_xtratime}",{p_utc},{p_force},{p_uncrtn}'
        )

    def gnssGeneralCommands21200InjectGpsOneXtraDataFileRead(
        self,
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 21200: Read the gpsOneXTRA data file.

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f"AT+QGPSXTRADATA?")

    def gnssGeneralCommands21200InjectGpsOneXtraDataFileWrite(
        self, p_xtradatafilename: str
    ) -> tuple[bool, list[str]]:
        """
        GNSS General Commands 21200: Inject the gpsOneXTRA data file.

        :param p_xtradatafilename:  String type. Filename of the gpsOneXTRA data file, e.g. "RAM:xtra2.bin" or
                                    "RAM:xtra3grc.bin", in which, RAM indicates the actual file storage area.

        :type p_xtradatafilename: str

        :return: Tuple containing the status of the command and the response.
        :rtype: tuple[bool, list[str]]
        """
        return self.sendCommand(f'AT+QGPSXTRADATA="{p_xtradatafilename}"')


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
def free_at_command(ctx, command: str):
    """Free AT command."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.freeAtCommand(command)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def configure_gnss(ctx):
    """Configure GNSS 20201."""
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
    status, response = client.configureGnss20201ConfigureOutputPortOfNmeaSentencesRead()
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
def write(ctx, out_port: str):  # type: ignore[reportRedeclaration]
    """Write the output port of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20201ConfigureOutputPortOfNmeaSentencesWrite(
        out_port
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
        client.configureGnss20202EnableDisableAcquisitionOfNmeaSentencesRead()
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
def write(ctx, nmea_src: int):  # type: ignore[reportRedeclaration]
    """Write the acquisition of NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20202EnableDisableAcquisitionOfNmeaSentencesWrite(nmea_src)
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
    status, response = client.configureGnss20203ConfigureOutputTypeOfGpsNmeaRead()
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
def write(ctx, gps_nmea_type: int):  # type: ignore[reportRedeclaration]
    """Write the output type of GPS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20203ConfigureOutputTypeOfGpsNmeaWrite(
        gps_nmea_type
    )
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
        client.configureGnss20204ConfigureOutputTypeOfGlonassNmeaSentencesRead()
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
def write(ctx, glonass_nmea_type: int):  # type: ignore[reportRedeclaration]
    """Write the output type of GLONASS NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20204ConfigureOutputTypeOfGlonassNmeaSentencesWrite(
            glonass_nmea_type
        )
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
        client.configureGnss20205ConfigureOutputTypeOfGalileoNmeaSentencesRead()
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
def write(ctx, galileo_nmea_type: int):  # type: ignore[reportRedeclaration]
    """Write the output type of Galileo NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20205ConfigureOutputTypeOfGalileoNmeaSentencesWrite(
            galileo_nmea_type
        )
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
        client.configureGnss20206ConfigureOutputTypeOfBeidouNmeaSentencesRead()
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
def write(ctx, beidou_nmea_type: int):  # type: ignore[reportRedeclaration]
    """Write the output type of Beidou NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20206ConfigureOutputTypeOfBeidouNmeaSentencesWrite(
            beidou_nmea_type
        )
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
        client.configureGnss20207ConfigureSupportedGnssConstellationsRead()
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
def write(ctx, gnss_config: int):  # type: ignore[reportRedeclaration]
    """Write the supported GNSS constellations."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20207ConfigureSupportedGnssConstellationsWrite(gnss_config)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_odp_mode(ctx):
    """Configure ODP mode."""
    pass


@configure_odp_mode.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the ODP mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20208ConfigureOdpModeRead()
    print(response if status else "Error")
    client.close()


@configure_odp_mode.command("write")
@click.pass_context
@click.option(
    "--odp-control",
    "-o",
    type=int,
    required=True,
    help="""
Set ODP mode.
                        - **0**: Disable ODP
                        - **1**: Low power mode
                        - **2**: Ready mode
""",
)
def write(ctx, odp_control: int):  # type: ignore[reportRedeclaration]
    """Write the ODP mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20208ConfigureOdpModeWrite(odp_control)
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def enable_disable_dpo_mode(ctx):
    """Enable/disable DPO mode."""
    pass


@enable_disable_dpo_mode.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the DPO mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20209EnableDisableDpoModeRead()
    print(response if status else "Error")
    client.close()


@enable_disable_dpo_mode.command("write")
@click.pass_context
@click.option(
    "--dpo-enable",
    "-d",
    type=int,
    required=True,
    help="""
Enable/Disable DPO.
                        - **0**: Disable DPO
                        - **1**: Enable DPO with dynamic duty cycle
""",
)
def write(ctx, dpo_enable: int):  # type: ignore[reportRedeclaration]
    """Write the DPO mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20209EnableDisableDpoModeWrite(dpo_enable)
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def enable_disable_gnss_extended_ggsv(ctx):
    """Enable/disable GNSS extended GGSV."""
    pass


@enable_disable_gnss_extended_ggsv.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GNSS extended GGSV."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20210EnableDisableGnssExtendedGgsvRead()
    print(response if status else "Error")
    client.close()


@enable_disable_gnss_extended_ggsv.command("write")
@click.pass_context
@click.option(
    "--gsvext-nmea-type",
    "-g",
    type=int,
    required=True,
    help="""
Enable/Disable extended GGSV.
                        - **0**: Disable extended GGSV
                        - **1**: Display extended GGSV
""",
)
def write(ctx, gsvext_nmea_type: int):  # type: ignore[reportRedeclaration]
    """Write the GNSS extended GGSV."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20210EnableDisableGnssExtendedGgsvWrite(
        gsvext_nmea_type
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_plane_mode_used_by_mo_agps_session(ctx):
    """Configure plane mode used by MO AGPS session."""
    pass


@configure_plane_mode_used_by_mo_agps_session.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the plane mode used by MO AGPS session."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20211ConfigurePlaneModeUsedByMoAgpsSessionRead()
    )
    print(response if status else "Error")
    client.close()


@configure_plane_mode_used_by_mo_agps_session.command("write")
@click.pass_context
@click.option(
    "--plane",
    "-p",
    type=int,
    required=True,
    help="""
The plane mode used by MO AGPS session.
                        - **0**: User plane without SSL
                        - **1**: User plane with SSL
                        - **2**: Control plane
""",
)
def write(ctx, plane: int):  # type: ignore[reportRedeclaration]
    """Write the plane mode used by MO AGPS session."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20211ConfigurePlaneModeUsedByMoAgpsSessionWrite(plane)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def enable_disable_gnss_to_run_automatically(ctx):
    """Enable/disable GNSS to run automatically."""
    pass


@enable_disable_gnss_to_run_automatically.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GNSS to run automatically."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20212EnableDisableGnssToRunAutomaticallyRead()
    )
    print(response if status else "Error")
    client.close()


@enable_disable_gnss_to_run_automatically.command("write")
@click.pass_context
@click.option(
    "--autogps",
    "-a",
    type=int,
    required=True,
    help="""
Enable/disable GNSS to run automatically after the module is powered on.
                        - **0**: Disable GNSS to run automatically
                        - **1**: Enable GNSS to run automatically
""",
)
def write(ctx, autogps: int):  # type: ignore[reportRedeclaration]
    """Write the GNSS to run automatically."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.configureGnss20212EnableDisableGnssToRunAutomaticallyWrite(autogps)
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_supl_protocol_version(ctx):
    """Configure SUPL protocol version."""
    pass


@configure_supl_protocol_version.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the SUPL protocol version."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20213ConfigureSuplProtocolVersionRead()
    print(response if status else "Error")
    client.close()


@configure_supl_protocol_version.command("write")
@click.pass_context
@click.option(
    "--supl-version",
    "-s",
    type=int,
    required=True,
    help="""
The SUPL protocol version.
                        - **0**: SUPL version 1.0
                        - **1**: SUPL version 2.0
""",
)
def write(ctx, supl_version: int):  # type: ignore[reportRedeclaration]
    """Write the SUPL protocol version."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20213ConfigureSuplProtocolVersionWrite(
        supl_version
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_agps_positioning_mode(ctx):
    """Configure AGPS positioning mode."""
    pass


@configure_agps_positioning_mode.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the AGPS positioning mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20214ConfigureAgpsPositioningModeRead()
    print(response if status else "Error")
    client.close()


@configure_agps_positioning_mode.command("write")
@click.pass_context
@click.option(
    "--agps-posmode",
    "-a",
    type=int,
    required=True,
    help="""
The AGPS positioning mode.
            - **Bit 0**: Standalone
            - **Bit 1**: UP MS-based
            - **Bit 2**: UP MS-assisted
            - **Bit 3**: CP MS-based (2G)
            - **Bit 4**: CP MS-assisted (2G)
            - **Bit 5**: CP UE-based (3G)
            - **Bit 6**: CP UE-assisted (3G)
            - **Bit 7**: UP network measurement report (2G)
            - **Bit 8**: UP MS-based (4G)
            - **Bit 9**: UP MS-assisted (4G)
            - **Bit 10**: CP MS-based (4G)
            - **Bit 11**: CP MS-assisted (4G)
            - **Bit 16**: Enabling of autonomous fallback for SUPL-MSB
            - **Bit 17**: A-GLONASS UP MS-based for 3G
            - **Bit 18**: A-GLONASS UP MS-assisted for 3G
            - **Bit 19**: A-GLONASS CP MS-based for 3G
            - **Bit 20**: A-GLONASS CP MS-assisted for 3G
            - **Bit 21**: A-GLONASS UP MS-based for 4G
            - **Bit 202**: A-GLONASS UP MS-assisted for 4G
            - **Bit 203**: A-GLONASS CP MS-based for 4G
            - **Bit 204**: A-GLONASS CP MS-assisted for 4Ge
""",
)
def write(ctx, agps_posmode: int):  # type: ignore[reportRedeclaration]
    """Write the AGPS positioning mode."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20214ConfigureAgpsPositioningModeWrite(
        agps_posmode
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_agnss_positioning_protocols(ctx):
    """Configure AGNSS positioning protocols."""
    pass


@configure_agnss_positioning_protocols.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the AGNSS positioning protocols."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20215ConfigureAgnssPositioningProtocolsRead()
    print(response if status else "Error")
    client.close()


@configure_agnss_positioning_protocols.command("write")
@click.pass_context
@click.option(
    "--agps-lp",
    "-a",
    type=int,
    required=True,
    help="""
A-GPS LPP positioning protocol in ORed. Default: 3:
                        - **1**: User plane LPP
                        - **2**: Control plane LPP
""",
)
@click.option(
    "--aglonass-lp",
    "-g",
    type=int,
    required=True,
    help="""
A-GLONASS positioning protocol in ORed. Default: 12087:
                        - **1**:       Control plane RRLP
                        - **2**:       Control plane RRC
                        - **4**:       Control plane LPP
                        - **2056**:     User plane RRLP
                        - **10204**:    User plane LPP
""",
)
def write(ctx, agps_lp: int, aglonass_lp: int):  # type: ignore[reportRedeclaration]
    """Write the AGNSS positioning protocols."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20215ConfigureAgnssPositioningProtocolsWrite(
        agps_lp, aglonass_lp
    )
    print(response if status else "Error")
    client.close()


@configure_gnss.group()
@click.pass_context
def configure_nmea_output_frequency(ctx):
    """Configure NMEA output frequency."""
    pass


@configure_nmea_output_frequency.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the NMEA output frequency."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20216ConfigureNmeaOutputFrequencyRead()
    print(response if status else "Error")
    client.close()


@configure_nmea_output_frequency.command("write")
@click.pass_context
@click.option(
    "--freq",
    "-f",
    type=int,
    required=True,
    help="""
NMEA sentence output frequency:
                        - **1**: 1 Hz
                        - **2**: 2 Hz
                        - **5**: 5 Hz
                        - **10**: 10 Hz
""",
)
def write(ctx, freq: int):  # type: ignore[reportRedeclaration]
    """Write the NMEA output frequency."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.configureGnss20216ConfigureNmeaOutputFrequencyWrite(freq)
    print(response if status else "Error")
    client.close()


@main.group()
@click.pass_context
def gnss_general_commands(ctx):
    """GNSS General Commands."""
    pass


@gnss_general_commands.command("delete-assistance-data")
@click.pass_context
@click.option(
    "--delete-type",
    "-d",
    type=int,
    required=True,
    help="""
Delete assistance data.
                        - **0**: Delete all assistance data. Enforce cold start after starting GNSS.
                        - **1**: Do not delete any data. Perform hot start if the conditions are permitted after starting GNSS.
                        - **2**: Delete some related data. Perform warm start if the conditions are permitted after starting GNSS.
                        - **3**: Delete the gpsOneXTRA assistance data injected into GNSS engine.
""",
)
def delete_assistance_data(ctx, delete_type: int):  # type: ignore[reportRedeclaration]
    """Delete assistance data."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20300DeleteAssistanceData(delete_type)
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def turn_on_gnss(ctx):
    """Turn on GNSS."""
    pass


@turn_on_gnss.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GNSS."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20400TurnOnGnssRead()
    print(response if status else "Error")
    client.close()


@turn_on_gnss.command("write")
@click.pass_context
@click.option(
    "--gnss-mode",
    "-g",
    type=int,
    required=True,
    help="""
GNSS working mode:
                        - **1**: Stand-alone
                        - **2**: MS-based
                        - **3**: MS-assisted
                        - **4**: Speed-optimal
""",
)
@click.option(
    "--fix-maxtime",
    "-t",
    type=int,
    help="""
The maximum positioning time, which indicates the response time of GNSS receiver while measuring the GNSS pseudo range and the upper time limit of GNSS satellite searching. It also includes the time for demodulating the ephemeris data and calculating the position. Range: 1–2055. Default: 2055. Unit: second.
""",
)
@click.option(
    "--fix-maxdist",
    "-d",
    type=int,
    help="Accuracy threshold of positioning. Range: 0–1000. Default: 50. Unit: meter.",
)
@click.option(
    "--fix-count",
    "-c",
    type=int,
    help="""
Positioning times. Range: 0–1000. Default: 0:
                        -**0**: Continuous positioning.
                        -**Other values**: Actual positioning times.
""",
)
@click.option(
    "--fix-rate",
    "-r",
    type=int,
    help="The interval between the first and the second positioning. Range: 1–65535. Default value: 1. Unit: second.",
)
def write(ctx, gnss_mode: int, fix_maxtime: int, fix_maxdist: int, fix_count: int, fix_rate: int):  # type: ignore[reportRedeclaration]
    """Write the GNSS."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20400TurnOnGnssWrite(
        gnss_mode, fix_maxtime, fix_maxdist, fix_count, fix_rate
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def turn_off_gnss(ctx):
    """Turn off GNSS."""
    pass


@turn_off_gnss.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GNSS."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20500TurnOffGnssRead()
    print(response if status else "Error")
    client.close()


@turn_off_gnss.command("write")
@click.pass_context
def write(ctx):  # type: ignore[reportRedeclaration]
    """Write the GNSS."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20500TurnOffGnssWrite()
    print(response if status else "Error")
    client.close()


@gnss_general_commands.command("acquire-positioning-information")
@click.pass_context
@click.option(
    "--mode",
    "-m",
    type=int,
    required=True,
    help="""
Latitude and longitude display format:
                        - **0**: <latitude>,<longitude> format: ddmm.mmmmN/S,dddmm.mmmmE/W
                        - **1**: <latitude>,<longitude> format: ddmm.mmmmmm,N/S,dddmm.mmmmmm,E/W
                        - **2**: <latitude>,<longitude> format: (-)dd.ddddd,(-)ddd.ddddd
""",
)
def acquire_positioning_information(ctx, mode: int):
    """Acquire positioning information."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20600AcquirePositioningInformation(
        mode
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def configure_supl_server_url(ctx):
    """Configure SUPL server URL."""
    pass


@configure_supl_server_url.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the SUPL server URL."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20700ConfigureSuplServerUrlRead()
    print(response if status else "Error")
    client.close()


@configure_supl_server_url.command("write")
@click.pass_context
@click.option(
    "--supl-url",
    "-s",
    type=str,
    required=True,
    help="""
SUPL server address. The address format is "URL:port_number" where the “port_number” can be omitted, for example "supl.server.com", "supl.server.com:72075". When the “port number” is omitted, the default value (72075) will be used.
""",
)
def write(ctx, supl_url: str):  # type: ignore[reportRedeclaration]
    """Write the SUPL server URL."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20700ConfigureSuplServerUrlWrite(
        supl_url
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def inject_supl_certificate(ctx):
    """Inject SUPL certificate."""
    pass


@inject_supl_certificate.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the SUPL certificate."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20800InjectSuplCertificateRead()
    print(response if status else "Error")
    client.close()


@inject_supl_certificate.command("write")
@click.pass_context
@click.option(
    "--ca-file-name",
    "-c",
    type=str,
    required=True,
    help="CA certificate file name.",
)
def write(ctx, ca_file_name: str):  # type: ignore[reportRedeclaration]
    """Write the SUPL certificate."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20800InjectSuplCertificateWrite(
        ca_file_name
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.command("acquire-nmea-sentences")
@click.pass_context
@click.option(
    "--nmea-type",
    "-n",
    type=str,
    required=True,
    help="""
Acquire NMEA sentences:
                        - **"RMC"**: Acquire RMC sentence
                        - **"GSV"**: Acquire GSV sentence
                        - **"GSA"**: Acquire GSA sentence
                        - **"VTG"**: Acquire VTG sentence
""",
)
def acquire_nmea_sentences(ctx, nmea_type: str):
    """Acquire NMEA sentences."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands20900AcquireNmeaSentences(nmea_type)
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def enable_disable_gps_one_xtra_assistance(ctx):
    """Enable/disable GPS One XTRA assistance."""
    pass


@enable_disable_gps_one_xtra_assistance.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GPS One XTRA assistance."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.gnssGeneralCommands21000EnableDisableGpsOneXtraAssistanceRead()
    )
    print(response if status else "Error")
    client.close()


@enable_disable_gps_one_xtra_assistance.command("write")
@click.pass_context
@click.option(
    "--xtra-enable",
    "-x",
    type=int,
    required=True,
    help="""
Enable/disable GPS One XTRA assistance.
                        - **0**: Disable GPS One XTRA assistance
                        - **1**: Enable GPS One XTRA assistance
""",
)
def write(ctx, xtra_enable: int):  # type: ignore[reportRedeclaration]
    """Write the GPS One XTRA assistance."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = (
        client.gnssGeneralCommands21000EnableDisableGpsOneXtraAssistanceWrite(
            xtra_enable
        )
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.command("inject-gps-one-xtra-time")
@click.pass_context
@click.option(
    "--type",
    "-t",
    type=int,
    required=True,
    help="""
Type of injecting time:
- **0**: Inject XTRA time manually    
""",
)
@click.option(
    "--xtra-time",
    "-x",
    type=str,
    required=True,
    help="""
Current UTC time.
Format: "YYYY/MM/DD,hh:mm:ss". e.g. "2019/01/05,08:30:30".
""",
)
@click.option(
    "--utc",
    "-u",
    type=int,
    required=True,
    help="""
UTC or GPS time that gpsOneXTRA time refers to:
- **0**: GPS time
- **1**: UTC time (Recommended).    
""",
)
@click.option(
    "--force",
    "-f",
    type=int,
    required=True,
    help="""
Whether to force GNSS to accept the data:
- **0**: Not force GNSS to accept the data
- **1**: Force acceptance of data (Recommended).
""",
)
@click.option(
    "--uncrtn",
    "-u",
    type=int,
    required=True,
    help="""
Uncertainty of time. It indicates the time difference between sending a
request to the SNTP server and receiving a response from the SNTP server. Default:
3500. Unit: millisecond.    
""",
)
def inject_gps_one_xtra_time(
    ctx, type: int, xtra_time: str, utc: int, force: int, uncrtn: int
):
    """Inject GPS One XTRA time."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands21100InjectGpsOneXtraTime(
        type, xtra_time, utc, force, uncrtn
    )
    print(response if status else "Error")
    client.close()


@gnss_general_commands.group()
@click.pass_context
def inject_gps_one_xtra_data_file(ctx):
    """Inject GPS One XTRA data file."""
    pass


@inject_gps_one_xtra_data_file.command("read")
@click.pass_context
def read(ctx):  # type: ignore[reportRedeclaration]
    """Read the GPS One XTRA data file."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands21200InjectGpsOneXtraDataFileRead()
    print(response if status else "Error")
    client.close()


@inject_gps_one_xtra_data_file.command("write")
@click.pass_context
@click.option(
    "--xtradatafilename",
    "-x",
    type=str,
    required=True,
    help="""
Filename of the gpsOneXTRA data file, e.g. "RAM:xtra2.bin" or
"RAM:xtra3grc.bin", in which, RAM indicates the actual file storage area.
""",
)
def write(ctx, xtradatafilename: str):  # type: ignore[reportRedeclaration]
    """Write the GPS One XTRA data file."""
    client: QuectelGnssATCommands = ctx.obj["client"]
    client.open()
    status, response = client.gnssGeneralCommands21200InjectGpsOneXtraDataFileWrite(
        xtradatafilename
    )
    print(response if status else "Error")
    client.close()


if __name__ == "__main__":
    main()
