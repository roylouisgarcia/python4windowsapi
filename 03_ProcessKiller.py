#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nostradmsx
# @Date: 2023-07-03 04:44:03
import ctypes

def main():
  k_handle = ctypes.WinDLL("Kernel32.dll") # Handle to Kernel.dll
  u_handle = ctypes.WinDLL("User32.dll") # Handle to User32.dll

  # Setting up all the Parameters Needed for Windows API call OpenProcess()
  PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF) 

  # Taking user input to grab the window name as a pointer and encoded for ANSI
  lpWindowName = ctypes.c_char_p(input("Enter Window Name To Kill: ").encode('utf-8'))
  
  # ------ FindWindowA -----------
  # Calling the FindWindowA to get the handle of the processes to be killed
  hWnd = u_handle.FindWindowA(None, lpWindowName)
  
  # Error Handling for FindWindowA
  if hWnd == 0:
    print("Error code: {0}. Did not get the handle".format(k_handle.GetLastError()))
    exit(1)
  else:
    print("Got Handle {0}".format(lpWindowName))

  # ------ GetWindowThreadProcessId -----------

  # DWORD = ctypes.c_ulong
  lpdwProcessId = ctypes.c_ulong()

  # Passing the above DWORD by reference into the API call GetWindowThreadId
  response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))
  
  # Error Handling for GetWindowThreadProcessId
  if response == 0:
    print("Error code: {0}. Didn't get the PID".format(k_handle.GetLastError()))
    exit(1)
  else:
    print("Got the PID {0}".format(response))

  # ------ OpenProcess -----------

  # Setting up the parameter for OpenProcess Windows API call
  dwDesiredAccess = PROCESS_ALL_ACCESS
  bInheritHandle = False
  dwProcessId = lpdwProcessId

  hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
  
  # Error Handling for OpenProcess
  if hProcess == 0:
    print("Error code: {0} - Could Not Grab Priv Handle".format(k_handle.GetLastError()))
    exit(1)
  else:
    print("Got the Handle {0}".format(response))



  # ------ TerminateProcess -----------

  # Setting up the parameter for TerminateProcess Windows API call
  uExitCode = 0x1

  response = k_handle.TerminateProcess(hProcess, uExitCode)

  # Error Handling for TerminateProcess
  if response == 0:
    print("Error code: {0} - Could Not Terminate Process".format(k_handle.GetLastError()))
    exit(1)
  else:
    print("Process ended.")


if __name__ == "__main__":
  main()
  
