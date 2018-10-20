#PowerRanks(mW) = Current(mA) * Voltage(V)
Voltage = 3.3
PR_1_Max = 840 * Voltage
PR_1_Typical = 400 * Voltage
PR_2_Max = 420 * Voltage
PR_2_Typical = 200 * Voltage
PR_3_Typical = 0.004 * Voltage

#Sleep
Sleep= 0

#After launch Turn on CDH
CDH_Turn_ON = 5                     #Assumed Value
CDH_Turn_ON_Duration = 1            #Assumed Value, 1 sec to turn on

#Periodic Communicaton With Other Sybsystems
COMM_Periodic= 0.00264              #[(4uA/5sec) * 3.3V ] -> Always On
COMM_Periodic_Duration = 5400       # Duration of 1 orbit

#Receiving Commands from Comms

#Recieve_COMM = 1                   #Assumed Value
#Recieve_COMM_Duration = 1          #Assumed Value
Turn_ON_Payload = PR_2_Typical
Turn_ON_Payload_Duration = 30        #Assumed Value

#Signal ADCS
Signal_ADCS = PR_2_Typical
Signal_ADCS_Duration = 30            #Assumed Value

#Signal COMMS to send Picture
Signal_COMMS = PR_2_Typical
Signal_COMMS_Duration = 30           #Assumed Value

#LATCH -> Turn Off then turn ON MCU
Turn_OFFON_MCU = 10                 #Assumed Value
Turn_OFFON_MCU_Duration = 2         #Assumed Value

#IF 1 MCU Dies, all power values 2/3

#MCs are put into low power Mode
MC_Low_Power_Mode = PR_3_Typical
