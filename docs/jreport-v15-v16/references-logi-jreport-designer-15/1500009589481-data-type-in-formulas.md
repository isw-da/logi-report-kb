---
title: "Data Type in Formulas"
id: 1500009589481
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589481-Data-Type-in-Formulas
updated_at: 2021-07-24T05:54:39Z
---

# Data Type in Formulas

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568322-Formula-Syntax)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568182-Built-in-Functions)

# Data Type in Formulas

This topic introduces the different Data Types used with formulas in Logi JReport Designer.

| **Type** | | | | **Description** |
| --- | --- | --- | --- | --- |
| **Numeric** | **Integer** | **int** | 32-bit two's complement | Defines a field containing a whole number between -2,147,483,648 and 2,147,483,647. Fractional values inserted into an Integer field are truncated. If specified as NOT NULL WITH DEFAULT, null values will be replaced by zero. |
| **long** | 64-bit two's complement | A data type that holds large integers. |
| **BigInt** |  | Immutable arbitrary-precision integers. |
| **Real Number** | **float** | 32-bit IEEE 754 | This data type defines an 32bit-IEEE standard 754 floating-point field. Floating-point fields can be defined as single or double (default) precision based on the value of Integer. If the value of integer is between 1 and 21, the type is single precision floating-point, which requires 4 bytes of storage. If the value of integer is between 22 and 53 inclusive, the type is double precision floating-point, which requires 8 bytes of storage. If a field is specified as NOT NULL WITH DEFAULT, null values will be replaced by zero. |
| **double** | 64-bit IEEE 754 | This data type defines an 64-bit IEEE standard 754 floating-point field. Floating-point fields can be defined as single or double (default) precision based on the value of integer. If the value of integer is between 22 and 53 inclusive, the type is double precision floating-point, which requires 8 bytes of storage. If a field is specified as NOT NULL WITH DEFAULT, null values will be replaced by zero. |
| **currency** |  | This data type contains a dollar amount between; -1012 and 1012 and is displayed in a user-defined format. |

| **Type** | | | **Description** |
| --- | --- | --- | --- |
| **DateTime** | **Date** | MM/dd/yy MM/dd/yyyy | Dates designate a point in time according to the Gregorian calendar. Historical dates may not follow this calendar. The standard input format for this data type is MM/dd/yy or MM/dd/yyyy (automatic conversion is performed between these two formats). |
| **Time** | HH:mm:ss  hh:mm:ss | The Time field data type is defined by the standard input format of HH:mm:ss (using hour in day 0--23) or hh:mm:ss (using in am/pm 1--12). |
| **TimeStamp** | yyyy-MM-dd hh:mm:ss | This combination Date and Time data type is displayed in the format yyyy-MM-dd-HH: mm.ss.nnnnnnn. |
| **Other Types** | **Char** | 16-bit Unicode character | A single character. |
| **String** |  | A data type that holds character information. |
| **Boolean** | true or false | True or false. |

**Notes**:

| **Format** | **Description** |
| --- | --- |
| yyyy | An Integer from 0001 to 9999, representing a year. |
| MM | An Integer from 1 to 12 representing a month |
| dd | An Integer from 1 to 31 (maximum depends on the month and year) representing the day of the month. |
| HH | An Integer from 0 to 23, representing the hour in day. |
| hh | An Integer from 1 to 12, representing the hour in am/pm. |
| mm | An Integer from 0 to 59, representing minutes. |
| ss | An Integer from 0 to 59 representing seconds (default 0). |
| nnnnnn | An Integer (up to 6 digits) representing microseconds. If any trailing digit is omitted, 0 is assumed. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568322-Formula-Syntax)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568182-Built-in-Functions)
