import sqlite_lib as sl
import pytest

@pytest.fixture
def before_after_oper():
    sl.connect('hw15.db')

    yield

    sl.close()
def test_get_years():
    sl.connect('hw15.db')
    result = sl.run_query_select('''
        SELECT YEAR FROM eurovision_winners
        LIMIT 1
    ''')
    assert result == [(1956,)]

def test_count_wins():
    sl.connect('hw15.db')
    result = sl.run_query_select('''
        SELECT count(*) from eurovision_winners
    ''')
    assert result == [(68,)]

def test_count_songs():
    sl.connect('hw15.db')
    result = sl.run_query_select('''
        SELECT count(*) from song_details
    ''')
    assert result == [(68,)]

def test_country_won(before_after_oper):
    result = sl.run_query_select(f'''
        SELECT country FROM eurovision_winners WHERE year = 2018
    ''')
    assert result == [('Israel',)]

def test_country_won_false_pos():
    sl.connect('hw15.db')
    result = sl.run_query_select(f'''
            SELECT country FROM eurovision_winners WHERE year = 2018
        ''')
    try:
        assert result == [('Colombia',)]
    finally:
        print("False Positive")

