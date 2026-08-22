---
title: "Other Operators"
id: 1500009589621
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589621-Other-Operators
updated_at: 2021-07-24T05:54:37Z
---

# Other Operators

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568282-Boolean-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590301-Object-Property-Reference)

# Other Operators

Below is a list of the other operators used in Logi JReport Designer:

> * [x in y](#in)
> * [[x, y, z]](#xyz)
> * [x[i]](#xi)
> * [x[i to j]](#xij)
> * [x[i \_to j]](#xijleft)
> * [x[i to\_ j]](#xijright)
> * [x[i \_to\_ j]](#xijboth)
> * [x[upfrom j]](#upfrom)
> * [x[upfrom\_ j]](#upfromright)
> * [x[upto j]](#upto)
> * [x[upto\_ j]](#uptoright)
> * [if(b) then{...} else{...}](#if)
> * [return x](#return)

## x in y

A statement used to tell whether x is in y, the return value is a boolean value.

**Examples**

* The return value of the following statement is false.

  `integer x[3] = [0,1,2];  
   integer xx = 3;  
   xx in x`
* `integer range intary=[30 to 50];   
   if (@"Product_ID" in intary) then   
   return "Within the Range"   
   else   
   return "Out of Range"`
* `if (@Customers_Region in ["CO","MT","UT","WY"]) then   
   "Rocky Mountain Region"   
   else   
   "Rest of Country"`

## [x, y, z]

A statement used to define an array.

**Example**

The return value of the following statement is 1996-11-27.

`date d[3] = [toDate(1997, 11, 27), toDate(1996, 11, 27), toDate(1995, 11, 27)];  
 date dd[3];  
 dd = d;  
 dd[1]`

## x[i]

A statement used to index a certain value in an array.

**Example**

The return value of the following statement is 14:11:27.

`time d[3] = [totime(12, 11, 27), totime(13, 11, 27), totime(14, 11, 27)];  
 time dd[3];  
 dd = d;  
 dd[2]`

## x[i to j]

A statement used to define an array.

**Example**

The return value of the following statement is true.

`string range strary = ["a" to "z"];  
string x = "d";  
x in strary`

## x[i \_to j]

It is used to specify a range of values greater than but not including the value i, and less than or equal to the value j. Both i and j are the type of Number.

**Example**

The return value of the following statement is true.

`integer a[] = [1,1,2,3,4];  
3 in a[2 _to 4];`

## x[i to\_ j]

It is used to specify a range of values greater than or equal to the value i, and less than but not including the j value. Both i and j are the type of Number.

**Example**

The return value of the following statement is true.

`integer a[] = [1,1,2,3,4];  
3 in a[2 to_ 4];`

## x[i \_to\_ j]

It is used to specify a range of values greater than but not including the value i, and less than but not including the value j. Both i and j are the type of Number.

**Example**

The return value of the following statement is true.

`integer a[] = [1,1,2,3,4];  
3 in a[2 _to_ 4];`

## x[upfrom j]

It is used to specify a range of values greater than or equal to the value j. j is the type of Number.

**Example**

The return value of the following statement is false.

`integer a[] = [1,1,2,3,4];  
3 in a[upfrom 4]`

## x[upfrom\_ j]

It is used to specify a range of values greater than but not including the value j. j is the type of Number.

**Example**

The return value of the following statement is true.

`integer a[] = [1,1,2,3,4];  
3 in a[upfrom_ 2];`

## x[upto j]

It is used to specify a range of values less than or equal to the value j. j is the type of Number.

**Example**

The return value of the following statement is true.

`integer a[] = [1,1,2,3,4];  
3 in a[upto 4];`

## x[upto\_ j]

It is used to specify a range of values less than but not including the value j. j is the type of Number.

**Example**

The return value of the following statement is false.

`integer a[] = [1,1,2,3,4];  
4 in a[upto_ 4];`

## if(b) then{...} else{...}

Conditional statement.

**Example**

The return value of the following statement is abc.

`integer s=5;  
 integer f=8;  
 if ( f>s )  
 then return "abc"  
 else return "def"`

## return x

Returns the value of X.

**Example**

The result of the following statement is 06/19/01.

`return Today ()`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568282-Boolean-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590301-Object-Property-Reference)
