from opcua import Client
import time

url = "opc.tcp://127.0.0.1:8899/freeopcua/server/"

client = Client(url)

client.connect()
print("client connected")

i = 1
while i < 60:
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

	
	value0 = val0.get_value()
	value1 = val1.get_value()
	value2 = val2.get_value()
	value3 = val3.get_value()
	value4 = val4.get_value()
	value5 = val5.get_value()
	value6 = val6.get_value()
	value7 = val7.get_value()
	value8 = val8.get_value()
	value9 = val9.get_value()
	value10 = val10.get_value()
	value11 = val11.get_value()
	value12 = val12.get_value()
	value13 = val13.get_value()
	value14 = val14.get_value()
	value15 = val15.get_value()
	value16 = val16.get_value()
	value17 = val17.get_value()
	value18 = val18.get_value()
	value19 = val19.get_value()
	value20 = val20.get_value()
	value21 = val21.get_value()
	value22 = val22.get_value()
	value23 = val23.get_value()
	value24 = val24.get_value()
	value25 = val25.get_value()
	value26 = val26.get_value()
	value27 = val27.get_value()
	value28 = val28.get_value()
	value29 = val29.get_value()
	value30 = val30.get_value()
	value31 = val31.get_value()
	value32 = val33.get_value()
	value33 = val33.get_value()
	

	print("BK: "+str(value5)+" - BK Res: "+str(value6))
	print("P: "+str(value7)+" - Q: "+str(value8)+" - V: "+str(value9))
	print("======================"+"\n")
	

	time.sleep(1)


client.disconnect()
