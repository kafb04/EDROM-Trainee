import os, sys
from transitions import Machine

# MAQUINA DE ESTADOS PARA UM CACHORRO PEGAR UMA BOLA

LEFT = 'Left' 
RIGHT = 'Right'
CENTER = 'Center'
BOTTOM = 'Bottom'
SIT = 'sit'

class StateMachine():
    def __init__(self):

        states = ['stand_still', 'walking', 'catch_ball', 'sit', 'impossible']

        go_to_stand_still_transitions = [
            {'trigger': 'go_to_stand_still', 'source': 'stand_still', 'dest': 'stand_still',
             'conditions': 'stand_still_condition', 'unless': 'sit_condition'},

            {'trigger': 'go_to_stand_still', 'source': 'sit', 'dest': 'stand_still',
             'conditions': 'stand_still_condition', 'unless': 'sit_condition'}
        ]

        go_to_catch_ball_transitions = [
            {'trigger': 'go_to_catch_ball', 'source': 'catch_ball', 'dest': 'catch_ball',
             'conditions': 'catch_ball_condition', 'unless': 'sit_condition'},

            {'trigger': 'go_to_catch_ball', 'source': 'stand_still', 'dest': 'catch_ball',
             'conditions': 'catch_ball_condition', 'unless': 'sit_condition'},
        ]

        go_to_sit_transitions = [
            {'trigger': 'go_to_sit', 'source': 'sit', 'dest': 'sit', 'conditions': 'sit_condition'}
        ]

        go_to_impossible_transitions = [
            {'trigger': 'go_to_stand_still', 'source': '*', 'dest': 'impossible', 
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_catch_ball', 'source': '*', 'dest': 'impossible', 
             'conditions': 'impossible_condition'},
            {'trigger': 'got_to_sit', 'source': '*', 'dest': 'impossible', 
             'conditions': 'impossible_condition'}
        ]

        all_transitions = (go_to_sit_transitions + go_to_stand_still_transitions 
                           + go_to_catch_ball_transitions + go_to_impossible_transitions)
        
        self.dog_state_machine = Machine(self, states=states, transitions=all_transitions, initial='sit')

    def request_state_machine_update(self, dog_position, ball_found):
        self.sit_condition_update(dog_position)
        self.catch_ball_condition_update(ball_found)
        print(f'-------------------\nEstado {str(self.state)}')        
        self.update_state()
    
    def update_state(self):
        if self.go_to_catch_ball():
            print('Transição para o catch_ball\n-------------------\n')
            return True
        elif self.go_to_sit():
            print('Transição para o sit\n-------------------\n')
            return True
        elif self.go_to_stand_still():
            print('Transição para o stand_still\n-------------------\n')
            return True
        else:
            return False

    def sit_condition_update(self, dog_position):
        if dog_position != SIT:
            self.sit_condition = True
        else:
            self.sit_condition = False

    def catch_ball_condition_update(self, ball_found):
        if ball_found:
            self.catch_ball_condition = True
        else:
            self.catch_ball_condition = False

    def catch_ball_condition(self): return False  
    def sit_condition(self): return self.sit_condition  
    def impossible_condition(self): return False