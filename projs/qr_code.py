import qrcode

url = input("Enter url : ")

filename = input("Enter the filename: ")
if not filename.endswith('.png'):
    filename += '.png'
    
img = qrcode.make(url)
img.save(filename)

# python3 projs/qr_code.py