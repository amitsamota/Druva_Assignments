Whenever a Python script is executed, the byte code is generated in memory and simply discarded when program exits.
But, if a Python module is imported, a .pyc file for the module is generated which contains its Byte code.
Thus, when the module is imported next time, the byte code from .pyc file is used, hence skipping the compilation 
step!

source code --> interpreter --> running code

source code -->Compiler --> byte code -->Python Virtual Machine(contains libraray modules) -->  Running Code