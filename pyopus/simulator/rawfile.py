"""
**SPICE OPUS raw file input/output**

SPICE OPUS results are stored in raw files. Every raw file can contain multiple 
plots. 

A **plot** is a group of vectors (arrays). Every plot has a title, a date, and 
a plot name associated with it. The vectors in a plot need not be of the same 
size or shape. Generally they are of the same shape and one of them is a 
so-called default scale. 

The **default scale** vector is the one that goes on the x-axis of plots. All 
other vectors represent y-axis values corresponding to various simulation 
results. 

Sometimes a vector in a plot has a different scale than the one given by the 
default scale vector. In that case the scale is also a vector in the same plot. 
Which vector is the (non-default) scale of a given vector is specified by a 
separate scales dictionary. 
"""
import _rawfile
from numpy import array
from time import strftime

__all__ = [ 'raw_read', 'raw_write' ]

def raw_write(filename, vectors, defaultScale='', scales={},  
				title='Untitled', date=None, plotName='unknown', 
				binary=True, append=False, padding=True, precision=15, debug=0):
	"""
	Writes a plot to a file named *filename*. If *append* is ``true`` the plot 
	is appended at the end of the file (makes it possible to store multiple 
	plots in a single file). 
	
	If *binary* is ``True`` the data are stored in binary format. Otherwise the 
	format is ASCII. 
	
	If *padding* is ``True`` the output is padded with zeros for arrays that 
	are shorter than the longest array in the plot. 
	
	*precision* specifies the number of significant digits to store if the 
	format is ASCII. 
	
	The vectors are specified in the *vectors* dictionary with vector name for 
	key. 
	
	*defaultScale* is the name of the defautl scale vector. 
	
	Vectors using a non-default scale are listed in the *scales* dictionary. 
	The vector name is the key while the scale name is the value. 
	
	*title*, *date*, and *plotName* are strings that specify the title, the 
	date, and the name of the plot. 
	
	Returns 0 on error. A nonzero value is returned if everything is OK. 
	"""
	if date is None:
		date=strftime('%a %b %d %H:%M:%S %Y')
	return _rawfile.raw_write(filename, vectors, defaultScale, scales, 
								title, date, plotName, 
								binary, append, padding, precision, debug)

def raw_read(filename, debug=0):
	"""
	Returns a list of tuples, where one tuple represents one plot obtained from 
	the raw file with *filename* for name. Every tuple consists of the 
	following members:
	
	0. a dictionary of vectors (arrays) with vector name for key
	1. the name of the default scale vector
	2. a dictionary specifying scales for vectors using a non-default scale. 
	   Keys are vector names while values are the names of non-default scale 
	   vectors
	3. a string with the title of the plot
	4. a string with the date of the plot
	5. a string with the name of the plot
	
	Automatically detects the format of the file (ASCII/binary). 
	
	Returns ``None`` if an error occurs during reading. 
	"""
	return _rawfile.raw_read(filename, debug)
