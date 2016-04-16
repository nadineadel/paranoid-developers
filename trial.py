import re
def catch():
    with open('register.py') as f:
        file = f.readlines()
        file2 = []
        r_expression = re.compile('def .*?')
        currentline = file[0]
        counter = 0
        print len(file)
        while counter < len(file):
            currentline = file[counter]
            print currentline
            if re.match(r_expression , currentline):
                variables = currentline.split('(')
                variables[1] = variables[1][:-3]
                print variables[1]
                v_groups = variables[1].split(',')
                dict = {}
                count = 0
                for v in v_groups:
                    dict.update({v: 'a'+str(count)})
                    count += 1
                print dict
                counter +=1
                currentline = file[counter]
                while not (currentline.startswith('def') or counter >= len(file)):
                    for key in dict:
                        currentline = currentline.replace('='+key,'='+dict[key])
                        currentline = currentline.replace('= '+key,'= '+dict[key])
                    file2.append(currentline)
                    counter += counter
                    if not counter >= len(file)-1:
                        currentline = file[counter]
            counter +=1
        print file2
        #matched_string = r_expression.find()
        # with open('main3.py', 'w') as f:
        #     f.write(file2)

if __name__ == "__main__":
    catch()
