import pymysql.cursors

conn = None
countries_by_name = []
country_details = []

def connect(db_name):
    global conn
    # Connect to the database
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db=db_name,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def get_15_cities():
    if( not conn):
        connect('world')

    query = "select * from city limit 15"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        cities = cursor.fetchall()
        return cities
 

def get_cities_by_population(equality,pop_required):
    if(not conn):
        connect('world')

    if equality == "<":
        query = "select * from city where population < %s"
    elif equality == ">":
        query = "select * from city where population > %s"
    elif equality == "=":
        query = "select * from city where population = %s"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query,(pop_required))
        cities = cursor.fetchall()
        return cities

def get_country_codes():
    if(not conn):
        connect('world')

    query = "select countrycode from city group by countrycode"


    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        codes = cursor.fetchall()
        return codes


def add_city(code,name,dist,pop):
    if(not conn):
        print('Not Connected')
        connect('world')
    else:
        print('Already Connected')

    query = "insert into city (CountryCode, Name, District, Population) values (%s,%s, %s, %s)"

    with conn:
        cursor = conn.cursor()
        num_rows = cursor.execute(query, (code, name, dist, pop))
        return num_rows

def view_country_by_name(name):
    if(not conn):
        print('Not Connected')
        connect('world')
    else:
        print('Already Connected')

    query = "select name, continent, population, headofstate from country where name like %s"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, (name + '%'))
        countries = cursor.fetchall()
        return countries


def get_country_details():
    global country_details
    if country_details:
        return country_details
    else:
        if(not conn):
            connect('world')

        query = "select code, name, continent, population from country"

        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            country_details = cursor.fetchall()
            return country_details

    

