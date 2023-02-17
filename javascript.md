## REGEX

## TEST METHOD

- returns True or False

```js
let myString = "Hello, World!";
let myRegex = /Hello/;
let result = myRegex.test(myString);
```

## `OR` `|` OPERATOR

- returns True if matches with at least one of the arguments

```js
let petString = "James has a pet cat.";
let petRegex = /dog|cat|bird|fish/;
let result = petRegex.test(petString);
```

## IGNORING CASE - CASE INSENSITIVE

- add `i` after the closing slash `/string/i` to return both lower case and capital letters

```js
let myString = "freeCodeCamp";
let fccRegex = /freeCodeCamp/i;
let result = fccRegex.test(myString);
```

## MATCH METHOD

- returns an array of matched strings

```js
let extractStr = "Extract the word 'coding' from this string.";
let codingRegex = /coding/;
let result = extractStr.match(codingRegex);
```

## FIND MORE THAN THE FIRST MATCH - GLOBAL SEARCH FLAG

- `/string/g`
- returns an array of matched strings

```js
let twinkleStar = "Twinkle, twinkle, little star";
let starRegex = /twinkle/g;
let result = twinkleStar.match(starRegex);
```

## WILDCARD `.`

- matches ANY one character
- `/hu./` - retunrs `hut`, `hug`, `hum` etc

```js
let exampleStr = "Let's have fun with regular expressions!";
let unRegex = /.un/; // Change this line
let result = unRegex.test(exampleStr);
```

## MATCH A SINGLE CHARACTER FROM A SET OF POSSIBLE MATCHES `[abc]`

- `[abc]`

```js
let quoteSample =
  "Beware of bugs in the above code; I have only proved it correct, not tried it.";
let vowelRegex = /[aeiou]/gi; // Change this line
let result = quoteSample.match(vowelRegex); // Change this line
```

## MATCHING LETTERS OF ALPHABET

- `[a-z]`

```js
let quoteSample = "The quick brown fox jumps over the lazy dog.";
let alphabetRegex = /[a-z]/gi; // Change this line
let result = quoteSample.match(alphabetRegex); // Change this line
```

## MATCHING NUMBERS AND LETTERS OF ALPHABET

- `[a-z0-9]`

```js
let quoteSample = "Blueberry 3.141592653s are delicious.";
let myRegex = /[h-s2-6]/gi; // Change this line
let result = quoteSample.match(myRegex); // Change this line
```

## MATCHING ALL CHARACTERS NOT SPECIFIED - `NEGATED CHARACTER SET`

- `/[^aeiou^0-9]/`

```js
let quoteSample = "3 blind mice.";
let myRegex = /[^aeiou^0-9]/gi; // Change this line
let result = quoteSample.match(myRegex); // Change this line
```

## MATCHING A CHARACTER OR A CONSECUTIVE SEQUENCE OF CHARACTERS THAT OCCUR ONCE OR MORE TIMES

- `/a+/g` - returns an array of 'a' or 'aa', or 'aaa' strings

```js
let difficultSpelling = "Mississippi";
let myRegex = /s+/g; // this is the solution
let result = difficultSpelling.match(myRegex);
```

## MATCHING CHARACTERS THAT OCCUR ZERO OR MORE TIMES

- `/go*/` - returns "go", "gooooo" and "g"

```js
let chewieQuote = "Aaaaaaaaaaaaaaaarrrgh!";
let chewieRegex = /Aa*/; // Change this line
let result = chewieQuote.match(chewieRegex);
```

## LAZY MATCHING

- In regular expressions, a greedy match finds the longest possible part of a string that fits the regex pattern and returns it as a match. The alternative is called a lazy match, which finds the smallest possible part of the string that satisfies the regex pattern.

Example of greedy matching:

`/t[a-z]*i/` to the string `titanic` will return `titani`

Example of lazy matching:

`/t[a-z]*?i/` to the string `titanic` will return `ti` 

```js
let text = "<h1>Winter is coming</h1>";
let myRegex = /<.*?>/; // it's the answer!
let result = text.match(myRegex);
```

## MATCHING BEGINING STRING PATTERNS

- `^` inside a character set `/[^a-z]/` is used to negate the character set
- `^` outside of a character set `/^Ricky/` is used to search for patterns at the begining of strings

```js
let rickyAndCal = "Cal and Ricky both like racing.";
let calRegex = /^Cal/; // Change this line
let result = calRegex.test(rickyAndCal);
```

## MATCHING ENDING STRING PATTERNS

- `/story$/` - will return true if a string is ended witha a word `story`

```js
let caboose = "The last car on a train is the caboose";
let lastRegex = /caboose$/; // Change this line
let result = lastRegex.test(caboose);
```

## MATCHING ALL LETTERS, NUMBERS AND UNDERSCORE

- `/\w/` is equal to `/[A-Za-z0-9_]/`
- it's a child class of a `Shorthand character class`

```js
let quoteSample = "The five boxing wizards jump quickly.";
let alphabetRegexV2 = /\w/g; // Change this line
let result = quoteSample.match(alphabetRegexV2).length;
```

## MATCHING EVERYTHING BUT LETTERS, NUMBERS AND UNDERSCORE

- `/\W/` is equal to `/[^A-Za-z0-9_]/`
- it's a child class of a `Shorthand character class`

```js
let quoteSample = "The five boxing wizards jump quickly.";
let nonAlphabetRegex = /\W/g; // Change this line
let result = quoteSample.match(nonAlphabetRegex).length;
```

## MATCHING ALL NUMBERS

