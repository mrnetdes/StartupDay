# Routines to print receipts to a printer
# Mark Ritchie 08/05/2017
# Uses win32print

import json # Support for json config file
import logging
import time
import os, sys
if (os.name != "posix"): import win32print

def print_receipt(transactionID, printer_name, jsonObject):
  basedir = jsonObject["RCPT_DIR"]
  if (printer_name == ""):
    printer_name = win32print.GetDefaultPrinter()

  if (os.name != "posix"):
    hPrinter = win32print.OpenPrinter(printer_name)
    f2 = open(os.path.join(basedir,transaction_number),"r")
    text_data = f2.read()
    f2.close()
    # Open a doc, open a page, wirte the page and close page and doc
    hJob = win32print.StartDocPrinter(hPrinter,1,("Startup Day Receipt",None,"TEXT"))
    win32print.StartPagePrinter(hPrinter)
    win32print.WritePrinter(hPrinter, text_data)
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
    win32print.ClosePrinter(hPrinter)
  # End of os.name != "posix"

# End of print_receipt

