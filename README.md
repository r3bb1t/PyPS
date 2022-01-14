# PyPS
Simple wrapper around System.Management.Automation.dll for python.

# Example Usage:

<pre>
import PyPS
print(run_ps_inline("get-process | select-object -property name"))  # prints output of "get-process | select-object -property name" powershell command
</pre>


P.s. This script requires pythonnet module to be installed. You can install it by typing:

pip install pythonnet

or 

pip install --pre pythonnet