- `/\d/` is equal to `/[0-9]/`
- it's a child class of a `Shorthand character class`

```js
let numRegex = /\d/g;
```

## MATCHING ALL NON NUMBERS

- `/\D/` is equal to `/[^0-9]/`
- it's a child class of a `Shorthand character class`

```js
let noNumRegex = /\D/g;
```

## MATCHING WHITESPACE AND OTHER DELIMINATION CHARACTERS

- `/\s/` - returns whitespace, carriage return, tab, form feed, and new line characters
- `/\s/` is equal to `/[\r\t\f\n\v]/`

```js
let sample = "Whitespace is important in separating words";
let countWhiteSpace = /\s/g; // Change this line
let result = sample.match(countWhiteSpace);
```

## MATCHING ALL NON WHITESPACE AND OTHER DELIMINATION CHARACTERS

- `/\S/` - returns everything BUT whitespace, carriage return, tab, form feed, and new line characters
- `/\S/` is equal to `/[^ \r\t\f\n\v]/`

```js
let sample = "Whitespace is important in separating words";
let countNonWhiteSpace = /\S/g; // Change this line
let result = sample.match(countNonWhiteSpace);
```

## SPECIFY THE UPPER AND LOWER NUNBER OF MATCHES

- `/x{3,6}/` - only return strings with letter `x` if it matches between 3 (lower bound) and 6 times (upper band)

```js
let ohStr = "Ohhh no";
let ohRegex = /Oh{3,6} no/; // Change this line
let result = ohRegex.test(ohStr);
```

## SPECIFY ONLY THE LOWER NUMBER OF MATCHES

- `/x{3,}/` - only return strings with letter `x` which appear at least 3 times

```js
let haStr = "Hazzzzah";
let haRegex = /Haz{4,}ah/; // Change this line
let result = haRegex.test(haStr);
```

## SPECIFY EXACT NUMBER OF MATCHES

- `/x{3}/` - only returns strings with letter `x` which appear exactly 3 times

```js
let timStr = "Timmmmber";
let timRegex = /Tim{4}ber/; // Change this line
let result = timRegex.test(timStr);
```

## OPTIONAL CHECK `?`. MATCHING IF IT EXISTS OR IT DOESN'T EXIST

- `/colou?r/` - it returns true for both `color` and `colour`

```js
let favWord = "favorite";
let favRegex = /favou?rite/; // Change this line
let result = favRegex.test(favWord);
```

## POSITIVE AND NEGATIVE LOOKAHEAD

- `/a(?=b)` - POSITIVE LOOKAHEAD, after regex found letter `a`, it will look ahead for `b`, if if found `b`, it will return `a`. If it didn't find `b`, it will return `null`
- `/a(?!b)` - NEGATIVE LOOKAHEAD, after regex found letter `a`, it will look ahead for `b`, if it didnt' find `b`, it will return `a`. If it found `b`, it will return `null`

Example 1: Here is a (naively) simple password checker that looks for between 3 and 6 characters and at least one number:

```js
let password = "abc123";
let checkPass = /(?=\w{3,6})(?=\D*\d)/;
checkPass.test(password);
```

Example 2: Match passwords that are greater than 5 characters long, and have exactly two consecutive digits.

```js
let sampleWord = "astronaut";
let pwRegex =  /(?=\w{6})(?=\w*\d{2})/;
let result = pwRegex.test(sampleWord);
```

## MATCHING MULTIPLE STRINGS (MIXED GROUPING OF CHARACTERS)

- `/T(o|i)m` - returns true for both `Tom` and `Tim`

If you want to find either Penguin or Pumpkin in a string, you can use the following Regular Expression: `/P(engu|umpk)in/g`

```js
let myString = "Eleanor Roosevelt";
let myRegex = /(Franklin |Eleanor ).*\s*Roosevelt$/; // Change this line
let result = myRegex.test(myString); // Change this line
```

## CAPTURE GROUPS

Say you want to match a word that occurs multiple times like below.

```js
let repeatStr = "row row row your boat";
```

You could use `/row row row/`, but what if you don't know the specific word repeated? Capture groups can be used to find repeated substrings.

Capture groups are constructed by enclosing the regex pattern to be captured in parentheses. In this case, the goal is to capture a word consisting of alphanumeric characters so the capture group will be \w+ enclosed by parentheses: `/(\w+)/`.

The substring matched by the group is saved to a temporary "variable", which can be accessed within the same regex using a backslash and the number of the capture group (e.g. `\1`). Capture groups are automatically numbered by the position of their opening parentheses (left to right), starting at 1.

The example below matches a word that occurs thrice separated by spaces:

```js
let repeatRegex = /(\w+) \1 \1/;
repeatRegex.test(repeatStr); // Returns true
repeatStr.match(repeatRegex); // Returns ["row row row", "row"]
```

Use capture groups in reRegex to match a string that consists of only the same number repeated exactly three times separated by single spaces.

```js
let repeatNum = "42 42 42";
let reRegex = /^(\d+) \1 \1$/; // Change this line
let result = reRegex.test(repeatNum);
```


## EXAMPLES

1. Usernames can only use alpha-numeric characters.

2. The only numbers in the username have to be at the end. There can be zero or more of them at the end. Username cannot start with the number.

3. Username letters can be lowercase and uppercase.

4. Usernames have to be at least two characters long. A two-character username can only use alphabet letters as characters.

```js
let username = "JackOfAllTrades";
let userCheck = /^[a-z][a-z]+\d*$|^[a-z]\d\d+$/i;
let result = userCheck.test(username);
```