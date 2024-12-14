print ('Siema')

input()
age = int(input('Ile masz lat?  '))

#print(f'Więc masz {age} lat')
#print(f'Będziesz dorosły za {18 - age} lat')

#if age < 0 and age < 18:
    #print(f'Więc masz {age} lat')
    #print(f'Będziesz dorosły za {18 - age} lat')
#else:
    #print('zły wiek')

while True:
    age = int(input('Ile masz lat?  '))
    if 0 < age< 18:
        print(f'Wiec masz {age} lat')
        print(f'Będziesz dorosły za {18 - age} lat')
        break
    else:
        print('zły wiek, jeszcze raz')





