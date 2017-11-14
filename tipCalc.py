
total = raw_input('Enter the total amount of the bill: ');
tipAm = raw_input('Enter the tip percentage: ')

try:
    total = float(total)
    tipAm = float(tipAm)
    tip = total * tipAm * .01
    print('Your tip should be ${0}.'.format(tip))
except ValueError:
    print('Please make sure you are entering just the number.')
