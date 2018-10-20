
import CDH_Constants as CDH
import Flags
#All POWER UNITS IN milliwatts(mW)
#ALL TIME UNITS IN seconds(s)
#Voltage Units in Volts(V)

def setflags(sysTime):
    global CDHMode
    if(Flags.Recieve_Flag_Comm == 1):
        Flags.Recieve_Flag_Comm = 0
        Flags.FLAG_Turn_ON_Payload = 1
        Flags.Flag_Signal_ADCS = 1
        CDHMode = 'receive comms'

    elif(Flags.FLAG_Receive_PayLoad == 1):
        Flags.FLAG_Receive_PayLoad =0
        Flags.Flag_Signal_COMMS = 1
        CDHMode = 'receive payload'

    elif(Flags.Flag_Latch_Up == 1):
        CDHMode = 'receive latchup'

    else:
        return


CDHstartTime = -1
def CDHPower(sysTime):
    global CDHstartTime
    global CDHMode
    if(CDHstartTime == -1):
      CDHstartTime = sysTime
      currentStateTimer = 0
    if(sysTime == 0):
        return (CDH.CDH_Turn_ON)

    if(sysTime > 0):
        if(CDHMode == 'receive comms'):
            return(CDH.Turn_ON_Payload + CDH.Signal_ADCS + CDH.COMM_Periodic)
        if(CDHMode == 'receive payload'):
            return(CDH.Signal_COMMS + CDH.COMM_Periodic)
        if(CDHMode == 'Receive Latchup'):
            return(CDH.Turn_OFFON_MCU)

        else:
            return(CDH.COMM_Periodic)

    #return(COMM_Periodic)


def main():
    b=[]
    for sysTime in range(50):              #One Orbit
        setflags(sysTime)
        b.append(CDHPower(sysTime))
        print(b[sysTime])

    CDH_Total_Power = sum(b)
    print(CDH_Total_Power)             #Total Power






main()
