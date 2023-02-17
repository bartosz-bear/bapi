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
