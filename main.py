import argparse
from register import register
from login import login
from update import update
from deactivate import deactivate
from db_manipulation import decrypt
from db_manipulation import encrypt

def main():
  parser = argparse.ArgumentParser(description="Command")  
  subparsers = parser.add_subparsers(title="register|login|update|deactivate", 
    help="Needs one of these commands \n\t\tregister\n\t\tlogin\n\t\tupdate\n\t\tdeactivate");
  subparsers.required = True
  subparsers.dest = "command"
  
  parser_register = subparsers.add_parser("register", help = "Insert username, password and e-mail to register")
  parser_register.add_argument("username", metavar="username", type=str, help="username")
  parser_register.add_argument("password", metavar="password", type=str, help="password")
  parser_register.add_argument("email", metavar="email", type=str,  help="email")

  parser_login = subparsers.add_parser("login",help = "Insert username and password to login" )
  parser_login.add_argument("username", metavar="username", type=str,  help="username")
  parser_login.add_argument("password", metavar="password", type=str,   help="password")

  parser_update = subparsers.add_parser("update",help = "Insert username and password to login First" )
  parser_update.add_argument("username", metavar="username", type=str,  help="username")
  parser_update.add_argument("type", metavar="type", type=str,  help="update password/email")
  parser_update.add_argument("change", metavar="change", type=str,   help="password/email needs to be updated")

  parser_deactivate = subparsers.add_parser("deactivate",help = "Insert username and password to login First" )
  parser_deactivate.add_argument("username", metavar="username", type=str,  help="username")
  parser_deactivate.add_argument("password", metavar="password", type=str,   help="password")

  args = parser.parse_args()
  # decrypt()
  if args.command == "register":
    print (register(args.username, args.password, args.email))
  elif args.command == "login":
    print (login(args.username, args.password))
  elif args.command == "update":
    print (update(args.username, args.type, args.change))
  elif args.command == "deactivate":
    print (deactivate(args.username, args.password))




if __name__ == "__main__":
  main()