---
title: "Appendix 1: Barcode Symbologies"
id: 1500009562562
section: "Appendices - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562562-Appendix-1-Barcode-Symbologies
updated_at: 2021-07-24T05:56:16Z
---

# Appendix 1: Barcode Symbologies

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561702-Appendices)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582961-Appendix-2-Parameters-of-User-Defined-Web-Actions)

# Appendix 1: Barcode Symbologies

Logi JReport Designer supports ten types of barcodes: [UPC-A](#UPC-A), [UPC-E](#UPC-E), [EAN-13](#EAN-13), [EAN-8](#EAN-8), [Code 39](#Code%2039), [Code 128](#Code%20128), [Code 128A](#Code%20128A), [Code 128B](#Code%20128B), [Code 128C](#Code%20128C) and [Codabar](#Codabar). This appendix briefly describes each one. For more detailed information on the symbologies of barcodes, refer to professional barcode technical documentation.

## UPC-A

![](https://devnet.logianalytics.com/hc/article_attachments/4404894011415/apdx_brcd_upca.gif)

| UPC-A Structure (From left to right) |
| --- |
| The Number System |
| Start guard bars, always with a pattern bar+space+bar. |
| The Manufacturer Code |
| Center guard bars, with a pattern space+bar+space+bar+space. |
| The Product Code |
| End guard bars, always with a pattern bar+space+bar. |
| The Check Digit |

UPC-A (Universal Product Code-A) is of fixed length. It encodes a twelve-digit numeric only number. The final digit is a check digit, which cannot be omitted. The usual height of a UPC-A bar code is one inch. The reduced size is 80% of the nominal size.

UPC-A is a subset of EAN-13. In fact, a UPC-A barcode is an EAN-13 barcode with the first EAN-13 number system digit set to "0". This means that any hardware or software capable of reading EAN-13 is automatically capable of reading UPC-A.

Usually, the number system digit is printed on the left of the barcode, and the check digit on the right; while the manufacturer and product codes are printed just below the barcode, separated by a guard bar.

Both the left and the right guard bar are encoded with 101 (bar space bar).

Usual X dimension is 13 mils. A magnification factor of 0.8 to 2.0 is permitted and, as a result, enables a printable X dimension values range of 10.4 to 24 mils.

## UPC-E

![](https://devnet.logianalytics.com/hc/article_attachments/4404894011671/apdx_brcd_upce.gif)

| UPC-E Structure (From left to right) |
| --- |
| Start guard bars, always with a pattern bar+space+bar. |
| Left half, five digits calculated from the equivalent UPC number. |
| Check digit. |
| Stop guard bars, always with a pattern bar+space+bar. |

UPC-E (Universal Product Code-E) is fixed in length and is a compressed six-digit code used for marking small packages including magazines and paperback books. The printed value of the UPC-E code is a twelve-digit code. UPC-E symbols are UPC-A symbols that have been zero suppressed (that is, consecutive zeros are not included in the symbol). The nominal height for the UPC-E bar code is one inch. The reduced size is 80% of the nominal size.

The left guard bar is encoded with 101, and the right guard bar is encoded with 010101.

## EAN-13

![](https://devnet.logianalytics.com/hc/article_attachments/4404889431191/apdx_brcd_ean13.gif)

| EAN-13 Structure (From left to right) |
| --- |
| The Number System |
| Start guard bars, always with a pattern bar+space+bar |
| The Manufacturer Code |
| Central guard bars, always with a pattern space+bar+space+bar+space |
| The Product Code |
| The Check Digit |
| End guard bars, always with a pattern bar+space+bar |

The EAN/JAN-13 is of fixed length and is similar to the UPC-A symbology, but encodes a 13th digit. Also, the 12th and 13th digits of an EAN-13 may represent a country code in its entirety or just the beginning of one, and can vary from 2 to 3 digits. The codes 00-04 and 06-09 have been assigned to the United States. The nominal height for the EAN-13 bar code is one inch. The reduced size is 80% of the nominal size.

## EAN-8

![](https://devnet.logianalytics.com/hc/article_attachments/4404889431447/apdx_brcd_ean8.gif)

| EAN-8 Structure (From left to right) |
| --- |
| Start guard bars, always with a pattern bar+space+bar |
| Two number system characters, encoded with character set A |
| The following two characters, encoded with character set A |
| Center guard bars, with a pattern space+bar+space+bar+space |
| Last three characters, encoded in character set C |
| Stop guard bars, always with a pattern bar+space+bar |

The EAN-8 is fixed length and is similar to the UPC-E code, but includes two more digits for the country code. The nominal height for the EAN-8 bar code is one inch. The reduced size is 80% of the nominal size.

## Code 39

![](https://devnet.logianalytics.com/hc/article_attachments/4404894011927/apdx_brcd_cd39.gif)

| Code39 Structure (From left to right) |
| --- |
| A start character – the asterisk (\*) |
| Message encoded |
| A stop character – the second asterisk (\*) |

Code 39 is of variable length and is the most frequently used symbology in industrial bar code systems today. The principal feature is that it encodes messages using a full alphanumeric character set. Three of the nine elements (bars) are wide and six elements are narrow. The Code 39 barcode uses four special characters "$", "/", "+", and "%" which allow a full ASCII character set when paired with alphanumeric characters.

Code 39 is designed to encode 26 upper case letters, 10 digits and 7 special characters:

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z   
 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  
 -, ., \*, $, /, +, %, SPACE.

It is called code 39 or three of nine because each encoded character is made up of 5 bars and 4 spaces to make a total of 9 elements. Also 3 out of the 9 elements are always wide.

The height of the bars must be at least 0.15 times the symbol's length or 0.25 inches, whichever is larger.

Code 39 is a discrete symbology. Two adjacent characters are separated by an inter-character gap. To achieve good barcode quality, the width of the inter-character gap should equal the width of the narrowest element, called X.

Code39 requires a starting quiet zone with a minimum 10 times the X dimension or 0.10 inch, whichever is greater. The same width requirement also applies to the trailing quiet zone.

## Code 128

![](https://devnet.logianalytics.com/hc/article_attachments/4404894012183/apdx_brcd_cd128.gif)

| Code128 Structure (From left to right) |
| --- |
| A start character |
| Message encoded |
| Check character |
| Stop Character |
| Termination bar (bar+space+bar) |

Code 128 is of variable length and encodes a full 128 ASCII character set. Each character is represented by 11 modules that can be one of four bar widths. Also, the encoding should not exceed 232 characters (including the starting and ending codes).

Among all the common linear symbologies, Code 128 is the most flexible. It supports both alpha and numeric characters easily, has the highest number of characters per inch, and is of variable length. Code 128 is usually the best choice when implementing a new symbology.

Check code is optional. Refer to the Code 128 code table to calculate it.

In an open system, the minimum value of the X dimension is 7.5 mils, and the minimum bar height is 15 percent of the symbol length or 0.25 inches, whichever is greater. The starting and trailing quiet zones are at least 0.25 inches wide.

## Code 128A

![](https://devnet.logianalytics.com/hc/article_attachments/4404894012439/apdx_brcd_cd128a.gif)

Code 128A allows for upper case characters, punctuation and numbers. Lower case characters create several special functions in Code 128A such as a return or tab. It may be necessary to use Code 128A to manually encode these functions in a barcode.

Code 128A includes all of the standard upper case alphanumeric keyboard characters plus the control and special characters.

## Code 128B

![](https://devnet.logianalytics.com/hc/article_attachments/4404894012695/apdx_brcd_cd128b.gif)

Code 128B is the most common because it encodes everything from ASCII 32 to ASCII 126. It allows for upper and lower case letters, punctuation, numbers and a few select functions.

Code 128B includes all of the standard upper and lower case alphanumeric keyboard characters and special characters.

## Code 128C

![](https://devnet.logianalytics.com/hc/article_attachments/4404889431703/apdx_brcd_cd128c.gif)

Code 128C encodes only numbers containing an even number of characters. Since the numbers are "interleaved" into pairs, with two numbers encoded into every barcode character, a very high-density barcode is created. If the number that is to be encoded does not contain an even number of characters, a leading zero will be added.

Code 128C includes a set of 100 numeric data character pairs from 00 through 99 inclusive, and also includes special characters. This enables double-density numeric digits (two digits per bar coded character) to be encoded. Data encoded in a Code 128C must contain an even number of characters. If the data contains an odd number of characters, a zero (0) will be inserted at the beginning of the bar code.

## Codabar

![](https://devnet.logianalytics.com/hc/article_attachments/4404894012951/apdx_brcd_cdbr.gif)

| Codabar Structure (From left to right) |
| --- |
| A start character from 4 choices: A, B, C and D. |
| Inter-character gap space |
| Encoded message |
| A stop character from 4 choices: A, B, C and D. |

Character set: 0 1 2 3 4 5 6 7 8 9 - $ . : / + \*

Starting code and ending code can be A, B, C or D.

Every character is represented by 4 black bars + 3 white spaces. Variable length, maximum 32 characters (including the starting and ending codes).

**Code table**

| Code | Logic |
| --- | --- |
| 0 | 0000011 |
| 1 | 0000110 |
| 2 | 0001001 |
| 3 | 1100000 |
| 4 | 0010010 |
| 5 | 1000010 |
| 6 | 0100001 |
| 7 | 0100100 |
| 8 | 0110000 |
| 9 | 1001000 |
| a | 0011010 |
| b | 0101001 |
| c | 0001011 |
| d | 0001110 |
| - | 0001100 |
| $ | 0011000 |
| . | 1010100 |
| / | 1010001 |
| : | 1000101 |
| + | 0010101 |

Digit 1, 3, 5 and 7 - black bar, 0 represents slim bar, and 1 represents thick bar.

Digit 2, 4 and 6 - white space, 0 represents slim space, and 1 represents thick space.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561702-Appendices)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582961-Appendix-2-Parameters-of-User-Defined-Web-Actions)
