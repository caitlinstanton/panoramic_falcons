from passlib.hash import pbkdf2_sha256
import pymongo
from pymongo import MongoClient

#Adds a user to database
def addUser(username, password):
    pass

#Returns boolean that indicates whether a user has inputted correct login information
def authenticate(username, password):
    return False

#Returns boolean indicating whether a certain username is taken
def checkUsername(username):
    return False

#Removes user from the database
def deleteUser(username):
    pass

# Hashes and returns password that is hashed and salted by 29000 rounds of pbkdf2 encryption                                          
def hashPass(password):
    return pbkdf2_sha256.encrypt(password)

# Returns true if password hashes into hashpass, false otherwise                                                                      
def verify(password, hashpass):
    return pbkdf2_sha256.verify(password,hashpass)
