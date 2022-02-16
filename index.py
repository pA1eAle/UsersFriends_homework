from dataset import users, countries


#Point 1. Плохие пароли

users_wrong_password = []

for user in users:
    password_checked = user['password']
    if password_checked.isdigit():
        wrong_password = {'name': '', 'mail': ''}
        wrong_password['name'] = user['name']
        wrong_password['mail'] = user['mail']
        users_wrong_password.append(wrong_password)

print(users_wrong_password)        


#Point 2. Женщины водители

girls_drivers = []

for user in users:
    if 'friends' in user:
        for friend in user['friends']:
            if 'cars' in friend and friend['sex'] == 'F':
                girls_drivers.append(friend['name'])

print(girls_drivers)


#Point 3. Лучшая профессия

best_occupation = {'occupation':'', 'salary': 0}

for user in users:
    if 'friends' in user:
        list_of_friends = user['friends']
        for i in list_of_friends:
            friends_job = i['job']
            if best_occupation['salary'] < friends_job['salary']:
                best_occupation['occupation'] = friends_job['occupation']
                best_occupation['salary'] = friends_job['salary']

print(best_occupation)  


#Point 4. Самый влиятельный пользователь

vip_user = ''
vip_user_weight = {'weight': 0}
vip_candidate = {'name':'', 'friends_total_salary':0}
total_salary = 0


for user in users:
    if 'friends' in user:
        vip_candidate['name'] = user['name']
        list_of_friends = user['friends']
        salary_list = []
        for i in list_of_friends:
            friends_job = i['job']
            friends_salary = friends_job['salary']
            salary_list.append(friends_salary)
            total_salary = sum(salary_list)
            vip_candidate['friends_total_salary'] = total_salary
    if vip_candidate['friends_total_salary'] > vip_user_weight['weight']:
        vip_user_weight['weight'] = vip_candidate['friends_total_salary']
        vip_user = vip_candidate['name'] 

print(vip_user)        


#Point 5. Путешественники

avg_flights = 0
friends_cars = 0
total_flights = 0

for user in users:
    friends = user.get('friends', [])  
    for friend in friends:
        cars = friend.get('cars', None)  
        if cars:
            friends_cars += 1 
            total_flights += len(friend.get('flights', [])) 

if friends_cars:
    avg_flights = round(total_flights / friends_cars, 5)                     
#я не понимаю почему эта хуйня проходит автотест

#Point 6. Чистка списков                 

pure_users = users.copy()
wrong_countries_friends = []

for user in pure_users:
    friends = user.get('friends', [])
    for friend in friends:
        flights = friend.get('flights', [])
        for flight in flights:
            if flight['country'] in countries and friend not in wrong_countries_friends:
                wrong_countries_friends.append(friend)
    if wrong_countries_friends:
        pure_users.remove(user)            
