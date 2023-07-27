import pytest
from lib.GrammarChecker import *

def test_grammar_stats_start_and_end_correct():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("It's a lovely day.")
    assert result1 == True
    result2 = check_grammar.check(" Will it rain today? ")
    assert result2 == True
    result3 = check_grammar.check("How are you today? ")
    assert result3 == True
    result4 = check_grammar.check(" The cat is crazy!")
    assert result4 == True

def test_grammar_stats_start_or_end_incorrect():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("my house is very nice.")
    assert result1 == False
    result2 = check_grammar.check(" Alice needs to ask a question ")
    assert result2 == False
    result3 = check_grammar.check(" finland is very cold.")
    assert result3 == False
    result4 = check_grammar.check("!The cat is crazy!")
    assert result4 == False
    result5 = check_grammar.check("This sentence wasn't finished,")
    assert result5 == False
    result6 = check_grammar.check("katie can't click: ")
    assert result6 == False

def test_grammar_stats_percent_good_100_1case():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("It's a lovely day.")
    assert result1 == True
    result2 = check_grammar.percentage_good()
    assert result2 == 100

def test_grammar_stats_percent_good_100_2cases():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("It's a lovely day.")
    assert result1 == True
    result2 = check_grammar.percentage_good()
    assert result2 == 100
    result3 = check_grammar.check(" Will it rain today? ")
    assert result3 == True
    result4 = check_grammar.percentage_good()
    assert result4 == 100

def test_grammar_stats_percent_good_50_2cases():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("It's a lovely day.")
    assert result1 == True
    result2 = check_grammar.percentage_good()
    assert result2 == 100
    result3 = check_grammar.check(" will it rain today? ")
    assert result3 == False
    result4 = check_grammar.percentage_good()
    assert result4 == 50

def test_grammar_stats_percent_good_67_3cases():
    check_grammar = GrammarStats()
    result1 = check_grammar.check("It's a lovely day.")
    assert result1 == True
    result2 = check_grammar.percentage_good()
    assert result2 == 100
    result3 = check_grammar.check(" will it rain today? ")
    assert result3 == False
    result4 = check_grammar.percentage_good()
    assert result4 == 50
    result5 = check_grammar.check("How are you today? ")
    assert result5 == True
    result6 = check_grammar.percentage_good()
    assert result6 == 67

def test_grammar_stats_percent_good_60_5cases():
    check_grammar = GrammarStats()
    result1 = check_grammar.check(" will it rain today? ")
    assert result1 == False
    result2 = check_grammar.check(" Will it rain today? ")
    assert result2 == True
    result3 = check_grammar.check("How are you today? ")
    assert result3 == True
    result4 = check_grammar.check("This sentence wasn't finished,")
    assert result4 == False
    result5 = check_grammar.check(" The cat is crazy!")
    assert result5 == True
    result6 = check_grammar.percentage_good()
    assert result6 == 60