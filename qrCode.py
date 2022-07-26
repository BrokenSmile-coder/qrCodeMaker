import qrcode

a = input("Welcome the qrCode maker. please enter the content of the qrCode you will make.\n")
code  = qrcode.make(a)
print("everything's okay. 'qr.png' is formening in this file now.")
code.save('qr.png')