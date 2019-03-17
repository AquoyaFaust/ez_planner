from appjar import gui
import appjar
import sys

def validate_user(usernames, user):
    """
    Returns location in file or path to correct data
    """
    for n in range(len(usernames)):
        if Usernames[n] == user:
            return True, n
    return False, -1 #Returns Boolean if user is valid and file location of password for user

def validate_password(info, p_correct):
    pass_loc = passwordLine[info]
    f = open(paths[info])
    f_lines = f.read().splitlines()
    password = f_lines[pass_loc]
    print password
    if p_correct == password:
        return True
    return False #Return's True or False

def press(btn_name):
    if btn_name == "Submit":
        user = app.getEntry("userEnt")
        password = app.getEntry("passEnt")
        check(user, password)
    elif btn_name == "Cancel":
        sys.exit()
    elif btn_name == "Create User":
        create_new_user() 

def create_gui():
    app.addLabel("userLab", "Username:", 0, 0)
    app.addEntry("userEnt", 0, 1)
    app.addLabel("passLab", "Password:", 1, 0)
    app.addEntry("passEnt", 1, 1)
    app.addButtons( ["Submit", "Cancel"], press, colspan=2)
    app.setFocus("userEnt")
    app.enableEnter(press)
    app.go()

def check(user, p_correct):
    valid, line = validate_user(Usernames, user)
    if valid:
        valid = validate_password(line, p_correct)
        if valid:
            return valid
        else:
            app.errorBox("Failed Login", "Invalid Username or |Password|")
    else:
        app.errorBox("Failed Login", "Invalid |Username| or Password")
    return valid

def create_new_user():


def main():
    create_gui()
    #End of Program
    print "anything"

    #validate_password()

if __name__ == '__main__':
    app = gui("Login Form")
    Usernames = ["Aquoya", "Nat", "Luke", "Pat", "Alex", "Travis"]
    passwordLine = [5] * len(Usernames)
    paths = [".\\test.txt"] * len(Usernames)
    main()
