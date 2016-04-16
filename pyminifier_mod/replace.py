import re
def replace(cache, filename):
  print('replace ' , cache)
  replacables = ['{0}(', 'import {0}']
  with open('main.py') as f:
    txt = f.read()
    for key, value in cache.items():
      for replacable in replacables:
        txt = txt.replace(replacable.format(key), replacable.format(value))
  with open('main2.py', 'w') as f:
    f.write(txt)
def replaceargs(filename):
  with open(filename) as f:
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
    with open('minified/'+filename, 'w') as x:
        line = ''
        x.write(line.join(file2))