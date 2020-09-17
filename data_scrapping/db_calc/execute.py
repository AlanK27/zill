
from db_calc.queries.queries import query


def calc_execute():
    x = query()
    x.initiate()

if __name__ == '__main__':
    calc_execute()
