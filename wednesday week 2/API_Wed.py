from flask import *
app = Flask(__name__)

app.secret_key= "12345"
dict1 = {}
store =[]

@app.route ('/',methods=['GET'])
def home():
    return jsonify({'meassage' : 'welcome home techies'})

@app.route ('/register',methods=['POST'])
def register():
    name=request.get_json()["name"]
    username=request.get_json()["username"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    dict1.update({username:{"name":name,"email":email,"password":password}})
    return jsonify({'meassage' : 'you are succesfully registered'})

def loginauth(username, password):
    if username in dict1:
        if password == dict1[username]["password"]:
            return True
    return False

@app.route('/login',methods=['POST','GET'])
def log_in():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    if loginauth(username, password):
        return jsonify({'meassage' : 'you are succesfully logged in'})
    else:
        return jsonify({'meassage' : 'you are not succesfully logged in'})

@app.route ('/comments_post',methods=['POST'])
def comments_post():
    comment=request.get_json()["comment"]
    store.append(comment)
    return jsonify({'meassage' : 'comments posted'})

@app.route ('/get_comments', methods=['GET'])
def get_comments():
    #comment=request.get_json()["comment"]
    if len(store)>0:
        return jsonify(store)
    else:
        return jsonify({'meassage' : 'no comments available'})

    

@app.route ('/delete_comments', methods=['DELETE', 'GET'])
def delete_comments():
    del store[:]
    return jsonify({'meassage' : 'comments delete'})

@app.route ('/get_users', methods=['GET'])
def get_users():
    return jsonify(dict1)

if __name__== '__main__':
    app.run(debug=True)