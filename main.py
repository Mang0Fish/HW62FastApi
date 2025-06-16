import sqlite_lib as sl

sl.connect('hw15.db')

result = sl.run_query_select('''
    SELECT * FROM eurovision_winners ORDER BY year DESC
    LIMIT 10
''')
print(result)

def has_won(country :str, year: int):
    result = sl.run_query_select(f'''
        SELECT country FROM eurovision_winners WHERE year = {year}
    ''')
    if result == [(country,)]:
        ans = sl.run_query_select(f'''
        SELECT song_name FROM eurovision_winners WHERE year = {year}
    ''')
        return ans
    else:
        return 'Wrong'

def change_genre(year,country,genre):
    if has_won(country,year) != 'Wrong':
        if [(genre,)] != sl.run_query_select(f'''
            SELECT genre FROM song_details
            WHERE year = {year}
        '''):
            sl.run_query_update(f'''
                        UPDATE song_details
                        set genre = {genre}
                        WHERE year = {year}

                    ''')
            return 'Done'
        else:
            return "Enter a different genre"
    else:
        return 'Wrong'
print(has_won('Israel',2018))
print(change_genre(2018,'Israel','Jazz'))


sl.close()
