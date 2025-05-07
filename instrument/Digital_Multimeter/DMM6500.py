import time

from api.__init__ import *
from controller.__init__ import *
import re


class USER_SETUP(Enum):
    """
    user-saved settings that are stored in setup memory.
    """
    SETUP_0 = 0
    SETUP_1 = 1
    SETUP_2 = 2
    SETUP_3 = 3
    SETUP_4 = 4


class EDGE_TYPE(Enum):
    FALLing = "FALLing"
    RISing = "RISing"
    EITHer = "EITHer"


class TTL(Enum):
    POSitive = "POSitive"
    NEGative = "NEGative"

class EVENT(Enum):
    NONE = "NONE"
    NOTify = "NOTify{n}"
    COMMand = "COMMand"
    DIGio = "DIGio{n}"
    TSPLink = "TSPLink{n}"
    LAN = "LAN{n}"
    BLENder = "BLENder{n}"
    TIMer = "TIMer{n}"
    EXTernal = "EXTernal"
    SCANCHANnel = "SCANCHANnel"
    SCANCOMPlete = "SCANCOMPlete"
    SCANMEASure = "SCANMEASure"
    SCANALARmlimit = "SCANALARmlimit"

class RANGE(Enum):
    DC_100mV = "100e-3"
    DC_1V = "1"
    DC_10V = "10"
    DC_100V = "100"
    DC_1000V = "1e3"
    AC_100mV = "100e-3"
    AC_1V = "1"
    AC_10V = "10"
    AC_100V = "100"
    AC_750V = "750"
    DC_10uA = "10e-6"
    DC_100uA = "100e-6"
    DC_1mA = "1e-3"
    DC_10mA = "10e-3"
    DC_100mA = "100e-3"
    DC_1A = "1"
    DC_3A = "3"
    DC_10A_ONLY_REAR_TERMINAL = "10"
    AC_1mA = "1e-3"
    AC_10mA = "10e-3"
    AC_100mA = "100e-3"
    AC_1A = "1"
    AC_3A = "3"
    AC_10A_ONLY_REAR_TERMINAL = "10"
    RES_2W_10ohm = "10"
    RES_2W_100ohm = "100"
    RES_2W_1kohm = "1e3"
    RES_2W_10kohm = "10e3"
    RES_2W_100kohm = "100e3"
    RES_2W_1mohm = "1e6"
    RES_2W_10mohm = "10e6"
    RES_2W_100mohm = "100e6"
    RES_4W_1ohm = "1"
    RES_4W_1Oohm = "10"
    RES_4W_100ohm = "100"
    RES_4W_1kohm = "1e3"
    RES_4W_10kohm = "10e3"
    RES_4W_100kohm = "100e3"
    RES_4W_1mohm = "1e6"
    RES_4W_10mohm = "10e6"
    RES_4W_100mohm = "100e6"
    RES_4W_OFFSET_1ohm = "1"
    RES_4W_OFFSET_1Oohm = "10"
    RES_4W_OFFSET_100ohm = "100"
    RES_4W_OFFSET_1kohm = "1e3"
    RES_4W_OFFSET_10kohm = "10e3"
    CAP_1nF = "1e-9"
    CAP_10nF = "10e-9"
    CAP_100nF = "100e-9"
    CAP_1uF = "1e-6"
    CAP_10uF = "10e-6"
    CAP_100uF = "100e-6"
    CAP_1mF = "1e-3"
    RATIO_DC_100mV = "100e-3"
    RATIO_DC_1V = "1"
    RATIO_DC_10V = "10"
    RATIO_DC_100V = "100"
    RATIO_DC_1000V = "1000"
    DIGI_VOLT_100mV = "100e-3"
    DIGI_VOLT_1V = "1"
    DIGI_VOLT_10V = "10"
    DIGI_VOLT_100V = "100"
    DIGI_VOLT_1000V = "1e3"
    DIGI_CURR_10uA = "10e-6"
    DIGI_CURR_100uA = "100e-6"
    DIGI_CURR_1mA = "1e-3"
    DIGI_CURR_10mA = "10e-3"
    DIGI_CURR_100mA = "100e-3"
    DIGI_CURR_1A = "1"
    DIGI_CURR_3A = "3"
    TIME_1ms = "1e-3"
    TIME_1us = "1e-6"
    TIME_1ns = "1e-9"


class DEFAULT_SETUP(Enum):
    """
    user-saved settings that are stored in setup memory.
    """
    DEFBUFFER1 = "defbuffer1"


class FUNCTION(Enum):
    """
    Functions available on the instrument
    """
    VOLT_DC = "VOLTage:DC"
    VOLT_AC = "VOLTage:AC"
    CURR_DC = "CURRent:DC"
    CURR_AC = "CURRent:AC"
    RES = "RESistance"
    FRES = "FRESistance"
    DIOD = "DIODe"
    CAP = "CAPacitance"
    TEMP = "TEMPerature"
    CONT = "CONTinuity"
    FREQ = "FREQuency:VOLTage"
    PER = "PERiod:VOLTage"
    VOLT_RAT = "VOLTage:DC:RATio"


class DIGITIZE_FUNCTION(Enum):
    VOLT = "VOLTage"
    CURR = "CURRent"


class BUFFER_ELEMENTS(Enum):
    """
    When specifying buffer elements, you can:
        • Specify buffer elements in any order.
        • Include up to 14 elements in a single list. You can repeat elements as long as the number of
        elements in the list is less than 14.
        • Use a comma to delineate multiple elements for a data point.
    """
    CHANnel = "CHANnel"
    DATE = "DATE"
    EXTRa = "EXTRa"
    EXTRAFORMatted = "EXTRAFORMatted"
    EXTRAUNIT = "EXTRAUNIT"
    FORMatted: "FORMatted"
    FRACtional = "FRACtional"
    READing = "READing"
    RELative = "RELative"
    SEConds = "SEConds"
    STATus = "STATus"
    TIME = "TIME"
    TSTamp = "TSTamp"
    UNIT = "UNIT"


class ROOT(Enum):
    SET_RCL = "*RCL {setup}"
    SET_SAV = "*SAV {setup}"
    GET_FETCh = ":FETCh? '{bufferName}', {bufferElements}"
    GET_MEASURE = ":MEASure? '{bufferName}', {bufferElements}"
    GET_MEASURE_WITH = ":MEASure:{function}? '{bufferName}', {bufferElements}"
    GET_MEASURE_DIGITIZE = ":MEASure:DIGitize? '{bufferName}', {bufferElements}"
    GET_MEASURE_DIGITIZE_WITH = ":MEASure:DIGitize:{function}? '{bufferName}', {bufferElements}"
    GET_READ = ":READ? '{bufferName}', {bufferElements}"
    GET_READ_DIGITIZE = ":READ:DIGitize? '{bufferName}', {bufferElements}"
    SET_TRIG = "*TRG"

class CALCulate(Enum):
    """
    The commands in this subsystem configure and control the math and limit operations
    """
    # Limit test sub system
    SET_LIMIt_STATe = ":CALCulate2:{function}:LIMit{Y}:STATe {state}, {channelList}"
    GET_LIMIt_STATe = ":CALCulate2:{function}:LIMit{Y}:STATe? {channelList}"
    SET_AUDible = ":CALCulate2:{function}:LIMit{Y}:AUDible {state}, {channelList}"
    GET_AUDible = ":CALCulate2:{function}:LIMit{Y}:AUDible? {channelList}"
    SET_CLEAr_AUTO = ":CALCulate2:{function}:CLEar:AUTO {state}, {channelList}"
    GET_CLEAr_AUTO = ":CALCulate2:{function}:CLEar:AUTO? {channelList}"
    SET_CLEAr_RESUtls = ":CALCulate2:{function}:LIMit{Y}:CLEar:IMMediate"
    GET_LIMIt_RESULts = ":CALCulate2:{function}:LIMIT{Y}:FAIL? {channelList}"
    SET_LOWEr_LIMIt = ":CALCulate2:{function}:LIMit{Y}:LOWer:DATA {n}, {channelList}"
    GET_LOWEr_LIMIt = ":CALCulate2:{function}:LIMit{Y}:LOWer:DATA? {channelList}"
    SET_UPPER_LIMIt = ":CALCulate2:{function}:LIMit{Y}:UPPer:DATA {n}, {channelList}"
    GET_UPPER_LIMIt = ":CALCulate2:{function}:LIMit{Y}:UPPer:DATA? {channelList}"

    # Math sub system
    SET_MATH_STATe = ":CALCulate1:{function}:STATe {state}, {channelList}"
    GET_MATH_STATe = ":CALCulate1:{function}:STATe? {channelList}"
    SET_MATH_FORMat = ":CALCulate1:{function}:FORMat {state}, {channelList}"
    GET_MATH_FORMat = ":CALCulate1:{function}:FORMat? {channelList}"
    SET_MATH_MBFactor = ":CALCulate1:{function}:MBFACTOR {n}, {channelList}"
    GET_MATH_MBFactor = ":CALCulate1:{function}:MBFACTOR? {channelList}"
    SET_MATH_MMFactor = ":CALCulate1:{function}:MMFACTOR {value}, {channelList}"
    GET_MATH_MMFactor = ":CALCulate1:{function}:MMFACTOR? {channelList}"
    SET_MATH_PERCent = ":CALCulate1:{function}:PERCent {value}, {channelList}"
    GET_MATH_PERCent = ":CALCulate1:{function}:PERCent? {channelList}"


