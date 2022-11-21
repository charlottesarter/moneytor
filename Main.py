from Finance import Finance

def read():
    f = open('data/sample_file.csv', 'r')
    while True:
        line = f.readline() # Read a line sequentially
        values = line.split(',')

        if values[0] == '':
            print('End of the data')
        else:
            finance = Finance(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
            print(finance)

        if not line:
            break
        # print(line)
    f.close()

while True:
    new_object = Finance.create()
    Finance.add(new_object, 'data/sample_file.csv')
    read()



