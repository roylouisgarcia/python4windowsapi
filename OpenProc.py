#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nostradmsx
# @Date: 2023-07-02 22:58:16
import ctypes

def main():
  k_handle = ctypes.WinDLL("Kernel32.dll")
  #PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF) 
  PROCESS_ALL_ACCESS = ( 0x0080 ) 

  dwDesiredAccess = PROCESS_ALL_ACCESS
  bInheritHandle = False
  dwProcessId = 0x1EE4


  response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

  error = k_handle.GetLastError()

  print(response)

  if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)



if __name__ == "__main__":
  main()
