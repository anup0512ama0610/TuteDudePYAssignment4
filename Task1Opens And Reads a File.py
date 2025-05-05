
try:
    file=open("Sample.txt","r")
    reading=file.read(27)
    reading1=file.read(28)
    print(reading)
    print(reading1)
    file.close()

except FileNotFoundError:
     print("Error: The File 'Sample.txt' was not found.")
'''
finally:
    print("File Closed")
'''
'''
try:
    file=open("Sample.txt","r")
    reading=file.readlines()
    print(reading)
    file.close()

except FileNotFoundError:
     print("Error: The File 'Sample.txt' was not found.")
'''