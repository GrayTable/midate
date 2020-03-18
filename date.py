import sys
import itertools
from micalendar import MiDate

def mindate(date_str: str) -> str:
    """
    Return the earliest possible date constructed with input string

    Parameters:
        date_str (str): String in "A/B/C" format

    Returns:
        str: Valid date in "YYYY-MM-DD" format or invalid input message
    """

    # playing it safe with the input
    try:
        date_list = list(map(int, date_str.split('/')))

        if len(date_list) < 3:
            raise ValueError
        
    except ValueError:
        return '%s is illegal' % date_str
    
    # used to gather all the possibilities
    possibilities = []
    
    # O(3!) complexity
    for perm in itertools.permutations(date_list):
        year, month, day = perm

        year = year if year > 999 else year + 2000

        try:
            possibilities.append(MiDate(year, month, day))

        except ValueError:
            continue

    if not possibilities:
        return '%s is illegal' % date_str
    
    return str(min(possibilities))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[!] Error. No input argument provided.\n')
        sys.exit()

    
    with open(sys.argv[1], 'r') as source:
        for line in source:
            stripped = line.rstrip()

            if stripped:
                print(mindate(stripped))
        
    
    
