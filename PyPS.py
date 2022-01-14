import clr
import sys
import os


SMA_Dir = (lambda s : s + os.listdir(s)[0])(r'C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Management.Automation\\')
sys.path.append(SMA_Dir)
clr.AddReference("System.Management.Automation")
clr.AddReference('System.Collections')
clr.AddReference('System.Management')

from System.Collections.ObjectModel import *
from System.Management.Automation import *
from System.Management.Automation.Runspaces import *
from System.Text import *





def run_ps_inline(cmd):
    runspace = RunspaceFactory.CreateRunspace()
    runspace.Open()
    scriptInvoker = RunspaceInvoke(runspace)

    pipeline = runspace.CreatePipeline()
    pipeline.Commands.AddScript(cmd)
    pipeline.Commands.Add("Out-String")


    result = pipeline.Invoke()
    runspace.Close()


    stringBuilder =  StringBuilder()


    for each in result:
        stringBuilder.Append(each)


    return stringBuilder.ToString()


cmd = "get-process | select-object -property name"


result = run_ps_inline(cmd)  # Enter your command here

print(result)