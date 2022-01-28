from random import randint

# ! flat
# + grey



wave_1 = []
wave_2 = []
wave_3 = []
wave_4 = []
wave_5 = []
wave_6 = []
wave_7 = []
wave_8 = []
wave_9 = []
wave_10 = []
wave_11 = []
wave_12 = []
wave_13 = []
wave_14 = []
wave_15 = []
wave_16 = []
wave_17 = []
wave_18 = []
wave_19 = []
wave_20 = []
wave_21 = []
wave_22 = []
wave_23 = []
wave_24 = []
wave_25 = []

level_1 = [wave_1,wave_2,wave_3,wave_4,wave_5]
level_2 = [wave_6,wave_7,wave_8,wave_9,wave_10]
level_3 = [wave_11,wave_12,wave_13,wave_14,wave_15]
level_4 = [wave_16,wave_17,wave_18,wave_19,wave_20]
level_5 = [wave_21,wave_22,wave_23,wave_24,wave_25]

levels = [level_1,level_2,level_3,level_4,level_5]



def level_generator(wave):

    for i in range(2):
        if len(wave) < 2:
            random_number = randint(1,2)

            if random_number == 1:
                wave.append("!")
            elif random_number == 2:
                wave.append("+")
        
            
def generate():
    for level in levels:
        for wave in level:
            level_generator(wave)
