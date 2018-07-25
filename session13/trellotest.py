from config import config
import requests

# first, I try to get all the boards in my account

board_endpoint = 'https://api.trello.com/1/members/me/boards'
boards = requests.request("GET", board_endpoint, params=config).json()

print len(boards)
for board in boards:
    print 'id:' + board['id']
    print 'name:' + board['name']
    print '\n'

# second, I try to get all the lists from my board using the board id i found the code above

bid = ''
list_endpoint = 'https://api.trello.com/1/boards/{}/lists'.format(bid)
lists = requests.request("GET", list_endpoint, params=config).json()

print lists

# third I use the id of the list i want to add cards to make a post request to add this sample todo to the list

list_id = ''
card_endpoint = 'https://api.trello.com/1/cards'
todo = 'i need to do this'
query = {"name": todo, "pos": "top", "idList": list_id, "key": config['key'], "token": config['token']}

# uncomment these following two lines to post the new card to the list

# card_post = requests.request("POST", card_endpoint, params=query).json()
# print card_post

# success!

# extra example to grab all the current cards on a list
list_id = ''
cards_endpoint = 'https://api.trello.com/1/lists/{}/cards?fields=id,name'.format(list_id)
cards = requests.request("GET", cards_endpoint, params=config).json()

print cards

tasks = []

for card in cards:
    tasks.append(card['name'])

print tasks
