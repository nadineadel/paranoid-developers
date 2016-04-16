import argparse
神=True
ﺰ=str
ᬰ=argparse.ArgumentParser
from register import register
from login import login
def ߤ():
 픧=ᬰ(description="Command")
 ﵸ=픧.add_subparsers(title="register|login",help="Needs one of these commands \n\t\tregister\n\t\tlogin");
 ﵸ.required=神
 ﵸ.dest="command"
 ﹷ=ﵸ.add_parser("register",help="Insert username, password and e-mail to register")
 ﹷ.add_argument("username",metavar="username",type=ﺰ,help="username")
 ﹷ.add_argument("password",metavar="password",type=ﺰ,help="password")
 ﹷ.add_argument("email",metavar="email",type=ﺰ,help="username")
 壟=ﵸ.add_parser("login",help="Insert username and password to login")
 壟.add_argument("username",metavar="username",type=ﺰ,help="username")
 壟.add_argument("password",metavar="password",type=ﺰ,help="password")
 뭝=픧.parse_args()
 if 뭝.command=="register":
  ݗ()
  print(register(뭝.username,뭝.password,뭝.email))
  encrypt()
 else:
  ݗ()
  print(login(뭝.username,뭝.password))
if __name__=="__main__":
 ߤ()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
