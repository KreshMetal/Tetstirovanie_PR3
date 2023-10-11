Feature: test

    Scenario: word is correct
        Given a word кабачок
        When check word
        Then number of guessed letters increase