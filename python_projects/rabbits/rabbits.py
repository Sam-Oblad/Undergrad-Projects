'''calculates when cages will be full of rabbits'''


def do_research(cages, initial_adults, initial_babies):
    '''determines when the cages will be full of rabbits'''
    with open('rabbits.csv', 'w', encoding="utf8") as rabbits:
        rabbits.write(
            '# Table of rabbit pairs\nMonth, Adults, Babies, Total\n')
        rabbits.close()

    adults = initial_adults
    babies = initial_babies
    month = 1

    while True:
        occupied_cages = adults + babies
        total = occupied_cages

        with open('rabbits.csv', 'a', encoding="utf8") as rabbits:
            rabbits.write(f"{month}, {adults}, {babies}, {total}\n")
            rabbits.close()

        new_babies = adults
        adults = adults + babies
        babies = new_babies
        month += 1
        occupied_cages = adults + babies

        if total >= cages:
            with open('rabbits.csv', 'a', encoding="utf8") as rabbits:
                rabbits.write(f'# Cages will run out in month {month-1}')
                break
