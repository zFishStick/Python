from flask import Flask, request, jsonify
import instaloader

L = instaloader.Instaloader()
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/get_followers', methods=['POST'])
def get_followers_list():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # # Usa i parametri come necessario
    # return jsonify({
    #     'username': username,
    #     'password': password
    # })
    
    L.login(username, password)  # (login)
    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, username)

    # Print list of followers
    follow_list = []
    count = 0
    for follower in profile.get_followers():
        follow_list.append(follower.username)
        file = open("followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1

    return print("Done!")