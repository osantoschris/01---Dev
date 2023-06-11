import tkinter as tk
from tkinter import ttk
from win10toast import ToastNotifier
import pandas as pd
import random

class RegisterParticipant():

    raffle = {}
    names = []
    friends = []
    item = 0

    def __init__(self):
        self.drawn = False
        self.friend = ''

    def register(self, name, telephone):
        participant = dict(Name= name, Telephone= telephone, Drawn= self.drawn, Friend= self.friend)

        RegisterParticipant.raffle[RegisterParticipant.item] = participant
        RegisterParticipant.names.append(name)
        RegisterParticipant.friends.append(self.friend)
        RegisterParticipant.item += 1
        
class RaffleNames():

    def __init__(self):
        self.raffle_names = RegisterParticipant.raffle

    def raffle_name(self):
        name = random.randint(0, len(RegisterParticipant.names) -1)
        name = RegisterParticipant.names[name]
        return name
    
    def raffle_friend(self):
        friend = random.randint(0, len(RegisterParticipant.friends) - 1)
        friend = RegisterParticipant.friends[friend]
        return friend
    
    def reffle_secret_friends(self):
        self.name = RaffleNames().raffle_name()
        self.friend = RaffleNames().raffle_friend()
        if self.name != self.friend:
            for indice, sub_dict in self.raffle_names.values:
                if sub_dict['Name'] == self.name:
                    sub_dict['Drawn'] = True
                    sub_dict['Friend'] = self.friend
                    RegisterParticipant.names.remove(self.name)
                    RegisterParticipant.friends.remove(self.friend)
            return True
        else:
            return False    

RegisterParticipant().register(name='Christian', telephone=123)
RegisterParticipant().register(name='Joyce', telephone=123)
RegisterParticipant().register(name='Nayara', telephone=123)

print(RaffleNames().raffle_names)