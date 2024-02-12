user_id = {
    0: 'Root',
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
}

def greeting(id):
    return 'Hi %s' % user_id[id]

greeting(1)
