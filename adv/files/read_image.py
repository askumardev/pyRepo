f= open('sample.jpg','rb')

f1=open('new.jpg','wb')

for i in f:
  print(i)

for i in f:
  # print(i)
  f1.write(i)

# python3 adv/files/read_image.py