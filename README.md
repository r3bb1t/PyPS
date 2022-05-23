# PyPS
Simple wrapper around the System.Management.Automation.dll for python. 

## Example Usage:
The following code prints the output of "get-process | select-object -property name" powershell command without leaving traces in the log files. (Optional)

<pre>
from PyPS import PyPs
PyPs(True).run_ps('get-process | select-object -property name')
</pre>


P.s. This script requires pythonnet module to be installed. You can install it by typing:

pip install pythonnet

or 

pip install --pre pythonnet