class DIGital(Enum):
    """
    This command sets the mode of the digital I/O line to be a digital line, trigger line, or synchronous line and sets
    the line to be input, output, or open-drain.
    """
    SET_DIGItal_LINE_MODE = ":DIGital:LINE{n}:MODE {lineType}, {lineDirection}"
    GET_DIGItal_LINE_MODE = ":DIGital:LINE{n}:MODE?"
    SET_DIGItal_LINE_STATe = ":DIGital:LINE{n}:STATe {state}"
    GET_DIGItal_LINE_STATe = ":DIGital:LINE{n}:STATe?"
    GET_DIGItal_READ = ":DIGital:READ?"
    SET_DIGItal_WRITE = ":DIGital:WRITE {n}"


class DISPlay(Enum):
    """
    This subsystem contains commands that control the front-panel display.
    """
    SET_DISPlay_BUFFer_ACTive = ":DISPlay:BUFFer:ACTive '{bufferName}'"
    GET_DISPlay_BUFFer_ACTive = ":DISPlay:BUFFer:ACTive?"
    SET_DISPlay_BUFFer_CLEar = ":DISPlay:CLEar"
    SET_DISPlay_DIGIits = ":DISPlay:{function}:DIGits {value}, {channelList}"
    GET_DISPlay_DIGIits = ":DISPlay:{function}:DIGits? {channelList}"
    SET_DISPlay_LIGHt_STATe = ":DISPlay:LIGHt:STATe {brightness}"
    GET_DISPlay_LIGHt_STATe = ":DISPlay:LIGHt:STATe?"
    SET_DISPlay_READing_FORMat = ":DISPlay:READing:FORMat {format}"
    GET_DISPlay_READing_FORMat = ":DISPlay:READing:FORMat?"
    SET_DISPlay_SCReen = ":DISPlay:SCReen {screenName}"
    SET_DISPlay_USER_TEXt = ":DISPlay:USER{n}:TEXT:DATA {textMessage}"
    SET_DISPlay_WATCh_CHANnels = ":DISPlay:WATCh:CHANnels (channelList)"
    GET_DISPlay_WATCh_CHANnels = ":DISPlay:WATCh:CHANnels?"


class FORMat(Enum):
    """
    The commands for this subsystem select the data format that is used to transfer instrument readings
    over the remote interface.
    """
    SET_FORMat_ASCii_PRECision = ":FORMat:ASCii:PRECision {value}"
    GET_FORMat_ASCii_PRECision = ":FORMat:ASCii:PRECision?"
    SET_FORMat_BORDer = ":FORMat:BORDer {name}"
    GET_FORMat_BORDer = ":FORMat:BORDer?"
    SET_FORMat_DATA = ":FORMat:DATA {type}"
    GET_FORMat_DATA = ":FORMat:DATA?"


class ROUTe(Enum):
    """
    The ROUTe subsystem contains commands to open, close, and set up scans for channels. It also
    contains a command you can use to verify whether the front or rear terminals are used for
    measurements.
    """
    SET_ABORt = ":ABORt"
    SET_INITiate_IMMediate = ":INITiate:IMMediate"
    SET_ROUTe_CHANnel_CLOSe = ":ROUTe:CHANnel:CLOSe {channelList}"
    GET_ROUTe_CHANnel_CLOSe = ":ROUTe:CHANnel:CLOSe?"
    GET_ROUTe_CHANnel_CLOSe_COUNt = ":ROUTe:CHANnel:CLOSe:COUNt? {channelList}"
    SET_ROUTe_CHANnel_DELay = ":ROUTe:CHANnel:DELay {value}, {channelList}"
    GET_ROUTe_CHANnel_DELay = ":ROUTe:CHANnel:DELay? {channelList}"
    SET_ROUTe_CHANnel_LABel = ":ROUTe:CHANnel:LABel {label}, {channelList}"
    GET_ROUTe_CHANnel_LABel = ":ROUTe:CHANnel:LABel? {channelList}"
    SET_ROUTe_CHANnel_MULTiple_CLOSe = ":ROUTe:CHANnel:MULTiple:CLOSe {channelList}"
    GET_ROUTe_CHANnel_MULTiple_CLOSe = ":ROUTe:CHANnel:MULTiple:CLOSe?"
    SET_ROUTe_CHANnel_MULTiple_OPEN = ":ROUTe:CHANnel:MULTiple:OPEN {channelList}"
    SET_ROUTe_CHANnel_OPEN = ":ROUTe:CHANnel:OPEN {channelList}"
    SET_ROUTe_CHANnel_OPEN_ALL = ":ROUTe:CHANnel:OPEN:ALL"
    GET_ROUTe_CHANnel_STATe = ":ROUTe:CHANnel:STATe? {channelList}"
    GET_ROUTe_CHANnel_TYPE = ":ROUTe:CHANnel:TYPE? {channelList}"
    SET_ROUTe_SCAN_ADD = ":ROUTe:SCAN:ADD {channelList}, {configurationList}, {index}"
    SET_ROUTe_SCAN_ADD_SINGle = ":ROUTe:SCAN:ADD:SINGle {channelList}, {configurationList}, {index}"
    SET_ROUTe_SCAN_ALARm = ":ROUTe:SCAN:ALARm {n}"
    GET_ROUTe_SCAN_ALARm = ":ROUTe:SCAN:ALARm?"
    SET_ROUTe_SCAN_BUFFer = ":ROUTe:SCAN:BUFFer '{bufferName}'"
    GET_ROUTe_SCAN_BUFFer = ":ROUTe:SCAN:BUFFer?"
    SET_ROUTe_SCAN_BYPass = ":ROUTe:SCAN:BYPass {bypass}"
    GET_ROUTe_SCAN_BYPass = ":ROUTe:SCAN:BYPass?"
    SET_ROUTe_SCAN_CHANnel_STIMulus = ":ROUTe:SCAN:CHANnel:STIMulus {eventID}"
    GET_ROUTe_SCAN_CHANnel_STIMulus = ":ROUTe:SCAN:CHANnel:STIMulus?"
    SET_ROUTe_SCAN_COUNt_SCAN = ":ROUTe:SCAN:COUNt:SCAN {scanCount}"
    GET_ROUTe_SCAN_COUNt_SCAN = ":ROUTe:SCAN:COUNt:SCAN?"
    GET_ROUTe_SCAN_COUNt_STEP = ":ROUTe:SCAN:COUNt:STEP?"
    SET_ROUTe_SCAN_CREate = ":ROUTe:SCAN:CREate {channelList}, {configurationList}, {index}"
    GET_ROUTe_SCAN_CREate = ":ROUTe:SCAN:CREate?"
    SET_ROUTe_SCAN_EXPOrt = ":ROUTe:SCAN:EXPort /usb1/{filename}, {when}, {what}"
    SET_ROUTe_SCAN_INTerval = ":ROUTe:SCAN:INTerval {interval}"
    GET_ROUTe_SCAN_INTerval = ":ROUTe:SCAN:INTerval?"
    SET_ROUTe_SCAN_LEARn_LIMIit = "ROUTe:SCAN:LEARn:LIMits {window}, {iterations}"
    SET_ROUTe_SCAN_MEASure_STIMulus = ":ROUTe:SCAN:MEASure:STIMulus {eventID}"
    GET_ROUTe_SCAN_MEASure_STIMulus = ":ROUTe:SCAN:MEASure:STIMulus?"
    SET_ROUTe_SCAN_MEASure_INTerval = ":ROUTe:SCAN:MEASure:INTerval {time}"
    GET_ROUTe_SCAN_MEASure_INTerval = ":ROUTe:SCAN:MEASure:INTerval?"
    SET_ROUTe_SCAN_MODE = ":ROUTe:SCAN:MODE {mode}"
    GET_ROUTe_SCAN_MODE = ":ROUTe:SCAN:MODE?"
    SET_ROUTe_SCAN_MONitor_CHANnel = ":ROUTe:SCAN:MONitor:CHANnel {@<channel>}"
    GET_ROUTe_SCAN_MOoNitor_CHANnel = ":ROUTe:SCAN:MONitor:CHANnel?"
    SET_ROUTe_SCAN_MONitor_LIMit_LOWer_DATA = ":ROUTe:SCAN:MONitor:LIMit:LOWer:DATA {n}"
    GET_ROUTe_SCAN_MONitor_LIMit_LOWer_DATA = ":ROUTe:SCAN:MONitor:LIMit:LOWer:DATA?"
    SET_ROUTe_SCAN_MONitor_LIMit_UPPER_DATA = ":ROUTe:SCAN:MONitor:LIMit:UPPER:DATA {n}"
    GET_ROUTe_SCAN_MONitor_LIMit_UPPER_DATA = ":ROUTe:SCAN:MONitor:LIMit:UPPER:DATA?"
    SET_ROUTe_SCAN_MONitor_MODE = ":ROUTe:SCAN:MONitor:MODE {mode}"
    GET_ROUTe_SCAN_MONitor_MODE = ":ROUTe:SCAN:MONitor:MODE?"
    SET_ROUTe_SCAN_RESTart = ":ROUTe:SCAN:REStart {n}"
    GET_ROUTe_SCAN_RESTart = ":ROUTe:SCAN:REStart?"
    SET_ROUTe_SCAN_STARt_STIMulus = ":ROUTe:SCAN:STARt:STIMulus {eventID}"
    GET_ROUTe_SCAN_STARt_STIMulus = ":ROUTe:SCAN:STARt:STIMulus?"
    GET_ROUTe_SCAN_STATe = ":ROUTe:SCAN:STATe?"
    GET_ROUTe_TERMinals = ":ROUTe:TERMinals?"


