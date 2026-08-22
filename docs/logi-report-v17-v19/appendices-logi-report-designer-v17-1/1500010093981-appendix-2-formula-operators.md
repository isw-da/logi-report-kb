---
title: "Appendix 2: Formula Operators"
id: 1500010093981
section: "Appendices - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093981-Appendix-2-Formula-Operators
updated_at: 2021-07-23T19:14:31Z
---

# Appendix 2: Formula Operators

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094001-Appendix-3-Parameters-of-User-Defined-Web-Actions)

# Appendix 2: Formula Operators

Logi Report provides four types of the operators to help you write your formulas. This topic describes the usage of each operator with examples.

Select the following links to view the formula operators of different types:

* [Math Operators](#Math)
* [Comparison Operators](#Comparison)
* [Boolean Operators](#Boolean)
* [Other Operators](#Others)

## Math Operators

| Operator | Description | Example |
| --- | --- | --- |
| date x + integer y | When you add a Date value to an Integer value, the return value is a Date value because the Integer value can change to a Date value. | If the date is Oct. 15, 1999, the return value of the following statement is "10-25-99". `ToDate (1999, 10, 15) + 10` |
| datetime x + integer y | When you add a DateTime value to an Integer value, the return value is a DateTime value because the Integer value can change to a DateTime value. | If the datetime is Aug. 10, 1999 10:21:30, the return value of the following statement is "1999-08-10 10:21:40". `ToDateTime (1999, 8, 10, 10, 21, 30) + 10` |
| numeric x + y | Adds x and y, and numeric adds to numeric. The return value's precision corresponds to the data type with the higher precision except when a BigInt value is added to a real number. In this case, the return value is a BigDecimal. Note icon Each data type has its own precision. For the Integer type data, BigInt has the highest precision while integer has the lowest precision. For the real number type data, Currency has the highest precision while Float has the lowest precision. So, if two numeric data fields of different precision are added together, the return value is the data type with the higher precision. For example, if an Integer is added to a Double, the return value is a Double value. | The return value of the following expression is "81.71". `55 + 26.71` |
| string x + boolean y | When you add a String to a Boolean value, the return value is a String because the Boolean value can change to a String value, while the String value cannot change to a Boolean value. | The return value of the following statement is "It is false". `"It is" + IsNull (3>2)` |
| string x + currency y | When you add a String to a Currency value, the return value is a String because the Currency value can change to a String value, while the String value cannot change to a Currency value. | The return value of the following statement is "I spent 9.56". `"I spent" + ToText($9.56)` |
| string x + date y | When you add a String to a Date value, the return value is a String because the Date value can change to a String value, while the String value cannot change to a Date value. | The return value of the following statement is "It is 1999-10-15". `"It is"+ToDate (1999, 10, 15)` |
| string x + datetime y | When you add a String to a DateTime value, the return value is a String because the DateTime value can change to a String value, while the String value cannot change to a Date value. | The return value of the following statement is "It is 1999-10-15 09:37:15". `"It is" + CurrentDateTime ()` |
| string x + integer y | When you add a String to an Integer value, the return value is a String because the Integer value can change to a String value, while the String value cannot change to an Integer value. | The return value of the following statement is "The result is 9". `"The result is" + 9` |
| string x + number y | When you add a String to a Number value, the return value is a String because the Number value can change to a String value, while the String value cannot change to a Number value. | The return value of the following statement is "The result is 9.56". `"The result is" + 9.56` |
| string x + string y | The return value is a String. | The return value of the following statement is "It is your bike".  `"It is" + " your bike."`  The following formula sets an URL, which can run one demo report on Server.  `String URL="http://localhost:8888/jinfonet/runReport.jsp?";   String Reports = "&jrs.report_sheet$report2=true";   String Catalog = "&jrs.catalog=/SampleReports/SampleReports.cat";   String ReportSet = "&jrs.report=/SampleReports/Detail Report Corporate Overview.cls";   String resultType = "&jrs.result_type=8";   String para = "&jrs.param$P_Category=Bold";   return URL + Reports + Catalog + ReportSet + resultType + para;` |
| string x + text y | When you add a String to a text value, the return value is a String because the text value can change to a String value, while the String value cannot change to a text value. | The return value of the following statement is "It is 07-Jul-99 7:12:21 AM". `"It is" + ToText (ToDateTime (1999, 7, 7, 7, 12, 21), "dd-MMM-yy h:mm:ss a", "AM")` |
| string x + time y | When you add a String to a Time value, the return value is a String because the Time value can change to a String value, while the String value cannot change to a Time value. | The return value of the following statement is "It is 10:10:10". `"It is" + ToTime (10, 10, 10)` |
| text x + boolean y | When you add a text value to a Boolean value, the return value is a text value because the Boolean value can change to a text value, while the text value cannot change to a Boolean value. | The return value of the following statement is "falsefalse". `ToText(3<2) + IsNull (2.5)` |
| text x + currency y | When you add a text value to a Currency value, the return value is a text value because the Currency value can change to a text value, while the text value cannot change to a Currency value. Note that with this option, when a Currency value is changed to a text value, the "$" symbol is not added. | The return value of the following statement is "false10.56". `ToText(3<2) + ToText($10.56)` |
| text x + date y | When you add a text value to a Date value, the return value is a text value because the Date value can change to a text value, while the text value cannot change to a Date value. | If the date is Aug.10, 1999 and the time is 10:21:30, the return value of the following statement is "10:21:301999-08-10". `ToText(ToTime(10,21,30), "hh:mm:ss") + ToDate(1999,8,10)` |
| text x + datetime y | When you add a text value to a DateTime value, the return value is a text value because the DateTime value can change to a text value, while the text value cannot change to a DateTime value. | If the date is Aug.10, 1999 and the time is 10:21:30, the return value of the following statement is "false1999-08-10 10:21:30". `ToText(3<2) + ToDateTime(1999,8,10,10,21,30)` |
| text x + integer y | When you add a text value to an Integer value, the return value is a text value because the Integer value can change to a text value, while the text value cannot change to an Integer value. | The return value of the following statement is "false10". `ToText(3<2) + 10` |
| text x + number y | When you add a text value to a Number value, the return value is a text value because the Number value can change to a text value, while the text value cannot change to a Number value. | The return value of the following statement is "false10.56". `ToText(3<2) + 10.56` |
| text x + string y | The return value is a String. | The return value of the following statement is "25.60is a number". `ToText(25.6, 2)+"is a number."` |
| text x + text y | The return value is a text value. | The return value of the following statement is "25.6and6.52". `ToText(25.6, 1)+"and"+ToText(6.52, 2)` |
| text x + time y | When you add a text value to a Date value, the return value is a text value because the Date value can change to a text value, while the text value cannot change to a Date value. | If the date is Aug.10, 1999 and the time is 10:21:30, the return value of the following statement is "99-08-1010:21:30". `ToText(ToDate(1999,8,10), "yy-MM-dd") + ToTime(10,21,30)` |
| time x + integer y | When you add a Time value an Integer value, the return value is a Time value because the Integer value will have changed to a Time value. | If the time is 10:15:25, the return value of the following statement is "10:15:35". `ToTime (10, 15, 25) + 10` |
| date x - date y | When you subtract a Date value from a Date value, the return value is an Integer. The result is the number of days between the two dates. | If one date is 1999-12-12, and the other date is 1995-12-12, the return value of the following statement is "1461".  `ToDate(1999, 12, 12) - ToDate(1995, 12, 12)`  The following formula sets values' background, in which way it can highlight report values that are out of range.  `if ((todate(@"Due Date")-CurrentDate())<0)   {return '0xff0000'}//red   else   {return '0x000000'}//black` |
| date x - integer y | When you subtract a Integer value from an Date value, the return value is a Date value because the Integer value can be changed into a Date value. | If the date is Oct. 18, 1999, the return value of the following statement is "10/16/99". `ToDate(1999, 10, 18) - 2` |
| datetime x - datetime y | When you subtract a DateTime value from a DateTime value, the return value is an Integer. The result is the number of seconds between the two DateTimes. | If one date time is 1999-12-12 10:10:10, and the other date time is 1995-12-12 10:10:10, the return value of the following statement is "126230400". `ToDateTime(1999, 12, 12, 10, 10, 10) - ToDateTime(1995, 12, 12, 10, 10, 10)` |
| datetime x - integer y | When you subtract an Integer value from a DateTime value, the return value is a DateTime value because the Integer value can be changed into a DateTime value. | If the date is Oct. 18, 1999, the time is 10:10:10, the return value of the following statement is "1999-10-18 10:10:08". `ToDateTime(1999, 10, 18, 10, 10, 10) - 2` |
| numeric x - numeric y | Subtracts y from x. When you subtract a numeric from a numeric, the precision of the return value corresponds to the data type with the higher precision. Note icon Each data type has its own precision. For the Integer type data, BigInt has the highest precision while integer has the lowest precision; for the real number type data, Currency has the highest precision while float has the lowest precision. Therefore, if two numeric datum of different precision are substraced from each other, the return value is of the data type with the higher precision. For example, if an Integer is subtracted from a Double, the return value is a Double value. | The return value of the following expression is "61.71". `87.71 - 26` |
| time x - integer y | When you subtract an Integer value from a Time value, the return value is a Time value because the Integer value can be changed into a Time value. | If the time is 10:10:10, the return value of the following statement is "10:10:08". `ToTime(10, 10, 10) - 2` |
| time x - time y | When you subtract a Time value from a Time value, the return value is an Integer. The result is the number of seconds between the two times. | If one time is 08:08:08, and the other time is 10:10:10, the return value of the following statement is "7322". `ToTime(10, 10, 10) - ToTime(8, 8, 8)` |
| currency x \* currency y | Multiplies x by y. When you multiply a Currency value by a Currency value, the return value is a Currency value. | The return value of the following statement is "2.88". `$2.4 * $1.2` |
| currency x \* integer y | Multiplies x by y. When you multiply a Currency value by an Integer value, the return value is a Currency value. | The return value of the following statement is "106.75". `$4.27 * 25` |
| currency x \* number y | Multiplies x by y. When you multiply a Currency value by a Number value, the return value is a Currency value. | The return value of the following statement is "3.25". `$1.27 * 2.56` |
| integer x \* currency y | Multiplies x by y. When you multiply an Integer value by a Currency value, the return value is a Currency value. | The return value of the following statement is "106.75". `25 * $4.27` |
| integer x \* integer y | Multiplies x by y. When you multiply an Integer value by an Integer value, the return value is an Integer value. | The return value of the following statement is "15". `3 * 5` |
| integer x \* number y | Multiplies x by y. When you multiply an Integer value by a Number value, the return value is a Number value. | The return value of the following statement is "104.25". `25 * 4.17` |
| number x \* currency y | Multiplies x by y. When you multiply a Number value by a Currency value, the return value is a Currency value. | The return value of the following statement is "3.25". `2.56 * $1.27` |
| number x \* integer y | Multiplies x by y. When you multiply a Number value by an Integer value, the return value is a Number value. | The return value of the following statement is "104.25". `4.17 * 25` |
| number x \* number y | Multiplies x by y. When you multiply a Number value by a Number value, the return value is a Number value. | The return value of the following statement is "2.88". `2.4 * 1.2` |
| currency x / currency y | Divides x by y. When you divide a Currency value by a Currency value, the return value is an Integer or a Currency value. | The return value of the following statement is "1.77". `$4.52 / $2.56` |
| currency x / integer y | Divides x by y. When you divide a Currency value by an Integer value, the return value is a Currency value. | The return value of the following statement is "1.28". `$2.56 / 2` |
| currency x / number y | Divides x by y. When a Currency is divided by a Number value, the return value is an Integer or a Currency value. | The return value of the following statement is "1.79". `$4.52 / 2.52` |
| integer x / currency y | Divides x by y. When you divide an Integer value by a Currency value, the return value is a Currency or an Integer. | The return value of the following statement is "21.87". `56 / $2.56` |
| integer x / integer y | Divides x by y. When you divide an Integer value by another Integer value, the return value is an Integer or a Number value. | `56 / 3` - Returns "18.67".  `10 / 3` - Returns "3.33". |
| integer x / number y | Divides x by y. When you divide an Integer value by a Number value, the return value is a Number or an Integer. | The return value of the following statement is "21.88". `56 / 2.56` |
| number x / currency y | Divides x by y. When you divide a Number value by a Currency value, the return value is a Currency value. | The return value of the following statement is "1.77". `4.52 / $2.56` |
| number x / integer y | Divides x by y. When you divide a Number value by an Integer value, the return value is a Number value. | The return value of the following statement is "0.51". `2.55 / 5` |
| number x / number y | Divides x by y. When you divide a Number value by a Number value, the return value is an Integer or a Number value. | The return value of the following statement is "1.77". `4.52 / 2.56` |
| number x \ number y | Divides x by y, and returns an Integer result. | `39.4 \ 3` - Returns "13.00".  `10 \ 3` - Returns "3.00". |
| currency -x | Returns the opposite value of x. If a Currency value is positive, the return value is negative; if the Currency value is negative, the return value is positive. | `-$2.57` - Returns "-$2.57".  `-(-$2.57)` - Returns "$2.57". |
| integer -x | Returns the opposite value of x. If an Integer value is positive, the return value is negative; if the Integer value is negative, the return value is positive. | `-25` - Returns "-25".  `-(-25)` - Returns "25". |
| number -x | Returns the opposite value of x. If a Number value is positive, the return value is negative; if the Number value is negative, the return value is positive. | `-5.28` - Returns "-5.28".  `-(-5.28)` - Returns "5.28" |
| currency x % currency y | Computes the percentage of dividing x by y. When you divide a Currency value by a Currency value, the return value is an Integer or a Currency value. | The return value of the following statement is "176.56". `4.52%2.56` |
| currency x % integer y | Computes the percentage of dividing x by y. When you divide a Currency value by an Integer value, the return value is an Integer or a Currency value. | The return value of the following statement is "226". `$4.52%2` |
| currency x % number y | Computes the percentage of dividing x by y. When you divide a Currency value by a Number value, the return value is an Integer or a Currency value. | The return value of the following statement is "120". `$1.44%1.2` |
| integer x % currency y | Computes the percentage of dividing x by y. When you divide an Integer value by a Currency value, the return value is an Integer or a Currency value. | The return value of the following statement is "40". `1%$2.5` |
| integer x % integer y | Computes the percentage of dividing x by y. When you divide an Integer value by an Integer value, the return value is an Integer or a Number value. | The return value of the following statement is "77.78". `7%9` |
| integer x % number y | Computes the percentage of dividing x by y. When you divide an Integer value by a Number value, the return value is a Number or an Integer value. | The return value of the following statement is "400". `6%1.5` |
| number x % currency y | Computes the percentage of dividing x by y. When you divide a Number value by a Currency value, the return value is an Integer or a Currency value. | The return value of the following statement is "500". `2.5%$0.5` |
| number x % integer y | Computes the percentage of dividing x by y. When you divide a Number value by an Integer value, the return value is an Integer or a Number value. | The return value of the following statement is "50". `2.5%5` |
| number x % number y | Computes the percentage of dividing x by y. When you divide a Number value by a Number value, the return value is an Integer or a Number value. | The return value of the following statement is "176.56". `4.52%2.56` |
| number x ^ number y | Raise x to the power of y. y can be fractional, positive, or negative. x can be fractional, but negative only when y is a whole number. | `2^2` - Returns "4".  `7^3.8` - Returns "1626.9438030745541". |
| number x \ number y | Divides x by y after rounding them to the nearest integer if they are not, and returns an Integer number. | `19.5 \ 2` - Returns "10.0".  `19.4 \ 2` - Returns "9.0". |

## Comparison Operators

| Operator | Description | Example |
| --- | --- | --- |
| date x > date y | If x is greater than y, the return value is "true"; if x is < and == y, the return value is "false". | The return value of the following statement is "true". `ToDate(1999, 10, 10) > ToDate(1999, 2, 5)` |
| datetime x > datetime y | If x is greater than y, the return value is "true"; if x is < and == y, the return value is "false". | The return value of the following statement is "true". `ToDateTime(1999, 10, 10, 10, 10, 10) > ToDateTime(1999, 5, 10, 8, 5, 5)` |
| numeric x > numeric y | If x is greater than y, the return value is "true", if x is < and == y, the return value is "false". | `3>2.56` - Returns "true".  `5.29>7.55` - Returns "fasle". |
| string x > string y | If x is greater than y, the return value is "true"; if x is < and == y, the return value is "false". | `"string abcd" > "string abc"` - Returns "true".  `"string abc" > "string abcd"` - Returns "fasle". |
| time x > time y | If x is greater than y, the return value is "true"; if x is < and == y, the return value is "false". | The return value of the following statement is "true". `ToTime(10, 10, 10) > ToTime(8, 10, 10)` |
| date x < date y | If x is less than y, the return value is "true"; if x is > and == y, the return value is "false". | The return value of the following statement is "false". `ToDate(1999, 10, 10) < ToDate(1999, 2, 5)` |
| datetime < datetime y | If x is less than y, the return value is "true"; if x is > and == y, the return value is "false". | The return value of the following statement is "false". `ToDateTime(1999, 10, 10, 10, 10, 10) < ToDateTime(1999, 5, 10, 8, 5, 5)` |
| numeric x < numeric y | If x is less than y, the return value is "true"; if x is > and == y, the return value is "false". | `2.56<3` - Returns "true".  `7.55<5.88` - Returns "fasle". |
| string x < string y | If x is less than y, the return value is "true"; if x is > and == y, the return value is "false". | `"string abc" < "string abcd"` - Returns "true".  `"string abcd" < "string abc"` - Returns "fasle". |
| time x < time y | If x is less than y, the return value is "true"; if x is > and == y, the return value is "false". | The return value of the following statement is "false". `ToTime(10, 10, 10) < ToTime(8, 10, 10)` |
| date x == date y | If x is equal to y, the return value is "true"; if x is not equal to y, the return value is "false". | The return value of the following statement is "false". `ToDate(1999, 10, 10) == ToDate(1999, 5, 10)` |
| datetime x == datetime y | If x is equal to y, the return value is "true"; if x is not equal to y, the return value is "false". | The return value of the following statement is "false". `ToDateTime(1999, 10, 10, 5, 10, 10) == ToDateTime(1999,10, 10, 10, 10, 10)` |
| numeric x == numeric y | If x is equal to y, the return value is "true"; if x is not equal to y, the return value is "false". | The return value of the following statement is "false". `5==4` |
| string x == string y | If x is equal to y, the return value is "true; if x is not equal to y, the return value is "false". | The return value of the following statement is "false". `"string abcd" == "string abc"` |
| time x ==  time y | If x is equal to y, the return value is "true"; if x is not equal to y, the return value is "false". | The return value of the following statement is "false". `ToTime(9, 10, 10) == ToTime(10, 10, 10)` |
| date x <> date y   or date x != date y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". `ToDate(1999, 10, 10) != ToDate(1999, 5, 10)` |
| datetime x <> datetime y or datetime x != datetime y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". `ToDateTime(1999, 10, 10, 5, 10, 10) != ToDateTime(1999,10, 10, 10, 10, 10)` |
| numeric x <> numeric y or numeric x != numeric y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "false". `4 <> 4` |
| string x <> string y or string x != string y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". `"string abc" != "string abcd"` |
| time x <> time y or time x != time y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". `ToTime(9, 10, 10) <> ToTime(10, 10, 10)` |

## Boolean Operators

The following are a set of truth tables showing the logic operations for 3-valued logic.

| A AND B | True | False | Null |
| --- | --- | --- | --- |
| True | True | False | Null |
| False | False | False | False |
| Null | Null | False | Null |

  

| A OR B | True | False | Null |
| --- | --- | --- | --- |
| True | True | True | True |
| False | True | False | Null |
| Null | True | Null | Null |

  

| A | NOT A |
| --- | --- |
| True | False |
| False | True |
| Null | Null |

The following table shows the usage about the Boolean operators：

| Operator | Description | Example |
| --- | --- | --- |
| Boolean x || Boolean y | Returns "true" if x is true or y is true. | `Integer s=4,d=8;  Integer f=6;  if ( f>s || f>d )  {  return "abc";  }` - Returns "abc".  `if ((@"Annual Sales" > 50000) ||(@"Annual Sales"<0)) then   "Customer needs attention"   else   "Normal customer"`    `If( ! isNull(@customerId) && ! isNull(@country)){                 If(@customerId > 10 || @country == ‘USA’){                                Integer newId =  @customerId + 1;  }  }  Else{                 // Some error processing logic here`  } |
| Boolean x && Boolean y | Returns "true" if x is true and y is true. | `Integer s=4,d=8;  Integer f=6;  if ( f>s && f<d )  {  return "abc";  }` - Returns "abc".  `if ((@"Annual Sales" <3000) && (@Customers_Country=="USA")) then   "Customer is in the USA and Annual Sales is less than 3000"   else   "Others"` |
| ! Boolean x | Returns "true" if x is false. | The return value of the following statement is "def". `Integer s=4, d=8;  Integer f=6;  if ( ! ( f>s ) )  return  "abc"  else  return "def"` |

## Other Operators

| Operator | Description | Example |
| --- | --- | --- |
| x in y | A statement used to tell whether x is in y, the return value is a Boolean value. | `integer x[3] = [0,1,2];  integer xx = 3;  xx in x` - Returns "false".  `integer range intary=[30 to 50];   if (@"Product_ID" in intary) then   return "Within the Range"   else   return "Out of Range"`  `if (@Customers_Region in ["CO","MT","UT","WY"]) then   "Rocky Mountain Region"   else   "Rest of Country"` |
| [x, y, z] | A statement used to define an array. | The return value of the following statement is "1996-11-27". `date d[3] = [toDate(1997, 11, 27), toDate(1996, 11, 27), toDate(1995, 11, 27)];  date dd[3];  dd = d;  dd[1]` |
| x[i] | A statement used to index a certain value in an array. | The return value of the following statement is "14:11:27". `time d[3] = [totime(12, 11, 27), totime(13, 11, 27), totime(14, 11, 27)];  time dd[3];  dd = d;  dd[2]` |
| x[i to j] | A statement used to define an array. | The return value of the following statement is "true". `string range strary = ["a" to "z"];  string x = "d";  x in strary` |
| x[i \_to j] | The operator specifies a range of values greater than but not including the value *i*, and less than or equal to the value *j*. Both *i* and *j* are of the Number type. | The return value of the following statement is "true". `integer a[] = [1,1,2,3,4];  3 in a[2 _to 4];` |
| x[i to\_ j] | The operator specifies a range of values greater than or equal to the value *i*, and less than but not including the *j* value. Both *i* and *j* are of the Number type. | The return value of the following statement is "true". `integer a[] = [1,1,2,3,4];  3 in a[2 to_ 4];` |
| x[i \_to\_ j] | The operator specifies a range of values greater than but not including the value *i*, and less than but not including the value *j*. Both *i* and *j* are of the Number type. | The return value of the following statement is "true". `integer a[] = [1,1,2,3,4];  3 in a[2 _to_ 4];` |
| x[upfrom j] | The operator specifies a range of values greater than or equal to the value *j*. *j* is of the Number type. | The return value of the following statement is "false". `integer a[] = [1,1,2,3,4];  3 in a[upfrom 4]` |
| x[upfrom\_ j] | The operator specifies a range of values greater than but not including the value *j*. *j* is of the Number type. | The return value of the following statement is "true". `integer a[] = [1,1,2,3,4];  3 in a[upfrom_ 2];` |
| x[upto j] | The operator specifies a range of values less than or equal to the value*j*. *j* is of the Number type. | The return value of the following statement is "true". `integer a[] = [1,1,2,3,4];  3 in a[upto 4];` |
| x[upto\_ j] | The operator specifies a range of values less than but not including the value *j*. *j* is of the Number type. | The return value of the following statement is "false". `integer a[] = [1,1,2,3,4];  4 in a[upto_ 4];` |
| if(b) then{...} else{...} | Conditional statement. | The return value of the following statement is "abc". `integer s=5;  integer f=8;  if ( f>s )  then return "abc"  else return "def"` |
| return x | Returns the value of X. | The result of the following statement is "06/19/01". `return Today ()` |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094001-Appendix-3-Parameters-of-User-Defined-Web-Actions)
