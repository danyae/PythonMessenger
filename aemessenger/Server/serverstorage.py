from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    info = Column(String)

    def __init__(self, login, info):
        self.login = login
        self.info = info

    def __repr__(self):
        return '<Client({0}, {1})>'.format(self.login, self.info)


class ClientHistory(Base):
    __tablename__ = 'client_history'
    id = Column(Integer, primary_key=True)
    login_time = Column(DateTime)
    ip = Column(String)
    clientid = Column(Integer, ForeignKey('clients.id'))

    def __init__(self, login_time, ip):
        self.login_time = login_time
        self.ip = ip

    def __repr__(self):
        str_log_in_at = self.login_time.strftime("%d-%m-%Y %H:%M:%S")
        return '<Client {0} logged in at {1}>'.format(self.ip, str_log_in_at)


class ContactList(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    ownerid = Column(Integer, ForeignKey('clients.id'))
    contactid = Column(Integer, ForeignKey('clients.id'))

    def __init__(self, ownerid, contactid):
        self.ownerid = ownerid
        self.contactid = contactid


class ServerDB:
    def __init__(self):
        package_dir = os.path.abspath(os.path.dirname(__file__))
        db_dir = os.path.join(package_dir, 'server.sqlite?check_same_thread=False')
        sqlite_path = ''.join(['sqlite:///', db_dir])
        self.engine = create_engine(sqlite_path)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


def mainloop():
    serverdb = ServerDB()
    print('Session:', serverdb.session)
    test_client = Client('testlogin', 'testinfo')
    dany_client = Client('Dany', 'admin')
    contact = ContactList(2, 1)
    name = 'Dany'
    # serverdb.session.add(test_client)
    # serverdb.session.add(dany_client)
    # serverdb.session.add(contact)
    # serverdb.session.commit()
    q_client = serverdb.session.query(Client).filter_by(login=name).first()
    print('Query:', q_client)


if __name__ == '__main__':
    mainloop()