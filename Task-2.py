user_input = input("Enter some data: ")
with open ('output.txt','w') as f1:
    r = f1.write(f'{user_input}\n')
print("Data successfully written to output.txt.")
user_input2 = input("Enter additional text to append: ")
with open ('output.txt','a') as f2:
    c  = f2.write(f'{user_input2}\n')
print('Data successfully appended.')

print('\n Final content of output.txt:')
with open ('output.txt','r') as f3:
    t = f3.read()
print(t)

