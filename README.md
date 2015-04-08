Some styles for ROOT
Uses [dotroot](https://github.com/nsmith-/.root)

To use a style from this package at login, 
 add to your `.rootlogon.C`, after dotroot:
```cpp
dotrootImport("nsmith-/ROOTStyles");
gROOT->SetStyle("tdrStyle");
```
