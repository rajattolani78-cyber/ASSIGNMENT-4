try:
    file1 = open('samplefile.txt','r')
    print("read file containt")
    r = file1.readline()
    t = file1.readline()
    print(f'line1:{r}')
    print(f'line2:{t}')
except (FileNotFoundError):
    print ("Error: The file 'sample.txt' was not found.")