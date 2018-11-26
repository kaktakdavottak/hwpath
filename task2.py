import os


a = os.path.join(os.path.dirname(__file__), 'Migrations')
b = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Migrations')
print(a)
print(b)