class SCRipt(Enum):
    """
    The SCRipt subsystem controls macro or instrument setup scripts.
    """
    SET_SCRIpt_RUN = ":SCRipt:RUN {scriptName}"


class SENSe1(Enum):
    """
    The SENSe1 subsystem commands configure and control the measurement functions of the
    instrument.
    Many of these commands are set for a specific function. For example, you can program a range
    setting for each function. The settings are saved with that function.
    """
    SET_SENSe1_APERture = ":SENSe1:{function}:APERture {n}, {channelList}"
    GET_SENSe1_APERture = ":SENSe1:{function}:APERture? {channelList}"
    SET_SENSe1_ATRigger_EDGE_LEVel = ":SENSe1:{function}:ATRigger:EDGE:LEVel {setting}, {channelList}"
    GET_SENSe1_ATRigger_EDGE_LEVel = ":SENSe1:{function}:ATRigger:EDGE:LEVel? {channelList}"
    SET_SENSe1_ATRigger_EDGE_SLOpe = ":SENSe1:{function}:ATRigger:EDGE:SLOpe {setting}, {channelList}"
    GET_SENSe1_ATRigger_EDGE_SLOpe = ":SENSe1:{function}:ATRigger:EDGE:SLOpe? {channelList}"
    SET_SENSe1_ATRigger_MODE = ":SENSe1:{function}:ATRigger:MODE {setting}, {channelList}"
    GET_SENSe1_ATRigger_MODE = ":SENSe1:{function}:ATRigger:MODE? {channelList}"
    SET_SENSe1_ATRigger_WINDow_DIRection = ":SENSe1:{function}:ATRigger:WINDow:DIRection {setting}, {channelList}"
    GET_SENSe1_ATRigger_WINDow_DIRection = ":SENSe1:{function}:ATRigger:WINDow:DIRection? {channelList}"
    SET_SENSe1_ATRigger_WINDow_LEVel_HIGH = ":SENSe1:{function}:ATRigger:WINDow:LEVel:HIGH {setting}, {channelList}"
    GET_SENSe1_ATRigger_WINDow_LEVel_HIGH = ":SENSe1:{function}:ATRigger:WINDow:LEVel:HIGH? {channelList}"
    SET_SENSe1_ATRigger_WINDow_LEVel_LOW = ":SENSe1:{function}:ATRigger:WINDow:LEVel:LOW {setting}, {channelList}"
    GET_SENSe1_ATRigger_WINDow_LEVel_LOW = ":SENSe1:{function}:ATRigger:WINDow:LEVel:LOW? {channelList}"
    SET_SENSe1_AVERage_COUNt = ":SENSe1:{function}:AVERage:COUNt {n}, {channelList}"
    GET_SENSe1_AVERage_COUNt = ":SENSe1:{function}:AVERage:COUNt? {channelList}"
    SET_SENSe1_AVERage_STATe = ":SENSe1:{function}:AVERage:STATe {state}, {channelList}"
    GET_SENSe1_AVERage_STATe = ":SENSe1:{function}:AVERage:STATe? {channelList}"
    SET_SENSe1_AVERage_TCONtrol = ":SENSe1:{function}:AVERage:TCONtrol {type}, {channelList}"
    GET_SENSe1_AVERage_TCONtrol = ":SENSe1:{function}:AVERage:TCONtrol? {channelList}"
    SET_SENSe1_AVERage_WINDow = ":SENSe1:{function}:AVERage:WINDow {n}, {channelList}"
    GET_SENSe1_AVERage_WINDow = ":SENSe1:{function}:AVERage:WINDow? {channelList}"
    SET_SENSe1_AZERo_STATe = ":SENSe1:{function}:AZERo:STATe {state}, {channelList}"
    GET_SENSe1_AZERo_STATe = ":SENSe1:{function}:AZERo:STATe? {channelList}"
    SET_SENSe1_BIAS_LEVel = ":SENSe1:{function}:BIAS:LEVel {n}, {channelList}"
    GET_SENSe1_BIAS_LEVel = ":SENSe1:{function}:BIAS:LEVel? {channelList}"
    SET_SENSe1_DB_REFerence = ":SENSe1:{function}:DB:REFERence {n}, {channelList}"
    GET_SENSe1_DB_REFerence = ":SENSe1:{function}:DB:REFERence? {channelList}"
    SET_SENSe1_DBM_REFerence = ":SENSe1:{function}:DBM:REFERence {n}, {channelList}"
    GET_SENSe1_DBM_REFerence = ":SENSe1:{function}:DBM:REFERence? {channelList}"
    SET_SENSe1_DELay_AUTO = ":SENSe1:{function}:DELay:AUTO {state}, {channelList}"
    GET_SENSe1_DELay_AUTO = ":SENSe1:{function}:DELay:AUTO? {channelList}"
    SET_SENSe1_DELay_USER = ":SENSe1:{function}:DELay:USER {delayTime}, {channelList}"
    GET_SENSe1_DELay_USER = ":SENSe1:{function}:DELay:USER? {channelList}"
    SET_SENSe1_DETector_BANDwidth = ":SENSe1:{function}:DETector:BANDwidth {n}, {channelList}"
    GET_SENSe1_DETector_BANDwidth = ":SENSe1:{function}:DETector:BANDwidth? {channelList}"
    SET_SENSe1_INPutimpedance = ":SENSe1:{function}:INPutimpedance {n}, {channelList}"
    GET_SENSe1_INPutimpedance = ":SENSe1:{function}:INPutimpedance? {channelList}"
    SET_SENSe1_LINE_SYNC = ":SENSe1:{function}:LINE:SYNC {state}, {channelList}"
    GET_SENSe1_LINE_SYNC = ":SENSe1:{function}:LINE:SYNC? {channelList}"
    SET_SENSe1_NPLCycle = ":SENSe1:{function}:NPLCycle {n}, {channelList}"
    GET_SENSe1_NPLCycle = ":SENSe1:{function}:NPLCycle? {channelList}"
    SET_SENSe1_OCOMpensated = ":SENSe1:{function}:OCOMpensated {state}, {channelList}"
    GET_SENSe1_OCOMpensated = ":SENSe1:{function}:OCOMpensated? {channelList}"
    SET_SENSe1_ODETector = ":SENSe1:{function}:ODETector {state}, {channelList}"
    GET_SENSe1_ODETector = ":SENSe1:{function}:ODETector? {channelList}"
    SET_SENSe1_RANGe_AUTO = ":SENSe1:{function}:RANGe:AUTO {state}, {channelList}"
    GET_SENSe1_RANGe_AUTO = ":SENSe1:{function}:RANGe:AUTO? {channelList}"
    SET_SENSe1_RANGe_UPPer = ":SENSe1:{function}:RANGe:UPPer {n}, {channelList}"
    GET_SENSe1_RANGe_UPPer = ":SENSe1:{function}:RANGe:UPPer? {channelList}"
    SET_SENSe1_RELative = ":SENSe1:{function}:RELative {state}, {channelList}"
    GET_SENSe1_RELative = ":SENSe1:{function}:RELative? {channelList}"
    SET_SENSe1_RELative_ACQuire = ":SENSe1:{function}:RELative:ACQuire"
    SET_SENSe1_RELative_METHod = ":SENSe1:{function}:RELative:METHod {n}, {channelList}"
    GET_SENSe1_RELative_METHod = ":SENSe1:{function}:RELative:METHod? {channelList}"
    SET_SENSe1_RELative_STATe = ":SENSe1:{function}:RELative:STATe {state}, {channelList}"
    GET_SENSe1_RELative_STATe = ":SENSe1:{function}:RELative:STATe? {channelList}"
    SET_SENSe1_RTD_ALPHa = ":SENSe1:{function}:RTD:ALPHa {n}, {channelList}"
    GET_SENSe1_RTD_ALPHa = ":SENSe1:{function}:RTD:ALPHa? {channelList}"
    SET_SENSe1_RTD_BETA = ":SENSe1:{function}:RTD:BETA {n}, {channelList}"
    GET_SENSe1_RTD_BETA = ":SENSe1:{function}:RTD:BETA? {channelList}"
    SET_SENSe1_RTD_DELTa = ":SENSe1:{function}:RTD:DELTa {n}, {channelList}"
    GET_SENSe1_RTD_DELTa = ":SENSe1:{function}:RTD:DELTa? {channelList}"
    SET_SENSe1_RTD_FOUR = ":SENSe1:{function}:RTD:FOUR {type}, {channelList}"
    GET_SENSe1_RTD_FOUR = ":SENSe1:{function}:RTD:FOUR? {channelList}"
    SET_SENSe1_RTD_THRee = ":SENSe1:{function}:RTD:THRee {type}, {channelList}"
    GET_SENSe1_RTD_THRee = ":SENSe1:{function}:RTD:THRee? {channelList}"
    SET_SENSe1_RTD_TWO = ":SENSe1:{function}:RTD:TWO {type}, {channelList}"
    GET_SENSe1_RTD_TWO = ":SENSe1:{function}:RTD:TWO? {channelList}"
    SET_SENSe1_RTD_ZERO = ":SENSe1:{function}:RTD:ZERO {n}, {channelList}"
    GET_SENSe1_RTD_ZERO = ":SENSe1:{function}:RTD:ZERO? {channelList}"
    SET_SENSe1_SRATe = ":SENSe1:{function}:SRATe {n}, {channelList}"
    GET_SENSe1_SRATe = ":SENSe1:{function}:SRATe? {channelList}"
    GET_SENSe1_SENSe_RANGe_AUTO = ":SENSe1:{function}:SENSe:RANGe:AUTO?"
    GET_SENSe1_SENSe_RANGe_UPPer = ":SENSe1:{function}:SENSe:RANGe:UPPer? {channelList}"
    SET_SENSe1_TCouple_RJUNtion_SIMulated = ":SENSe1:{function}:TCouple:RJUNtion:SIMulated {tempValue}, {channelList}"
    GET_SENSe1_TCouple_RJUNtion_SIMulated = ":SENSe1:{function}:TCouple:RJUNtion:SIMulated? {channelList}"
    SET_SENSe1_TCouple_RJUNtion_RSELect = ":SENSe1:{function}:TCouple:RJUNtion:RSELect {type}, {channelList}"
    GET_SENSe1_TCouple_RJUNtion_RSELect = ":SENSe1:{function}:TCouple:RJUNtion:RSELect? {channelList}"
    SET_SENSe1_TCouple_TYPE = ":SENSe1:{function}:TCouple:TYPE {indentifier}, {channelList}"
    GET_SENSe1_TCouple_TYPE = ":SENSe1:{function}:TCouple:TYPE? {channelList}"
    SET_SENSe1_THERmistor = ":SENSe1:{function}:THERmistor {n}, {channelList}"
    GET_SENSe1_THERmistor = ":SENSe1:{function}:THERmistor? {channelList}"
    SET_SENSe1_THREshold_RANGe = ":SENSe1:{function}:THREshold:RANGe {n}, {channelList}"
    GET_SENSe1_THREshold_RANGe = ":SENSe1:{function}:THREshold:RANGe? {channelList}"
    SET_SENSe1_THREshold_RANGe_AUTO = ":SENSe1:{function}:THREshold:RANGe:AUTO {state}, {channelList}"
    GET_SENSe1_THREshold_RANGe_AUTO = ":SENSe1:{function}:THREshold:RANGe:AUTO? {channelList}"
    SET_SENSe1_TRANsducer = ":SENSe1:{function}:TRANsducer {type}, {channelList}"
    GET_SENSe1_TRANsducer = ":SENSe1:{function}:TRANsducer? {channelList}"
    SET_SENSe1_UNIT = ":SENSe1:{function}:UNIT {unitOfMeasure}, {channelList}"
    GET_SENSe1_UNIT = ":SENSe1:{function}:UNIT? {channelList}"
    SET_SENSe1_AZERo_ONCE = ":SENSe1:AZERo:ONCE"
    GET_SENSe1_CONFiguration_LIST_CATalog = ":SENSe1:CONFiguration:LIST:CATalog?"
    SET_SENSe1_CONFiguration_LIST_CREate = ":SENSe1:CONFiguration:LIST:CREate {name}"
    SET_SENSe1_CONFiguration_LIST_DELEte = ":SENSe1:CONFiguration:LIST:DELEte {name}, {index}"
    GET_SENSe1_CONFiguration_LIST_QUERy = ":SENSe1:CONFiguration:LIST:QUERY? {name}, {index}, {fieldSeparator}"
    SET_SENSe1_CONFiguration_LIST_RECall = ":SENSe1:CONFiguration:LIST:RECall {name}, {index}"
    GET_SENSe1_CONFiguration_LIST_SIZE = ":SENSe1:CONFiguration:LIST:SIZE? {name}"
    SET_SENSe1_CONFiguration_LIST_STORe = ":SENSe1:CONFiguration:LIST:STORe {name}, {index}"
    SET_SENSe1_COUNt = ":SENSe1:{function}:COUNt {n}, {channelList}"
    GET_SENSe1_COUNt = ":SENSe1:{function}:COUNt? {channelList}"
    SET_SENSe1_DIGitize_COUNt = ":SENSe1:{function}:DIGitize:COUNt {n}, {channelList}"
    GET_SENSe1_DIGitize_COUNt = ":SENSe1:{function}:DIGitize:COUNt? {channelList}"
    SET_SENSe1_DIGitize_FUNCtion_ON = ":SENSe1:{function}:DIGitize:FUNCtion:ON {function}, {channelList}"
    GET_SENSe1_DIGitize_FUNCtion_ON = ":SENSe1:{function}:DIGitize:FUNCtion:ON? {channelList}"
    SET_SENSe1_FUNCtion_ON = ":SENSe1:{function}:FUNCtion:ON {function}, {channelList}"
    GET_SENSe1_FUNCtion_ON = ":SENSe1:{function}:FUNCtion:ON? {channelList}"


