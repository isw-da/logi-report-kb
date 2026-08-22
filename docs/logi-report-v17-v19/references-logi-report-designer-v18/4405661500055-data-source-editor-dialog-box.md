---
title: "Data Source Editor Dialog Box"
id: 4405661500055
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661500055-Data-Source-Editor-Dialog-Box
updated_at: 2022-01-27T20:38:12Z
---

# Data Source Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664450967-Display-Attributes-Dialog-Box)

# Data Source Editor Dialog Box

You can use the Data Source Editor dialog box to simplify using cached query results by [adding or editing a data source driver](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results#Manage) in a catalog. This topic describes the options in the dialog box.

Designer displays the Data Source Editor dialog box when you select New, or select a data source driver and then select Edit in the [Data Source Drivers dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box).

![Data Source Editor](https://devnet.logianalytics.com/hc/article_attachments/4420542159767/dtsrcedtr.gif)

You see the following options in the dialog box:

**Driver Name**

Specify the name you want to use for the data source driver.

**URL**

Select to specify the URL of the driver definition.

The URL contains three parts: scheme, qualified class name, and arguments. If the data source driver does not use arguments, the argument part does not appear in the URL. Its syntax is: URL = "jrquery" ":" "/" qualified\_classname[ ";" params].

**Driver**

Select to specify the driver configuration if you don't specify the URL.

* **Scheme**  
  Specify the scheme of the driver. Currently only "jrquery" is available.
* **Class Name**  
  Specify the qualified class name.
* **Parameters**  
  Specify the arguments for the data source driver. You should separate the arguments by semicolons (";").

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661498903-Data-Source-Drivers-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664450967-Display-Attributes-Dialog-Box)
