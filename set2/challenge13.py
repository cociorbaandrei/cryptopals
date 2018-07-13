
import re
from random import randrange
def parse_cookie(cookie):
    parsed = {}
    for keyvalue in cookie.split("&"):
        keypair = keyvalue.split("=")
        parsed[keypair[0]] = keypair[1]
    return parsed

def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def encode_dictionary(dictionary):
    encoded = ""
    count = 0
    for key, value in dictionary.iteritems():
        encoded += str(key) + "=" + str(value)
        count += 1
        if(count != len(dictionary)):
            encoded += "&"
    return encoded

def profile_for(email):
    if(not valid_email(email))
        raise Exception("Invalid email address!")
    else:
        user_profile["email"] = email
        user_profile["uid"]  = randrange(1,1000)
        user_profile["role"] = "user"
        return encode_dictionary(user_profile)


if __name__ == '__main__':
    print parse_cookie("foo=bar&baz=qux&zap=zazzle")