class STATus(Enum):
    """
    The STATus subsystem controls the status registers of the instrument.
    """
    SET_STATus_CLEAr = ":STATus:CLEAr"
    GET_STATus_OPERation_CONDition = ":STATus:OPERation:CONDition?"
    SET_STATus_OPERation_ENABle = ":STATus:OPERation:ENABle {n}"
    GET_STATus_OPERation_ENABle = ":STATus:OPERation:ENABle?"
    SET_STATus_OPERation_MAP = ":STATus:OPERation:MAP {bitNumber}, {setEvent}, {clearEvent}"
    GET_STATus_OPERation_MAP = ":STATus:OPERation:MAP? {bitNumber}"
    GET_STATus_OPERation_EVENt = ":STATus:OPERation:EVENt?"
    SET_STATus_PRESet = ":STATus:PRESet"
    GET_STATus_QUEStionable_CONDition = ":STATus:QUEStionable:CONDition?"
    SET_STATus_QUEStionable_ENABle = ":STATus:QUEStionable:ENABle {n}"
    GET_STATus_QUEStionable_ENABle = ":STATus:QUEStionable:ENABle?"
    SET_STATus_QUEStionable_MAP = ":STATus:QUEStionable:MAP {bitNumber}, {setEvent}, {clearEvent}"
    GET_STATus_QUEStionable_MAP = ":STATus:QUEStionable:MAP? {bitNumber}"
    GET_STATus_QUEStionable_EVENt = ":STATus:QUEStionable:EVENt?"


class SYSTem(Enum):
    """
    This subsystem contains commands that affect the overall operation of the instrument, such as
    passwords, beepers, communications, event logs, and time. It also contains queries to determine the
    card and channels that are available in the DMM6500.
    """
    SET_SYSTem_ACCess = ":SYSTem:ACCess {permissions}"
    GET_SYSTem_ACCess = ":SYSTem:ACCess?"
    SET_SYSTem_BEERer_IMMediate = ":SYSTem:BEERer:IMMediate {frequency}, {duration}"
    GET_SYSTem_CARD1_IDN = ":SYSTem:CARD1:IDN?"
    GET_SYSTem_CARD1_VCHannel_STARt = ":SYSTem:CARD1:VCHannel:STARt?"
    GET_SYSTem_CARD1_VCHannel_END = ":SYSTem:CARD1:VCHannel:END?"
    GET_SYSTem_CARD1_VMAX = ":SYSTem:CARD1:VMAX?"
    SET_SYSTem_CLEAr = ":SYSTem:CLEAr"
    SET_SYSTem_COMMunication_LAN_CONFigure_AUTO = ":SYSTem:COMMunication:LAN:CONFigure 'AUTO'"
    SET_SYSTem_COMMunication_LAN_CONFigure_MANu = ":SYSTem:COMMunication:LAN:CONFigure 'MANual,{IPaddress},{NETmask},{GATeway}'"
    GET_SYSTem_COMMunication_LAN_CONFigure = ":SYSTem:COMMunication:LAN:CONFigure?"
    GET_SYSTem_COMMunication_LAN_MACaddress = ":SYSTem:COMMunication:LAN:MACaddress?"
    GET_SYSTem_ERRor_NEXT = ":SYSTem:ERRor:NEXT?"
    GET_SYSTem_ERRor_CODE_NEXT = ":SYSTem:ERRor:CODE:NEXT?"
    GET_SYSTem_ERRor_COUNt = ":SYSTem:ERRor:COUNt?"
    GET_SYSTem_EVENtlog_COUNt = ":SYSTem:EVENtlog:COUNt? {eventType}, {eventType}, {eventType}"
    GET_SYSTem_EVENtlog_NEXT = ":SYSTem:EVENtlog:NEXT? {eventType}, {eventType}, {eventType}"
    SET_SYSTem_EVENtlog_POST = ":SYSTem:EVENtlog:POST? {message}, {eventType}"
    SET_SYSTem_EVENtlog_SAVE = ":SYSTem:EVENtlog:SAVE {filename}, {eventType}"
    SET_SYSTem_GPIB_ADDRess = ":SYSTem:GPIB:ADDRess {address}"
    GET_SYSTem_GPIB_ADDRess = ":SYSTem:GPIB:ADDRess?"
    GET_SYSTem_LFRequency = ":SYSTem:LFRequency?"
    SET_SYSTem_PASSword_NEW = ":SYSTem:PASSword:NEW {password}"
    SET_SYSTem_PCARD1 = ":SYSTem:PCARD1 {cardNumber}"
    SET_SYSTem_POSetup = ":SYSTem:POSetup {name}"
    GET_SYSTem_POSetup = ":SYSTem:POSetup?"
    SET_SYSTem_TIME_FULL = ":SYSTem:TIME {year}, {month}, {day}, {hour}, {minute}, {second}"
    SET_SYSTem_TIME_HMS = ":SYSTem:TIME {hour}, {minute}, {second}"
    GET_SYSTem_TIME = ":SYSTem:TIME?"
    GET_SYSTem_TIME_DEFault = ":SYSTem:TIME? 1"
    GET_SYSTem_VERSion = ":SYSTem:VERSion?"


