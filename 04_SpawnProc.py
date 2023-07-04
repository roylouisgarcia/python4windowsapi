#!/usr/bin/env python

"""
This script uses the Windows API calls to create a new process and its primary thread. Also, the new process runs in the security context of the calling process.
"""
import ctypes
from ctypes.wintypes import HANDLE,DWORD,LPWSTR,WORD,LPBYTE

k_handle = ctypes.WinDLL("Kernel32.dll")

__author__ = "Roy Louis Garcia"
__copyright__ = "2023, 04_SpawnProc" 
__date__ = "2023-07-04 04:03:28"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roy Louis Garcia"

# Structure for Startup Info
class STARTUPINFO(ctypes.Structure):
 _fields_ = [
   ("cb", DWORD),
   ("lpReserved", LPWSTR),
   ("lpDesktop", LPWSTR),
   ("lpTitle", LPWSTR),
   ("dwX", DWORD),
   ("dwY", DWORD),
   ("dwXSize", DWORD),
   ("dwYSize", DWORD),
   ("dwXCountChars", DWORD),
   ("dwYCountChars", DWORD),
   ("dwFillAttribute", DWORD),
   ("dwFlags", DWORD),
   ("wShowWindow", WORD),
   ("cbReserved2", WORD),
   ("lpReserved2", LPBYTE),
   ("hStdInput", HANDLE),
   ("hStdOutput", HANDLE),
   ("hStdError", HANDLE),
 ]

# Structure for Process Info
class PROCESS_INFORMATION(ctypes.Structure):
 _fields_ = [
   ("hProcess", HANDLE),
   ("hThread", HANDLE),
   ("dwProcessId", DWORD),
   ("dwThreadId", DWORD),
 ]


def main():
  # Setting up the parameters
  lpApplicationName = "C:\\Windows\\System32\\calc.exe" # to spawn the calculator app
  lpCommandLine = None
  lpProcessAttributes = None
  lpThreatAttributes = None
  lpEnvironment = None
  lpCurrentDirectory = None

  dwCreationFlags = 0x00000010

  bInheritHandle = False

  lpProcessInformation = PROCESS_INFORMATION()

  lpStartupInfo = STARTUPINFO()

  lpStartupInfo.wShowWindow = 0x1

  lpStartupInfo.dwFlags = 0x1

  response = k_handle.CreateProcessW(
    lpApplicationName,
    lpCommandLine,
    lpProcessAttributes,
    lpThreatAttributes,
    bInheritHandle,
    dwCreationFlags,
    lpEnvironment,
    lpCurrentDirectory,
    ctypes.byref(lpStartupInfo),
    ctypes.byref(lpProcessInformation))
  
  # Error checking for the CreateProcessW Windows API call
  if response > 0:
    print("Proc is Running")
  else:
    print("Failed. Error Code: {0}".format(k_handle.GetLastError()))





if __name__ == "__main__":
  main()
