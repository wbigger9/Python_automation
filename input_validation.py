import pyinputplus as pyip

#while True:
 #   age = pyip.inputPassword()
  #  try:
   #     age = int(age)
   # except:
    #    print('Please use numeric digits')
     #   continue
   # if age < 1:
    #    print('Please enter a positve number')
     #   continue
    # break
# print(f'your age is {age}')



print("what is 100 divided by 4?")
response = pyip.inputChoice(['6','25','9','12'],  blank=False)
if response != '25':
    print('wrong')



