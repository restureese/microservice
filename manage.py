from server import db, service

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(service,db)
manager = Manager(service)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	manager.run()