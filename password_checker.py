import requests
import hashlib
import sys


def request_api_data(query_char):

    '''
    return a status code to see if password was leaked

    '''
    url  ='https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again!')

    return response



def get_password_leaks_count(response, hash_to_check):
    '''
    return a response for hased password to see how many times the password was leaked

    '''
    response = (line.split(":") for line in response.text.splitlines())
    for item, count in response:
        if item == hash_to_check:
            return count
    return 0


def pwned_check_api(password):

    """ 
    Check password if exist in API response
    
    """
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first_5char)
    return get_password_leaks_count(response, tail)
    

def main(args):

    for password in args:
        
        count = pwned_check_api(password)
        if count:
            print(f'{password} was found {count} times! You should probably change your password')
        else:
            print(f'{password} was not found, carry on!')
    return 'All done, take care!'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

