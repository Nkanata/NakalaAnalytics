import csv

arr1 = ['AFG', 'Asia', 'Afghanistan', '2020-02-25', '5.0', '0.0', '', '', '', '', '0.126', '0.0', '', '', '', '', '',
        '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '8.33', '39835428.0', '54.422', '18.6', '2.581', '1.337', '1803.987', '', '597.029', '9.59', '', '', '37.746',
        '0.5', '64.83', '0.511', '']


def lastline():
    with open('owid-covid-data.csv', mode='r') as csv_file:
        arr = csv_file.readlines()[-1].split(',')
    return arr


arr = lastline()
for i, v in enumerate(arr, start=1):
    print(i, v)


def write():
    with open('owid-covid-data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        mx = 2
        output = open('output.txt', 'w')

        for row in csv_reader:
            if line_count == 0:
                print(len(row))
                output.write("\n".join(row))
                line_count += 1
                continue
            print(row)
            line_count += 1
            if line_count == 3:
                break
        csv_file.close()
        output.close()
