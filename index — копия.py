from dataset import users, countries

'''
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
'''

#Point 5. Путешественники

avg_flights = 0

for user in users:
    if 'friends' in user:
        friends_with_cars = 0
        friends_travels_total = 0
        for friend in user['friends']:
            if 'cars' in friend and 'flights' in friend:
                friends_with_cars += 1
                friends_travels_total += len(friend['flights']) 
    avg_flights = round(friends_travels_total / friends_with_cars, 5)           
                        

'''
#Point 6. Чистка списков

pure_users = users.copy()

for user in pure_users:
    if 'friends' in user:
        list_of_friends = user['friends']
        list_of_friends_who_traveled_in_wrong_countries = []
        for i in list_of_friends:
            if 'flights' in i:
                list_of_flights = i['flights']
                for j in list_of_flights:
                    if j['country'] in countries:
                        if i not in list_of_friends_who_traveled_in_wrong_countries:
                            list_of_friends_who_traveled_in_wrong_countries.append(i)
    if list_of_friends_who_traveled_in_wrong_countries:
        pure_users.remove(user)                  
                    

#Point 5. Путешественники

for user in users:
    avg_flights = 0
    friends_with_cars = []
    particular_friends_number_of_flights = 0
    number_of_flights = []
    if 'friends' in user:
        list_of_friends = user['friends']
        for i in list_of_friends:
            if isinstance(i, dict):
                if 'cars' in i:
                    if 'flights' in i:
                        friends_with_cars.append(i)
                        particular_friends_number_of_flights = len(i['flights'])
                        number_of_flights.append(particular_friends_number_of_flights)
        if len(friends_with_cars):
            avg_flights = round(sum(number_of_flights) / len(friends_with_cars), 5)                    



'''
