FILENAME = 'scores.txt'
FILENAME_2 = 'log.txt'
MODE_W = 'w'
MODE_R = 'r'

total = 0
count = 0

with open(FILENAME_2,MODE_W) as names_file2:

    try:    
        with open(FILENAME,MODE_R) as names_file:
            
            for line in names_file:
                name, score = line.split()
                try:
                    total = total + int(score)
                    names_file2.write(line)
                except ValueError :
                    message = f'Bad score value for {name}, ignored\n'
                    print(message) 
                    names_file2.write(message)
                    continue
                count = count + 1
            try:
                average = total/count
                message = f'The class average is {average} for {count} students\n'
                print(message)
                names_file2.write(message)
            except ValueError as error:
                print(f'Value error::{error}')
                names_file2.write(f'Value error::{error}')
    except IOError as error:
        print(f'I/O error:: {error}')
        names_file2.write(f'I/O error:: {error}')

    