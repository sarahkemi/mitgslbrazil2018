from config import config
import requests

board_endpoint = 'https://api.trello.com/1/members/me/boards'
boards = requests.request("GET", board_endpoint, params=config).json()

print len(boards)
for board in boards:
	print 'id:' + board['id']
	print 'name:' + board['name']
	print '\n'

# #gsl bot board id is [removed]
bid = ''
list_endpoint = 'https://api.trello.com/1/boards/{}/lists'.format(bid)
lists = requests.request("GET", list_endpoint, params=config).json()

print lists
list_id = ''
cards_endpoint = 'https://api.trello.com/1/lists/{}/cards?fields=id,name'.format(list_id)
cards = requests.request("GET", cards_endpoint, params=config).json()

print cards

tasks = []

for card in cards:
	tasks.append(card['name'])

print tasks

#desired list id is [removed]

list_id = ''
card_endpoint =  'https://api.trello.com/1/cards'
todo = 'i need to do this'
query = {"name":todo,"pos":"top","idList":list_id,"key":config['key'],"token":config['token']}

# card_post = requests.request("POST", card_endpoint, params=query).json()

# print card_post

#success!