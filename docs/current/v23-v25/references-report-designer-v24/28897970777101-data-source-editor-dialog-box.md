---
title: "Data Source Editor Dialog Box"
id: 28897970777101
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897970777101-Data-Source-Editor-Dialog-Box
updated_at: 2024-09-30T09:10:44Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Data Source Editor Dialog Box

You can use the Data Source Editor dialog box  to simplify using cached query results by  adding or editing a data source driver in a catalog. This topic describes the options in the dialog box.
    

Designer displays the Data Source Editor dialog box when you select New, or select a data source driver and then select Edit in the Data Source Drivers dialog box.

Designer displays these options:

Driver Name

Specify the name you want to use for the data source driver.

URL

Select  to specify the URL of the driver definition.

The URL contains three parts: scheme, qualified class name, and arguments. If the data source driver does not use arguments, the argument part does not appear in the URL. Its syntax is: URL = "jrquery" ":" "/" qualified_classname[ ";" params].

Driver

Select to specify the driver configuration if you don't specify the URL. 

- 
Scheme
Specify the scheme of the driver. Currently only "jrquery" is available.

- 
Class Name
Specify the qualified class name.

- 
Parameters
Specify the arguments for the data source driver. You should separate the arguments by semicolons (";").

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
