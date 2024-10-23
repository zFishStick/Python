# Get instance
import instaloader

L = instaloader.Instaloader()

# Login or load session
username = 'gabri.pesce_'
password = r'hoztyb-1Gasna-vurgur'
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followees
follow_list = []
count = 0
for followee in profile.get_followees():
    follow_list.append(followee.username)
    file = open("followees.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
# (likewise with profile.get_followers())