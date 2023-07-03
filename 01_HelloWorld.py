#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nostradmsx
# @Date: 2023-07-02 17:55:03
import ctypes

def main():
  user_handle = ctypes.WinDLL("User32.dll") # Handle to User32.dll
  k_handle = ctypes.WinDLL("Kernel32.dll")  # Handle to Kernel32.dll

  hWnd = None # Not Used
  lpText = "Hello Roy" # Parameter for whatever text will show up on the body of message
  lpCaption = "Hello World!" # Parameter for whatever text will show up on the title bar of message
  uType = 0x00000001 # This ANSI code controls what buttons will show up on the message box


  response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)
  error = k_handle.GetLastError()

  if error !=0:
    print("Error Code: {0}".format(error))
    exit(1)
  
  if response == 1:
    print("User clicked OK!")
  elif response == 2:
    print("User clicked CANCEL!")

if __name__ == "__main__":
  main()
