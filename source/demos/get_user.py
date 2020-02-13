
import os

users = {
    0: 'root',
    1000: 'bent'
}

getUser = os.geteuid()

if getUser == 0:
    print('script eksekveres af root')
else:
    print(f'script eksekveres af user {users[getUser]}')
