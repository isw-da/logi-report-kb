---
title: "Other Functions"
id: 1500009589561
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions
updated_at: 2021-07-24T05:54:38Z
---

# Other Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589581-Operators)

# Other Functions

Below is a list of other functions used in Logi JReport Designer:

> * [Choose()](#Choose)
> * [currentBurstingSchema()](#currentBurstingSchema)
> * [eqv()](#eqv)
> * [GetInfo()](#GetInfo)
> * [getLanguage()](#getLanguage)
> * [getLocale()](#getLocale)
> * [GetOrgInfo()](#GetOrgInfo)
> * [getSecurityContext()](#getSecurityContext)
> * [GetUserInfo()](#GetUserInfo)
> * [isAll()](#isAll)
> * [isCountry()](#isCountry)
> * [IsNoRecord()](#IsNoRecord)
> * [IsNull()](#IsNull)
> * [isNumeric()](#isNumeric)
> * [isRunBursting()](#isRunBursting)
> * [Next()](#Next)
> * [nextMember()](#nextMember)
> * [openBinFile()](#openBinFile)
> * [openBinURL()](#openBinURL)
> * [openTxtFile()](#openTxtFile)
> * [openTxtURL()](#openTxtURL)
> * [Prev()](#Prev)
> * [prevMember()](#prevMember)
> * [PutInfo()](#PutInfo)
> * [PutOrgInfo()](#PutOrgInfo)
> * [PutUserInfo()](#PutUserInfo)
> * [RemoveInfo()](#RemoveInfo)
> * [RemoveOrgInfo()](#RemoveOrgInfo)
> * [RemoveUserInfo()](#RemoveUserInfo)
> * [reportName()](#reportName)
> * [Switch()](#Switch)
> * [toBool()](#toBool)
> * [toNumber()](#toNumber)
> * [xor()](#xor)

## Choose(Integer, Array)

Returns a value from the array based on the value of Integer. For example, if integer is 0, it returns the first element in the array, and if index is 1 it returns the second element in the array.

**Parameters**

* Integer - A Number or numeric expression that specifies the index of the element. The minimum value is 0, and the maximum is the number of available elements minus 1. If it is out of bounds, no value will be returned.
* Array - An array that contains all the available elements to choose from. All elements must be of the same type. A choice can be any simple type (Number, Currency, String, Boolean, Date, Time or DateTime), or range type (Number Range, Currency Range, String Range, Date Range, Time Range or DateTime Range), but it may not be an array.

**Return value**

A value from the element in the given array. The type of the returned value is the same as the type of the element.

**Examples**

* `Choose(1,["Poor","Fair","Good","Excellent"])` - Returns Fair.
* `Choose(2,["1 to 10","11 to 20", "21 to 30"])` - Returns 21 to 30.
* `Choose(2,[1,2,3,4,5,6])` - Returns 3.
* `Choose(2,[Todate('1998/5/4'),ToDate('1999/5/5'),ToDate('1996/5/6')])` - Returns 5/6/96.

## currentBurstingSchema()

Returns the names of the applied bursting schemas in the current report. When [isRunBursting()](#isRunBursting) returns false, the returned value of currentBurstingSchema() is NULL.

**Return value**

The return value is a String.

**Example**

If the current report has been applied two bursting schemas: VP and Manager, the return value of the following statement is *VP,Manager*:

`currentBurstingSchema()`

## eqv(booleanx, booleany)

Returns a Boolean value of booleanx eqv booleany,

* if x = true and y = true, returns the value of true.
* if x = true and y = false, returns the value of false.
* if x = false and y = true, returns the value of false.
* if x = false and y = false, returns the value of true.

**Parameters**

* booleanx - A Boolean value.
* booleany - A Boolean value.

**Return value**

Boolean value.

**Examples**

* `eqv(true, true)` - Returns true.
* `eqv(true, false)` - Returns false.

## GetInfo(String)

This function is used to get information of a given key in the global level information container of the Information Bus.

**Parameter**

A String indicating the information in the container.

**Return value**

The return value is a String value.

**Example**

If you want to get information containing a key-value pair, TestKey and TestValue, use the following statement:

`GetInfo("TestKey")` - Returns TestValue.

## getLanguage()

Returns the language name of the locale that the current running task is based on.

**Return value**

The return value will either be the empty string or a lowercase ISO 639 code.

**Example**

When the locale is set to en\_US, the return value of the following statement is *en*:

`getLanguage()`

## getLocale()

Returns the language and locale name that the current running task is based on.

**Return value**

The return value is a string containing language and locale information, for example, country.

**Example**

When the locale is set to en\_US, the return value of the following statement is *en\_US*:

`getLocale()`

## GetOrgInfo(String)

This function is used to get information of a given key in the organization level information container of the Information Bus that the current user can access.

**Parameter**

A String indicating the information in the container.

**Return value**

The return value is a String value.

**Example**

If you want to get information containing a key-value pair, TestKey and TestValue, use the following statement:

`GetOrgInfo("TestKey")` - Returns TestValue.

## getSecurityContext()

Returns a security context object, which provides the method get() to get the Security Context instance from Logi JReport Server or Logi JReport Designer.

**Return value**

The return value is a DbSecurityContext object.

**Example**

`Import userClass from "UserFunction";  
userClass.getData(getSecurityContext(), @country, …);`

## GetUserInfo(String)

This function is used to get information of a given key in the user level information container of the Information Bus that the current user can access.

**Parameter**

A String indicating the information in the container.

**Return value**

The return value is a String value.

**Example**

If you want to get information containing a key-value pair, TestKey and TestValue, use the following statement:

`GetUserInfo("TestKey")` - Returns TestValue.

## isAll(Array)

Checks whether the value of the specified parameter is "ALL".

**Return value**

The return value is true or false.

**Example**

When the parameter PEndDate supports multiple values and its value is set to "All", the following statement returns true.

`isAll(@PEndDate)`

## isCountry(String)

Compares the input parameter with that of the country setting of JVM based on default locale.

**Parameter**

The input string must be an uppercase 2-letter ISO 3166 code.

**Return value**

The return value is true or false.

**Examples**

* If getLanguage() return zh, isCountry("CN") will return *true*.
* If getLanguage() return en, isCountry("CN") will return *false*.

## IsNoRecord()

This function tells whether a report has returned a record or not. If the report has no value returned, the function will return True, otherwise False.

**Note:** A formula which calls this function cannot be applied to queries, and this formula only takes effect when laying out this report which contains it.

**Example**

When using this function, you should refer to a DBField to identify whether this formula is a record level formula so that it can be calculated when fetching the record. For example,

|  |
| --- |
| ``` @"Customers_Customer ID"; if(IsNoRecord())   return "There is no data" else   return "Total number of records="+@"Count_Customer Name5" ``` |

In this example, if no data returned, a tip "There is no data" will be displayed. If data is returned, the Total number of records will be displayed.

## IsNull(DBfield a)

This function tells whether a specified value (especially the value of a DBField) is null or not. If the value is Null, the function will return True, otherwise False.

**Parameter**

a - A specified value especially a value of a DBField.

**Return value**

The return value is True or False.

**Examples**

* The return value of the following statement is false.

  `IsNull(2.5)`
* If you build a report about customer order, suppose one of the values of the field "Shipped" is Null, the return value of the following statement is true.

  `IsNull(@shipped)`
* `Integer Total=0;  
   if (!isnull(@grandTotal))   
   Total= Total+@grandTotal;   
   else   
   Total=Total+0;`

  This formula can summarize the Grand Total while ignoring the null value or no-record column.

## isNumeric(inString)

Returns a Boolean value if the inString is a math number string.

**Parameter**

inString - A String type value.

**Return value**

Boolean value.

**Examples**

* `isNumeric("true")` - Returns false.
* `isNumeric("false")` - Returns false.
* `isNumeric("1234")` - Returns true.
* `isNumeric("122 322323")` - Returns false.

## isRunBursting()

Returns true if the current report is running based on a bursting schema, else returns false.

**Return value**

The return value is true or false.

**Examples**

* If a bursting report is scheduled to run based on a bursting schema, the return value of the following statement is *true*:

  `isRunBursting()`
* If a bursting report is scheduled to run a normal result, the return value of the following statement is *false*:

  `isRunBursting()`

## Next()

### Next(DBfield a)

This function returns the next value of the current DBField.

**Parameter**

a - A DBField value.

**Return value**

The return value is a DBField value.

**Example**

Suppose you build a report about customer orders. If you use this function on "Ship Date" and insert it into the Detail Section, then when you run the report, you will see after each record, the next records will be displayed according to the following statement.

`Next(@"Ship Date")`

### Next(DBfield a, BigInt b)

This function returns the next Nth record decided by the argument b.

**Parameters**

* a - A DBField value.
* b - A BigInt value.

**Return value**

The return value is a DBField value.

**Example**

Suppose you build a report about customer orders. If you use this function on "Ship Date" and set the argument b as 1, then when you run the report, you will see after each record, the next first record will be displayed according to the following statement.

`Next(@"Ship Date", 1)`

**Note:** Due to some implementation limitation, the argument b cannot be equal to or larger than 2.

## nextMember()

The function is used to navigate the next member of a group or detail object when composing a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements#CustomAgg) in a business view. It can be used as the member argument in the expression of a custom aggregation.

nextMember() and [prevMember()](#prevMember) are navigation functions that do not actually return a member because formulas do not have a member data type. Instead, the functions only locate a specific member of a group or detail object when a custom aggregation expression is executed on a specific group node or on a crosstab cell. When the custom aggregation is executed on an ALL member, the functions will always locate the ALL member itself.

The order of the members could be the following:

* If the group in the aggregation is used as a group in a data component with order, the members take the order in the data component, or else they are sorted in the ascending order.
* For a group used more than once in a data component, get the highest group setting. If it is used on both row header and column header of a crosstab, get the highest group setting on the row header.
* The previous/next member of the "All" member is also "All".

Whether the members of a group or detail object can be located by a navigation function depends on whether the range of members is defined clearly. The range of members of a group or detail object is confined to the current values of all the parent groups if there are any parent groups. The hierarchy of groups is taken into consideration. For example, we have two groups Country and City with members as below:

China

> Beijing  
>  Shanghai

USA

> New York

When talking about city.FIRSTMEMBER, we first consider what the country is. If current country is China, then it is Beijing and city.LASTMEMBER is Shanghai. If current country is USA, then it is New York. In this way, inappropriate combinations such as the country China and the city New York can be effectively avoided.

**Note:** Since the combination of the country China and the city New York in a crosstab cell is displayed as blank, the navigation functions will not execute on such combination and therefore the corresponding crosstab cells are kept as blank.

### nextMember()

Locates the next member of a group or detail object.

Suppose that a group or detail object contains x members (confined to all parent groups' current members) and the custom aggregation is executed on the ith member, if i = x, this function cannot locate any member.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, and the custom aggregation is executed on 20, the following expression returns 30.

`nextMember()`

### nextMember(n)

Locates the next nth member of a group or detail object.

Suppose that a group or detail object contains x members (confined to all parent groups' current members) and the custom aggregation is executed on the ith member, if i + n > x , this function cannot locate any member.

**Parameter**

n - An integer starting from 1.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, and the custom aggregation is executed on 20, the following expression returns 50.

`nextMember(3)`

### nextMember(n, start)

Locates the next nth member after the member specified in the start parameter.

Suppose that a group or detail object contains x members (confined to all parent groups' current members), when start is the jth member, if j + n > x , this function cannot locate any member.

**Parameters**

* n - An integer starting from 1.
* start - A constant member of a group or detail object such as 'USA', FIRSTMEMBER, and LASTMEMBER.
* FIRSTMEMBER - Always locates the first member of a group or detail object.
* LASTMEMBER - Always locates the last member of a group or detail object.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, the following expression returns 50.

`nextMember(2,30)`

## openBinFile(string a)

This function is used to open an image file which is saved in your file system according to the path specified by the parameter.

**Parameter**

a - A String value which indicates the full path of the image file.

**Return value**

The return value is a binary image file.

**Example**

Suppose you have an image file photo1.gif which is saved in the following directory `c:\images`. The following example will open this image file.

`openBinFile("c:\\images\\photo1.gif")`

## openBinURL(string a)

This function is used to open a binary image file according to the URL which is specified by the parameter.

**Parameter**

a - A String value which indicates the URL of the image file.

**Return value**

The return value is a binary image file.

**Example**

Suppose you have an image file in the following URL `http://www.jinfonet.com/../../asset/images/Pic1.gif`. The following example will open this image file Pic1.gif.

`openBinURL("http://www.jinfonet.com/../../asset/images/Pic1.gif")`

## openTxtFile(string a)

This function is used to open a text file which is kept in your file system according to the path specified by the parameter.

**Parameter**

a - A String value which indicates the full path of the text file.

**Return value**

The return value is a long varchar.

**Example**

Suppose you have a text file report.int in the following directory `C:\Logi JReport\Designer`. The following example will open this text file report.ini.

`openTxtFile("C:\\Logi JReport\\Designer\\report.ini")`

## openTxtURL(string a)

This function is used to open a text file according to the URL specified by the parameter.

**Parameter**

a - A String value which indicates the URL of the text file.

**Return value**

The return value is a long varchar.

**Example**

Suppose you have a text file at the following URL http://www.jinfonet.com/Logi JReport/report.ini. The following example will open the text file report.ini.

`openTxtURL("http://www.jinfonet.com/Logi JReport/report.ini")`

## Prev()

### Prev(DBfield a)

This function returns the previous value of the current DBField.

**Parameter**

a - A DBField value.

**Return value**

The return value is a DBField value.

**Example**

Suppose you build a report about customer orders. If you use this function on "Ship Date" and insert it into the Detail Section, after the report has been run, you will see the previous records displayed after each record, according to the following statement.

`Prev(@"Ship Date")`

### Prev(DBfield a, BigInt b)

This function returns the previous Nth record decided by the argument b.

**Parameters**

* a - A DBField value.
* b - A BigInt value.

**Return value**

The return value is a DBField value.

**Example**

Suppose you build a report about customer orders. If you use this function on "Ship Date" and set the argument b as 4, then when you run the report, you will see before each record, the previous 4th record displayed according to the following statement.

`Prev(@"Ship Date", 4)`

**Note:** Due to some implementation limitation, the argument b cannot be equal to or less than -2.

## prevMember()

The function is used to navigate the previous member of a group or detail object when composing a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements#CustomAgg) in a business view. It can be used as the member argument in the aggregation expression of a custom aggregation. Select [here](#Navigate) for more information about navigation functions.

### prevMember()

Locates the previous member of a group or detail object.

Suppose that a group or detail object contains x members (confined to all parent groups' current members) and the custom aggregation is executed on the ith member, if i = 1, this function cannot locate any member.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, and the custom aggregation is executed on 20, the following expression returns 10.

`prevMember()`

### prevMember(n)

Locates the previous nth member of a group or detail object.

Suppose that a group or detail object contains x members (confined to all parent groups' current members) and the custom aggregation is executed on the ith member, if i - n < 1 , this function cannot locate any member.

**Parameter**

n - An integer starting from 1.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, and the custom aggregation is executed on 40, the following expression returns 10.

`prevMember(3)`

### prevMember(n, start)

Locates the previous nth member before the member specified in the start parameter.

Suppose that a group or detail object contains x members (confined to all parent groups' current members), when start is the jth member, if j - n < 1 , this function cannot locate any member.

**Parameters**

* n - An integer starting from 1.
* start - A constant member of a group or detail object such as 'USA', FIRSTMEMBER, and LASTMEMBER.
* FIRSTMEMBER - Always locates the first member of a group or detail object.
* LASTMEMBER - Always locates the last member of a group or detail object.

**Return value**

A member of a group or detail object.

**Example**

When a detail object contains these members: 10, 20, 30, 40, 50, the following expression returns 30.

`prevMember(2,50)`

## PutInfo(String a, String b)

This function is used to put or replace information of a given key in the global level information container of the Information Bus.

**Parameters**

* a - A String indicating the information in the container.
* b - A String value.

**Return value**

No return value.

**Example**

If you want to put information containing a key-value pair, TestKey and TestValue, use the following statement:

`PutInfo("TestKey", "TestValue")`

## PutOrgInfo(String a, String b)

This function is used to put or replace information of a given key in the organization level information container of the Information Bus that the current user can access.

**Parameter**

* a - A String indicating the information in the container.
* b - A String value.

**Return value**

No return value.

**Example**

If you want to put information containing a key-value pair, TestKey and TestValue, use the following statement:

`PutOrgInfo("TestKey", "TestValue")`

## PutUserInfo(String a, String b)

This function is used to put or replace information of a given key in the user level information container of the Information Bus that the current user can access.

**Parameter**

* a - A String indicating the information in the container.
* b - A String value.

**Return value**

No return value.

**Example**

If you want to put information containing a key-value pair, TestKey and TestValue, use the following statement:

`PutUserInfo("TestKey", "TestValue")`

## RemoveInfo(String)

This function is used to remove information of a given key in the global level information container of the Information Bus.

**Parameter**

A String indicating the information in the container.

**Return value**

No return value.

**Example**

If you want to remove information containing a key named TestKey, use the following statement:

`RemoveInfo("TestKey")`

## RemoveOrgInfo(String)

This function is used to remove information of a given key in the organization level information container of the Information Bus that the current user can access.

**Parameter**

A String indicating the information in the container.

**Return value**

No return value.

**Example**

If you want to remove information containing a key named TestKey, use the following statement:

`RemoveOrgInfo("TestKey")`

## RemoveUserInfo(String)

This function is used to remove information of a given key in the user level information container of the Information Bus that the current user can access.

**Parameter**

A String indicating the information in the container.

**Return value**

No return value.

**Example**

If you want to remove information containing a key named TestKey, use the following statement:

`RemoveUserInfo("TestKey")`

## reportName()

This function returns the current report name.

**Return value**

The return value is a String.

**Example**

If the current report name is Employee Information, the return value of the following statement is Employee Information.

`reportName()`

## Switch(Boolean[], Array)

The elements in the two parameters corresponding with each other. This function evaluates the elements in the first parameter from left to right, and returns element associated with the first element to evaluate to True.
For example,

`Switch([1, 2, 3], [a, b, c])`

if 1 is true, Switch returns a. If 2 is true, Switch returns b. If 3 is true, Switch returns c.

**Parameters**

* Boolean[] - A Boolean type array, which contains the elements that are to be evaluated.
* Array - An array, which contains all the available values that may be returned.

**Return value**

One of the elements of the parameter array. The type of the returned value is the same as the element in the array.

**Example**

Insert the following function into the Detail section of a report,

`Switch([@"Customers_Customer ID"< 5, @"Customers_Customer ID" > 50,true],["small", "large", "medium"])`

* if Customer ID < 5 is true, returns small.
* if Customer ID >50 is true, returns large.
* if 5 < Customer ID < 50 (true), returns medium.

## toBool(number or currency)

Returns True if the parameter is positive or negative but not 0, and returns False if the parameter is 0.

**Parameter**

Can be either a Number, Currency value, or expression.

**Return value**

Boolean value.

**Example**

`toBool(@Discount)` - Returns false if the discount is 0. Otherwise, returns true.

## toNumber(Boolean)

Returns 1 if the parameter is True, and returns 0 if the parameter is False.

**Parameter**

True or false.

**Return value**

1 or 0.

**Examples**

* `toNumber(True)` - Returns 1.
* `toNumber(False)` - Returns 0.

## xor(booleanx, booleany)

Returns a Boolean value of booleanx Exclusive OR booleany,

* if x = true and y = true, returns the value of false.
* if x = true and y = false, returns the value of true.
* if x = false and y = true, returns the value of true.
* if x = false and y = false, returns the value of false.

**Parameters**

* booleanx - A Boolean value.
* booleany - A Boolean value.

**Return value**

Boolean value.

**Examples**

* `xor(true, true)` - Returns false.
* `xor(true, false)` - Returns true.
* `xor((@"Customer ID"<=20),(Remainder(@"Customer ID", 2) == 0));`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589581-Operators)
