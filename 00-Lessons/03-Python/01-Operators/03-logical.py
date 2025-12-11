print('Operators logical examples\n')
balance = 1000
whitdrawn = 250
limit = 200
can_withdraw = (whitdrawn <= limit) and (whitdrawn <= balance)

print('\nCan withdraw?', can_withdraw)
if whitdrawn > limit:
    print('The amount to be withdrawn exceeds your limit!')
if whitdrawn > balance:
    print('The amount to be withdrawn exceeds your balance!')

verdadeiro = True
falso = False

print('verdadeiro and falso is:', verdadeiro and falso)
print('verdadeiro or falso is:', verdadeiro or falso)
print('not verdadeiro is:', not verdadeiro)
print('not falso is:', not falso)

truthTable = '''
  A	     B	    NOT A	A AND B	  A OR B	A XOR B	  A NAND B	 A NOR B
False	False	True	 False	  False	     False	    True	 True
False	True	True	 False	  True	     True	    True	 False
True	False	False	 False	  True	     True	    True	 False
True	True	False	 True	  True	     False	    False	 False
'''
print(truthTable)
print('-'*60)
