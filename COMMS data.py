# Units are in milliWatt
# Time is in seconds

COMMS_transmit = 0
COMMS_sleep = 1
COMMS_idle = 0
state_timer = 0

hours = 60 * 60

# Idle waiting for
idle_state = 1
idle_power_max = 540
idle_power_typical = 298
idle_time = 90 * 60 - 90  # For all time except for 90s transmission

# Sleep during launch
sleep_time = 60 * 30  # 30 minutes
sleep_power = 0
sleep_out_time = 60  # assumed

# Transmit Picture
transmit_time = 90
transmit_power = 3410  # Max and typical are similar values

def commsPower():

    global COMMS_transmit
    global COMMS_sleep
    global COMMS_idle

    if COMMS_transmit:
        return transmit_power

    elif COMMS_sleep:
        return sleep_power

    elif COMMS_idle:
        return idle_power_typical

def resetFlag():

    global COMMS_transmit
    global COMMS_sleep
    global COMMS_idle
    global state_timer

    state_timer += 1

    if (COMMS_sleep == 1 and state_timer >= sleep_out_time):
        COMMS_sleep = 0
        COMMS_idle = 1
        state_timer = 0
        return

    elif(COMMS_transmit == 1 and state_timer >=transmit_time):
        COMMS_transmit = 0
        COMMS_idle = 1
        state_timer = 0
        return
