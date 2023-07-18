rate = {int(input()): 'Петя', int(input()): 'Вася', int(input()): 'Толя'}
rate = sorted(rate.items(), reverse=True)
print(
    f'''          {rate[0][1]}          
  {rate[1][1]}  
                  {rate[2][1]}  
   II      I      III   
''')