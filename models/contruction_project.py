# stored in postgresql
from company import Company


class ConstructionProject:
    def __init__(self, name: str = None,  start_date: int = None,
                 end_date: int = None, budget: int = None,
                 actual_cost: int = None, company: Company = None,
                 number_of_workers: int = None,
                 number_of_engineers: int = None,
                 ):
        self.id = id
        self.name: str = name
        self.start_date: int = start_date
        self.end_date: int = end_date
        self.budget: int = budget
        self.actual_cost: int = actual_cost
        self.company: Company = company
        self.number_of_workers: int = number_of_workers
        self.number_of_engineers: int = number_of_engineers

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "cost": self.cost,
        }


def create_construction_project_table():
    pass


def insert_construction_project():
    pass


def get_construction_project():
    pass
