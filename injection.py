from PCANBasic import *

f1 = open('C:\\Users\\LISA\Desktop\\CAN-FD injection\\G80 CANFD C-CAN 2021.10.25 - 2.trc', 'r', encoding='utf-8')

CAN_FD_TRC = f1.readlines()
#print(CAN_FD_Data[15])


CAN_FD = PCANBasic()
CAN_BUS = PCAN_USBBUS2
bitrate =  b"f_clock=20000000,nom_brp=5,nom_tseg1=5,nom_tseg2=2,nom_sjw=1,data_brp=2,data_tseg1=3,data_tseg2=1,data_sjw=1"
#print(CAN_FD.GetValue(PCAN_USBBUS2, PCAN_BITRATE_INFO_FD))
CAN_FD.InitializeFD(CAN_BUS, bitrate)

message = TPCANMsgFD()
data = [0 for col in range(64)]

for i in range(15,len(CAN_FD_TRC)):
    data = CAN_FD_TRC[i].split(' ')
    print(data)
    ID = int(data[15],16)
    data_len = int(data[17])
    CAN_FD_Data = data[18:18+int(data_len)]
    for j in range(0, int(data_len)):
        message.DATA[j] = int(CAN_FD_Data[j],16)
    message.ID = int(ID)
    message.MSGTYTPE = PCAN_MESSAGE_BRS #PCAN_MESSAGE_FD #PCAN_MESSAGE_BRS
    message.DLC = data_len
    CAN_FD.WriteFD(CAN_BUS, message)


