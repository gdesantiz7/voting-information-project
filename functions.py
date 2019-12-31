import pandas as pd

def character_length_checker(string: str, number_of_characters: int) -> bool:
    "Checks if the number of characters provided equals the number of characters in all strings with a boolean"
    for i in string:
        if len(i) == number_of_characters:
            return True
        else:
            return False
        
def precinct_check(row) -> str:
    "Checks if State_ADDRESSES column corresponds with Begin_ID_PRECINCTS column"
    if (row['State_ADDRESSES'] == 'MA') and (row['Begin_ID_PRECINCTS'] == 'MAS'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'WI') and (row['Begin_ID_PRECINCTS'] == 'WIS'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'CA') and (row['Begin_ID_PRECINCTS'] == 'CAL'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'ME') and (row['Begin_ID_PRECINCTS'] == 'MAI'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'PA') and (row['Begin_ID_PRECINCTS'] == 'PEN'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'GA') and (row['Begin_ID_PRECINCTS'] == 'GEO'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'FL') and (row['Begin_ID_PRECINCTS'] == 'FLO'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'NJ') and (row['Begin_ID_PRECINCTS'] == 'NEWJ'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'AZ') and (row['Begin_ID_PRECINCTS'] == 'ARI'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'MN') and (row['Begin_ID_PRECINCTS'] == 'MIN'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'NY') and (row['Begin_ID_PRECINCTS'] == 'NEWY'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'VA') and (row['Begin_ID_PRECINCTS'] == 'VIR'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'CT') and (row['Begin_ID_PRECINCTS'] == 'CON'):
        return 'Match'
    elif (row['State_ADDRESSES'] == 'IL') and (row['Begin_ID_PRECINCTS'] == 'ILL'):
        return 'Match'
    elif (row['State_ADDRESSES'] != 'MA') and (row['Begin_ID_PRECINCTS'] != 'MAS'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'WI') and (row['Begin_ID_PRECINCTS'] != 'WIS'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'CA') and (row['Begin_ID_PRECINCTS'] != 'CAL'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'ME') and (row['Begin_ID_PRECINCTS'] != 'MAI'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'PA') and (row['Begin_ID_PRECINCTS'] != 'PEN'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'GA') and (row['Begin_ID_PRECINCTS'] != 'GEO'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'FL') and (row['Begin_ID_PRECINCTS'] != 'FLO'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'NJ') and (row['Begin_ID_PRECINCTS'] != 'NEWJ'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'AZ') and (row['Begin_ID_PRECINCTS'] != 'ARI'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'MN') and (row['Begin_ID_PRECINCTS'] != 'MIN'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'NY') and (row['Begin_ID_PRECINCTS'] != 'NEWY'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'VA') and (row['Begin_ID_PRECINCTS'] != 'VIR'):
        return 'Mismatch'
    elif (row['State_ADDRESSES'] != 'CT') and (row['Begin_ID_PRECINCTS'] != 'CON'):
        return 'Mismatch'
    else:
        return 'Mismatch'