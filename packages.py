# add package searching directory

import sys
sys.path.append('test') # test is the directory name relative to current directory

# through command line 
# export PYTHONPATH=test # test --> directory 

# to create a package
# create __init__.py file in the root folder location 

# see __init__.py, where code is written so that reader.Reader() can be used directly 

# to create test.gz 
# python3 -m reader.compressed.gzipped test.gz data compressed with gzip

# when __main__.py is created that directory acts as executable directory
# python3 reader test.gz

# can create zip of the folder reader and python can execute code inside zip files 
# to create zip file : zip -r ../reader.zip * 
# to execute : python3 reader.zip test.gz 


