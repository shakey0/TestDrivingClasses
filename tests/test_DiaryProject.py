from lib.DiaryProject import *

def test_DiaryProject_format():
    garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
    clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    result1 = garden_chores.format()
    assert result1 == "Garden Chores: You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed."
    result2 = clean_the_house.format()
    assert result2 == "Clean the House: We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom."

def test_DiaryProject_count_words():
    garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
    clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    result1 = garden_chores.count_words()
    assert result1 == 35
    result2 = clean_the_house.count_words()
    assert result2 == 30

def test_DiaryProject_reading_times():
    garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
    clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    result1 = garden_chores.reading_times(5)
    assert result1 == 7
    result2 = clean_the_house.reading_times(3)
    assert result2 == 10
    result3 = garden_chores.reading_times(6)
    assert result3 == 6
    result4 = clean_the_house.reading_times(4)
    assert result4 == 8
    result5 = garden_chores.reading_times(40)
    assert result5 == 1
    result6 = clean_the_house.reading_times(9)
    assert result6 == 3

def test_DiaryProject_reading_chunks():
    garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
    clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    result1 = garden_chores.reading_times(7)
    assert result1 == 5
    result2 = garden_chores.reading_chunk(7, 1)
    assert result2 == "You need to cut the grass and"
    result3 = garden_chores.reading_chunk(14, 1)
    assert result3 == "then trim the edges of the lawn, then pull out as many weeds as"
    result4 = garden_chores.reading_chunk(4, 2)
    assert result4 == "you can from the flowerbeds, and finally trim"
    result5 = garden_chores.reading_chunk(9, 1)
    assert result5 == "the hedges next to the shed."
    result6 = garden_chores.reading_chunk(17, 2)
    assert result6 == "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the"
    result7 = garden_chores.reading_chunk(17, 2)
    assert result7 == "shed."
    result8 = garden_chores.reading_chunk(15, 3)
    assert result8 == "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed."
    result9 = garden_chores.reading_chunk(3, 5)
    assert result9 == "You need to cut the grass and then trim the edges of the lawn, then"
    result10 = clean_the_house.reading_times(8)
    assert result10 == 4
    result11 = clean_the_house.reading_chunk(100, 7)
    assert result11 == "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom."
    result12 = clean_the_house.reading_chunk(6, 3)
    assert result12 == "We need to wipe down all the surfaces in the kitchen as well as all the tables around"
    result13 = clean_the_house.reading_chunk(3, 4)
    assert result13 == "the house, then hoover all the carpets, and finally clean the bathroom."
    result14 = clean_the_house.reading_chunk(1, 1)
    assert result14 == "We"