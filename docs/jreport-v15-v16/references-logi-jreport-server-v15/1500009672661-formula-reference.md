---
title: "Formula Reference"
id: 1500009672661
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009672661-Formula-Reference
updated_at: 2021-07-24T20:54:18Z
---

# Formula Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671441-Sort)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648122-Formula-Levels-)

# Formula Reference

A formula is a symbolic statement of the manipulations you want to perform on certain data. Logi JReport provides a number of built-in functions for you to build your formula. Also it provides user-defined formula (UDF) functions that allow you to design your own formula functions.

Generally, formulas can be used:

* to calculate information you cannot obtain directly from database data fields,
* to compare data,
* to join text with data,
* to convert data from one form to another,
* to enhance the formatting options with text strings, and
* to do a number of other things to customize your reports.

**Note:** When running in the Java VM environment using JDK, Logi JReport Server can use javac.exe in the JDK to compile formulas. However if Logi JReport runs with JRE, you need to specify a Java compiler for compiling formulas, otherwise formulas in reports may not work or even result in the failure of running the reports. In the JRE environment, if you are going to use Eclipse to compile formulas, add the option *-Djavacompiler=ECJcompiler* in the startup file of Logi JReport Server. If you are to use tools.jar to compile, copy tools.jar from `JDK(where the JRE is located)\lib` to the `JRE\lib` folder and add the option *-Djavacompiler=SysCompiler* in the Logi JReport Server startup file.

The following topics provide additional information about formulas:

* [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500009648122-Formula-Levels-)
* [Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/1500009672901-Formula-Syntax)
* [Data Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009648082-Data-Type)
* [Built-In Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009672681-Built-In-Functions)
* [Operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009648142-Operators)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671441-Sort)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648122-Formula-Levels-)
