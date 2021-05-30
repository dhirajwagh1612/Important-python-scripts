# -*- coding: utf-8 -*-
"""
Created on Sun May 30 07:48:24 2021

@author: Dhiraj Wagh
"""
# Generate Fake Data using python Faker Module

# importing faker package
from faker import Faker

# create Instance
fake = Faker()


# printing fake data
print("Name : ", fake.name())
print("Email : ", fake.email())
print("Country : ", fake.country())
print("Text : ", fake.text())
print("url : ", fake.url())


# printing profile
print("fake profile : ", fake.profile())



# generating fake date and time.
fakeit = Faker()

# generating fake data and time.
print(fakeit.century())
print(fakeit.year())
print(fakeit.month())
print(fakeit.day_of_month())


# change language using faker.
fake = Faker('hi_IN')

# hi_IN change in language into hindi (Devnagari)

for i in range(0,15):
    print("name : ", fake.name())