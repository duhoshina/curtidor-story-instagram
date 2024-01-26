import json

with open('growbot-queue.txt', 'r', encoding='utf-8') as file:
    data = file.read()

user_data = json.loads(data)

# Extrai os usernames
usernames = [user['username'] for user in user_data]

with open('seguidores.txt', 'w', encoding='utf-8') as output_file:
    for username in usernames:
        output_file.write(username + '\n')

print("Usernames foram extraídos e salvos no arquivo seguidores.txt")
