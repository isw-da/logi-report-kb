---
title: "String Functions"
id: 1500009568262
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions
updated_at: 2021-07-24T05:54:37Z
---

# String Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions)

# String Functions

Below is a list of the strings used in Logi JReport Designer:

> * [Asc()](#Asc)
> * [ByteToText()](#ByteToText)
> * [Chr()](#Chr)
> * [ExchGetId()](#ExchGetId)
> * [ExchGetOrganization()](#ExchGetOrganization)
> * [ExchGetPath()](#ExchGetPath)
> * [ExchGetSite()](#ExchGetSite)
> * [ExtractString()](#ExtractString)
> * [filter()](#filter)
> * [InStr()](#InStr)
> * [join()](#join)
> * [LastIndexOf()](#LastIndexOf)
> * [Left()](#Left)
> * [Length()](#Length)
> * [LooksLike()](#LooksLike)
> * [LowerCase()](#LowerCase)
> * [Mid()](#Mid)
> * [NumericText()](#NumericText)
> * [Picture()](#Picture)
> * [ProperCase()](#ProperCase)
> * [ReplaceString()](#ReplaceString)
> * [ReplicateString()](#ReplicateString)
> * [Right()](#Right)
> * [Soundex()](#Soundex)
> * [Space()](#Space)
> * [StrCmp()](#StrCmp)
> * [StringSplit()](#StringSplit)
> * [strReverse()](#strReverse)
> * [toLongString()](#toLongString)
> * [ToNumber()](#ToNumber)
> * [toString()](#toString)
> * [ToText()](#ToText)
> * [ToWords()](#ToWords)
> * [Translate()](#Translate)
> * [Trim()](#Trim)
> * [TrimLeft()](#TrimLeft)
> * [TrimRight()](#TrimRight)
> * [UpperCase()](#UpperCase)
> * [Val()](#Val)

## Asc(Char a)

This function evaluates the ASCII value of the first character of the argument.

**Parameter**

a - A Char value.

**Return value**

The return value is an Integer.

**Example**

The return value of the following statement is 97.

`Asc("abc")`

## ByteToText(byte)

This function will return the size of a message in the "appropriate" unit.

* If the parameter is less than 1024, the result will be in bytes.
* If the parameter is between 1024 and 1048576, then the result will be in kilobytes.
* Otherwise, the result will be in megabytes.

**Parameter**

Byte is the size of a message in bytes.

**Return value**

String.

**Examples**

* `ByteToText(1000)` - Returns 1000 bytes.
* `ByteToText(251561)` - Returns 245 KB.
* `ByteToText(10000000)` - Returns 9 MB.
* `ByteToText(25454464)` - Returns 24 MB.

## Chr(Integer a)

This function returns a single character string associated with the ASCII value passed as the argument.

**Parameter**

a - A BigInt value.

**Return value**

The return value is a String.

**Examples**

* The return value of the following statement is character c.

  `Chr(99)`
* The return value of the following statement is character {.

  `Chr(123)`

## ExchGetId (address)

This function will begin by determining whether the address is in X500 or X400 format. Once this has been ascertained, the function will then determine the ID.

* If the field is in X500 format, the function will extract the last instance of the "CN=" code (not case sensitive)
* If the field is in the X400 format, it will extract the SMTP or MS Ids.

**Note:** The fields must follow the address type standards for the functions to operate them.

**Parameter**

address - The address of sender/recipient (String data type).

**Return value**

String value.

**Examples**

* `ExchGetID("/o=Jinfonet Software/ou=Logi JReport /cn=Configuration/cn=Servers/cn=ESPRESSO/cn=Fredt")` - Returns "Fredt".
* `ExchGetID("c=US ;a= ;p=Jinfonet; o=apps-wga; dda:smtp=Jenny@jinfonet.com")` - Returns "Jenny@jinfonet.com".
* `ExchGetID("c=US; a= ;p=Jinfonet;o=apps-wga;dda:ms=com/Logi JReport/Jenny")` - Returns "com/Logi JReport/Jenny".

## ExchGetOrganization(address)

This function will begin by determining whether the address is in X500 or X400 format. Once this has been ascertained, the function will then determine the Organization Name.

* If the field is in X500 format, the function will extract the last instance of the "/O=" code (not case sensitive).
* If the field is in the X400 format, it will extract the instance of the "P=" code (not case sensitive).

**Note:** The fields must follow the address type standards for the functions to operate on them.

**Parameter**

address - The address of the sender/recipient (String data type).

**Return value**

String value.

**Examples**

* `ExchGetOrganization("c=US ;a= ;p=Jinfonet; o=apps-wga; dda:ms=com/Logi JReport/Jenny")` - Returns "Jinfonet".
* `ExchGetOrganization("c=US ;a= ;p=Jinfonet; o=apps-wga; dda:smtp=Jenny@jinfonet.com")` - Returns "Jinfonet".

## ExchGetPath(path)

This function will return the container information in an address field.

* If the address type is X500, the function will return all of the information from the first instance of the "CN=" code until the last instance of the "CN=" code. If there is only one instance of the "CN=" code, the function will return NULL.
* If the address type is X400, the function will return all "OU\*=" codes (residing between the "P=" and "O=" codes).
* If the address starts with "DDA:", the function will return all information after the "DDA:" code.
* If the field is blank, "UNKNOWN ADDRESS" will be returned.

**Parameter**

path - The address of sender/receiver (String data type).

**Examples**

* `ExchGetPath("/o=Jinfonet Software/ou=Logi JReport /cn=Configuration/cn=Servers/cn=ESPRESSO/cn=Fredt")` - Returns "cn=Configuration/cn=Servers/cn=ESPRESSO".
* `ExchGetPath("c=US; a= ; p=Jinfonet; ou1=Jenny; ou2=Logi JReport; o=apps-wga;")` - Returns "ou1=Jenny; ou2=Logi JReport".
* `ExchGetpath("DDA:MS=Logi JReport/JENNY/Logi JReport")` - Returns "MS=Logi JReport/JENNY/Logi JReport".

## ExchGetSite(address)

The function will begin by determining whether the address is in X500 or X400 format. Once this has been ascertained, the function will then determine the Site Name.

* If the field is in X500 format, the function will extract the last instance of the "/OU=" code (not case sensitive).
* If the field is in the X400 format, it will extract the instance of the "O=" code (not case sensitive).

**Note:** The fields must follow the address type standards for the functions to operate on them.

**Parameter**

address - The address of sender/recipient (String data type).

**Return value**

String value.

**Examples**

* `ExchGetSite("/o=Jinfonet Software/ou=Logi JReport/cn=Configuration/cn=Servers/cn=ESPRESSO/cn=Fredt")` - Returns "Logi JReport".
* `ExchGetSite("c=US; a= ;p=Jinfonet;o=apps-wga; dda:smtp=Jenny@jinfonet.com")` - Returns "apps-wga".

## ExtractString(String origin, String start, String end)

This function is used to evaluate an origin string and returns the first occurrence of a String that starts with the Start String and ends with the End String (the End String is excluded). If the End String is not found, the string that starts with the Start String till its end will be returned.

**Parameters**

* origin - A String value.
* start - A String value.
* end - A String value.

**Return value**

The return value is a String.

**Examples**

* The return value of the following statement is a String *day*.

  `ExtractString("one day after that day", "d", " ")`
* The return value of the following statement is *day after that day*.

  `ExtractString("one day after that day", "d", "c")`
* ExtractString("The rain in Spain falls on the plain","rain", "plain")
  - Returns *rain in Spain falls on the*.

## filter(inString, searchString)

This function is designed to search the string in the specified strings. It searches an array of strings for a specified string, and returns the strings in an array.

**Overloads**

* filter(inString, searchString)
* filter(inString, searchString, include)
* filter(inString, searchString, include, compare)

**Parameters**

* inString - An array of string which you want to find the search string from.
* searchString - A String which you want to search for.
* include - An optional Boolean value indicating whether to return substrings that include or exclude searchString. If include is True, Filter returns the subset of the array that contains searchString as a substring. If include is False, Filter returns the subset of the array that does not contain searchString as a substring. If omitted, the value True will be used.
* compare - An optional Number value indicating the kind of string comparison to use,
  + 0 performs a comparison that is case sensitive.
  + 1 performs a comparison that is case insensitive.
  + If omitted, a case sensitive comparison is performed.

**Return value**

Array of String values.

**Examples**

Suppose that inString = [ "abc", "Abc", "abcdfg", "asdfabc", "sdfdfd"], searchString = "abc"

* `filter(inStrings, searchString)` - Returns ["abc", "abcdfg", "asdfabc"].
* `filter(inStrings, searchString, true)` - Returns ["abc", "abcdfg", "asdfabc"].
* `filter(inStrings, searchString, false)` - Returns ["abc"].
* `filter(inStrings, searchString, true, 0)``]"asdfabc", "abcdfg", "abc"- Returns [`
* `filter(inStrings, searchString, true, 1)` - Returns ["abc", "Abc", "abcdfg", "asdfabc"].
* `filter(inStrings, searchString, false, 1)` - Returns ["abc", "Abc"].
* `string inString[]=["John","Paul","George","Ringo"];   
  join(filter(inString,"o"),",");` 

  This formula can search strings which include the word "o" and use comma to compart them.

## InStr()

### InStr(String a, String b)

This function returns the position of the first occurrence of one string within another. If String a is not found in String b, the InStr function will return -1.

**Parameters**

* a - A String value to be sought.
* b - A String value to be searched.

**Return value**

The return value is an Integer.

**Examples**

* The return value of the following statement is 6.

  `InStr("my", "he is my brother")`
* The return value of the following statement is -1.  

  `InStr("our", "she is my mother")`
* `String value = toText(@Price, "####.##", 2, "", ".");   
  integer dot = InStr(".", value);   
    
  if (dot >= 0)   
  {   
  return ToWords(ToNumber(left(value, dot)), 0) + " dollars "   
  +ToWords(ToNumber(mid(value, dot + 1)), 0) + " cents";   
  }   
  else   
  {   
  return ToWords(ToNumber(value), 0) + " dollars";   
  }`

  This formula can convert number format to dollars and cents pattern.

### InStr(Number a, String b, String c)

This function returns the position of the first occurrence of one string within another, starting at the position specified by argument a. If String c is not found in String b, the InStr function will return -1.

**Parameters**

* a - A BigInt value that is the character position in String b where the search is to begin.
* b - A String value to be searched.
* c - A String value to be sought.

**Return value**

The return value is an Integer.

**Examples**

* The return value of the following statement is 6.

  `InStr(3, "he is my brother", "my")`
* The return value of the following statement is -1.

  `InStr(3, "he is my brother", "our")`

## join(stringArray)

Returns a string created by joining a number of substrings contained in an array.

**Overloads**

* join(stringArray)
* join(stringArray, delimiterString)

**Parameters**

* stringArray - A String array containing substrings to be joined.
* dimiterString - An optional String used to separate the substrings in the returned string. If omitted, the space character (" ") is used. If the delimiter is a zero-length string(" "), then all items in the list will be concatenated with no delimiters.

**Return value**

String value.

**Examples**

Assume that the stringArray list in the examples consists of the following three elements: Welcome, Use and Logi JReport.

* `join(list)` - Returns the string **Welcome Use Logi JReport**.
* `join(list, ", ")` - Returns the string **Welcome, Use, Logi JReport**.

## LastIndexOf()

### LastIndexOf(String a, String b)

This function returns the position of the last occurrence of one string within another, if String b is not found in String a, the InStr function will return -1.

**Parameters**

* a - A String value to be searched.
* b - A String value to be sought.

**Return value**

The return value is an Integer.

**Examples**

* The return value of the following statement is 9.

  `LastIndexOf("avcievmgbvi","v")`
* The return value of the following statement is -1.

  `LastIndexOf("avcievmgbvi","n")`

### LastIndexOf(BigInt a, String b, String c)

This function returns the position within this string of the first occurrence of the specified substring, searching backward starting at the position specified by argument a. If String c is not found in String b, the InStr function will return -1.

**Parameters**

* a - A BigInt value that is the character position in String b where the search is to end.
* b - A String value to be searched.
* c - A String value to be sought.

**Return value**

The return value is an Integer.

## Left(String a, Number b)

This function returns a substring that contains the specified number of characters from the left side of a string.

**Parameters**

* a - A String value.
* b - A BigInt value indicating the number of characters to be extracted from String a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is he is.

`Left("he is my father", 5)`

## Length(String a)

This function returns the number of characters in a String.

**Parameter**

a - A String value.

**Return value**

The return value is an Integer.

**Example**

The return value of the following statement is 16.

`Length("she is my mother")`

## LooksLike(String a, String b)

This function enables you to locate field values using standard DOS wildcards ( ? is a wildcard for a single character, \* is a wildcard for any number of characters). It does this by comparing a String to a mask which contains one or more wildcards. The function returns True if the string matches the mask, and False if the string does not match the mask.

**Parameters**

* a - A String value to be compared to the mask.
* b - A String that provides a mask for comparing the value in String a.

**Return value**

The return value is True or False.

**Examples**

* The return value of the following statement is False.

  `LooksLike("he is my brother", "he is my brother and friend")`
* The return value of the following statement is True.

  `LooksLike("he is my brother", "he is my brother")`
* `LooksLike("George Peck", "G?orge*")` - Returns True.

## LowerCase(String a)

This function returns a String that contains all lowercase letters converted from String a.

**Parameter**

a - A String value.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is this is her book.

`LowerCase("This is HER book")`

## Mid()

### Mid(String a, Number b)

This function returns a number of characters from a specified position of a String.

**Parameters**

* a - A String value to be extracted.
* b - A BigInt value indicating the position of the first character to extract.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is my father.

`Mid("he is my father", 6)`

### Mid(String a, BigInt b, BigInt c)

This function returns a specified number of characters from a specified position of a String.

**Parameters**

* a - A String value to be extracted.
* b - A BigInt value indicating the position of the first character to extract.
* c - A BigInt value indicating the number of characters to be extracted from String a.

**Return value**

The return value is a String.

**Examples**

* `Mid("he is my father", 9, 6)` - Returns "father".
* `Integer ln,i;   
   String str1;   
   str1="";   
   ln=length(@col);   
   for (i=1;i<ln ; i=i+1)   
   str1=str1 + mid(@col, i, 1) + "\n";   
   return str1;` 

  This formula can convert a DBField string from a normal horizontal pattern to a vertical pattern.

## NumericText(String a)

This function is used to test if the content of the string is a Number.

**Parameter**

a - A String value to be tested.

**Return value**

The return value is Boolean.

**Examples**

* The return value of the following statement is False.

  `NumericText("she is my mother")`
* The return value of the following statement is True.

  `NumericText("123456")`

## Picture(String a, String b)

This function prints a string or values in a string in a predetermined format.

**Parameters**

* a - A String value to be formatted according to the picture format.
* b - A String value representing the way you want the characters in the string to be printed.

**Return value**

The return value is a string.

**Examples**

* The return value of the following statement is *Brother Tom*.

  `Picture("Brother", "XxXXxxx Tom")`
* The return value of the following statement is *He is Tom*.

  `Picture("He Tom", "xx is")`
* `Picture("8007733472", "Phone: (xxx) xxx-xxxx")` - Returns *Phone: (800) 773-3472*.

## ProperCase()

Capitalizes the first letter in a text string and any other letter that follows a character other than a letter, and converts all other letters to lowercase letters.

**Overloads**

ProperCase(String)

**Parameter**

String - A text string.

**Return value**

String value.

**Examples**

* ProperCase('LINDA FONG') - Return "Linda Fong".
* ProperCase("123Michael's") - Return "123Michael'S".
* ProperCase("2-cent's worth") - Return "2-Cent'S Worth".
* ProperCase('76BudGet') - Return "76Gudget".

## ReplaceString(inString, searchString, replaceString, startPosition, count, compare)

Returns a String in which a specified substring has been replaced with another substring a specified number of times. As an option, you can also specify a location in the string where the replacing process will begin from (returns a string starting from that position). This function is typically used in a string to systematically replace one substring with another.

**Overloads**

* ReplaceString(inString, searchString, replaceString)
* ReplaceString(inString, searchString, replaceString, startPosition)
* ReplaceString(inString, searchString, replaceString, startPosition, count)
* ReplaceString(inString, searchString, replaceString, startPosition, count, compare)

**Parameters**

* inString - A String containing substring to replace.
* searchString - A substring being searched for.
* replaceString - The replacement substring.
* startPosition - An optional Number indicating the position within inString where the substring search is to begin from. If omitted, 1 will be used.
* count - An optional Number of substring substitutions to be performed. If omitted, the default value is -1, which means make all possible substitutions.
* compare - An optional Number indicating the kind of comparison to use when evaluating substrings:
  + 0 performs a comparison that is case-sensitive
  + 1 performs a comparison that is case-insensitive
  + If omitted, a case-sensitive comparison will be performed

**Return value**

String value.

**Examples**

Assume that inStrings = "abc Abc abcdfg asdfabc sdfdfd", searchString = "abc", replaceString = "ABC".

* `ReplaceString(inStrings, searchString, replaceString)` - Returns "ABC Abc ABCdfg asdfABC sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 5)` - Returns "abc Abc ABC dfg asdfABC sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 0)` - Returns "ABC Abc ABCdfg asdfABC sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 0, 0)` - Returns "abc Abc abcdfg asdfabc sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 0, 1)` - Returns "ABC Abc abcdfg asdfabc sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 0, -1,1)` - Returns "ABC ABC ABCdfg asdfABC sdfdfd".
* `ReplaceString(inStrings, searchString, replaceString, 0, -1, 0)` - Returns "ABC Abc ABCdfg asdfABC sdfdfd".

**Note:** The return value of the replace function is a String, with the specified substring replacements made, beginning at the position specified by startPosition, and endings at the end of the inString string. It is not a start to finish copy of the original string.

## ReplicateString(String a, Integer b)

This function replicates the string in String a the number of times specified by b.

**Parameters**

* a - A String value to be replicated.
* b - A BigInt value indicating the number of times that String a is to be replicated.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is Stop! Stop! Stop!.

`ReplicateString("Stop!", 3)`

## Right(String a, Integer b)

This function is used to extract the specified number of characters in String a from the right side.

**Parameters**

* a - A String value to be extracted.
* b - A BigInt value indicating the number of characters to be extracted from String a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is mother.

`Right("She is my mother", 6)`

## Soundex(string)

Evaluates a text string and returns a four-character value that symbolizes the way the string sounds. Use this function whenever you want to locate records based on two or more field values that are spelled differently yet sound alike. This function can also be used to find customer names that have been misspelled.

**Parameter**

String is one of two or more strings that sound alike.

**Return value**

Text string.

**Examples**

* `Soundex("Jinfonet")` - Returns *J515*.
* `if (Soundex("George") == Soundex("gorge")) then   
  "Sound the same"   
  else   
  "Different sound"`

  - Returns *Sound the same*.

**Notes**:

* The value string must be in quotes.
* Soundex works only with values that begin with the same letter. For example, Soundex will return the same value for Chris and Cris **C620** but not for Kris K620.
  Soundex creates a code based on the first character in the string plus three characters based on the following:
  + Non-alpha characters like numbers and punctuation become -1.
  + The characters a, e, i, o, u, y, h, and w are ignored (except when they are the first character in the original string).
  + The characters b, f, p, and v become 1.
  + The characters c, g, j, k, q, s, x, and z become 2.
  + The characters d and t become 3.
  + The character l becomes 4.
  + The characters m and n become 5.
  + The character r becomes 6.
* If the resulting code is only 2 or 3 characters long, Soundex uses zeros to fill it out to four characters. For example, in the name Lauren, only the L, r, and n are translated (Lrn), so the resulting Soundex code becomes L650.
* If the resulting code is more than four characters long, all characters after the fourth character will be ignored. For example, in the name Patrick, the P, t, r, c, and k can be translated (Ptrck), but the resulting Soundex code will only be four characters P362.

## Space(Integer a)

This function returns a String value that contains a specified number of spaces.

**Parameter**

a - A BigInt value indicating the number of spaces.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is   .

`Space(3)`

## StrCmp(String a, String b)

This function is used to compare two strings. It returns positive if String a is greater than String b, returns 0 if String a is equal to String b, and returns negative if String a is less than String b.

**Parameters**

* a- A String value.
* b- A String value.

**Return value**

The return value is an Integer.

**Examples**

* The return value of the following statement is -1.

  `StrCmp("He is Tom", "I am student")`
* The return value of the following statement is 0.

  `StrCmp("He is Tom", "He is Tom")`
* The return value of the following statement is 1.

  `StrCmp("I am student", "He is Tom")`

## StringSplit(inString, delimiterString, count, compare)

This function takes a String that contains a number of substrings, breaks it up into a specified number of substrings and returns an array containing the substrings.

**Overloads**

* stringSplit(inString)
* stringSplit(inString, delimiterString)
* stringSplit(inString, delimiterString, count)
* stringSplit(inString, delimiterString, count, compare)

**Parameters**

* inString - A String expression containing substrings and delimiters.
* delimiterString - An optional String character used to identify substring limits. If omitted, the space character (" ") is assumed to be the delimiter. If the delimiter is a zero-length string, a single-element array containing the entire inString string will be returned.
* count - An optional Number value of substrings to be returned. The value -1 indicates that all substrings will be returned. If omitted, -1 will be used.
* compare - An optional Number indicating the kind of comparison to use when evaluating the delimiter string:
  + 0 performs a comparison that is case-sensitive.
  + 1 performs a comparison that is case-insensitive.
  + If omitted, a case-sensitive comparison is performed.

**Return value**

Array of String values.

**Examples**

Assume that inString = "Welcome use Logi JReport"

* `StringSplit(inString)` - Returns [ "Welcome", "use", "Logi JReport"]
* `StringSplit(inString, "use")` - Returns [ "Welcome", "Logi JReport"]
* `StringSplit(inString, " ", 2)` - Returns [ "Welcome", "use Logi JReport"]

**Note:** If count, c, is less than the total number of substrings in inString, then at most c substrings will be returned as elements in the resultant array. The last element in the array is a concatenation of the substring and all the remaining substrings.

## strReverse(inString)

This function is designed to reverse the string. It returns a String in which the character order of inString is reversed. If inString is a zero-length string (" "), a zero-length string will be returned.

**Parameter**

inString - A String whose characters are to be reversed.

**Return value**

String value.

**Examples**

* `strReverse("abc")` - Returns cba.
* `strReverse("false")` - Returns eslaf.

## toLongString(String a)

This function converts a string to a long string.

**Parameter**

a - A String value.

**Return value**

The return value is a LongString.

**Example**

The return value of the following statement is aa.

`LongString a=toLongString("aa");  
string b="bb";  
if (b > toString(a)) then   
return a  
else   
return toLongString(b);`

## ToNumber()

### ToNumber(Currency a)

This function converts a Currency to a Number.

**Parameter**

a - A Currency value.

**Return value**

The return value is a Number.

**Examples**

* The return value of the following statement is 4.32.

  `ToNumber($4.32)`
* The result value of the following statement is 4.68.

  `ToNumber($4.68)`

### ToNumber(String a)

This function converts a specified string to a Number.

**Parameter**

a - A Char value.

**Return value**

The return value is a Number.

**Example**

The return value of the following statement is 123.00.

`ToNumber("123")`

**Note:** In this function, the format of the string should be [#] or [#].[#]. If you input a character string as the argument, the return value will be NULL.

## toString(LongString a)

This function converts a long string to a string.

**Parameter**

a - A LongString value.

**Return value**

The return value is a String.

**Examples**

The return value of the following statement is aa.

`LongString a=toLongString("aa");  
 string b="bb";  
 if (b > toString(a)) then   
 return a  
 else   
return toLongString(b);`

## ToText()

### ToText(Bit a)

This function converts a Bit value to a String, either true or false.

**Parameter**

a - A Bit value.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is false.

`ToText(3<2)`

### ToText(Currency a)

This function converts a Currency value to a String.

**Parameter**

a - A Currency value to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $123.45.

`ToText($123.45)`

### ToText(Currency a, String b)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* b - A String indicating the format for displaying the value in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $123.45.

`ToText($123.45, "$##0.00")`

### ToText(Currency a, String b, Integer c)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $123.5.

`ToText($123.456, "$##0.00", 1)`

### ToText(Currency a, String  b, Integer c, String d)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $1\*234.57.

`ToText($1234.57, "$#,###.000", 2, "*")`

### ToText(Currency a, String b, Integer c, String d, String e)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Examples**

* The return value of the following statement is $4,567.123.

  `ToText($4567.123, "$#,##0.00", 3, "," , ".")`
* The return value of the following statement is $4&567\*1.

  `ToText($4567.123, "$#,##0.00", 1, "&", "*")`

### ToText(Currency a, Integer c)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* c - The number of decimal places to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $123.46.

`ToText($123.4567, 2)`

### ToText(Currency a, Integer c, String d)

This function converts a Currency value to a String.

**Parameters**

* a - A Currency value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $1,234.57.

`ToText($1234.567, 2, ",")`

### ToText(Currency a, Integer c, String d,String e)

This function converts a Currency value to a String.

**Parameters**

* a - A currency value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is $1,234.57.

`ToText($1234.567, 2, ",", ".")`

### ToText(Date a)

This function converts a Date value to a String.

**Parameter**

a - A Data value.

**Return value**

The return value is a String.

**Example**

Suppose the date is July 15,1999, the return value of the following statement is 15-Jul-99.

`ToText(ToDate(1999,7,15))`

### ToText(Date a, String b)

This function converts a Date value to a String.

**Parameters**

* a - A Date value.
* b - A String that defines how the Data value in a to be formatted.

**Return value**

The return value is a String.

**Example**

Suppose the date is July 15,1999, the return value of the following statement is 15-Jul-99.

`ToText(ToDate(1999,7,15), "dd-MMM-yy")`

### ToText(DateTime a)

This function converts a DateTime value to a String.

**Parameter**

a - A TimeStamp value to be converted.

**Return value**

The return value is a String.

**Example**

Suppose the date is July 15,1999 and time is 7:42:51, the return value of the following statement is 15-Jul-99 7:42:51 AM.

`ToText(ToDateTime(1999,7,15,7,42,51))`

### ToText(DateTime a, String b)

This function converts a DateTime value to a String.

**Parameters**

* a - A TimeStamp value to be converted.
* b - A String that defines how the DateTime value in a to be formatted.

**Return value**

The return value is a String.

**Example**

Suppose the date is July 15,1999 and time is 7:42:51, the return value of the following statement is 07-15-99 7:42:51.

`ToText(ToDateTime(1999,7,15,7,42,51), "MM-dd-yy h:mm:ss")`

### ToText(DateTime a, String b, String c)

This function converts a DateTime value to a String.

**Parameters**

* a - A TimeStamp value to be converted.
* b - A String that defines how the DateTime value in a to be formatted.
* c - A String to be used as a label for A.M. (morning) hours.

**Return value**

The return value is a String.

**Example**

Suppose the date is July 15,1999 and time is 7:42:51, the return value of the following statement is 15-Jul-99 7:42:51 AM.

`ToText(ToDateTime(1999,7,15,7,42,51), "dd-MMM-yy h:mm:ss a", "AM")`

### ToText(DateTime a, String  b, String c, String d)

This function converts a DateTime value to a String.

**Parameters**

* a - A TimeStamp value to be converted.
* b - A String that defines how the DateTime value in a to be formatted.
* c - A String to be used as a label for A.M. (morning) hours.
* d - A String to be used as a label for P.M. (evening) hours.

**Return value**

The return value is a String.

**Examples**

* Suppose the date is Oct. 7,1999 and time is 7:42:51, the return value of the following statement is 07-Oct-99 7:42:51 AM.

  `ToText(ToDateTime(1999,10,7,7,42,51), "dd-MMM-yy h:mm:ss a", "AM", "PM")`
* Suppose the date is Oct. 7,1999 and time is 18:42:51, the return value of the following statement is 07-Oct-99 6:42:51 PM.

  `ToText(ToDateTime(1999,10,7,18,42,51), "dd-MMM-yy h:mm:ss a","AM", "PM")`

### ToText(Integer a)

This function converts a BigInt value to a String.

**Parameter**

a - A BigInt value to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 456.

`ToText(456)`

### ToText(Integer a, String b)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* b - A String value indicating the format for displaying the value in argument a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 456.

`ToText(456, "###")`

### ToText (Integer a, String b, Integer c)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 456.00.

`ToText(456, "###", 2)`

### ToText(Integer a, String b, Integer c, String d)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.00.

`ToText(1234, "#,###", 2, ",", ".")`

### ToText(Integer a, String b, Integer c, String d, String e)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.00.

`ToText(1234, "#,###", 2, ",", ".")`

### ToText(Integer a, Integer c)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* c - The number of decimal places to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 123.00.

`ToText(123, 2)`

### ToText(Integer a, Integer c, String d)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.00.

`ToText(1234, 2, ",")`

### ToText(Integer a, Integer c, String d, String e)

This function converts a BigInt value to a String.

**Parameters**

* a - A BigInt value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 12,345.00.

`ToText(12345, 2, ",", ".")`

### ToText(Number a)

This function converts a Double value to a String.

**Parameter**

a - A Double value to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 123.456.

`ToText(123.456)`

### ToText(Number a, String b)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* b - A String indicating the format for displaying the value in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1236.46.

`ToText(1236.456, "###0.00")`

### ToText(Number a, String b, Integer c)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.

**Return value**

The return value is a string.

**Example**

The return value of the following statement is 123.46.

`ToText(123.456, "###.00", 2)`

### ToText(Number a, String b, Integer c, String d)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.57.

`ToText(1234.567, "#,###.000", 2, ",")`

### ToText(Number a, String b, Integer c, String d,String e)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* b - A String indicating the format for displaying the value in a.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.57.

`ToText(1234.567, "#,###.000", 2, ",", ".")`

### ToText(Number a, Integer c)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* c - The number of decimal places to be converted.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 123.46.

`ToText(123.456, 2)`

### ToText(Number a, Integer c, String d)

This function converts a Double value to a string.

**Parameters**

* a - A Double value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234.6.

`ToText(1234.567, 1, ",")`

### ToText(Number a, Integer c, String d, String e)

This function converts a Double value to a String.

**Parameters**

* a - A Double value to be converted.
* c - The number of decimal places to be converted.
* d - A single character string indicating the character to be used to separate thousands in a.
* e - A single character string indicating to be used as a decimal separator.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is 1,234,57.

`ToText(1234.567, 2, "," , ",")`

### ToText(Time a)

This function converts a Time value to a String.

**Parameter**

a - A Time value.

**Return value**

The return value is a String.

**Example**

Suppose the time is 12:40:30, the return value of the following statement is 12:40:30 PM.

`ToText(ToTime(12,40,30))`

### ToText(Time a, String b)

This function converts a Time value to a String.

**Parameters**

* a - A Time value to be converted.
* b - A String that defines how the value in a to be formatted.

**Return value**

The return value is a String.

**Example**

Suppose the time is 08:48:58, the return value of the following statement is 8:48:58.

`ToText(ToTime(8,48,58), "h:mm:ss")`

### ToText(Time a, String b, String c)

This function converts a Time value to a String.

**Parameters**

* a - A Time value to be converted.
* b - A String that defines how the value in a to be formatted.
* c - A String to be used as a label for A.M. (morning) hours.

**Return value**

The return value is a String.

**Example**

Suppose the time is 8:48:58 in the morning, the return value of the following statement is 8:48:58 AM.

`ToText(ToTime(8,48,58), "h:mm:ss a", "AM")`

### ToText(Time a, String b,String c, String d)

This function converts a Time value to a String.

**Parameters**

* a - A Time value to be converted.
* b - A String that defines how the value in a to be formatted.
* c - A String to be used as a label for A.M. (morning) hours.
* d - A String to be used as a label for P.M. (evening) hours.

**Return value**

The return value is a String.

**Examples**

* Suppose the time is 08:48:58, the return value of the following statement is 8:48:58 AM.

  `ToText(ToTime(8,48,58), "h:mm:ss a", "AM", "PM")`
* Suppose the time is 21:49:59, the return value of the following statement is 9:49:59 PM.

  `ToText(ToTime(21,49,59), "h:mm:ss a", "AM", "PM")`

**Notes:**

* When converting a Double value, Currency value or a BigInt value to a String, special characters used as format in argument b are following:

  | **Symbol** | **Meaning** | **Notes** |
  | --- | --- | --- |
  | 0 | a digit |  |
  | \* | a digit, zero shows as a star | Can't mix 0, \*, and \_ in same format |
  | \_ | a digit, zero shows as a space | Can't mix 0, \*, and \_ in same format |
  | # | a digit, zero shows as absent |  |
  | . | placeholder for decimal separator |  |
  | , | placeholder for grouping delimiter | Shows the interval to be used |
  | ; | separates formats | positive and negative. |
  | - | if there is no explicit negative sign, - is prefixed | "0.00" -> "0.00;-0.00" |
  | % | divide by 100 and show as percentage |  |
  | X | any other characters can be used in the prefix or suffix |  |
* **Time format syntax:** The time format is specified by means of a String time pattern. In this pattern, all ASCII letters are reserved as pattern letters, which are defined as the following:

  | **Symbol** | **Meaning** | **Presentation** | **Example** |
  | --- | --- | --- | --- |
  | G | era designator | Text | AD |
  | y | year | Number | 1996 |
  | M | month in year | Text & Number | July & 07 |
  | d | day in month | Number | 10 |
  | h | hour in am/pm (1~12) | Number | 12 |
  | H | hour in day (0~23) | Number | 0 |
  | m | minute in hour | Number | 30 |
  | s | second in minute | Number | 55 |
  | S | millisecond | Number | 978 |
  | E | day in week | Text | Tuesday |
  | D | day in year | Number | 189 |
  | F | day of week in month | Number | 2 (2nd Wed in July) |
  | w | week in year | Number | 27 |
  | W | week in month | Number | 2 |
  | a | am/pm marker | Text | PM |
  | k | hour in day (1~24) | Number | 24 |
  | K | hour in am/pm (0~11) | Number | 0 |
  | z | time zone | Text | Pacific Standard Time |
  | ' | escape for text |  |  |
  | '' | single quote |  |  |

## ToWords()

### ToWords(Currency a)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameter**

a - A Currency value to be converted into words.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is three and 15/100.

`ToWords($3.15)`

### ToWords(Currency a, Integer b)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameters**

* a - A Currency value to be converted into words.
* b - A BigInt value indicating the number of decimal places to be converted. This argument is optional.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is three and 5/10.

`ToWords($3.45, 1)`

### ToWords(Integer a)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameter**

a - A BigInt value to be converted into words.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is twenty and xx/100.

`ToWords(20)`

### ToWords(Integer a, Integer b)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameters**

* a - A BigInt value to be converted into words.
* b - A BigInt value indicating the number of decimal places to be converted. This argument is optional.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is three and x/10.

`ToWords(3, 1)`

### ToWords(Number a)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameter**

a - A fractional number to be converted into words.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is ten and 12/100.

`ToWords(10.12)`

### ToWords(Number a, Integer b)

This function converts a Number field value or the result of a numeric calculation to words.

**Parameters**

* a - A Number value to be converted into words.
* b - A BigInt value indicating the number of decimal places to be converted. This argument is optional.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is three and 1/10.

`ToWords(3.14, 1)`

## Translate()

Used for applying the NLS feature to the formula result. For an illustrate example, see [Built-in Functions for NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009589981-Built-in-Functions-for-NLS).

### Translate(String a)

This function searches for the NLS translation of current field value in the bound data mapping file.

* **Parameter**  
   a - A String to which a corresponding data mapping file can be bound.
* **Return value**  
   The return value is a String. It is the NLS translation of the field value if a data mapping file is bound to it and the NLS translation can be found, or null if the string is null, or the string itself when the corresponding NLS translation cannot be found in the data mapping file or the file cannot be found.
* **Example**  
   The return value of the following statement is "美国" and the locale is China if the language of the data mapping file bound to it is Chinese and it contains the mapping: ["USA", "美国"].
* `Translate(@country)`, where @country has the value "USA".

### Translate(String a, String b)

This function accesses the corresponding data mapping file dynamically according to the language selected from the language drop-down list on the NLS language toolbar and searches for the NLS translation of String b in the data mapping file.

* **Parameters**  
  + a - A String, which is the prefix of the data mapping file name. For example, if the name is Category\_de\_DE.properties, set the string as Category (without the language and locale part).
  + b - A String indicating the string to be translated.
* **Return value**  
   The return value is a String. It is the NLS translation of the field value if a data mapping file is bound to it and the NLS translation can be found, or null if the string is null, or the string itself when the corresponding NLS translation cannot be found in the data mapping file or the file cannot be found.
* **Examples**  
   The return value of the following statement is "美国" and the locale is China if the language of the data mapping file bound to it is Chinese and it contains the mapping: ["USA", "美国"].
  + `Translate("mapping_file_country", "USA")`
  + `Translate("mapping_file_country", @country)`, where @country has the value "USA".

## Trim(String a)

This function is used to remove the leading and the trailing spaces from string arguments.

**Parameter**

a - A String value.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is he is a boy*.*

`Trim("he is a boy")`

## TrimLeft(String a)

This function is used to remove the spaces on the left side of the string.

**Parameter**

a - A String value to be trimmed.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is he is a boy.

`TrimLeft("he is a boy")`

## TrimRight(String a)

This function is used to remove the spaces on the right side of the string.

**Parameter**

a - A String value to be trimmed.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is he is a boy.

`TrimRight("he is a boy")`

## UpperCase(String a)

This function converts all letters in string a to uppercase letters.

**Parameter**

a - A String value.

**Return value**

The return value is a String.

**Example**

The return value of the following statement is HE IS A BOY.

`UpperCase("he is a boy")`

## Val(String a)

This function reads a string containing numbers (for example, address, phone or social security number), and converts them to a decimal value. Val stops reading when it finds the first character in the string.

**Parameter**

a - A String value.

**Return value**

The return value is a Number.

**Example**

The return value of the following statement is 63,550,513.00.

`Val("63550513Mr.Tom")`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions)
