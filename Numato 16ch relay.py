#!/usr/bin/env python
# coding: utf-8

# In[73]:


import sys
import serial

#Relay  Find serial port number (eg. COOM5) in Device Manager for Windows
numato1= serial.Serial("COM5", 9600)

if not numato1.isOpen():
    print ('Numator board not communicating....')


# In[74]:


def relay_off(board, channel):
    cmd='relay off ' + str(channel)+ '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd


# In[75]:


def relay_on(board, channel):
    cmd='relay on ' + str(channel)+ '\n\r'
    command=bytes(cmd.encode())
    board.write(command)    
    return cmd


# In[79]:


relay_on(numato1,1)


# In[80]:


relay_off(numato1,1)


# In[81]:


relay_on(numato1,1)


# In[82]:


relay_off(numato1,1)


# In[50]:





# In[68]:





# In[72]:


numato1.close()


# In[ ]:




