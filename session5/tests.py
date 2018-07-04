from requests import put, get, delete

# restart server before running these tests!!!


def test(req, ans):
    return "Test Passed: {}, result was {}.".format(req == ans, req)


# get list of todos
test1 = test(get('http://localhost:5000/todos').json(), ['iron clothes', 'do programming hw', 'build a startup'])
print("1: " + test1)

# add a todo
test2 = test(put('http://localhost:5000/add', json={'todo': 'never sleep'}).json(), 'todo (never sleep) added')
print("2: " + test2)

# todo list should be updated now
test3 = test(get('http://localhost:5000/todos').json(), ['iron clothes', 'do programming hw', 'build a startup', 'never sleep'])
print("3: " + test3)

# delete a todo
test4 = test(delete('http://localhost:5000/delete', json={'todo': 'never sleep'}).json(), 'todo (never sleep) deleted')
print("4: " + test4)

# todo list should be updated now
test5 = test(get('http://localhost:5000/todos').json(), ['iron clothes', 'do programming hw', 'build a startup'])
print("5: " + test5)
