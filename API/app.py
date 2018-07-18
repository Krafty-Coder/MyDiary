"""Import python modules"""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

entries = [{'id' : 1, 'title' : u'this is one', 'content' : u'this is content'},
           {'id' : 1, 'title' : u'this is two', 'content' : u'this is content'}]

@app.route('/diary/api/v1/entries', methods=['POST'])

def create_entry():
    """ This is a funtion for creating an entry"""
    if not request.json or not 'title' in request.json:
        abort(400)
    entry = {
        'id' : entries[-1]['id'] + 1,
        'title': request.json['title'],
        'content': request.json['content']
    }
    entries.append(entry)
    return jsonify({'entry' : entry})

@app.route('/diary/api/v1/entries', methods=['GET'])
def get_entries():
    """This is a function for viewing a list of diary entries"""
    return jsonify({'entries' : entries})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['GET'])
def view_one_entry(entry_id):
    """This is a function for getting a single entry"""
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if len(entry) == 0:
        abort(404)
    return jsonify({'entry': entry[0]})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if not request.json:
        abort(404)
    entry[0]['title'] = request.json.get('title', entry[0]['title'])
    entry[0]['content'] = request.json.get('content', entry[0]['content'])
    return jsonify({'entry': entry[0]})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """This is a function for deleting an entry"""
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if len(entry) == 0:
        return jsonify({'message' : "No entry found"})
    entries.remove(entry[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
