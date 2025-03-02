from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
import functions

app = Flask(__name__)
CORS(app,origins='*', supports_credentials=True)
app.secret_key = "102394020"

@app.route('/')
def main_page():
    print(f"Current session : {session}")
    if 'username' in session:
        return render_template("index.html", logged_in =True, username_session = session['username'])
    else:
        return render_template("index.html", logged_in = False)
    


@app.route('/sign_up')

def render_sign_up():
    if 'username' in session:
        return redirect(url_for('main_page'))
    return render_template("signup.html")

@app.route('/login')

def render_log_in():
    if 'username' in session:
        return redirect(url_for('main_page'))
    
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main_page'))

@app.route('/validate_credentials',  methods = ['POST'])

def validate():


    user_data = request.get_json()

    if not user_data:

        return jsonify({"message" : "Invalid JSON"})  



    username = user_data['username']
    password = user_data['password']

    user_credentials = functions.specific_user_credentials(username)
    if user_credentials!=None:
        real_passwd = user_credentials[-1]
        if password == real_passwd:
            session['username'] = username
            print("This is the checkpoint!")
            print(f"Set session : {session}")
            return jsonify({"message" : "Your password is correct!", "flag" : '1'})
        else:
            return jsonify({"message" : "Your password is not correct!", "flag" : "0"})
        

    else:
        return jsonify({"message" : "user does not exist", "flag" : '2'})     
    


@app.route('/insert_data_into_DB', methods = ["POST",])

def insert_data():

    user_data = request.get_json()
    print(user_data['username'], user_data['password'])
    
    creds = functions.specific_user_credentials(user_data['username'])
    print(creds)
    if creds is None:
        functions.insert_data((user_data['username'], user_data['password']))

    else:
        return jsonify({"message" : "user already exists", "flag" : '0'})
    

    current_data = functions.select_data(("Username", "Password"))
    print(current_data)
    



    return jsonify({"message" : "inserted data", "flag" : '1'})


if __name__ == "__main__":
    app.run(debug=True)
