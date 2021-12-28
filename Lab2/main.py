import psycopg2
import controller
from view import Menu

try:
    Menu.menu()
except (Exception , psycopg2.Error) as error :
        controller.msg("PostgreSQL Error: {}".format(error))
finally:
    controller.msg("PostgreSQL connection is closed")