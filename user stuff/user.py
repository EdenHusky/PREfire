# -*- coding: utf-8 -*-
"""
Created on 2/3/24

@author: Matt
"""

#Construct a Complex Class that will be used to Create and Store a User(s)-------------------------
class User:
    #Constructor of the User Class :)
    def __init__(self,  UserName = 'mmouse', Password = 'Disney', Hint = "Where I work"):
        self.__UserName = UserName
        self.__Password = Password
        self.__hint = Hint
        return
    
    #"Getter" Methods for the Variables listed in the Constructor Parameters
    def getUser(self):
        return self.__UserName
    def getPass(self):
        return self.__Password
    def getHint(self):
        return self.__hint

    #"Setter" Methods for the Variables listed in the Constructor Parameters
    def setUser(self, NewUserName):
        self.__UserName = NewUserName
        return
    def setPass(self, NewPassword):
        self.__Password = NewPassword
        return
    def setHint(self, NewHint):
        self.__hint = NewHint
        return
