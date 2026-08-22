---
title: "Applying Dynamic Names for Published Report Files"
id: 5741483587607
section: "Running and Scheduling Reports Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741483587607-Applying-Dynamic-Names-for-Published-Report-Files
updated_at: 2022-10-31T17:18:21Z
---

# Applying Dynamic Names for Published Report Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports)

# Applying Dynamic Names for Published Report Files

This topic describes how you can use dynamic file names and dynamic directory paths to save report outputs when you publish reports to disk or to email.

If you schedule to publish a report periodically with a fixed name, then Server only keeps the last generated report output. To save the output generated every time, you need to use a dynamic file name. Similarly, you can use a dynamic directory path to avoid report management difficulties, since for a fixed directory path too many outputs might be generated in a single folder.

Server provides you with the following defined strings to form a dynamic name:

| By | Strings Defined | Description (Sample) |
| --- | --- | --- |
| Time |  | Form the file name using the date/time when Server generates the output (for example, 2006-07-25, 00:00:00 AM). |
|  | yyyy | Return the year (for example, 2006). |
|  | yy | Return the year in short form (for example, 06). |
|  | MM | Return the month of the year, shown in number format (for example, 12). |
|  | dd | Return the day of the month, (for example, 25). |
|  | hh | Return the hour of the day (for example, 05). It is for the 12-hour time. |
|  | HH | Return the hour of the day (for example, 05). It is for the 24-hour time. |
|  | mm | Return the minute of the hour (for example, 00). |
|  | ss | Return the second of the minute (for example, 00). |
|  | m | Return the AM/PM marker (for example, AM). |
|  | +/- | Perform the +/- operation on the date/time (for example, if current date is June 20, the result of [dd+2] is 22 and that of [dd-5] is 15 ). |
| Field |  | Form the file name using the value of the column specified by <ColName>. |
|  | recipMapping\_<colName> | This property is for bursting report output. It returns the value of the column or field whose mapping name in the catalog is <ColName>. The column must be one in the recipient queries defined in the bursting schemas that you selected for the schedule. |
| Parameter |  | Form the file name using the value of the parameter specified by <param\_name>. |
|  | param\_<param\_name> | Return the value of <param\_name>. |
|  | paramDisplay\_<param\_name> | Return the display value of <param\_name>. |
| User |  | Form the file name using username. |
|  | name | Return the name of the user who currently signed into the computer (for example, Mike). |
|  | z | Return the ordinal number (for example, 001.pdf, 002.pdf, and 003.pdf). |
| System |  | Form the file name using the system variables. |
|  | language | Return local computer configuration language (for example, en). |
|  | zone | Return the system configuration time zone (for example, GMT-05.00). |
|  | encoding | Return the file encoding (for example, Cp1252). |
|  | region | Return the system configuration region (for example, US). |
| Logi Report |  |  |
|  | pathcat | Return the catalog file name, with its path and extension (for example, path.SampleReports.cat). |
|  | CAT | Return the catalog file name, with its extension (for example, SampleReports.cat). |
|  | cat | Return the catalog file name, without its path and extension (for example, SampleReports). |
|  | pathcls | Return the report file name, with its full path (for example, catalog path and report path) and extension (for example, path1.path2.Employee Information List.cls). |
|  | CLS | Return the report file name, with its extension (for example, Employee Information List.cls). |
|  | cls | Return the report file name, without its extension and path (for example, Employee Information List). |
|  | sheet | Return the report tab name in the report (for example, report1). However, for formats such as .rst, .rsd, and .wst, Server interprets the string "[sheet]" literally as "[sheet]" itself. |

**Naming rules**

* The defined strings are case-sensitive.
* You must enclose defined strings by square brackets ([ ]) which must appear in pairs, for example, [yyyy].

  If the string is not a defined string but enclosed by square brackets, Server will display an error message. For example, if you use myHTMLResult\_[yy]$[YYYY][MM]M[dd]D[ABCD] $name$cls[cls].html as the report file name, you will get an error message saying Invalid file name, since ABCD is not defined, but appears in square brackets.
* You should never use square brackets to enclose strings that are not defined in the preceding table. Strings that are not in square brackets will be directly used as (part of) the file name.
* If you want the square brackets and the strings enclosed by them to appear in the file name exactly as they are, that is, not to be parsed as defined strings, you can add a dollar sign ($) before the string. For example, if the string is $[yyyy], the report file name will be [yyyy], instead of a specific year, such as 2006.

  If you want to keep the dollar sign ($) together with the square brackets and the strings, you should add another dollar sign ($). For example, if the string is $$[m], the report file name will be $[m], and if the string is $$$$[m], the report file name will be $$$[m].
* You can use more than one defined string in the dynamic report file name, except for the ordinal number (z), such as [m][name], [yyyy].[MM].[dd], [region][yy].
* You can add characters between different defined strings. For example, if the string is [yy]Year[MM]Month, the result could be 02Year2thMonth.
* The number of digits of the ordinal number is determined by the total number of "z"s. For example, zzz indicates 001, 002, and so on, and zz indicates 01, 02, and so on.

See the following examples of dynamic report file names:

| Sample Name | Report File Name |
| --- | --- |
| myTXTResult\_[yyyy].[MM].[dd].[hh].[mm].[ss].txt | myTXTResult\_2003.10.30.05.14.45.txt |
| myTXTResult\_[MM-1].[param\_pCountry].[param\_pDate].[param\_pTime].txt | myTxtResult\_05.China\_USA.29.param\_pTime.txt |
| myPDFResult\_CT[zone][language][region]my$$[1].pdf | myPDFResult\_CTGMT-05.00enUSmy$[1].pdf |
| myRSTResult\_[pathcat][CLS].rst | myRSTResult\_SampleReports.SampleReports.catEmployee Information List.cls.rst |
| myRSTResult\_[zzz].rst | myRSTResult\_001.rst, myRSTResult\_002.rst, ... |
| myHTMLResult[cat]\_[cls]\_[zz].html | myHTMLResultSampleReports\_Corporate Overview\_01.html, myHTMLResultSampleReports\_Corporate Overview\_02.html,... |
| myHTMLResult\_[yy]$[YYYY][MM]M[dd]D$name$cls[cls].html | myHTMLResult\_02[YYYY]06M21D$name$clsCorporate Overview.html |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* There are two differences between the naming rules of dynamic report file name and the dynamic directory name:
  + Server only supports the string "z" in the naming report file, but not in the naming dynamic directory. For example, `C:\folder[zz]\folder` is incorrect because Server does not support the sequence for directory.
  + Server replaces "/" by "." in the naming report file. However, for naming a dynamic directory, this rule does not apply.
* When you publish a report to email, the string "z" is not dynamic. For example, zzz only indicates 001 and zz only indicates 01.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports)
