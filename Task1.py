try:
    file = open('sample.txt','r')
    line1 = file.readline()
    line2 = file.readline()
    print("Line1: ", line1)
    print("Line2: ", line2)

except FileNotFoundError:
    print('File not found! Please check the File Name or Path')

finally:
    print("File opened successfully")
