---
title: "User Defined Format for Parameters"
id: 1500009590281
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590281-User-Defined-Format-for-Parameters
updated_at: 2021-07-24T05:54:27Z
---

# User Defined Format for Parameters

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568602-Parameter-Application-Cases)

# User Defined Format for Parameters

This topic introduces user defined format for parameters such as date format, decimal number format, and string format.

Below is a list of the sections covered in this topic:

> * [Date Format Syntax](#Date)
> * [Decimal Number Format Syntax](#Decimal)
> * [String Format Syntax](#String)

## Date Format Syntax

How can you define formats for different types of parameters? The most commonly used are the Date and Time formats.

To specify the time format, use a time pattern string. In this pattern, all ASCII letters are reserved as pattern letters, and are defined as follows:

| Symbol | Meaning | Presentation | Example |
| --- | --- | --- | --- |
| G | Era designator | Text | AD |
| y | Year | Number | 1996 |
| M | Month in a year | Text & Number | July & 07 |
| d | Day in a month | Number | 10 |
| h | Hour in am/pm (1~12) | Number | 12 |
| H | Hour in a day (0~23) | Number | 0 |
| m | Minute in an hour | Number | 30 |
| s | Second in a minute | Number | 55 |
| S | millisecond | Number | 978 |
| E | Day in a week | Text | Tuesday |
| D | Day in a year (Julian) | Number | 189 |
| F | Day of the week in a month | Number | 2 (2nd Wed in July) |
| w | Week in a year | Number | 27 |
| W | Week in a month | Number | 2 |
| a | Am/pm marker | Text | PM |
| k | Hour in a day (1~24) | Number | 24 |
| K | Hour in am/pm (0~11) | Number | 0 |
| z | Time zone | Text | Pacific Standard Time |
| ' | Escape for text |  |  |
| '' | Single quote |  |  |

**Notes:**

* The count of pattern letters determines the format in months and years.
* Month: 4 or more pattern letters, use full form; 3 use short form in capital letters.
* Number: the minimum number of digits. Shorter numbers are zero-padded to this amount. For example M for month will show 1 digit for January - September and 2 digits for October - December. However, Year is handled in a different way. If the number of 'y' letters is 2, then the year will be truncated to 2 digits.
* Text & Number: 3 or over, uses text, otherwise uses number. For example MMM shows JAN and MM shows 01.
* Any characters in the pattern that are not in the ranges of ['a'..'z'] and ['A'..'Z'] will be treated as quoted text. For example, characters such as ':', '.', ' ', '#' and '@' will appear in the resulting time text even if they have not been single quoted.
* A pattern containing any invalid pattern letter will result in a thrown exception during formatting or parsing.
* Java will automatically show the alpha dates such as month in the user's specified language.

**Examples**

* Format Pattern: "yyyy.MM.dd G 'at' hh:mm:ss z"  
   Result: 2017.07.10 AD at 15:08:56 PDT
* Format Pattern: "EEE, MMM d, ''yy"  
   Result: Wed, July 10, 17
* Format Pattern: "h:mm a"  
   Result: 12:08 PM
* Format Pattern: "hh 'o''clock' a, zzzz"  
   Result: 12 o'clock PM, Pacific Daylight Time
* Format Pattern: "K:mm a, z"  
   Result: 0:00 PM, PST
* Format Pattern: "MMMM dd yyyy GGG hh:mm aaa"  
   Result: January 10 2017 AD 12:08 PM
* Format Pattern: "dd-MMM-yyyy"
    
  Result: 10-JAN-2017

## Decimal Number Format Syntax

| **Symbol** | **Meaning** | **Notes** |
| --- | --- | --- |
| 0 | A digit |  |
| \* | A digit, zero shows as a star | Can't mix 0, \*, and \_ in same format |
| \_ | A digit, zero shows as a space | Can't mix 0, \*, and \_ in same format |
| # | A digit, zero shows as blank | The actual number may be much larger than the format provided |
| . | Placeholder for decimal separator, it may be a comma in some locales. |  |
| , | Placeholder for grouping delimiter, it may be a period in some locales. | Shows the interval to be used |
| ; | Separates formats | positive and negative. |
| - | If there is no explicit negative sign, - is prefixed | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
| % | Divides by 100 and shows as a percentage |  |
| X | Any other characters can be used in the prefix or suffix |  |

## String Format Syntax

| Symbol | Meaning | Example |
| --- | --- | --- |
| % | Any string of zero or more characters. | WHERE title LIKE '%computer%' finds all book titles with the word 'computer' anywhere in the book title. |
| \_ (underscore) | Any single character. | WHERE au\_fname LIKE '\_ean' finds all four-letter first names that end with ean (Dean, Sean, and so on). |
| [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au\_lname LIKE '[C-P]arsen' finds author last names ending with arsen and beginning with any single character between C and P, for example Carsen, Larsen, Karsen, and so on. |
| [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au\_lname LIKE 'de[^l]%' all author last names beginning with de and where the following letter is not l. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter)

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568602-Parameter-Application-Cases)
