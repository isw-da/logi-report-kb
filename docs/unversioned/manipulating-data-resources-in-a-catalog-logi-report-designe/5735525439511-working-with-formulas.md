---
title: "Working with Formulas"
id: 5735525439511
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525439511-Working-with-Formulas
updated_at: 2022-11-02T07:57:58Z
---

# Working with Formulas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532445591-Importing-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels)

# Working with Formulas

Formulas are objects that are computed at runtime, which enable you to manipulate field data by performing calculations on it. They control the data to display, and can even create new data that is not directly available from the database. This topic introduces the levels and syntax of the Logi Report formulas, and how you can create formulas in a catalog, apply user-defined functions (UDF), and use formulas to control report object properties.

A formula is a symbolic statement of the manipulations that Logi Report Engine performs on certain data before it displays the data in your report. For example, if your report contains a "Sales" field and a "Cost" field, and you want to create a "GrossProfit" formula, you can designate its value as *@Sales - @Cost*. "GrossProfit" is a simple formula that tells Logi Report Engine to subtract the value of the "Cost" field from the value of the "Sales" field, and then to display the result. You can use formulas to calculate numeric values, compare one value to another, select alternative actions based on the comparison, and join multiple text strings into a single string. In general, you can use formulas to achieve the following:

* Calculating information you cannot directly obtain from database data fields
* Comparing data
* Joining text with data
* Converting data from one form to another
* Enhancing formatting options with text strings
* Doing other things that customize your reports

Logi Report provides a number of built-in functions for you to build your formulas. It also provides user-defined formula functions that enable you to design your own formula functions.

Select the following links to view the topics:

* [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels)
* [Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax)
* [Creating Formulas in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog)
* [Using User-Defined Formula Functions](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions)
* [Using Formulas to Control Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif)

* You can only use JDK (not JRE) to compile formulas created in Logi Report.
* Logi Report formulas search for javac based on the "java.home" option, but this way may fail under some user environments. To ensure the formulas can work, you should use the "javac\_path" option to specify the full path of javac yourself, for example, set `-Djavac_path=c:\jdk1.8.0\bin\javac.exe` in the startup file of the Logi Report products.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532445591-Importing-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels)