class TRACe(Enum):
    """
    The TRACe subsystem contains commands that control the reading buffers.
    """
    GET_TRACe_ACTual = ":TRACe:ACTual? '{bufferName}'"
    GET_TRACe_ACTual_END = ":TRACe:ACTual:END? '{bufferName}'"
    GET_TRACe_ACTual_STARt = ":TRACe:ACTual:STARt? '{bufferName}'"
    SET_TRACe_CHANnel_MATH = None  # This CMD need special configuration to it parameter, so I will split it into smaller functions for easier approach
    SET_TRACe_CLEAr = ":TRACe:CLEAr '{bufferName}'"
    GET_TRACe_DATA = ":TRACe:DATA? {startIndex}, {endIndex}, '{bufferName}', {bufferElements}"
    SET_TRACe_DELete = ":TRACe:DELEte '{bufferName}'"
    SET_TRACe_FILL_MODE = ":TRACe:FILL:MODE {fillType}, '{bufferName}'"
    GET_TRACe_FILL_MODE = ":TRACe:FILL:MODE? '{bufferName}'"
    SET_TRACe_LOG_STATe = ":TRACe:LOG:STATe {state}, '{bufferName}'"
    GET_TRACe_LOG_STATe = ":TRACe:LOG:STATe? '{bufferName}'"
    SET_TRACe_MAKE = ":TRACe:MAKE '{bufferName}', {bufferSize}, {bufferStyle}"
    SET_TRACe_MATH = None  # This CMD need special configuration to it parameter, so I will split it into smaller functions for easier approach
    SET_TRACe_POINts = ":TRACe:POINts {newSize}, '{bufferName}'"
    GET_TRACe_POINts = ":TRACe:POINts? '{bufferName}'"
    SET_TRACe_SAVE = ":TRACe:SAVE {filename}, '{bufferName}', {what}, {start}, {end}"
    SET_TRACe_SAVE_APPend = ":TRACe:SAVE:APPend {filename}, '{bufferName}', {timeFormat}, {start}, {end}"
    GET_TRACe_STATistics_AVERage = ":TRACe:STATistics:AVERage? '{bufferName}', {@<channelName>}"
    SET_TRACe_STATistics_CLEAr = ":TRACe:STATistics:CLEAr '{bufferName}'"
    GET_TRACe_STATistics_MAXimum = ":TRACe:STATistics:MAXimum? '{bufferName}', {@<channelName>}"
    GET_TRACe_STATistics_MINimum = ":TRACe:STATistics:MINimum? '{bufferName}', {@<channelName>}"
    GET_TRACe_STATistics_PK2Pk = ":TRACe:STATistics:PK2Pk? '{bufferName}', {@<channelName>}"
    GET_TRACe_STATistics_SPAN = ":TRACe:STATistics:SPAN? '{bufferName}', {@<channelName>}"
    GET_TRACe_STATistics_STDDev = ":TRACe:STATistics:STDDev? '{bufferName}', {@<channelName>}"
    SET_TRACe_TRIGger = ":TRACe:TRIGger '{bufferName}'"
    SET_TRACe_TRIGger_DIGitize = ":TRACe:TRIGger:DIGitize '{bufferName}'"
    SET_TRACe_UNIT = ":TRACe:UNIT CUSTOM{n}, {unitOfMeasure}, '{bufferName}'"
    SET_TRACe_WRITe_FORMat = ":TRACe:WRITe:FORMat '{bufferName}', {units}, {displayDigits}, {extraUnits}, {ExtraDigits}"
    SET_TRACe_WRITe_READing = None  # This CMD need special configuration to it parameter, so I will split it into smaller functions for easier approach


class TRIGger(Enum):
    """
    The commands in this subsystem configure and control the trigger operations, including the
    trigger model.
    """
    SET_ABORT = ":ABORT"
    SET_INITiate_IMMediate = ":INITiate:IMMediate"
    SET_TRIGger_BLENder_CLEAr = ":TRIGger:BLENder{n}:CLEAr"
    SET_TRIGger_BLENder_MODE = ":TRIGger:BLENder{n}:MODE {operation}"
    GET_TRIGger_BLENder_MODE = ":TRIGger:BLENder{n}:MODE?"
    GET_TRIGger_BLENder_OVERrun = ":TRIGger:BLENder{n}:OVERrun?"
    SET_TRIGger_BLENder_STIMulus = ":TRIGger:BLENder{n}:STIMulus{m} {event}"
    GET_TRIGger_BLENder_STIMulus = ":TRIGger:BLENder{n}:STIMulus{m}?"
    SET_TRIGger_BLOCk_BRANch_ALWays = ":TRIGger:BLOCk:BRANch:ALWays {blockNumber}, {branchToBlock}"
    SET_TRIGger_BLOCk_BRANch_COUNter = ":TRIGger:BLOCk:BRANch:COUNter {blockNumber}, {targetCount}, {branchToBlock}"
    GET_TRIGger_BLOCk_BRANch_COUNter_COUNt = ":TRIGger:BLOCk:BRANch:COUNter:COUNt? {blockNumber}"
    SET_TRIGger_BLOCk_BRANch_COUNter_RESet = ":TRIGger:BLOCk:BRANch:COUNter:RESet {blockNumber}, {counter}"
    SET_TRIGger_BLOCk_BRANch_DELTa = ":TRIGger:BLOCk:BRANch:DELta {blockNumber}, {targetDifference}, {branchToBlock}, {measureDigitizeBlock}"
    SET_TRIGger_BLOCk_BRANch_EVENt = ":TRIGger:BLOCk:BRANch:EVENt {blockNumber}, {event}, {branchToBlock}"
    SET_TRIGger_BLOCk_BRANch_LIMit_CONStant = ":TRIGger:BLOCk:BRANch:LIMit:CONStant {blockNumber}, {limitType}, {LimitA}, {LimitB}, {branchToBlock}, {measureDigitizeBlock}"
    SET_TRIGger_BLOCk_BRANch_LIMit_DYNamic = ":TRIGger:BLOCk:BRANch:LIMit:DYNAmic {blockNumber}, {limitType}, {LimitA}, {LimitB}, {branchToBlock}, {measureDigitizeBlock}"
    SET_TRIGger_BLOCk_BRANch_ONCE = ":TRIGger:BLOCk:BRANch:ONCE {blockNumber}, {branchToBlock}"
    SET_TRIGger_BLOCk_BRANch_ONCE_EXCLuded = ":TRIGger:BLOCk:BRANch:ONCE:EXCLuded {blockNumber}, {branchToBlock}"
    SET_TRIGger_BLOCk_BUFFer_CLEar = ":TRIGger:BLOCk:BUFFer:CLEar {blockNumber}, '{bufferName}'"
    SET_TRIGger_BLOCk_CONFig_NEXT = ":TRIGger:BLOCk:CONFig:NEXT {blockNumber}, {configurationList}"
    SET_TRIGger_BLOCk_CONFig_PREVious = ":TRIGger:BLOCk:CONFig:PREvious {blockNumber}, {configurationList}"
    SET_TRIGger_BLOCk_CONFig_RECall = ":TRIGger:BLOCk:CONFig:RECall {blockNumber}, {configurationList}, {index}"
    SET_TRIGger_BLOCk_DELay_CONStant = ":TRIGger:BLOCk:DELay:CONStant {blockNumber}, {time}"
    SET_TRIGger_BLOCk_DELay_DYNamic = ":TRIGger:BLOCk:DELay:DYNamic {blockNumber}, MEASure{n}"
    SET_TRIGger_BLOCk_DIGital_IO = ":TRIGger:BLOCk:DIGital:IO {blockNumber}, {bitPattern}, {bitMask}"
    GET_TRIGger_BLOCk_LIST = ":TRIGger:BLOCk:LIST?"
    SET_TRIGger_BLOCk_LOG_EVENt = ":TRIGger:BLOCk:LOG:EVENt {blockNumber}, {eventNumber}, {message}"
    SET_TRIGger_BLOCk_MDIGitize = ":TRIGger:BLOCk:MDIGitize {blockNumber}, '{bufferName}', {count}"
    SET_TRIGger_BLOCk_NOP = ":TRIGger:BLOCk:NOP {blockNumber}"
    SET_TRIGger_BLOCk_NOTify = ":TRIGger:BLOCk:NOTify {blockNumber}, {notifyID}"
    SET_TRIGger_BLOCk_WAIT = ":TRIGger:BLOCk:WAIT {blockNumber}, {event}, {clear}, {logic}, {event}, {event}"
    SET_TRIGger_CONTinuous = ":TRIGger:CONTinuous {setting}"
    GET_TRIGger_CONTinuous = ":TRIGger:CONTinuous?"
    SET_TRIGger_DIGital_IN_CLEar = ":TRIGger:DIGital{n}:IN:CLEar"
    SET_TRIGger_DIGital_IN_EDGE = ":TRIGger:DIGital{n}:IN:EDGE {detectedEdge}"
    GET_TRIGger_DIGital_IN_EDGE = ":TRIGger:DIGital{n}:IN:EDGE?"
    GET_TRIGger_DIGital_IN_OVERrun = ":TRIGger:DIGital{n}:IN:OVERrun?"
    SET_TRIGger_DIGital_OUT_LOGic = ":TRIGger:DIGital{n}:OUT:LOGic {logicType}"
    GET_TRIGger_DIGital_OUT_LOGic = ":TRIGger:DIGital{n}:OUT:LOGic?"
    SET_TRIGger_DIGital_OUT_PULSewidth = ":TRIGger:DIGital{n}:OUT:PULSewidth {width}"
    GET_TRIGger_DIGital_OUT_PULSewidth = ":TRIGger:DIGital{n}:OUT:PULSewidth?"
    SET_TRIGger_DIGital_OUT_STIMulus = ":TRIGger:DIGital{n}:OUT:STIMulus {event}"
    GET_TRIGger_DIGital_OUT_STIMulus = ":TRIGger:DIGital{n}:OUT:STIMulus?"
    SET_TRIGger_EXTernal_IN_CLEar = ":TRIGger:EXTernal:IN:CLEar"
    SET_TRIGger_EXTernal_IN_EDGE = ":TRIGger:EXTernal:IN:EDGE {detectedEdge}"
    GET_TRIGger_EXTernal_IN_EDGE = ":TRIGger:EXTernal:IN:EDGE?"
    GET_TRIGger_EXTernal_IN_OVERrun = ":TRIGger:EXTernal:IN:OVERrun?"
    SET_TRIGger_EXTernal_OUT_LOGic = ":TRIGger:EXTernal:OUT:LOGic {logicType}"
    GET_TRIGger_EXTernal_OUT_LOGic = ":TRIGger:EXTernal:OUT:LOGic?"
    SET_TRIGger_EXTernal_OUT_STIMulus = ":TRIGger:EXTernal:OUT:STIMulus {event}"
    GET_TRIGger_EXTernal_OUT_STIMulus = ":TRIGger:EXTernal:OUT:STIMulus?"
    SET_TRIGger_LAN_IN_CLEar = ":TRIGger:LAN:n:IN:CLEar"
    SET_TRIGger_LAN_IN_EDGE = ":TRIGger:LAN{n}:IN:EDGE {mode}"
    GET_TRIGger_LAN_IN_EDGE = ":TRIGger:LAN{n}:IN:EDGE?"
    GET_TRIGger_LAN_IN_OVERrun = ":TRIGger:LAN{n}:IN:OVERrun?"
    SET_TRIGger_LAN_OUT_CONNect_STATe = ":TRIGger:LAN{n}:OUT:CONNect:STATe {state}"
    GET_TRIGger_LAN_OUT_CONNect_STATe = ":TRIGger:LAN{n}:OUT:CONNect:STATe?"
    SET_TRIGger_LAN_OUT_IP_ADDRess = ":TRIGger:LAN{n}:OUT:IP:ADDRess {address}"
    GET_TRIGger_LAN_OUT_IP_ADDRess = ":TRIGger:LAN{n}:OUT:IP:ADDRess?"
    SET_TRIGger_LAN_OUT_LOGic = ":TRIGger:LAN{n}:OUT:LOGic {logicType}"
    GET_TRIGger_LAN_OUT_LOGic = ":TRIGger:LAN{n}:OUT:LOGic?"
    SET_TRIGger_LAN_OUT_PROTocol = ":TRIGger:LAN{n}:OUT:PROTocol {protocol}"
    GET_TRIGger_LAN_OUT_PROTocol = ":TRIGger:LAN{n}:OUT:PROTocol?"
    SET_TRIGger_LAN_OUT_STIMulus = ":TRIGger:LAN{n}:OUT:STIMulus {LANevent}"
    GET_TRIGger_LAN_OUT_STIMulus = ":TRIGger:LAN{n}:OUT:STIMulus?"
    SET_TRIGger_LOAD_ConfigList = ":TRIGger:LOAD 'ConfigList', {measureConfigList}, {delay}, '{bufferName}'"
    SET_TRIGger_LOAD_DurationLoop = ":TRIGger:LOAD 'DurationLoop', {duration}, {delay}, {readingBuffer}"
    SET_TRIGger_LOAD_Empty = ":TRIGger:LOAD 'EMPTY'"
    SET_TRIGger_LOAD_GradeBinning = None  # This CMD need special configuration to it parameter, so I will split it into smaller functions for easier approach
    SET_TRIGger_LOAD_LogicTrigger = ":TRIGger:LOAD 'LogicTrigger', {digInLine}, {digOutLine}, {count}, {clear}, {delay}, '{bufferName}'"
    SET_TRIGger_LOAD_LoopUntilEvent = ":TRIGger:LOAD 'LoopUntilEvent', {eventConstant}, {position}, {clear}, {delay}, '{bufferName}'"
    SET_TRIGger_LOAD_SimpleLoop = ":TRIGger:LOAD 'SimpleLoop', {count}, {delay}, '{bufferName}'"
    SET_TRIGger_LOAD_SortBinning = None  # This CMD need special configuration to it parameter, so I will split it into smaller functions for easier approach
    SET_TRIGger_PAUSe = ":TRIGger:PAUSe"
    SET_TRIGger_RESume = ":TRIGger:RESume"
    GET_TRIGger_STATe = ":TRIGger:STATe?"
    SET_TRIGger_TIMer_CLEar = ":TRIGger:TIMer{n}:CLEar"
    SET_TRIGger_TIMer_COUNt = ":TRIGger:TIMer{n}:COUNt {count}"
    GET_TRIGger_TIMer_COUNt = ":TRIGger:TIMer{n}:COUNt?"
    SET_TRIGger_TIMer_DELay = ":TRIGger:TIMer{n}:DELay {interval}"
    GET_TRIGger_TIMer_DELay = ":TRIGger:TIMer{n}:DELay?"
    SET_TRIGger_TIMer_STARt_FRACtional = ":TRIGger:TIMer{n}:STARt:FRACtional {time}"
    GET_TRIGger_TIMer_STARt_FRACtional = ":TRIGger:TIMer{n}:STARt:FRACtional?"
    SET_TRIGger_TIMer_STARt_GENerate = ":TRIGger:TIMer{n}:STARt:GENerate {state}"
    GET_TRIGger_TIMer_STARt_GENerate = ":TRIGger:TIMer{n}:STARt:GENerate?"
    GET_TRIGger_TIMer_STARt_OVERrun = ":TRIGger:TIMer<n>:STARt:OVERrun?"
    SET_TRIGger_TIMer_STARt_SEConds = ":TRIGger:TIMer{n}:STARt:SEConds {time}"
    GET_TRIGger_TIMer_STARt_SEConds = ":TRIGger:TIMer{n}:STARt:SEConds?"
    SET_TRIGger_TIMer_STARt_STIMulus = ":TRIGger:TIMer{n}:STARt:STIMulus {event}"
    GET_TRIGger_TIMer_STARt_STIMulus = ":TRIGger:TIMer{n}:STARt:STIMulus?"
    SET_TRIGger_TIMer_STATe = ":TRIGger:TIMer{n}:STATe {state}"
    GET_TRIGger_TIMer_STATe = ":TRIGger:TIMer{n}:STATe?"


