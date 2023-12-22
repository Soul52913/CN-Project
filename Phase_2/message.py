import shelve

def add_comment(comment):
    with shelve.open('comments') as db:
        if 'comments' not in db:
            db['comments'] = []
        db['comments'].append(comment)

def get_comments():
    with shelve.open('comments') as db:
        if 'comments' not in db:
            return []
        return db['comments']