#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nostradmsx
# @Date: 2023-07-02 22:58:16
import ctypes

def main():
  # Setting up the handles
  k_handle = ctypes.WinDLL("Kernel32.dll")
  
  # Setting up all access security rights
  PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF) 

  # Setting up all the Parameters Needed for Windows API call OpenProcess()
  dwDesiredAccess = PROCESS_ALL_ACCESS
  bInheritHandle = False
  dwProcessId = 0x1EE4 # Hardcoded the hex of arbitrary PID seen from process list on "Task Manager"

  # The Sucess of calling this depends on the process choice and if called from an Admin privileged window or not
  response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

  # Error Handling
  error = k_handle.GetLastError()
  if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)
  else:
    print(response)



if __name__ == "__main__":
  main()
