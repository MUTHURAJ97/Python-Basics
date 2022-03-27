# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:56:44 2022

@author: Muthuraj.Jayaseelan
"""

import sys

class ParentClass:
    def __init__(self,uname,pword):
       self.uname = uname
       self.pword = pword 
    
    def loginCheck(self):
        if (self.uname=="muthu" and self.pword=="123"):
            print("Login Success")
        else:
            print("Incorrect Login")
            sys.exit()
            
class Childclass(ParentClass):
    def __init__(self, uname, pword):
        ParentClass.__init__(self,uname, pword)
        
    def movieSelection(self):
        print("\nWelcome to Online Movie Ticket Booking Portal")
        print("\nSelect a movie")
        movieList =	{
            "1":"RRR",
            "2":"Etharkkum Thunindhavan",
            "3":"The Kashmir Files",
            "4":"Uncharted"
            }
        for i in movieList:
            print(i,"-",movieList[i])
        self.movieNum = input()
        self.selectedMovie = movieList[self.movieNum]
        
        screenList =	{
            "1":"Screen 1",
            "2":"Screen 2",
            "3":"Screen 3",
            "4":"Screen 3"
            }
        self.selectedScreen = screenList[self.movieNum]
        
        return self.selectedMovie,self.selectedScreen
        
        
        
    def DisplayshowTimeSelection(self):
        
        print("\nSelect a show timing (1-5)\n")
        if (self.movieNum == "1" or self.movieNum == "3"):
            slotTime = {
                "1":"10:30 AM",
                "2":"01:00 PM",
                "3":"03:30 PM",
                "4":"06:00 PM",
                "5":"08:30 PM"
                }
            for i in slotTime:
                print(i,"-",slotTime[i])
            
        else:
            slotTime = {
                "1":"11:00 AM",
                "2":"01:30 PM",
                "3":"04:00 PM",
                "4":"06:30 PM",
                "5":"09:00 PM"
                }
            for i in slotTime:
                print(i,"-",slotTime[i])

        self.slotSelection = input()
        self.selectedSlot = slotTime[self.slotSelection]
        return self.selectedSlot
        
    def DisplayTicketSelection(self):
        print("\n Enter the number of tickets to be booked")
        self.ticketSelection = int(input())
        if (self.ticketSelection > 10):
            print("Tickts cannot exceed more than 10 for a single session")
        else:
            return self.ticketSelection
        
print("\nEnter the username")
username = input()
print("\nEnter the password")
password = input()

c1 = Childclass(username, password)  
c1.loginCheck()
c1.movieSelection()
c1.DisplayshowTimeSelection()
c1.DisplayTicketSelection()

movie = c1.selectedMovie
screen = c1.selectedScreen
time = c1.selectedSlot
tickets = c1.ticketSelection


print("- ---------------------------------------------------")
print(f"-\t\t\t\tBooking Confirmed\n-\n-\n-\tMovie - {movie}\t\t\tScreen - {screen}\n-\n-\tShow Time - {time}\t\tTickets - {tickets}\n-\n-\n-")
print("- ---------------------------------------------------")  