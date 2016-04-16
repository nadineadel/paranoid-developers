import argparse
쪣=True
ޟ=str
恃=argparse.ArgumentParser
from register import register
from login import login
def 寬():
 ࠄ=恃(description="Command")
 廘=ࠄ.add_subparsers(title="register|login",help="Needs one of these commands \n\t\tregister\n\t\tlogin");
 廘.required=쪣
 廘.dest="command"
 赯=廘.add_parser("register",help="Insert username, password and e-mail to register")
 赯.add_argument("username",metavar="username",type=ޟ,help="username")
 赯.add_argument("password",metavar="password",type=ޟ,help="password")
 赯.add_argument("email",metavar="email",type=ޟ,help="username")
 軠=廘.add_parser("login",help="Insert username and password to login")
 軠.add_argument("username",metavar="username",type=ޟ,help="username")
 軠.add_argument("password",metavar="password",type=ޟ,help="password")
 ﶏ=ࠄ.parse_args()
 if ﶏ.command=="register":
  print(register(ﶏ.username,ﶏ.password,ﶏ.email))
 else:
  print(login(ﶏ.username,ﶏ.password))
if __name__=="__main__":
 寬()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
