from segno import *

contents = input("Enter in a URL or any text: ")

backg = input("Enter in background color: ")

foreg = input("Enter in foreground color: ")

data_b = input("Enter in background color for data: ")

data_f = input("Enter in foreground colour for data: ")

file_name = input("Enter in a file name for your QR code (with extension): ")

code = make_qr(contents)

code.save(
    file_name,
    scale = 10,
    dark = foreg,
    light = backg,
    data_dark = data_b,
    data_light = data_f

)