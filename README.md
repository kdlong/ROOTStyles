Some styles for ROOT

To use a style from this package at login, 
 add to your `.rootlogon.py`
 
```python
import os,sys
import ROOT
sys.path.append(os.path.expanduser('~'))
from ROOTStyles import tdrStyle
ROOT.gROOT.SetStyle("tdrStyle")
```
