COUNTRIES = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps", "Argentina",
"Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
"Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei",
"Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Rep",
"Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo {Democratic Rep}", "Costa Rica",
"Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
"East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji",
"Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
"Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
"Iraq", "Ireland {Republic}", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan",
"Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
"Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia",
"Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
"Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
"Myanmar", " {Burma}", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
"Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
"Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts & Nevis",
"St Lucia", "Saint Vincent & the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia",
"Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
"Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden",
"Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago",
"Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela",
"Vietnam","Yemen", "Zambia", "Zimbabwe")

GENRES = ("Action", "Adventure", "Adult", "Animation", "Comedy", "Crime", "Documentary", "Drama",
"Fantasy", "Family", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Short", "Thriller", "War",
"Western")

def input_text(prompt, min_char, max_char):
    while True:
        promp = input(prompt)
        length = 'short'
        if len(promp) >= max_char:
            length = 'long'
        if min_char <= len(promp) <= max_char:
            return promp
        print('Text is to ' + str(length) + '!')


#   print(input_text('hvaherre',3,5))

def input_num(prompt, min_num, max_num):
    while True:
        try:
            num = int(input(prompt))
            if min_num <= num <= max_num:
                return num
            print('Must be a number between', min_num, 'and', max_num)
        except:
            print('Must be an integer')

#print(input_num('hva herre', 3, 5))

def input_selection(prompt, selections):
    while True:
        inp = input(prompt)
        if inp in selections:
            return inp
        print('Not valid chioce!')
        print('Options that start with', inp[:2])
        for opt in selections:
            if inp[:2].lower() == opt[:2].lower():
                print(opt)

def enter_title():
    print('Enter the following data about the film')
    title = input_text('Title: ', 1, 100)
    year = input_num('Year: ', 1900, 2019)
    genre = input_selection('Genre: ', GENRES)
    age = input_num('Age rating (0-18): ', 0, 18)
    country = input_selection('Country: ', COUNTRIES)
    score = input_num('Score (0-100): ', 0, 100)
    comment = input_text('Comment: ', 10, 100)
    return (title, year, genre, age, country, score, comment)

#print(enter_title())
#print(input_selection('Country: ', COUNTRIES))




def add_movies():
    db = {}
    while True:
        while True:
            y_n = input('Do you want to enter a movie (y/n)? ')
            if y_n.lower() == 'y':
                y_n = True
                break
            if y_n.lower() == 'n':
                y_n = False
                break
            print('Not a valid input')
        if not y_n:
            break
        movie = enter_title()
        if movie[0] in db:
            print(movie[0], 'has been updated')
        else:
            print(movie[0], 'has been added')
        db[movie[0]] = movie[1:]

    return db



def save_movies(db):
    save = input_text('Save database to filename: ', 5, 20)
#try:
    with open(save, 'a') as f:
        for key, values in db.items():
            f.write(key+':'+str(values)+'\n')
#except:
    print('Database could not be saved to', save)
#    else:
    print('The database was saved to', save)

save_movies({'a':(1,2,3,4),'b':(1,2,3,3)})
