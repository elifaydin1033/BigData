#Elif Aydin Lab1
#Part A
fullName='Aydin, Elif'
indexofComma=fullName.index(',')
#print(indexofComma)
firstName=fullName[indexofComma +2:]
lastName=fullName[:indexofComma]
modifiedFullName=firstName+ ' ' + lastName
print(modifiedFullName)
#Part B
originalBill= input('please enter the bill amount:\n>>')
tipInput= input('please enter the percent you would like to tip \n>>')
#print(originalBill,tipInput)
billFloat= float(originalBill)
tipFloat= float(tipInput)
total = (billFloat* tipFloat* .01) + billFloat
print('Your total bill with a',tipInput,'percent tip is:$',total)
print('Your total bill with a',tipInput,'percent tip is:','${0:,.2f}'.format(total))