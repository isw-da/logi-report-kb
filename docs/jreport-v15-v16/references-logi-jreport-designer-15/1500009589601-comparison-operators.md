---
title: "Comparison Operators"
id: 1500009589601
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589601-Comparison-Operators
updated_at: 2021-07-24T05:54:36Z
---

# Comparison Operators

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568302-Math-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568282-Boolean-Operators)

# Comparison Operators

Below is a list of the Comparison operators used in Logi JReport Designer:

> * [x > y](#1)
> * [x < y](#2)
> * [x == y](#3)
> * [x <> y or x != y](#4)

## x > y

### date x > date y

If x is greater than y, the return value will be true. If x is < and == y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToDate(1999, 10, 10) > ToDate(1999, 2, 5)`

### datetime x > datetime y

If x is greater than y, the return value will be true. If x is < and == y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToDateTime(1999, 10, 10, 10, 10, 10) > ToDateTime(1999, 5, 10, 8, 5, 5)`

### numeric x > numeric y

If x is greater than y, the return value will be true. If x is < and == y, the return value will be false.

**Examples**

* The return value of the following statement is true.

  `3>2.56`
* The return value of the following statement is false.

  `5.29>7.55`

### string x > string y

If x is greater than y, the return value will be true. If x is < and == y, the return value will be false.

**Examples**

* The return value of the following statement is true.

  `"string abcd" > "string abc"`
* The return value of the following statement is false.

  `"string abc" > "string abcd"`

### time x > time y

If x is greater than y, the return value will be true. If x is < and == y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToTime(10, 10, 10) > ToTime(8, 10, 10)`

## x < y

### date x < date y

If x is less than y, the return value will be true. If x is > and == y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToDate(1999, 10, 10) < ToDate(1999, 2, 5)`

### datetime < datetime y

If x is less than y, the return value will be true. If x is > and == y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToDateTime(1999, 10, 10, 10, 10, 10) < ToDateTime(1999, 5, 10, 8, 5, 5)`

### numeric x < numeric y

If x is less than y, the return value will be true. If x is > and == y, the return value will be false.

**Examples**

* The return value of the following statement is true.

  `2.56<3`
* The return value of the following statement is false.

  `7.55<5.88`

### string x < string y

If x is less than y, the return value will be true. If x is > and == y, the return value will be false.

**Examples**

* The return value of the following statement is true.

  `"string abc" < "string abcd"`
* The return value of the following statement is false.

  `"string abcd" < "string abc"`

### time x < time y

If x is less than y, the return value will be true. If x is > and == y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToTime(10, 10, 10) < ToTime(8, 10, 10)`

## x == y

### date x == date y

If x is equal to y, the return value is true. If x is not equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToDate(1999, 10, 10) == ToDate(1999, 5, 10)`

### datetime == datetime y

If x is equal to y, the return value will be true. If x is not equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToDateTime(1999, 10, 10, 5, 10, 10) == ToDateTime(1999,10, 10, 10, 10, 10)`

### numeric x == numeric y

If x is equal to y, the return value will be true. If x is not equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`5==4`

### string x == string y

If x is equal to y, the return value is true. If x is not equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`"string abcd" == "string abc"`

### time x ==  time y

If x is equal to y, the return value will be true. If x is not equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`ToTime(9, 10, 10) == ToTime(10, 10, 10)`

## x <> y or x != y

### date x <> date y   or date x != date y

If x is not equal to y, the return value will be true. If x is equal to y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToDate(1999, 10, 10) != ToDate(1999, 5, 10)`

### datetime x <> datetime y or datetime x != datetime y

If x is not equal to y, the return value will be true. If x is equal to y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToDateTime(1999, 10, 10, 5, 10, 10) != ToDateTime(1999,10, 10, 10, 10, 10)`

### numeric x <> numeric y or numeric x != numeric y

If x is not equal to y, the return value will be true. If x is equal to y, the return value will be false.

**Example**

The return value of the following statement is false.

`4 <> 4`

### string x <> string y or string x != string y

If x is not equal to y, the return value will be true. If x is equal to y, the return value will be false.

**Example**

The return value of the following statement is true.

`"string abc" != "string abcd"`

### time x <> time y or time x != time y

If x is not equal to y, the return value will be true. If x is equal to y, the return value will be false.

**Example**

The return value of the following statement is true.

`ToTime(9, 10, 10) <> ToTime(10, 10, 10)`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568302-Math-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568282-Boolean-Operators)
