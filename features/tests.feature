Feature: test

    Scenario: letter is in word
        Given a word морковка
        Given a letter а
        When check letter
        Then number of guessed letters increase

    Scenario: letter is not in word
        Given a word кабачок
        Given a letter ы
        When check letter
        Then number of guessed letters not changed

    Scenario: word is correct
        Given a word кабачок
        When check word
        Then number of guessed letters increase

    Scenario: letter is more than one in word
        Given a word змееед
        Given a letter е
        When find char positions
        Then length of returned array is 3

	Scenario: user input is word
        Given a word змеед
        When get user input
        Then result is tuple of змеед and 0
