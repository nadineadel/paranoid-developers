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
