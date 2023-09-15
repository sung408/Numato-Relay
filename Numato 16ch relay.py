import sys
import serial
import time

channel_conversion={10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

#Relay  Find serial port number (eg. COOM5) in Device Manager for Windows
numato1= serial.Serial("COM5", 9600)
if not numato1.isOpen():    
    print ('Numator board not communicating....')
else:
    print ('connected')

def relay_on(board, channel):
    if channel<10:
        ch=str(channel)
    else:
        ch=channel_conversion[channel]    
    
    cmd='relay on ' + ch + '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd

def relay_off(board, channel):
    if channel<10:
        ch=str(channel)
    else:
        ch=channel_conversion[channel]     
    cmd='relay off ' + ch + '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd


def all_channel_off(board, total_channel=16):
        for i in range(total_channel):            
            relay_off(board, i)
            time.sleep(0.2)



def all_channel_off(board, total_channel=16):
        for i in range(total_channel):            
            relay_off(board, i)
            time.sleep(0.2)



relay_on(numato1,11)
relay_off(numato1,11)

all_channel_on(numato1)
all_channel_off(numato1)



