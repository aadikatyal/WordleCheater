# WordleCheater

Simple Python script that helps Wordle enthusiasts solve their daily puzzle!

### Sample Usage:

Users are prompted to enter a 5 letter sequence of letters. Lower-case letters denote letters that are present in the word but in the wrong position. Upper-case letters denote letters in the correct pisition. ? denotes any letters that the user is unsure about. Users then enter a sequence of letters that are not present in the word. The Wordle Cheater will define the contraints and provide a list of potential answers. Users may continue to enter additional letters that are not present in the word until they reach success.

```
[Welcome to Wordle Cheater]

[Input capital letters if in correct position]
[Input lower case letters if in word but wrong position]
[Input ? if unsure of letter in word]

[Input must be 5 characters]
Enter word: onc??
Enter letters not in the word (- for none): adieusprtmh

Potential Guesses: [knock, clown, colon]
Add additional letters not in word (- for none): k

Potential Guesses: [clown, colon]
Add additional letters not in word (- for none): w

Potential Guesses: [colon]
```

---
Aadi Katyal, 2022
