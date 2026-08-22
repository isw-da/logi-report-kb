---
title: "Applying Dynamic Names for Published Result Files"
id: 1500009724322
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files
updated_at: 2021-07-25T07:18:40Z
---

# Applying Dynamic Names for Published Result Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724242-Scheduling-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results)

# Applying Dynamic Names for Published Result Files

When publishing a report to disk or to e-mail, if you schedule to publish the report result periodically with a fixed name, then only the last generated report result can be kept. In order to save the result generated every time, a dynamic result file name must be used. Similarly, you can use a dynamic directory path to avoid report management difficulties, since when a fixed directory path is specified too many results may be generated in a single directory. Logi Report Server provides you with the following defined strings to form a dynamic name:

| By | Strings Defined | Description (Sample) |
| --- | --- | --- |
| Time | Forms the file name using the date/time when the result is generated (for example, 2006-07-25, 00:00:00 AM). |
| > | yyyy | Returns the year (for example, 2006). |
|  | yy | Returns the year in short form (for example, 06). |
|  | MM | Returns the month of the year, shown in number format (for example, 12). |
|  | dd | Returns the day of the month, (for example, 25). |
|  | hh | Returns the hour of the day (for example, 05). It is used for the 12-hour time. |
|  | HH | Returns the hour of the day (for example, 05). It is used for the 24-hour time. |
|  | mm | Returns the minute of the hour (for example, 00). |
|  | ss | Returns the second of the minute (for example, 00). |
|  | m | Returns the AM/PM marker (for example, AM). |
|  | +/- | Performs simple +/- operation on the date/time (for example, if current date is June 20, the result of [dd+2] is 22 and that of [dd-5] is 15 ). |
| Parameter |  | Forms the file name using the parameter value specified for <param\_name>. |
|  | param\_<param\_name> | Returns the value of <param\_name>. |
|  | paramDisplay\_<param\_name> | Returns the display value of <param\_name>. |
| User |  | Forms the file name using user name. |
|  | name | Returns the name of the user who is currently logged onto the computer (for example, Mike). |
|  | z | Returns the ordinal number (for example, 001.pdf, 002.pdf, 003.pdf). |
| System |  | Forms the file name using the system variables. |
|  | language | Returns local computer configuration language (for example, en). |
|  | zone | Returns the system configuration time zone (for example, GMT-05.00). |
|  | encoding | Returns the file encoding (for example, Cp1252). |
|  | region | Returns the system configuration region (for example, US). |
| Logi Report |  |  |
|  | pathcat | Returns the catalog file name, with its path and extension (for example, path.SampleReports.cat). |
|  | CAT | Returns the catalog file name, with its extension (for example, SampleReports.cat). |
|  | cat | Returns the catalog file name, without its path and extension (for example, SampleReports). |
|  | pathcls | Returns the report file name, with its full path (for example, catalog path and report path) and extension (for example, path1.path2.Employee Information List.cls). |
|  | CLS | Returns the report file name, with its extension (for example, Employee Information List.cls). |
|  | cls | Returns the report file name, without its extension and path (for example, Employee Information List). |
|  | sheet | Returns the report tab name in the report (for example, report1). However for formats such as .rst, .rsd, and .wst, the string "[sheet]" will be interpreted literally as "[sheet]" itself. |

**Naming rules**

* The defined strings are case-sensitive.
* Defined strings must be enclosed by square brackets ([ ]) which must appear in pairs, for example, [yyyy].

  If the string is not a defined string but enclosed by square brackets, an error message will be shown. For example, if you use myHTMLResult\_[yy]$[YYYY][MM]M[dd]D[ABCD] $name$cls[cls].html as the result file name, you will get an error message (Invalid file name), since ABCD is not defined, but appears in square brackets.
* You should never use square brackets to enclose strings that are not defined in the above table. Strings that are not in square brackets will be directly used as (part of) the file name.
* If you want the square brackets and the strings enclosed by them to appear in the file name exactly as they are, that is, not to be parsed as defined strings, you can add a dollar sign ($) before the string. For example, if the string is $[yyyy], the result file name will be [yyyy], instead of a specific year, such as 2006.

  If you want to keep the dollar sign ($) together with the square brackets and the strings, you should add another dollar sign ($). For example, if the string is $$[m], the result file name will be $[m], and if the string is $$$$[m], the result file name will be $$$[m].
* More than one defined string can be used in the dynamic result file name, except for the ordinal number (z), such as [m][name], [yyyy].[MM].[dd], [region][yy].
* Characters are permitted to be added between different defined strings. For example, if the string is [yy]Year[MM]Month, the result could be 02Year2thMonth.
* The number of digits of the ordinal number is determined by the total number of "z"s. For example, zzz indicates 001, 002, and so on, and zz indicates 01, 02, and so on.

Here are some examples of the dynamic result file name:

| Sample Name | Result File Name |
| --- | --- |
| myTXTResult\_[yyyy].[MM].[dd].[hh].[mm].[ss].txt | myTXTResult\_2003.10.30.05.14.45.txt |
| myTXTResult\_[MM-1].[param\_pCountry].[param\_pDate].[param\_pTime].txt | myTxtResult\_05.China\_USA.29.param\_pTime.txt |
| myPDFResult\_CT[zone][language][region]my$$[1].pdf | myPDFResult\_CTGMT-05.00enUSmy$[1].pdf |
| myRSTResult\_[pathcat][CLS].rst | myRSTResult\_SampleReports.SampleReports.catEmployee Information List.cls.rst |
| myRSTResult\_[zzz].rst | myRSTResult\_001.rst, myRSTResult\_002.rst, ... |
| myHTMLResult[cat]\_[cls]\_[zz].html | myHTMLResultSampleReports\_Corporate Overview\_01.html, myHTMLResultSampleReports\_Corporate Overview\_02.html,... |
| myHTMLResult\_[yy]$[YYYY][MM]M[dd]D$name$cls[cls].html | myHTMLResult\_02[YYYY]06M21D$name$clsCorporate Overview.html |

**Notes:**

* There are two differences between the naming rules of dynamic result file name and the dynamic directory name:
  + String "z" is only supported in the naming result file, but not in the naming dynamic directory. For example, `C:\folder[zz]\folder` is incorrect because the sequence for directory is not supported.
  + "/" will be replaced by "." in the naming result file. However, for naming a dynamic directory, this rule does not apply.
* When you publish a report to e-mail, string "z" is not dynamic. For example, zzz only indicates 001 and zz only indicates 01.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724242-Scheduling-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results)
