from opcua import Server
from opcua import ua
from opcua import Client
from random import randint
import datetime
import time

server = Server()
url = "opc.tcp://0.0.0.0:8899/freeopcua/server/"
server.set_endpoint(url)

name="OPC_UA_SERVER"
addspace = server.register_namespace(name)

#Define Variant Data Type  2 = Integer ; 4 = float
variant = None
variant = ua.Variant(0, ua.VariantType.Int16)

variant2 = None
variant2 = ua.Variant(0, ua.VariantType.Float)



node = server.get_objects_node()
Substation3 = node.add_object(addspace,"S3")


S3_M1_B25_Li_02_25_CB_ctrl = Substation3.add_variable(addspace,"S3_M1_B25_Li_02_25_CB_ctrl",variant)
S3_M1_B25_Li_02_25_CB_ctrl.set_writable(True)
S3_M1_B25_Li_02_25_CB_res = Substation3.add_variable(addspace,"S3_M1_B25_Li_02_25_CB_res",variant)
S3_M1_B25_Li_02_25_CB_res.set_writable(True)
S3_M1_B25_Li_02_25_P_res = Substation3.add_variable(addspace,"S3_M1_B25_Li_02_25_P_res",variant2)
S3_M1_B25_Li_02_25_P_res.set_writable(True)
S3_M1_B25_Li_02_25_Q_res = Substation3.add_variable(addspace,"S3_M1_B25_Li_02_25_Q_res",variant2)
S3_M1_B25_Li_02_25_Q_res.set_writable(True)
S3_M1_B25_Li_02_25_I_res = Substation3.add_variable(addspace,"S3_M1_B25_Li_02_25_I_res",variant2)
S3_M1_B25_Li_02_25_I_res.set_writable(True)
S3_M2_B25_Ld25_CB_ctrl = Substation3.add_variable(addspace,"S3_M2_B25_Ld25_CB_ctrl",variant)
S3_M2_B25_Ld25_CB_ctrl.set_writable(True)
S3_M2_B25_Ld25_CB_res = Substation3.add_variable(addspace,"S3_M2_B25_Ld25_CB_res",variant)
S3_M2_B25_Ld25_CB_res.set_writable(True)
S3_M2_B25_Ld25_P_res = Substation3.add_variable(addspace,"S3_M2_B25_Ld25_P_res",variant2)
S3_M2_B25_Ld25_P_res.set_writable(True)
S3_M2_B25_Ld25_Q_res = Substation3.add_variable(addspace,"S3_M2_B25_Ld25_Q_res",variant2)
S3_M2_B25_Ld25_Q_res.set_writable(True)
S3_M2_B25_Ld25_V_res = Substation3.add_variable(addspace,"S3_M2_B25_Ld25_V_res",variant2)
S3_M2_B25_Ld25_V_res.set_writable(True)
S3_M3_B25_Tr_CB_ctrl = Substation3.add_variable(addspace,"S3_M3_B25_Tr_CB_ctrl",variant)
S3_M3_B25_Tr_CB_ctrl.set_writable(True)
S3_M3_B25_Tr_CB_res = Substation3.add_variable(addspace,"S3_M3_B25_Tr_CB_res",variant)
S3_M3_B25_Tr_CB_res.set_writable(True)
S3_M3_B25_Tr_tap_ctrl = Substation3.add_variable(addspace,"S3_M3_B25_Tr_tap_ctrl",variant)
S3_M3_B25_Tr_tap_ctrl.set_writable(True)
S3_M3_B25_Tr_tap_mode = Substation3.add_variable(addspace,"S3_M3_B25_Tr_tap_mode",variant)
S3_M3_B25_Tr_tap_mode.set_writable(True)
S3_M3_B25_Tr_tap = Substation3.add_variable(addspace,"S3_M3_B25_Tr_tap",variant)
S3_M3_B25_Tr_tap.set_writable(True)
S3_M3_B25_Tr_tap_res = Substation3.add_variable(addspace,"S3_M3_B25_Tr_tap_res",variant)
S3_M3_B25_Tr_tap_res.set_writable(True)
S3_M3_B25_Tr_Ld_res = Substation3.add_variable(addspace,"S3_M3_B25_Tr_Ld_res",variant2)
S3_M3_B25_Tr_Ld_res.set_writable(True)
S3_M3_B25_Tr_f_res = Substation3.add_variable(addspace,"S3_M3_B25_Tr_f_res",variant2)
S3_M3_B25_Tr_f_res.set_writable(True)
S3_M3_B25_Tr_V_res = Substation3.add_variable(addspace,"S3_M3_B25_Tr_V_res",variant2)
S3_M3_B25_Tr_V_res.set_writable(True)
S3_M4_B25_Li_25_26_CB_ctrl = Substation3.add_variable(addspace,"S3_M4_B25_Li_25_26_CB_ctrl",variant)
S3_M4_B25_Li_25_26_CB_ctrl.set_writable(True)
S3_M4_B25_Li_25_26_CB_res = Substation3.add_variable(addspace,"S3_M4_B25_Li_25_26_CB_res",variant)
S3_M4_B25_Li_25_26_CB_res.set_writable(True)
S3_M4_B25_Li_25_26_P_res = Substation3.add_variable(addspace,"S3_M4_B25_Li_25_26_P_res",variant2)
S3_M4_B25_Li_25_26_P_res.set_writable(True)
S3_M4_B25_Li_25_26_Q_res = Substation3.add_variable(addspace,"S3_M4_B25_Li_25_26_Q_res",variant2)
S3_M4_B25_Li_25_26_Q_res.set_writable(True)
S3_M4_B25_Li_25_26_I_res = Substation3.add_variable(addspace,"S3_M4_B25_Li_25_26_I_res",variant2)
S3_M4_B25_Li_25_26_I_res.set_writable(True)
S3_M5_B37_Tr_CB_ctrl = Substation3.add_variable(addspace,"S3_M5_B37_Tr_CB_ctrl",variant)
S3_M5_B37_Tr_CB_ctrl.set_writable(True)
S3_M5_B37_Tr_CB_res = Substation3.add_variable(addspace,"S3_M5_B37_Tr_CB_res",variant)
S3_M5_B37_Tr_CB_res.set_writable(True)
S3_M6_B37_G8_CB_ctrl = Substation3.add_variable(addspace,"S3_M6_B37_G8_CB_ctrl",variant)
S3_M6_B37_G8_CB_ctrl.set_writable(True)
S3_M6_B37_G8_CB_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_CB_res",variant)
S3_M6_B37_G8_CB_res.set_writable(True)
S3_M6_B37_G8_P_ctrl = Substation3.add_variable(addspace,"S3_M6_B37_G8_P_ctrl",variant2)
S3_M6_B37_G8_P_ctrl.set_writable(True)
S3_M6_B37_G8_P_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_P_res",variant2)
S3_M6_B37_G8_P_res.set_writable(True)
S3_M6_B37_G8_Q_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_Q_res",variant2)
S3_M6_B37_G8_Q_res.set_writable(True)
S3_M6_B37_G8_V_ctrl = Substation3.add_variable(addspace,"S3_M6_B37_G8_V_ctrl",variant2)
S3_M6_B37_G8_V_ctrl.set_writable(True)
S3_M6_B37_G8_V_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_V_res",variant2)
S3_M6_B37_G8_V_res.set_writable(True)
S3_M6_B37_G8_f_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_f_res",variant2)
S3_M6_B37_G8_f_res.set_writable(True)
S3_M6_B37_G8_Ld_res = Substation3.add_variable(addspace,"S3_M6_B37_G8_Ld_res",variant2)
S3_M6_B37_G8_Ld_res.set_writable(True)


server.start()

print("Server start at {}".format(url))

