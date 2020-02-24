import project_pythonDB
import pymysql


def menu_select_1():
    # User is shown first
    # 15 cities in world database
    print('='*60)
    print('| ' + '{:3s}'.format('ID') + ' | ' +
          '{:16s}'.format('Name') + ' | ' +
          '{:16s}'.format('District') + ' | ' +
          '{:12s}'.format('Population') + ' |')
    print('='*60)
    cities = project_pythonDB.get_15_cities()
    for city in cities:
        print('| ' + '{:3d}'.format(city['ID']) + ' | ' +
              '{:16s}'.format(city['Name']) + ' | ' +
              '{:16s}'.format(city['District']) + ' | ' +
              '{:12d}'.format(city['Population']) + ' |' )
    print('='*60)


def menu_select_2():
    equal_syms = ['<','>','=']
    print('Cities by Population')
    print('--------------------')
    while True:
        equality = input("Enter < > or = : ")
        if equality in equal_syms:
            break
        else:
            print('Incorrect Symbol, Try Again ')

    while True:
        try:
            population = int(input("Enter Population: "))
            break
        except:
            print('Please Enter an Integer:')

    cities = project_pythonDB.get_cities_by_population(equality,population)
    print('='*42)
    print('| ' + '{:4s}'.format('ID') + ' | ' +
          '{:16s}'.format('Name') + ' | ' +
          '{:12s}'.format('Population') + ' |')
    print('='*42)
    for city in cities:
        print('| ' + '{:4d}'.format(city['ID']) + ' | ' +
              '{:16s}'.format(city['Name']) + ' | ' +
              '{:12d}'.format(city['Population']) + ' |')

    print('='*42)

def check_code(codes,code):
    for item in codes:
        if item['countrycode'] == code:
            return True
    return False


def menu_select_3():
    print('Add New City')
    print('------------')
    codes = project_pythonDB.get_country_codes()

    while True:
        country_code = input("Enter Country Code:")
        if check_code(codes,country_code):
            break
        else:
            print('Invalid Country Code, Try Again')


    city_name = input("Enter City Name:")
    district = input("Enter District:")
    while True:
        try:
            population = int(input("Enter Population: "))
            break
        except:
            print('Please Enter an Integer:')

    try:
        rows = project_pythonDB.add_city(country_code, city_name, district, population)
    except pymysql.err.ProgrammingError as e:
        print('Programming Error:', e)
    except pymysql.err.IntegrityError as e:
        print('Insertion Error:',e)
    except Exception as e:
        print('Error Adding City:',e)


def menu_select_4():
    print("Menu 4:")


def menu_select_5():
    print("Menu 5:")


def menu_select_6():
    print('Countries by Name')
    print('-----------------')
    name = input('Enter Country Name:')

    countries = project_pythonDB.view_country_by_name(name)
    print('='*156)
    print('| ' + '{:55s}'.format('Name') + ' | ' +
          '{:16s}'.format('Continent') + ' | ' +
          '{:12s}'.format('Population') + ' | ' +
          '{:60s}'.format('Head of State') + ' |')
    print('='*156)
    for country in countries:
        print('| ' + '{:55s}'.format(country['name']) + ' | ' +
              '{:16s}'.format(country['continent']) + ' | ' +
              '{:12d}'.format(country['population']) + ' | ' +
              '{:60s}'.format(country['headofstate']) + ' |')

    print('='*156)

def get_pop(country,equality,popu_req):
    country_pop = []
    if equality == ">":
        for item in country:
            if item['population'] > popu_req:
                country_pop.append(item)
        
        return country_pop

    elif equality == "<":
        for item in country:
            if item['population'] < popu_req:
                country_pop.append(item)

        return country_pop

    elif equality == "=":
        for item in country:
            if item['population'] == popu_req:
                country_pop.append(item)

        return country_pop



def menu_select_7():
    equal_syms = ['<', '>', '=']
    print('Countries by Population')
    print('-----------------------')
    while True:
        equality = input("Enter < > or = : ")
        if equality in equal_syms:
            break
        else:
            print('Incorrect Symbol, Try Again ')

    while True:
        try:
            population = int(input("Enter Population: "))
            break
        except:
            print('Please Enter an Integer:')

    countries = project_pythonDB.get_country_details()
    pop_count = get_pop(countries,equality,population)
 
    print('='*100)
    print('| ' + '{:4s}'.format('Code') + ' | ' +
          '{:55s}'.format('Name') + ' | ' +
          '{:16s}'.format('Continent') + ' | ' +
          '{:12s}'.format('Population') + ' |')
    print('='*100)
    for country in pop_count:
        print('| ' + '{:4s}'.format(country['code']) + ' | ' +
              '{:55s}'.format(country['name']) + ' | ' +
              '{:16s}'.format(country['continent']) + ' | ' +
              '{:12d}'.format(country['population']) + ' |')

    print('='*100)


def display_menu():
    print("MENU")
    print("====")
    print("1 - View 15 Cities \n" \
    "2 - View Cities by Population \n" \
    "3 - Add New City \n" \
    "4 - Find Car by Engine Size \n" \
    "5 - Add New Car \n" \
    "6 - View Countries by Name \n" \
    "7 - View Countries by Population \n" \
    "x - Exit Application")

def main():
    while True:
        display_menu()
        inp = input("Choice:")
        if inp == "x":
            break
        elif inp == "1":
            menu_select_1()
        elif inp == "2":
            menu_select_2()
        elif inp == "3":
            menu_select_3()
        elif inp == "4":
            menu_select_4()
        elif inp == "5":
            menu_select_5()
        elif inp == "6":
            menu_select_6()
        elif inp == "7":
            menu_select_7()



if __name__ == "__main__":
    main()
