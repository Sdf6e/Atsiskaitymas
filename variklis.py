from sqlalchemy import Column, Integer, String, VARCHAR, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/duomenys.db')
base = declarative_base()

class Mainwallet(base):
    __tablename__ = "Mainwallet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    use = Column("USE", VARCHAR)
    amount = Column("AMOUNT", Float)
    from_to = Column("FROM / TO", VARCHAR)
    date_when = Column("DATE", DateTime, default=datetime.utcnow())

    def __init__(self, use, amount, from_to):
        self.use = use
        self.amount = amount
        self.from_to = from_to

    def __repr__(self):
        return f'|Mainwallet| {self.id} : {self.use} | {self.amount} | {self.from_to} | {self.date_when}'

class Savingswallet(base):
    __tablename__ = "Savingswallet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    use = Column("USE", VARCHAR)
    amount = Column("AMOUNT", Float)
    from_to = Column("FROM / TO", VARCHAR)
    date_when = Column("DATE", DateTime, default=datetime.utcnow())

    def __init__(self, use, amount, from_to):
        self.use = use
        self.amount = amount
        self.from_to = from_to

    def __repr__(self):
        return f'|Savingswallet| {self.id} : {self.use} | {self.amount} | {self.from_to} | {self.date_when}'

base.metadata.create_all(engine)