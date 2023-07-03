# Python and Windows API 
This is a repository of Python scripts that interacts with the Windows API. 

------

### **Script** 01_HelloWorld.py 

**Description:**  A traditional HelloWorld script that explores the concept of Windows DLL, handles and the necessary parameters to call the Windows API call MessageBoxW().

**The Code:**

![Python Code for HelloWorld.py](./images/00_helloworld_code.png)

**Windows API Documentation Link**: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw

**Windows API Documentation Excerpt:**

<img src="./images/00_api_doc.png" alt="Screenshot of Windows API call MessageBoxW" style="zoom:200%;" />

**Results:**

![Windows Message Box](./images/00_ss_helloworld.png)

------

## **Script:** 03_ProcessKiller.py

**Description:** A script that uses the Windows API calls or systems calls via Python Script that in order to kill any Windows Process

**The Code:**

*Initialization and User Input:*

![The part of the code that asks the user what process to kill](./images/01_project_ss.png)



***FindWindowA*** *(code and documentation)*

![FindWindowA Code](./images/02_project_ss.png)

![FindWindowA Documentation](./images/01_api_doc.png)

**Windows API Documentation Link**: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindowa

***GetWindowThreadProcessId*** *(Code and Documentation)*

![GetWindowThreadProcessId Code](./images/03_project_ss.png)

![GetWindowThreadProcessId Documentation](./images/02_api_doc.png)



**Windows API Documentation Link**: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid

***OpenProcess*** *(code and documentation)*

![OpenProcess Code](./images/04_project_ss.png)

![OpenProcess Documentation](./images/03_api_doc.png)

**Windows API Documentation Link**: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess

***TerminateProcess*** *(Code and Documentation)*

![TerminateProcess Code](./images/05_project_ss.png)

![TerminateProcess Documentation](./images/04_api_doc.png)

**Windows API Documentation Link**: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess
