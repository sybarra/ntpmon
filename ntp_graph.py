# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:29:02 2015

@author: sybarra
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def ParseCommand():
    parser = argparse.ArgumentParser('Python tool to graph ntpq output .. ntpGraph.py')
    parser.add_argument('-f', '--fileName',
                        help='Specify the input file(s). Enter multiple files separated by space',
                        nargs='+')

    global gbl_args
    global gbl_fileName
    gbl_args = parser.parse_args()
    

def GetHeaders(infile):
    for line in infile:
        if 'remote' in line:
            header = line.split()
            break
    return(header)


def NtpqParse(infile):
    #Return a list of tuples containing the NTPq output
    statList = []
    headers = GetHeaders(infile)
    statList.append(tuple(headers))
    for line in infile:
        if  '*' in line: #only looking for the active NTP source
            ntpVal = line.split()
            statList.append(tuple(ntpVal))
    return(statList)


def ArrayFromList(inList):
    #Create an array from the parsed NTPq ouput
    dataArray = np.asarray(inList)
    return(dataArray)


def GraphNtpq(dataArray,svr):
    #Create plots
    fig = plt.figure(figsize=(9,5))

    #Delay
    ax1 = fig.add_subplot(311)
    ax1.set_title(svr + ' NTP Delay')
    delay = data[1:,7]
    ax1.plot(delay)

    #Offset
    ax2 = fig.add_subplot(312)
    ax2.set_title(svr + ' NTP Offset')
    offset = data[1:,8]
    ax2.plot(offset)

    #Jitter
    ax3 = fig.add_subplot(313)
    ax3.set_title(svr + ' NTP Jitter')
    jitter = data[1:,9]
    ax3.plot(jitter)

    plt.tight_layout()
    pp.savefig()


if __name__ in '__main__':
    ParseCommand()
    pp = PdfPages('NTPGraphs.pdf')
    for fileName in gbl_args.fileName:
        infile = open(fileName,'r')
        inList = NtpqParse(infile)
        data = ArrayFromList(inList)
        GraphNtpq(data, fileName)
        plt.show()

    pp.close()


