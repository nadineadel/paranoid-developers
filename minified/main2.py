import argparse
from register import register
from login import login

def main():
  parser = argparse.ArgumentParser(description="Command")  
  subparsers = parser.add_subparsers(title="register|login", help="Needs one of these commands \n\t\tregister\n\t\tlogin");
  subparsers.required = True
  subparsers.dest = "command"
  
  parser_register = subparsers.add_parser("register", help = "Insert username, password and e-mail to register")
  parser_register.add_argument("username", metavar="username", type=str, help="username")
  parser_register.add_argument("password", metavar="password", type=str, help="password")
  parser_register.add_argument("email", metavar="email", type=str,  help="username")

  parser_login = subparsers.add_parser("login",help = "Insert username and password to login" )
  parser_login.add_argument("username", metavar="username", type=str,  help="username")
  parser_login.add_argument("password", metavar="password", type=str,   help="password")

  args = parser.parse_args()
  if args.command == "register":
    decrypt()
    print (register(args.username, args.password, args.email))
    encrypt()
  else:
    decrypt()
    print (login(args.username, args.password))




if __name__ == "__main__":
  main()