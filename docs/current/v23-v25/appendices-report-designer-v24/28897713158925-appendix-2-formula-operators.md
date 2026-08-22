---
title: "Appendix 2: Formula Operators"
id: 28897713158925
section: "Appendices - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897713158925-Appendix-2-Formula-Operators
updated_at: 2024-09-30T09:10:35Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Appendix 2: Formula Operators

Report provides four types of the operators to help you write your formulas. This topic describes the usage of each operator with examples.

Select the following links to view the formula operators of different types:

- Math Operators

- Comparison Operators

- Boolean Operators

- Other Operators

## 
Math Operators

| Operator | Description | Example |
| --- | --- | --- |
| date x + integer y | When you add a Date value to an Integer value, the return value is a Date value because the Integer value can change to a Date value. | If the date is Oct. 15, 1999, the return value of the following statement is "10-25-99". ToDate (1999, 10, 15) + 10 |
| datetime x + integer y | When you add a DateTime value to an Integer value, the return value is a DateTime value because the Integer value can change to a DateTime value. | If the datetime is Aug. 10, 1999 10:21:30, the return value of the following statement is "1999-08-10 10:21:40". ToDateTime (1999, 8, 10, 10, 21, 30) + 10 |
| numeric x + y | Adds x and y, and numeric adds to numeric. The return value's precision corresponds to the data type with the higher precision except when a BigInt value is added to a real number. In this case, the return value is a BigDecimal. Each data type has its own precision. For the Integer type data, BigInt has the highest precision while integer has the lowest precision. For the real number type data, Currency has the highest precision while Float has the lowest precision. So, if two numeric data fields of different precision are added together, the return value is the data type with the higher precision. For example, if an Integer is added to a Double, the return value is a Double value. | The return value of the following expression is "81.71". 55 + 26.71 |
| string x + boolean y | When you add a String to a Boolean value, the return value is a String because the Boolean value can change to a String value, while the String value cannot change to a Boolean value. | The return value of the following statement is "It is false". "It is" + IsNull (3>2) |
| string x + currency y | When you add a String to a Currency value, the return value is a String because the Currency value can change to a String value, while the String value cannot change to a Currency value. | The return value of the following statement is "I spent 9.56". "I spent" + ToText($9.56) |
| string x + date y | When you add a String to a Date value, the return value is a String because the Date value can change to a String value, while the String value cannot change to a Date value. | The return value of the following statement is "It is 1999-10-15". "It is"+ToDate (1999, 10, 15) |
| string x + datetime y | When you add a String to a DateTime value, the return value is a String because the DateTime value can change to a String value, while the String value cannot change to a Date value. | The return value of the following statement is "It is 1999-10-15 09:37:15". "It is" + CurrentDateTime () |
| string x + integer y | When you add a String to an Integer value, the return value is a String because the Integer value can change to a String value, while the String value cannot change to an Integer value. | The return value of the following statement is "The result is 9". "The result is" + 9 |
| string x + number y | When you add a String to a Number value, the return value is a String because the Number value can change to a String value, while the String value cannot change to a Number value. | The return value of the following statement is "The result is 9.56". "The result is" + 9.56 |
| string x + string y | The return value is a String. | The return value of the following statement is "It is your bike". "It is" + " your bike." The following formula sets an URL, which can run one demo report on Server. String URL="http://localhost:8888/jinfonet/runReport.jsp?"; String Reports = "&jrs.report_sheet$report2=true"; String Catalog = "&jrs.catalog=/SampleReports/SampleReports.cat"; String ReportSet = "&jrs.report=/SampleReports/Detail Report Corporate Overview.cls"; String resultType = "&jrs.result_type=8"; String para = "&jrs.param$P_Category=Bold"; return URL + Reports + Catalog + ReportSet + resultType + para; |
| string x + text y | When you add a String to a text value, the return value is a String because the text value can change to a String value, while the String value cannot change to a text value. | The return value of the following statement is "It is 07-Jul-99 7:12:21 AM". "It is" + ToText (ToDateTime (1999, 7, 7, 7, 12, 21), "dd-MMM-yy h:mm:ss a", "AM") |
| string x + time y | When you add a String to a Time value, the return value is a String because the Time value can change to a String value, while the String value cannot change to a Time value. | The return value of the following statement is "It is 10:10:10". "It is" + ToTime (10, 10, 10) |
| text x + boolean y | When you add a text value to a Boolean value, the return value is a text value because the Boolean value can change to a text value, while the text value cannot change to a Boolean value. | The return value of the following statement is "falsefalse". ToText(3Comparison Operators

| Operator | Description | Example |
| --- | --- | --- |
| date x > date y | If x is greater than y, the return value is "true"; if x is  ToDate(1999, 2, 5) |
| datetime x > datetime y | If x is greater than y, the return value is "true"; if x is  ToDateTime(1999, 5, 10, 8, 5, 5) |
| numeric x > numeric y | If x is greater than y, the return value is "true", if x is 2.56 - Returns "true". 5.29>7.55 - Returns "fasle". |
| string x > string y | If x is greater than y, the return value is "true"; if x is  "string abc" - Returns "true". "string abc" > "string abcd" - Returns "fasle". |
| time x > time y | If x is greater than y, the return value is "true"; if x is  ToTime(8, 10, 10) |
| date x  and == y, the return value is "false". | The return value of the following statement is "false". ToDate(1999, 10, 10)  and == y, the return value is "false". | The return value of the following statement is "false". ToDateTime(1999, 10, 10, 10, 10, 10)  and == y, the return value is "false". | 2.56 and == y, the return value is "false". | "string abc"  and == y, the return value is "false". | The return value of the following statement is "false". ToTime(10, 10, 10)  date y or date x != date y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". ToDate(1999, 10, 10) != ToDate(1999, 5, 10) |
| datetime x <> datetime y or datetime x != datetime y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". ToDateTime(1999, 10, 10, 5, 10, 10) != ToDateTime(1999,10, 10, 10, 10, 10) |
| numeric x <> numeric y or numeric x != numeric y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "false". 4 <> 4 |
| string x <> string y or string x != string y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". "string abc" != "string abcd" |
| time x <> time y or time x != time y | If x is not equal to y, the return value is "true"; if x is equal to y, the return value is "false". | The return value of the following statement is "true". ToTime(9, 10, 10) <> ToTime(10, 10, 10) |

## 
Boolean Operators

The following are a  set of truth tables showing the logic operations for 3-valued logic.

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
| Boolean x \|\| Boolean y | Returns "true" if x is true or y is true. | Integer s=4,d=8; Integer f=6; if ( f>s \|\| f>d ) { return "abc"; } - Returns "abc". if ((@"Annual Sales" > 50000) \|\|(@"Annual Sales" 10 \|\| @country == ‘USA’){ Integer newId = @customerId + 1; } } Else{ // Some error processing logic here } |
| Boolean x && Boolean y | Returns "true" if x is true and y is true. | Integer s=4,d=8; Integer f=6; if ( f>s && fs ) ) return "abc" else return "def" |

## 
Other Operators

| Operator | Description | Example |
| --- | --- | --- |
| x in y | A statement used to tell whether x is in y, the return value is a Boolean value. | integer x[3] = [0,1,2]; integer xx = 3; xx in x - Returns "false". integer range intary=[30 to 50]; if (@"Product_ID" in intary) then return "Within the Range" else return "Out of Range" if (@Customers_Region in ["CO","MT","UT","WY"]) then "Rocky Mountain Region" else "Rest of Country" |
| [x, y, z] | A statement used to define an array. | The return value of the following statement is "1996-11-27". date d[3] = [toDate(1997, 11, 27), toDate(1996, 11, 27), toDate(1995, 11, 27)]; date dd[3]; dd = d; dd[1] |
| x[i] | A statement used to index a certain value in an array. | The return value of the following statement is "14:11:27". time d[3] = [totime(12, 11, 27), totime(13, 11, 27), totime(14, 11, 27)]; time dd[3]; dd = d; dd[2] |
| x[i to j] | A statement used to define an array. | The return value of the following statement is "true". string range strary = ["a" to "z"]; string x = "d"; x in strary |
| x[i _to j] | The operator specifies a range of values greater than but not including the value i, and less than or equal to the value j. Both i and j are of the Number type. | The return value of the following statement is "true". integer a[] = [1,1,2,3,4]; 3 in a[2 _to 4]; |
| x[i to_ j] | The operator specifies a range of values greater than or equal to the value i, and less than but not including the j value. Both i and j are of the Number type. | The return value of the following statement is "true". integer a[] = [1,1,2,3,4]; 3 in a[2 to_ 4]; |
| x[i _to_ j] | The operator specifies a range of values greater than but not including the value i, and less than but not including the value j. Both i and j are of the Number type. | The return value of the following statement is "true". integer a[] = [1,1,2,3,4]; 3 in a[2 _to_ 4]; |
| x[upfrom j] | The operator specifies a range of values greater than or equal to the value j. j is Number data type. | The return value of the following statement is "false". integer a[] = [1,1,2,3,4]; 3 in a[upfrom 4] |
| x[upfrom_ j] | The operator specifies a range of values greater than but not including the value j. j is Number data type. | The return value of the following statement is "true". integer a[] = [1,1,2,3,4]; 3 in a[upfrom_ 2]; |
| x[upto j] | The operator specifies a range of values less than or equal to the valuej. j is Number data type. | The return value of the following statement is "true". integer a[] = [1,1,2,3,4]; 3 in a[upto 4]; |
| x[upto_ j] | The operator specifies a range of values less than but not including the value j. j is Number data type. | The return value of the following statement is "false". integer a[] = [1,1,2,3,4]; 4 in a[upto_ 4]; |
| if(b) then{...} else{...} | Conditional statement. | The return value of the following statement is "abc". integer s=5; integer f=8; if ( f>s ) then return "abc" else return "def" |
| return x | Returns the value of X. | The result of the following statement is "06/19/01". return Today () |

Previous Topic  Next Topic
