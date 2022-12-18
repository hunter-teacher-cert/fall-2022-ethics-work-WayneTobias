#Gerrymandering Simulation
#Code Component for Final Project
#By Wayne Tobias and Ed Hawkins

import random

#declare and initialize variables
districts = 0
districtVoters = 0
totalRepublicanVotes = 0
totalDemocratVotes = 0
totalElectionTrials = 0
totalDemocratWins = 0
totalRepublicanWins = 0
elections = 0

#get user input
districtVoters = int(input("How many voters are in each district? "))
districts = int(input("How many districts would you like to create? "))
totalElectionTrials = int(input("How many elections would you like to run? "))

#loop to run general election trials
while elections < totalElectionTrials:

#declare and initialize variables to keep track of districts won
    democraticDistricts = 0
    republicanDistricts = 0

  #loop to run all district elections
    i=0
    while i < districts - 1:
        democratVotes = 0
        republicanVotes = 0

      #loop to run each individual district election
        j = 0
        while j < districtVoters:
          #cast each vote randomly and update vote count
            if random.randint(1, 100) < 51:
                democratVotes += 1
            else:
                republicanVotes += 1
            j += 1
          
        #determine winner of district election
        if democratVotes > republicanVotes:
            democraticDistricts += 1
        else:
            republicanDistricts += 1

        #update vote counts for general election
        totalDemocratVotes += democratVotes
        totalRepublicanVotes += republicanVotes
        i += 1

    #ensure that general election vote is tied
    democratTieVotes = int(districts * districtVoters/2 - totalDemocratVotes)
    republicanTieVotes = int(districts * districtVoters/2 - totalRepublicanVotes)

    #determine winner of final district and update count
    if democratTieVotes > republicanTieVotes:
        democraticDistricts += 1
    else:
        republicanDistricts += 1

    totalRepublicanVotes += republicanTieVotes
    totalDemocratVotes += democratTieVotes

  #ouptut results of each general election trial and update count
    print("Total Republican Votes = ", totalRepublicanVotes)
    print("Total Democratic Votes = ", totalDemocratVotes)
    print("Republican Districts Won = ", republicanDistricts)
    print("Democratic Districts Won = ", democraticDistricts)
    if republicanDistricts > democraticDistricts:
        totalRepublicanWins += 1
        print("Republicans win the election.")
    else:
        totalDemocratWins += 1
        print("Democrats win the election.") 
    print()
    
    elections += 1

#output overall results of simulation
print("Gerrymandering simulation results for",districts,"districts with",districtVoters,"voters each:")
print("Total number of election simulations = ", totalElectionTrials)
print("Total Democratic Wins = ", totalDemocratWins)
print("Total Republican Wins = ", totalRepublicanWins)
