#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[37]:





# In[54]:


def relay_on(board, channel):
    if channel<10:
        ch=str(channel)
    else:
        ch=channel_conversion[channel]    
    
    cmd='relay on ' + ch + '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd


# In[62]:


def relay_off(board, channel):
    if channel<10:
        ch=str(channel)
    else:
        ch=channel_conversion[channel]     
    cmd='relay off ' + ch + '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd


# In[63]:


# def relay_on(board, channel=16):
#     cmd='relay on ' + str(channel)+ '\n\r'
#     command=bytes(cmd.encode())
#     board.write(command)    
#     return cmd


# In[64]:


def all_channel_off(board, total_channel=16):
        for i in range(total_channel):            
            relay_off(board, i)
            time.sleep(0.2)


# In[65]:


def all_channel_on(board, total_channel=16):
        for i in range(total_channel):
            relay_on(board, i)
            time.sleep(0.2)


# In[68]:


all_channel_off(numato1)


# In[67]:


all_channel_on(numato1)


# In[53]:


relay_on(numato1,11)


# In[52]:


relay_off(numato1,1)


# In[47]:


relay_on(numato1,5)


# In[48]:


relay_off(numato1,5)


# In[18]:





# In[1]:


print (numato1.isOpen())


# In[2]:


numato1.close()


# In[ ]:




