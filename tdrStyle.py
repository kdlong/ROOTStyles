import ROOT
"""
tdrStyle
 Taken from https:#ghm.web.cern.ch/ghm/plots/MacroExample/tdrstyle.C
 and modified a bit.  Additions:
  - Legend formatting
  - Color and Style name constants instead of numbers
 
"""
tdrStyle = ROOT.TStyle("tdrStyle","Style for P-TDR")

# For the canvas:
tdrStyle.SetCanvasBorderMode(0)
tdrStyle.SetCanvasColor(ROOT.kWhite)
tdrStyle.SetCanvasDefH(600) #Height of canvas
tdrStyle.SetCanvasDefW(600) #Width of canvas
tdrStyle.SetCanvasDefX(0)   #POsition on screen
tdrStyle.SetCanvasDefY(0)

# For the Pad:
tdrStyle.SetPadBorderMode(0)
# tdrStyle.SetPadBorderSize(1)
tdrStyle.SetPadColor(ROOT.kWhite)
tdrStyle.SetPadGridX(False)
tdrStyle.SetPadGridY(False)
tdrStyle.SetGridColor(0)
tdrStyle.SetGridStyle(3)
tdrStyle.SetGridWidth(1)

# For the frame:
tdrStyle.SetFrameBorderMode(0)
tdrStyle.SetFrameBorderSize(1)
tdrStyle.SetFrameFillColor(ROOT.kWhite)
tdrStyle.SetFrameFillStyle(0)
tdrStyle.SetFrameLineColor(1)
tdrStyle.SetFrameLineStyle(1)
tdrStyle.SetFrameLineWidth(1)

# For the histo:
# tdrStyle.SetHistFillColor(1)
# tdrStyle.SetHistFillStyle(0)
tdrStyle.SetHistLineColor(1)
tdrStyle.SetHistLineStyle(0)
tdrStyle.SetHistLineWidth(1)
# tdrStyle.SetLegoInnerR(0.5)
# tdrStyle.SetNumberContours(20)

tdrStyle.SetEndErrorSize(2)
# tdrStyle.SetErrorMarker(20)
#tdrStyle.SetErrorX(0.)

tdrStyle.SetMarkerStyle(20)

#For the fit/function:
tdrStyle.SetOptFit(1)
tdrStyle.SetFitFormat("5.4g")
tdrStyle.SetFuncColor(2)
tdrStyle.SetFuncStyle(1)
tdrStyle.SetFuncWidth(1)

#For the date:
tdrStyle.SetOptDate(1)
tdrStyle.GetAttDate().SetTextFont(42)
tdrStyle.GetAttDate().SetTextColor(ROOT.kGray)
# tdrStyle.SetDateX(0.01)
# tdrStyle.SetDateY(0.01)

# For the statistics box:
tdrStyle.SetOptFile(0)
tdrStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
tdrStyle.SetStatColor(ROOT.kWhite)
tdrStyle.SetStatFont(42)
tdrStyle.SetStatFontSize(0.025)
tdrStyle.SetStatTextColor(1)
tdrStyle.SetStatFormat("6.4g")
tdrStyle.SetStatBorderSize(1)
tdrStyle.SetStatH(0.1)
tdrStyle.SetStatW(0.15)
# tdrStyle.SetStatStyle(1001)
# tdrStyle.SetStatX(0)
# tdrStyle.SetStatY(0)

# Margins:
tdrStyle.SetPadTopMargin(0.05)
tdrStyle.SetPadBottomMargin(0.13)
tdrStyle.SetPadLeftMargin(0.14)
tdrStyle.SetPadRightMargin(0.04)

# For the Global title:
tdrStyle.SetOptTitle(0)
tdrStyle.SetTitleFont(42)
tdrStyle.SetTitleColor(1)
tdrStyle.SetTitleTextColor(1)
tdrStyle.SetTitleFillColor(ROOT.kWhite)
tdrStyle.SetTitleFontSize(0.05)
# tdrStyle.SetTitleH(0) # Set the height of the title box
# tdrStyle.SetTitleW(0) # Set the width of the title box
# tdrStyle.SetTitleX(0) # Set the position of the title box
# tdrStyle.SetTitleY(0.985) # Set the position of the title box
# tdrStyle.SetTitleStyle(1001)
# tdrStyle.SetTitleBorderSize(2)

# For the axis titles:
tdrStyle.SetTitleColor(1, "XYZ")
tdrStyle.SetTitleFont(42, "XYZ")
tdrStyle.SetTitleSize(0.05, "XYZ")
# tdrStyle.SetTitleXSize(0.02) # Another way to set the size?
# tdrStyle.SetTitleYSize(0.02)
tdrStyle.SetTitleXOffset(0.9)
tdrStyle.SetTitleYOffset(1.25)
# tdrStyle.SetTitleOffset(1.1, "Y") # Another way to set the Offset

# For the legends:
tdrStyle.SetLegendFont(42)
tdrStyle.SetLegendBorderSize(0)
tdrStyle.SetLegendFillColor(ROOT.kWhite)

# For the axis labels:
tdrStyle.SetLabelColor(1, "XYZ")
tdrStyle.SetLabelFont(42, "XYZ")
tdrStyle.SetLabelOffset(0.007, "XYZ")
tdrStyle.SetLabelSize(0.03, "XYZ")

# For the axis:
tdrStyle.SetAxisColor(1, "XYZ")
tdrStyle.SetStripDecimals(True)
tdrStyle.SetTickLength(0.03, "XYZ")
tdrStyle.SetNdivisions(6 + 5*100 + 0*10000, "XYZ") # Primary, Secondary, and Tertiary divisons
tdrStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
tdrStyle.SetPadTickY(1)

# Postscript options:
tdrStyle.SetPaperSize(20.,20.)
# tdrStyle.SetLineScalePS(3)
# tdrStyle.SetLineStyleString(i, text)
# tdrStyle.SetHeaderPS(header)
# tdrStyle.SetTitlePS(pstitle)

# tdrStyle.SetBarOffset( 0.5)
# tdrStyle.SetBarWidth(0.5)
# tdrStyle.SetPaintTextFormat("g")

# provide default jet coloring
tdrStyle.SetPalette(1)

# tdrStyle.SetTimeOffset()
# tdrStyle.SetHistMinimumZero(True)

tdrStyle.SetHatchesLineWidth(5)
tdrStyle.SetHatchesSpacing(0.05)

