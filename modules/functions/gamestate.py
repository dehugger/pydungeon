import _pickle

def save_object(obj):
    save_name = 'saves/' + obj.name + '.p'
    _pickle.dump(obj, open(save_name, 'wb'), protocol=0)

def load_object(name):
    save_name = 'saves/' + name + '.p'
    name = _pickle.load( open(save_name, 'rb'))
    return name

def save_obj_list(obj_names):
    save_name = 'saves/objlist.p'
    _pickle.dump(obj_names, open(save_name, 'wb'))

def load_obj_names():
    save_name = 'saves/objlist.p'
    obj_names = _pickle.load(open(save_name, 'rb'))
    return obj_names

def save_game(objs, save_name='default'):
    class objNames():
        obj_names = []

    Objects = objNames()

    for obj in objs:
        save_object(obj)
        Objects.obj_names += obj.name

    save_obj_list(Objects)

    return 'Gamestate Saved'

def load_game():
    Objects = load_obj_names()
    objs = []
    for obj in Objects.obj_names:
        pass