class DMM6500_V1(VISA_INSTRUMENT):
    def __init__(self, visa_port=None, connection_type=None):
        super().__init__(visa_port, connection_type)
        self.scanner_card = False
        # self.controller._connection.timeout = 60000

    def cmd_formatter(self, command: str):
        if self.scanner_card:
            return command
        else:
            if not "?" in command:
                # Replace the unwanted part
                cleaned_command = re.sub(r", {channelList}", "", command)
                return cleaned_command
            elif "?" in command:
                cleaned_command = re.sub(r" {channelList}", "", command)
                return cleaned_command

    def rcl(self,
            user_setup=USER_SETUP.SETUP_0.value) -> None:
        """
        Brief:
            -   This command returns the instrument to the setup that was saved with the *SAV command.
        Details:
            -   Restores the state of the instrument from a copy of user-saved settings that are stored in setup
            memory. The settings are saved using the *SAV command.

            -   If you view the user-saved settings from the front panel of the instrument, these are stored as scripts
            named Setup0<n>.
        Example:
            -   CMD: *RCL 3
        :return: None
        """
        cmd = ROOT.SET_RCL.value.format(setup=user_setup)
        self.write(command=cmd)

    def sav(self,
            user_setup=USER_SETUP.SETUP_1.value) -> None:
        """
        Brief:
            -   Save the present instrument settings as a user-saved setup.
        Details:
            -   Most commands that are affected by *RST can be saved with the *SAV command.
            -   You can save up to five user-saved setups. Any settings that had been stored previously as <n> are
                overwritten.
            -   If you view the user-saved setups from the front panel of the instrument, they are stored as scripts
                named Setup0<n>.
        Example:
            -   CMD: *SAV 2
        :return: None
        """
        cmd = ROOT.SET_SAV.value.format(setup=user_setup)
        self.write(command=cmd)

    def fetch(self,
              buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
              buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
        Brief:
            -   This command requests the latest reading from a reading buffer.
        Details:
            -   This command requests the last available reading from a reading buffer. If you send this command
            more than once and there are no new readings, the returned values are the same. If the reading
            buffer is empty, an error is returned.
        Example:
            -   CMD: :FETCh? "<bufferName>", <bufferElements>
        :return: string
        """
        cmd = ROOT.GET_FETCh.value.format(bufferName=buffer_name,
                                          bufferElements=buffer_elements)
        return self.query(command=cmd)

    def measure(self,
                buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
                buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
        Brief:
            -   This command makes measurements with the current function (except for digitize),
            and places them in a reading buffer, and returns the last reading.
        Details:
            -   This command makes a measurement using the specified function and stores the reading in a
            reading buffer.
            -   If you do not define the function parameter, the instrument uses the presently selected measure
            function. If a digitize function is presently selected, an error is generated.
            -   This query makes the number of readings specified by [:SENSe[1]]:COUNt. When you use a
            reading buffer with a command or action that makes multiple readings, all readings are available in
            the reading buffer. However, only the last reading is returned as a reading with the command.
            -   If you define a specific reading buffer, the reading buffer must exist before you make the
            measurement.
            -   To get multiple readings, use the :TRACe:DATA? command.
            -   :MEASure? performs the same function as READ?.
            -   :MEASure:<function>? performs the same function as sending :SENse:FUNCtion, then READ?.
        Example:
            -   CMD: :MEASure? "<bufferName>", <bufferElements>
        :return: string
        """
        cmd = ROOT.GET_MEASURE.value.format(bufferName=buffer_name,
                                            bufferElements=buffer_elements)
        return self.query(command=cmd)

    def measure_with(self,
                     function=FUNCTION.VOLT_DC.value,
                     buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
                     buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
            Brief:
                -   Same as measure but with a specific function (except for digitize)
            Details:
                -   Refer to measure()
            Example:
                -   CMD: :MEASure:<function>? "<bufferName>", <bufferElements>
            :return: string
        """
        cmd = ROOT.GET_MEASURE_WITH.value.format(function=function,
                                                 bufferName=buffer_name,
                                                 bufferElements=buffer_elements)
        return self.query(command=cmd)

    def measure_digitize(self,
                         buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
                         buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
            Brief:
                -   This command makes a digitize measurement with the current function, places it in a reading buffer, and returns the reading
            Details:
                -   This command makes a digitize measurement using the specified function and stores the reading in a
                reading buffer. Sending this command changes the measurement function to the one specified by
                <function>. This function remains selected after the measurement is complete.
                -   If you do not define the function parameter, the instrument uses the presently selected function. If a
                digitize function is presently selected, an error is generated.
                -   When you use a reading buffer with a command or action that makes multiple readings, all readings
                are available in the reading buffer. However, only the last reading is returned as a reading with the
                command.
                -   If you define a specific reading buffer, the reading buffer must exist before you make the
                measurement.
                -   To get multiple readings, use the :TRACe:DATA? command.
                -   :MEASure:DIGitize? performs the same function as READ:DIGitize?.
                -   :MEASure:DIGitize:<function>? performs the same function as sending
                -   :SENse:DIGitize:FUNCtion "<function>", then READ?.
            Example:
                -   CMD: :MEASure:DIGitize? "<bufferName>", <bufferElements>
            :return: string
        """
        cmd = ROOT.GET_MEASURE_DIGITIZE.value.format(bufferName=buffer_name,
                                                     bufferElements=buffer_elements)
        return self.query(command=cmd)

    def measure_digitize_with(self,
                              function=DIGITIZE_FUNCTION.VOLT.value,
                              buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
                              buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
            Brief:
                -   Same as measure_digitize but with a specific function
            Details:
                -   Refer to measure_digitize()
            Example:
                -   CMD: :MEASure:DIGitize:<function>? "<bufferName>", <bufferElements>
            :return: string
        """
        cmd = ROOT.GET_MEASURE_DIGITIZE_WITH.value.format(function=function,
                                                          bufferName=buffer_name,
                                                          bufferElements=buffer_elements)
        return self.query(command=cmd)

    def read(self,
             buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
             buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
        Brief:
            -   This command requests the latest reading from a reading buffer.
        Details:
            -   This query makes the number of readings specified by [:SENSe[1]]:COUNt. If multiple readings
            are made, all readings are available in the reading buffer.
            -   However, only the last reading is returned as a reading with the command.
            -   To get multiple readings, use the :TRACe:DATA? command.
        Example:
            -   CMD: :READ? "<bufferName>", <bufferElements>
        :return: string
        """
        cmd = ROOT.GET_READ.value.format(bufferName=buffer_name,
                                         bufferElements=buffer_elements)
        return self.query(command=cmd)

    def read_digitize(self,
                      buffer_name=DEFAULT_SETUP.DEFBUFFER1.value,
                      buffer_elements=BUFFER_ELEMENTS.READing.value) -> str:
        """
        Brief:
            -   This command requests the latest reading from a reading buffer.
        Details:
            -   You must set the instrument to a digitize function before sending this command.
            -   This query makes the number of readings specified by [:SENSe[1]]:DIGitize:COUNt. If multiple
            readings are made, all readings are available in the reading buffer.
            -   However, only the last reading is returned as a reading with the command.
            -   To get multiple readings, use the :TRACe:DATA? command.
        Example:
            -   CMD: :READ:DIGitize? "<bufferName>", <bufferElements>
        :return: string
        """
        cmd = ROOT.GET_READ_DIGITIZE.value.format(bufferName=buffer_name,
                                                  bufferElements=buffer_elements)
        return self.query(command=cmd)

    def set_range(self, function: str = None,
                  n: str = None,
                  channelList="{channelList}"):
        range_cmd = self.cmd_formatter(SENSe1.SET_SENSe1_RANGe_UPPer.value.format(function=function,
                                                                                  n=n,
                                                                                  channelList=channelList))
        self.write(range_cmd)

    def get_range(self, function: str = None,
                  n: str = None,
                  channelList="{channelList}"):
        range_cmd = self.cmd_formatter(SENSe1.GET_SENSe1_RANGe_UPPer.value.format(function=function,
                                                                                  channelList=channelList))
        return self.query(command=range_cmd)

    # -----------------------------------------------------------------------------------------------------------------
    def load_trigger(self, **kwargs):
        mode = kwargs["mode"]
        cmd = None
        if mode.lower() == "empty":
            cmd = TRIGger.SET_TRIGger_LOAD_Empty.value

        self.write(command=cmd)

    def set_trigger_block_buffer_clear(self,
                                       blockNumber=0,
                                       bufferName="defbuffer1"):
        cmd = self.cmd_formatter(TRIGger.SET_TRIGger_BLOCk_BUFFer_CLEar.value.format(blockNumber=blockNumber,
                                                                                     bufferName=bufferName))
        self.write(cmd)

    def set_trigger_block_delay_constant(self,
                                         blockNumber=0,
                                         time=RANGE.TIME_1ms.value):
        cmd = self.cmd_formatter(TRIGger.SET_TRIGger_BLOCk_DELay_CONStant.value.format(blockNumber=blockNumber,
                                                                                       time=time))
        self.write(cmd)

    def set_trigger_block_mdigitize(self,
                                    blockNumber=0,
                                    bufferName="defbuffer1",
                                    count=0):
        cmd = self.cmd_formatter(TRIGger.SET_TRIGger_BLOCk_MDIGitize.value.format(blockNumber=blockNumber,
                                                                                  bufferName=bufferName,
                                                                                  count=count))
        self.write(cmd)

    def set_trigger_block_branch_limit_constant(self,
                                                blockNumber=0,
                                                limitType="ABOVe",
                                                LimitA=0.0,
                                                LimitB=0.0,
                                                branchToBlock=0,
                                                measureDigitizeBlock=0):

        cmd = self.cmd_formatter(TRIGger.SET_TRIGger_BLOCk_BRANch_LIMit_CONStant.value.format(blockNumber=blockNumber,
                                                                                              limitType=limitType,
                                                                                              LimitA=LimitA,
                                                                                              LimitB=LimitB,
                                                                                              branchToBlock=branchToBlock,
                                                                                              measureDigitizeBlock=measureDigitizeBlock))
        self.write(cmd)

    def init(self):
        self.write(ROUTe.SET_INITiate_IMMediate.value)

    # -----------------------------------------------------------------------------------------------------------------

    def set_trigger_external_in_clear(self):
        cmd = TRIGger.SET_TRIGger_EXTernal_IN_CLEar.value
        self.write(command=cmd)

    def set_trigger_external_in_edge(self, edgeType=EDGE_TYPE.FALLing.value):
        cmd = TRIGger.SET_TRIGger_EXTernal_IN_EDGE.value.format(detectedEdge=edgeType)
        self.write(command=cmd)

    def get_trigger_external_in_edge(self):
        cmd = TRIGger.GET_TRIGger_EXTernal_IN_EDGE.value
        return self.query(command=cmd)

    def get_trigger_external_in_overrun(self):
        cmd = TRIGger.GET_TRIGger_EXTernal_IN_OVERrun.value
        return self.query(command=cmd)

    def set_trigger_external_out_logic(self, logicType=TTL.NEGative.value):
        cmd = TRIGger.SET_TRIGger_EXTernal_OUT_LOGic.value.format(logicType=logicType)
        self.write(command=cmd)

    def get_trigger_external_out_logic(self):
        cmd = TRIGger.GET_TRIGger_EXTernal_OUT_LOGic.value
        return self.query(command=cmd)

    def set_trigger_external_out_stimulus(self, event=EVENT.NONE.value):
        cmd = TRIGger.SET_TRIGger_EXTernal_OUT_STIMulus.value.format(event=event)
        self.write(command=cmd)

    def get_trigger_external_out_stimulus(self):
        cmd = TRIGger.GET_TRIGger_EXTernal_OUT_STIMulus.value
        return self.query(cmd)


"""
class DMM6500:
    def __init__(self, visa_port=None, connection_type=None):
        self.visa_port = visa_port
        self.connection_type = connection_type
        self.controller = None
        self.__connect()

    def __connect(self):
        if self.connection_type == "USB":
            pass
        elif self.connection_type == "TCP/IP":
            self.controller = TCPIP_Controller(ip_address=self.visa_port)
            self.__cls()
        elif self.connection_type == "Serial":
            self.controller = SERIAL_Controller(port=self.visa_port)
            self.__cls()

    def __cls(self):
        self.controller.write('*CLS')

    def write(self, command: str) -> None:
        self.controller.write(command)

    def query(self, command: str) -> str:
        return self.controller.query(command)

    def fetch(self, buffer_name="defbuffer1"):
        return self.controller.query(f':FETCh? "{buffer_name}"')

    def close(self):
        self.controller.close()

    def meas_vdc(self, meas_range='AUTO'):
        # cmd = r"[:SENSe[1]]:VOLTage[:DC]:RANGe: AUTO"
        cmd = "VOLT:DC:RANG:AUTO ON"
        # cmd = ":SENS:VOLT:DC:RANG AUTO"

        self.write(cmd)

        return self.query(":MEASure:VOLTage:DC?")

    def meas_idc(self, meas_range='AUTO'):
        # cmd = r"[:SENSe[1]]:VOLTage[:DC]:RANGe: AUTO"
        cmd = "CURR:DC:RANG:AUTO ON"
        # cmd = ":SENS:VOLT:DC:RANG AUTO"

        self.write(cmd)

        return self.query(":MEASure:CURRent:DC?")

    def meas_vac(self, meas_range='AUTO'):
        # cmd = r"[:SENSe[1]]:VOLTage[:DC]:RANGe: AUTO"
        cmd = "VOLT:AC:RANG:AUTO ON"
        # cmd = ":SENS:VOLT:DC:RANG AUTO"

        self.write(cmd)

        return self.query(":MEASure:VOLTage:AC?")

    def meas_2w(self, meas_range='AUTO'):
        cmd = "RES:RANG:AUTO ON"
        self.write(cmd)

        return self.query(":MEASure:RESistance?")

    def clear_trigger(self):
        scpi_instruction = {
            'cmd1': ':*RST',
        }
        for key, value in scpi_instruction.items():
            self.write(value)

    def trigger_mode(self):
        range_cmd = ":SENS:VOLT:DC:RANG 10"
        self.write(range_cmd)

        scpi_instruction = {
            'cmd1': ':*RST',
            'cmd2': ':TRIGger:LOAD "EMPTY"',
            'cmd3': ':TRIGger:BLOCk:BUFFer:CLE 1, "defbuffer1"',
            'cmd4': ':TRIGger:BLOCk:DELay:CONStant 2, 1e-3',
            'cmd5': ':TRIGger:BLOCk:MDIGitize 3, "defbuffer1", 1',
            'cmd6': ':TRIGger:BLOCk:BRANch:LIMit:CONStant 4, ABOVe, 0, 1.6, 1,3',
            'cmd7': ':TRIGger:BLOCk:MDIGitize 5, "defbuffer1", 1',
            'cmd8': ':TRIGger:BLOCk:BRANch:LIMit:CONStant 6, BELow, 1.5, 0, 0,5',
            'cmd9': ':INIT'
        }
        for key, value in scpi_instruction.items():
            self.write(value)

    def get_data_from_trigger_model(self):
        while True:
            data = self.query(':TRIGger:STATe?')
            print(data)  # "IDLE;IDLE;6"
            results = data.split(sep=';')
            if results[0] == "IDLE" and results[1] == "IDLE" and results[2] == "6":
                return round(float(self.fetch()), 3)
            time.sleep(0.001)
"""


class UNITTEST:
    def __init__(self, visa_port, connection_type):
        self.dmm = DMM6500_V1(visa_port=visa_port, connection_type=connection_type)

    def ieee488_2_common_commands(self):
        self.dmm.controller.cc_cls()
        self.dmm.controller.cc_ese()
        self.dmm.controller.cc_opc()

    def method_test(self):
        # self.dmm.sav()
        # self.dmm.rcl()
        print(self.dmm.measure())
        # print(self.dmm.measure_with())
        # print(self.dmm.read())
        print(self.dmm.fetch())

        # print(self.dmm.measure_digitize_with())
        # print(self.dmm.read_digitize())

    def trigger_mode(self):
        self.dmm.set_range(function=FUNCTION.VOLT_DC.VOLT_DC.value,
                           n=RANGE.DC_10V.value)
        self.dmm.load_trigger(mode="empty")
        self.dmm.set_trigger_block_buffer_clear(blockNumber=1)
        self.dmm.set_trigger_block_delay_constant(blockNumber=2, time=RANGE.TIME_1ms.value)
        self.dmm.set_trigger_block_mdigitize(blockNumber=3, count=1)
        self.dmm.set_trigger_block_branch_limit_constant(blockNumber=4,
                                                         limitType="ABOVe",
                                                         LimitA=0,
                                                         LimitB=3.0,
                                                         branchToBlock=1,
                                                         measureDigitizeBlock=3
                                                         )
        self.dmm.set_trigger_block_mdigitize(blockNumber=5, count=1)
        self.dmm.set_trigger_block_branch_limit_constant(blockNumber=6,
                                                         limitType="BELow",
                                                         LimitA=1.8,
                                                         LimitB=0,
                                                         branchToBlock=0,
                                                         measureDigitizeBlock=5
                                                         )
        self.dmm.init()

    def get_data_from_trigger_model(self):
        while True:
            data = self.dmm.query(':TRIGger:STATe?')
            print(data)  # "IDLE;IDLE;6"
            results = data.split(sep=';')
            if results[0] == "IDLE" and results[1] == "IDLE" and results[2] == "6":
                return round(float(self.dmm.fetch()), 3)
            time.sleep(0.001)

    def trigger_in_out_test(self):
        self.dmm.set_trigger_external_in_clear()
        self.dmm.set_trigger_external_out_logic(logicType=TTL.NEGative.value)
        self.dmm.set_trigger_external_out_stimulus(event=EVENT.COMMand.value)

        print("Before trigger")
        self.dmm.write(ROOT.SET_TRIG.value)
        print("After trigger")

if __name__ == "__main__":
    scanner = PyVISAScanner()
    connect_type, port = scanner.scan_for_instruments(expected_id="DMM6500")

# ---
    instr = UNITTEST(visa_port=port, connection_type=connect_type)
    print("Current Test")
    instr.dmm.set_range(function=FUNCTION.CURR_DC.value,
                        n=RANGE.AC_100mA.value)
    value = round(float(instr.dmm.measure_with(function=FUNCTION.CURR_DC.value)),ndigits=3)
    range = instr.dmm.get_range(function=FUNCTION.CURR_DC.value)

    print(f"{value} mA")
    instr.dmm.close()
# ---

    # instr.trigger_mode()
    # print(instr.get_data_from_trigger_model())
    # instr.trigger_in_out_test()
