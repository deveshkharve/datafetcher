
def getUser(username, password):
    data = {}

    myStatisUser = {
        'id': 1,
        'username': 'test@test.test',
        'password': '936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af' #hash of helloworld
    }

    if username == myStatisUser['username'] and password == myStatisUser['password']:
        return myStatisUser
