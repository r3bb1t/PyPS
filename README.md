# PyPS
Simple wrapper around System.Management.Automation.dll for python.

## Example Usage:
The following code prints the output of "get-process | select-object -property name" powershell command

<pre>
from PyPS import run_ps_inline
print(run_ps_inline("get-process | select-object -property name"))
</pre>


P.s. This script requires pythonnet module to be installed. You can install it by typing:

pip install pythonnet

or 

pip install --pre pythonnet
