from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format("root", "password", "netflix2"), pool_pre_ping=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees_data = [
        {'name': 'Brian', 'email': 'Brian@doe.com', 'age': 27},
        {'name': 'Jane', 'email': 'Jane@mine.com', 'age': 22},
        {'name': 'Max', 'email': 'Max@doe.com', 'age': 19},
        {'name': 'Calvis', 'email': 'Calvis@levert.com', 'age': 20}
]

for employee_data in employees_data:
    new_employee = Employee(name=employee_data['name'], email=employee_data['email'], age=employee_data['age'])
    session.add(new_employee)

session.commit()

employees = session.query(Employee).all()
for employee in employees:
    print(employee.id, employee.name, employee.email, employee.age)

session.close()
