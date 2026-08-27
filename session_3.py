# class & objects : A blueprint
# self : act on this particular object's data

# class Message:
#     def __init__(self, role, content):
#         self.role = role
#         self.content = content

#     def __repr__(self):
#         return f"role={self.role}, content={self.content}"


# chat = Message("user", "Hello")
# print(chat.content)
# print(repr(chat))


# decorators - takes a function and executes it

# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# def hello():
#     print("Hello!")

# decorated_function = my_decorator(hello)
# decorated_function()


# generators: a function that returns value one at a time

# def count():
#     yield 1
#     yield 2
#     yield 3

# numbers = count()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))



# Fast API: A framework to build REST api in python

# from fastapi import FastAPI

# creates the instance of the project
# app = FastAPI()

# @app.get("/")
#     async def read_root():
#         return {"Hello World!"}

# SQLAlchemy: ORM library for python
# pyhton code ----(SQLAchemy: acts as a translator between pyton code and relational DB)---- MySQL
# from sqlalchemy import create_backend, String, Integer, Column
# from sqlalchemy.orm import declarative_base, sessionMaker, Session
# SessionLocal = sessionMaker()
# DATABASE_URL = "db_address/db_name.db"

# class DB:

# def get_db():
#     db = SessionLocal()

# Git and Github

# branch: used for tracking the change
# new branch: git checkout -b 'branch_name'

# fetch: remote status
# pull : fetch and merge
# git add .

# ------ End of python ------- #

# ------ LLMs ------- #

# Basics of LLM