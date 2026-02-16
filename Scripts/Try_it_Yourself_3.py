#Guest list 

Guest = ['alen', 'randy', 'domnic', 'roman','alisha']
print("Hi",Guest[0],"You are invited to the party ")

Not_availabe = Guest.remove('domnic')
print(Not_availabe , "unable to attend the party today" )
Guest.insert(2,'Rey')
print("so that",Guest[2],"Will attend the party with us..")

Guest.append('Rambo')

#shrinking Guest list:
print('You can invite only two people for the dinner .')

crash = Guest.pop()
print("Sorry",crash,"Unfortunately we can't invite to the dinner because, they dinner table is not arrived..")
crash = Guest.pop()
print("Sorry",crash,"Unfortunately we can't invite to the dinner because, they dinner table is not arrived..")
crash = Guest.pop()
print("Sorry",crash,"Unfortunately we can't invite to the dinner because, they dinner table is not arrived..")

print(Guest)
# del Guest[2]

#3.9 Dinenr Guest. use len()
print(len(Guest))


