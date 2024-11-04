# stored in postgresql
import psycopg2 as ps


class Company:
    def __init__(self, company_name):
        self.company_id: int
        self.company_name: str = company_name


def create_company_table():
    pass


def insert_company():
    pass


def get_company():
    pass
