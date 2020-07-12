#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:26:00 2019
@institute: Centro de Investigaciones en \'Optica A.C.
@group: Applied Sceince THz Group
@author: Jorge Ludwig Regalado de la Rosa
"""
import serial#, time
#Function to ask something to SR830 Lock-In Amplifier==========================
def ask_device(cmd):
    try:
        lok = serial.Serial("/dev/ttyUSB0", 9600, 8, 'N', 1, timeout=0.1)
    except:
        print("Error opening Lock-In port. Quitting.")
    lok.write(cmd.encode())
    lok.flush()
    ret = lok.readline()
    lok.close()
    return str(ret,'utf-8')#This line gets ret from binary to utf-8 encoding
#Function to set something in SR830 Lock-In Amplifier==========================
def set_device(cmd):
    try:
        lok = serial.Serial("/dev/ttyUSB0", 9600, 8, 'N', 1, timeout=0.1)
    except:
        print("Error opening Lock-In port. Quitting.")
    lok.write(cmd.encode())
    lok.flush()
    lok.close()
#    return
#==============================================================================
#Defining functions for queryng SR830 Lock-In Amplifier's settings=============
#==============================================================================

#Reference and phase queries (page 5-4)----------------------------------------
def get_phas():#Queries the reference phase shift
    return ask_device('PHAS?\n')[:-1]
def get_ref_source():#Queries the reference source.
    return ask_device('FMOD?\n')[:-1]
def get_freq():#Queries the reference frequency.
    return ask_device('FREQ?\n')[:-1]
def get_trigshape():#Queries the reference trigger when using the external reference mode.
    return ask_device('RSLP?\n')[:-1]
def get_harm():#Queries the detection harmonic.
    return ask_device('HARM?\n')[:-1]
def get_ampl():#Queries the amplitude of the sine amplitude.
    return ask_device('SLVL?\n')[:-1]
#Input and filter queries(page5-5)---------------------------------------------
def get_input():#Queries the input configuration.
    return ask_device('ISRC?\n')[:-1]
def get_ground():#Queries the input shield grounding.
    return ask_device('IGND?\n')[:-1]
def get_couple():#Queries the input coupling.
    return ask_device('ICPL?\n')[:-1]
def get_filter():#Queries the input line notch filter status.
    return ask_device('ILIN?\n')[:-1]
#Gain and time constant queries (page 5-6)-------------------------------------
def get_sens():#Queries the sensitivity
    return ask_device('SENS?\n')[:-1]
def get_reserve():#Queries the reserve mode.
    return ask_device('RMOD?\n')[:-1]
def get_tau():#Queries the time constant.
    return ask_device('OFLT?\n')[:-1]
def get_slope():#Queries the low pass filter slope.
    return ask_device('OFSL?\n')[:-1]
def get_sync():#Queries the synchronous filter status.
    return ask_device('SYNC?\n')[:-1]
#Display and output queries (page 5-8)-----------------------------------------
def get_disp_rate(i):#Selects the CH1 or CH2 displays.
    int(i)
    if i == 1 or i == 2:
        reply = ask_device('DDEF? '+str(i)+'\n')
    else:
        reply = print("Invalid channel, select 1 or 2")
    return reply[:-1]
def get_fpop():#Queries the front panel output sources.
    return ask_device('FPOP?\n')
def get_exp_off(i):#Queries the output offsets and expands.
    int (i)[:-1]
    if i == 1 or i == 2:
        reply = ask_device('OEXP? '+str(i)+'\n')
    else:
        reply = print("Invalid channel, select 1 or 2")
    return reply[:-1]
#AUX input and outputs queries (page 5-9)--------------------------------------
def get_aux_inp(i):#Queries the Aux input values of 1,2,3 or 4 channel.
    int(i)
    if i == 1 or i == 2 or i == 3 or i == 4:
        reply = ask_device('OAUX? '+str(i)+'\n')
    else:
        reply = print("Invalid channel, select 1, 2,3 or 4")
    return reply[:-1]
def get_auxv(i):#Queries the Aux output voltage of 1,2,3 or 4 channel.
    int(i)
    if i == 1 or i == 2 or i == 3 or i == 4:
        reply = ask_device('AUXV? '+str(i)+'\n')
    else:
        reply = print("Invalid channel, select 1, 2,3 or 4")
    return reply[:-1]
#Setup queries (page5-10)------------------------------------------------------
def get_outx():#Queries the status of output interface.
    return ask_device('OUTX?\n')[:-1]
def get_kclk():#Queries the status of the key click.
    return ask_device('KCLK?\n')[:-1]
def get_alrm():#Queries the status of the alarm.
    return ask_device('ALRM?\n')[:-1]
#Data storage queries (page 5-13)----------------------------------------------
def get_sam_rate():#Queries the sample rate.
    return ask_device('SRAT?\n')[:-1]
def get_send():#Queries the end of bufer mode.
    return ask_device('SEND?\n')[:-1]
def get_trig():#Queries the trigger start mode.
    return ask_device('TSTR?\n')[:-1]
#Data storage settings (page 5-13)---------------------------------------------
def set_sam_rate(i):#Sets the data sample rate
    str(i)
    rates = {'62.5 mHz' : '0',
             '125 mHz'  : '1',
             '250 mHz'  : '2',
             '500 mHz'  : '3',
             '1 Hz'     : '4',
             '2 Hz'     : '5',
             '4 Hz'     : '6',
             '8 Hz'     : '7',
             '16 Hz'    : '8',
             '32 Hz'    : '9',
             '64 Hz'    : '10',
             '128 Hz'   : '11',
             '256 Hz'   : '12',
             '512 Hz'   : '13',
             'Trigger'  : '14'
             }
    if i in rates:
        set_device('SRAT '+rates[i]+'\n')
        print('Sample rate selected: '+rates[i])
    else:
        print('Invalid entry.')
def set_send(i):#Sets the end of buffer mode.
    modes = {0 : 'Shot',
             1 : 'Loop'}
    int(i)
    if i in modes:
        set_device('SEND '+str(i)+'\n')
        print(modes[i]+' mode selected.')
def trig():#Trigger command.
    set_device('TRIG\n')
def set_trig(i):#Sets the trigger start mode.
    int(i)
    modes = {0 : 'Trigger start status: OFF.',
             1 : 'Trigger start status: ON.'}
    if i in modes:
        set_device('TSTR '+str(i)+'\n')
        print(modes[i])
def set_strt():#Starts or resumes data storage.
    set_device('STRT\n')
def pause():#Pauses data storage.
    set_device('PAUS\n')
def reset_buffer():#Resets data buffer.
    set_device('REST\n')
#==============================================================================
#Defining functions for setting SR830 Lock-In Amplifier's settings=============
#==============================================================================
    
#Reference and phase commands (page 5-4)---------------------------------------
def set_phas(phi):#Sets the phase shift.
    if phi > -360.00 and phi <729.99:
        reply = set_device('FREQ'+str(phi)+'\n')
    else:
        reply = 'Phase may be programmed from -360.00 to 729.99'
    return reply
def set_fmod(i):#Sets the reference source.
    int(i)
    if i == 0 or i == 1:
        set_device('FMOD '+str(i)+'\n')
        if i == 0:
            reply = 'External reference.'
        else:
            reply = 'Internal source.'
    else:
        reply = 'Invalid entry, select 0 (external) or 1 (internal).'
    return reply
def set_freq(freq):#Sets the reference frequency if the source is internal.
    i = get_ref_source()
    if i == '1':
        if freq >= 0.001 and freq <= 102000:
            set_device('FREQ '+str(freq)+'\n')
            reply = 'Reference frequeny setted at '+str(freq)+' Hz.'
        else:
            reply = 'Frequency value must be 0.001 <= f <= 102000'
    else:
        reply = 'This command is allowed only if the reference source is internal.'
    return reply 

def set_trigshape(i):#Sets the reference trigger when using the external reference mode.
    int(i)
    if i == 0 or i == 1 or i == 2:
        set_device('RSLP'+str(i)+'\n')
def set_harm(i):#Sets the detection harmonic.
    int(i)
    if i in range(19999):
        set_device('HARM '+str(i)+'\n')
def set_ampl(i):#Sets the amplitude of the sine output.
    if i >= 0.004 and i <= 5.000:
        set_device('SLVL '+str(i)+'\n')
    else:
        print ('Invalid value.')
#Input and filter commands (page 5-5)------------------------------------------

def set_input(i):#Sets the input configuration.
    int(i)
    if i == 0 or i == 1 or i == 2 or i == 3:
        set_device('ISRC '+str(i)+'\n')
def set_ground(i):#Sets the input shield grounding.
    int(i)
    if i == 0 or i ==1:
        set_device('IGND '+str(i)+'\n')
def set_couple(i):#Sets the input coupling.
    int(i)
    if i == 0 or i == 1:
        set_device('ICPL '+str(i)+'\n')
def set_filter(i):#Sets the input line notch filter status.
    int(i)
    if i ==0 or i == 1 or i == 2 or i == 3:
        set_device('ILIN '+str(i)+'\n')
#Gain and time constants commands (page 5-6)-----------------------------------
def set_sens(i):#Sets the sensitivity.
    str(i)
    sensset={
                "2nV"   : '0',
                "5nV"   : '1',
                "10nV"  : '2',
                "20nV"  : '3',
                "50 nV" : '4',
                "100nV" : '5',
                "200nV" : '6',
                "500nV" : '7',
                "1muV"  : '8',
                "2muV"  : '9',
                "5muV"  : '10',
                "10muV" : '11',
                "20muV" : '12',
                "50muV" : '13',
                "100muV": '14',
                "200muV": '15',
                "500muV": '16',
                "1mV"   : '17',
                "2mV"   : '18',
                "5mV"   : '19',
                "10mV"  : '20',
                "20mV"  : '21',
                "50mV"  : '22',
                "100mV" : '23',
                "200mV" : '24',
                "500mV" : '25',
                "1V"    : '26'}
    if i in sensset:
        set_device('SENS '+sensset[i]+'\n')
def set_reserve(i):#Sets the reserve mode
    int(i)
    if i == 0 or i == 1 or i ==2:
        set_device('RMOD '+str(i)+'\n')
    else:
        print('Invalid entry.')
def set_tau(i):#Sets the time constant
    str(i)
    tauset={
                "10mus" : '0',
                "30mus" : '1',
                "100mus": '2',
                "300mus": '3',
                "1ms"   : '4',
                "3ms"   : '5',
                "10ms"  : '6',
                "30ms"  : '7',
                "100ms" : '8',
                "300ms" : '9',
                "1s"    : '10',
                "3s"    : '11',
                "10s"   : '12',
                "30s"   : '13',
                "100s"  : '14',
                "300s"  : '15',
                "1ks"   : '16',
                "3ks"   : '17',
                "10ks"  : '18',
                "30ks"  : '19'}
    if i in tauset:
        set_device('OFLT '+tauset[i]+'\n')
def set_slope(i):#Sets the low pass filter slope.
    int(i)
    if i == 0 or i == 1 or i == 2 or i ==2:
        set_device('OFSL '+str(i)+'\n')
def set_sync(i):#Sets the synchronous filter status.
    int(i)
    if i == 0 or i == 1:
        set_device('SYNC '+str(i)+'\n')
#Display and output commands (page 5-8)----------------------------------------
def set_disp_rate(i,j,k):#Sets the CH1 and CH2 displays.
    int(i)
    int(j)
    int(k)
    if i == 1 or i == 2 and j in range(5) and k in range(3):
        set_device('DDEF '+str(i)+', '+str(j)+', '+str(k)+'\n')
    else:
        print('Invalid entry.')
def set_fpop(i,j):#Sets the front panel output sources.
    int(i)
    int(j)
    if i == 1 or i == 2 and j == 0 or j == 1:
        set_device('FPOP '+str(i)+', '+str(j)+'\n')
    else:
        print('Invalid entry.')
def set_exp_off(i,x,j):#Sets the output offsets and expands.
    int(i)
    int(j)
    if i == 1 or i == 2 or i == 3 and j == 0 or j == 1 or j == 2 and x >= -105.00 and x<= 105.00:
        set_device('OEXP '+str(i)+', '+str(x)+', '+str(j)+'\n')
#AUX input and output commands (page 5-9)--------------------------------------
def set_aux_inp(i,x):#Sets the Aux input values.
    int(i)
    if i == 1 or i == 2 or i == 3 or i == 4 and x >= -10.500 and x< 10.500:
        set_device('AUXV '+str(i)++', '+str(x)+'\n')
#Setup commands (page 5-10)----------------------------------------------------
def set_outx(i):#Sets the output interface RS232 (i=0) or GPIB (i=1)
    int(i)
    if i == 0 or i ==1:
        set_device('OUTX'+str(i)+'\n')
    else:
        print('Invalid entry.')
def enable_front_panel():#Activates the front panel when GPIB remote is activated
    set_device('OVRM 0\n')
    print('GPIB remote activated, front panel activated.')
def disable_front_panel():#Deactivates the front panel when GPIB remote is activated
    set_device('OVRM 1\n')
    print('GPIB remote activated, front panel deactivated.')
def set_kclk(i):#Sets the key click on (i=1) or off (i=0) state.
    int(i)
    if i == 0:
        set_device('KCLK 0\n')
        print('Key click off.')
    elif i == 1:
        set_device('KCLK 1\n')
        print('Key click on.')
def save_set(i):#Saves the lock-in setup in buffer.
    int(i)
    buffer = [1,2,3,4,5,6,7,8,9]
    if i in buffer:
        set_device('SSET '+str(i)+'\n')
def call_set(i):#Recalls the lock-in setup from buffer.
    int(i)
    buffer = [1,2,3,4,5,6,7,8,9]
    if i in buffer:
        set_device('RSET '+str(i)+'\n')
#Auto functions (page 5-11)----------------------------------------------------
def auto_gain():#Performs the Auto Gain function.
    set_device('AGAN\n')
def auto_reserve():#Performs the Auto Reserve function.
    set_device('ARSV\n')
def auto_phas():#Performs tha Auto Phase command.
    set_device('APHS')
def auto_offset(i):#Automatically offsets X (i=1) Y (i=2) or R (i=3) to zero.
    int(i)
    values = {1:'X',2:'Y',3:'R'}
    if i in values:
        set_device('AOFF '+str(i)+'\n')
        print(values[i]+' offsetted to zero.')
        
#==============================================================================
#Defining functions to get data from SR830 Lock-In Amplifier's functions=======
#==============================================================================

#Data transfer commands (page 5-15)--------------------------------------------
def get_outp(i):#Reads the value of X(1), Y(2), R(3) and \theta(4)
    if i == 1 or i == 2 or i == 3 or i == 4:
        reply = ask_device('OUTP? '+str(i)+'\n')
    else:
        reply = print("Invalid option, select 1 (X), 2 (Y), 3(R) or 4 (angle)")
    return float(reply)
def get_outr(i):#Reads the value of X(1), Y(2), R(3) and \theta(4)
    if i == 1 or i == 2 or i == 3 or i == 4:
        reply = ask_device('OUTR? '+str(i)+'\n')
    else:
        reply = print("Invalid channel, select 1, 2")
    return float(reply)
def get_snap(i,j,k,l,m,n):#Records the values of either 2,3,4,5 or 6 at a single instant
    entry = [int(i),int(j),int(k),int(l),int(m),int(n)]
    invalid_chan = False
    channels = []
    for i in entry:#Looks for invalid channels
        if i > 11 or i < 0:
            invalid_chan = True
    if entry[0] == 0 or entry[1] == 0:#Returns channels 1-4 if first two entries are 0  
        reply = ask_device('SNAP?1,2,3,4\n')                      
    elif invalid_chan == True:#Forbids negative values
        reply = print("Invalid input, only channels from 1 to 11 are valid.")
    else:#Creates the querie avoiding the ceros if there was
        for i in entry:
            if i != 0:
                channels.append(str(i))
        cmd = ','.join(channels)
        reply = ask_device('SNAP?'+cmd+'\n')    
    return list(map(float,reply[:-1].split(',',6)))
def get_spts():#Queries the number of points stored in the buffer (page 5-16)
    return ask_device('SPTS?\n')
#Interface comands (page 5-19)-------------------------------------------------
def reset():#Resets the SR830 to its default configurations.
    return set_device('*RST\n')
def get_idn():#Queries the SR830's device identification string.
    return ask_device('*IDN?\n')
def set_locl(i):#Sets the local/remote function.
    int(i)
    if i == 0 or i == 1 or i== 2:
        reply = set_device('LOCL?'+str(i))
    else:
        reply = 'Invalid entry, only 1,2 or 3 are valid'
    return reply
#out = get_idn()
#print(out)