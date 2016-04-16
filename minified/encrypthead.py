import re
ﮘ=open
ﮃ=file
ገ=len
ꢭ=dict
ﺰ=str
ޟ=re.match
䨈=re.compile
def ﮅ():
 with ﮘ('login.py')as f:
  ﮃ=f.readlines()
  츋=[]
  ﴞ=䨈('def .*?')
  ﺛ=ﮃ[0]
  ﵩ=0
  while ﵩ<ገ(ﮃ):
   ﺛ=ﮃ[ﵩ]
   if ޟ(ﴞ,ﺛ):
    ﳐ=ﺛ.split('(')
    ﳐ[1]=ﳐ[1][:-3]
    ﮢ=ﳐ[1].split(',')
    ꢭ={}
    ጜ=0
    for v in ﮢ:
     ꢭ.update({v:'a'+ﺰ(ጜ)})
     ጜ+=1
    for ﻔ in ꢭ:
     ﺛ=ﺛ.replace(ﻔ,ꢭ[ﻔ])
     ﺛ=ﺛ.replace(ﻔ,ꢭ[ﻔ])
    print ﺛ
    츋.append(ﺛ)
    ﵩ+=1
    ﺛ=ﮃ[ﵩ]
    while not(ﺛ.startswith('def')):
     for ﻔ in ꢭ:
      ﺛ=ﺛ.replace('='+ﻔ,'='+ꢭ[ﻔ])
      ﺛ=ﺛ.replace('= '+ﻔ,'= '+ꢭ[ﻔ])
     츋.append(ﺛ)
     ﵩ+=1
     if not ﵩ>=ገ(ﮃ):
      ﺛ=ﮃ[ﵩ]
     else:
      break
   else:
    츋.append(ﺛ)
   ﵩ+=1
  with ﮘ('encrypted.py','w')as x:
   细=''
   x.write(细.join(츋))
if __name__=="__main__":
 ﮅ()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
