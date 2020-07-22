from opcua import Client
from opcua import ua
import time

url = "opc.tcp://127.0.0.1:8899/freeopcua/server/"

client = Client(url)

client.connect()
print("client connected")

val0 = client.get_node("ns=2;i=2")
val1 = client.get_node("ns=2;i=3")
val2 = client.get_node("ns=2;i=4")
val3 = client.get_node("ns=2;i=5")
val4 = client.get_node("ns=2;i=6")
val5 = client.get_node("ns=2;i=7")
val6 = client.get_node("ns=2;i=8")
val7 = client.get_node("ns=2;i=9")
val8 = client.get_node("ns=2;i=10")
val9 = client.get_node("ns=2;i=11")
val10 = client.get_node("ns=2;i=12")
val11 = client.get_node("ns=2;i=13")
val12 = client.get_node("ns=2;i=14")
val13 = client.get_node("ns=2;i=15")
val14 = client.get_node("ns=2;i=16")
val15 = client.get_node("ns=2;i=17")
val16 = client.get_node("ns=2;i=18")
val17 = client.get_node("ns=2;i=19")
val18 = client.get_node("ns=2;i=20")
val19 = client.get_node("ns=2;i=21")
val20 = client.get_node("ns=2;i=22")
val21 = client.get_node("ns=2;i=23")
val22 = client.get_node("ns=2;i=24")
val23 = client.get_node("ns=2;i=25")
val24 = client.get_node("ns=2;i=26")
val25 = client.get_node("ns=2;i=27")
val26 = client.get_node("ns=2;i=28")
val27 = client.get_node("ns=2;i=29")
val28 = client.get_node("ns=2;i=30")
val29 = client.get_node("ns=2;i=31")
val30 = client.get_node("ns=2;i=32")
val31 = client.get_node("ns=2;i=33")
val32 = client.get_node("ns=2;i=34")
val33 = client.get_node("ns=2;i=35")


print("--")
val1.set_value(999, ua.VariantType.Int16)


client.disconnect()

