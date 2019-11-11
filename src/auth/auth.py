from src.auth import authUtils
import hashlib


def validateUser(email, password):
    passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    email = str(email).lower()
    res = authUtils.getUser(email, passwordHash)
    if res:
        return res
    return None

def addUser(role, email, username, password, department):
    role = role.lower()
    department = department.lower()
    passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    userData = {'username': username, 'email': email, 'password': passwordHash, 'role': role , 'department': department}
    user = authUtils.addCustomer(userData)
    return  user

