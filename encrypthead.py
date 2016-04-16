import re
def catch():
    with open('register.py') as f:
        file = f.readlines()
        file2 = []
        r_expression = re.compile('def .*?')
        currentline = file[0]
        counter = 0
        while counter < len(file):
            currentline = file[counter]
            if re.match(r_expression , currentline):
                variables = currentline.split('(')
                variables[1] = variables[1][:-3]
                v_groups = variables[1].split(',')
                dict = {}
                count = 0
                for v in v_groups:
                    dict.update({v: 'a'+str(count)})
                    count += 1
                for key in dict:
                    currentline = currentline.replace(key,dict[key])
                    currentline = currentline.replace(key,dict[key])
                print currentline     
                file2.append(currentline)        
                counter += 1
                currentline = file[counter]
                while not (currentline.startswith('def')):
                    for key in dict:
                        currentline = currentline.replace('='+key,'='+dict[key])
                        currentline = currentline.replace('= '+key,'= '+dict[key])
                    file2.append(currentline)
                    counter += 1
                    if not counter >= len(file):
                        currentline = file[counter]
                    else:
                        break
            else:
                file2.append(currentline)
            counter +=1
        with open('encrypted.py', 'w') as x:
            line = ''
            x.write(line.join(file2))

if __name__ == "__main__":
    catch()
