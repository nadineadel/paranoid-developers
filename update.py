import argparse

def update(username, password):
  parser = argparse.ArgumentParser(description="Update which info, you can only update password and email")  
  subparsers = parser.add_subparsers(title="password|email", help="Needs one of these attributes \n\t\password\n\t\temail");
  subparsers.required = True
  subparsers.dest = "update"
  parser_login = subparsers.add_parser("login",help = "Insert username and password to login" )
  parser_login.add_argument("username", metavar="username", type=str,  help="username")
  parser_login.add_argument("password", metavar="password", type=str,   help="password")
  if args.command == "login":
    decrypt()
    login-state = login(args.username, args.password)
  if login-state:
    parser_password = subparsers.add_parser("password", help = "Insert new password")
    parser_password.add_argument("password", metavar="password", type=str, help="password")
   

    parser_email = subparsers.add_parser("email",help = "Insert new email" )
    parser_email.add_argument("email", metavar="email", type=str,  help="email")

    args = parser.parse_args()
    decrypt()
    if args.command == "password":
      with sqlite3.connect("milestone2.db") as conn:
        c = conn.cursor()
        update_user = c.execute("UPDATE user SET password = 'password' WHERE username = username;".format(username = username, password = password))
        conn.commit()
        conn.close();
        return "password updated"
    else:
      with sqlite3.connect("milestone2.db") as conn:
        c = conn.cursor()
        update_user = c.execute("UPDATE user SET email = 'email' WHERE username = username;".format(username = username, email = email))
        conn.commit()
        conn.close();
        return "email updated"
    encrypt()
  else:
    return "Please login first"

if __name__ == "__main__":
  update()