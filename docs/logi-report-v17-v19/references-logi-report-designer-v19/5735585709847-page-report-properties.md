---
title: "Page Report Properties"
id: 5735585709847
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735585709847-Page-Report-Properties
updated_at: 2022-11-02T08:18:47Z
---

# Page Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533514391-Export-Page-Setting-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties)

# Page Report Properties

This topic describes the properties of a Page Report object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) A page report may contain one or more report tabs. By default, the root node in the report structure tree represents the current report tab. You can select **Forward**![](https://devnet.logianalytics.com/hc/article_attachments/9898404942615/btn_forwd.gif) on the Report Inspector toolbar to show the page report as the root node (if the current root node represents the report body of the current report tab, you need to select the button twice). After showing the page report node in the Report Inspector, you can select the node to set its properties.

| Property Name | Description |
| --- | --- |
| General (available for query-based page report) | |
| Class Type | Shows the class type of the object. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Others | |
| Constrained Data | Specifies whether to constrain users to use the business views the page report applies only, if they need to add more data components into the report at runtime. Data type: Boolean |
| Import Parameter Values | Specifies the name of a class name with the full package name, from which to import default values for the parameters the page report applies, when you set Parameter List Auto to "false". See [Importing Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/5735532445591-Importing-Parameter-Values). Data type: String |
| Parameter List Auto | Specifies whether to get the default values for the parameters the page report applies from the values you have defined in the catalog. When you set this property to "false", Logi Report Engine gets the default parameter values from the class file you specify via the Import Parameter Values property. Data type: Boolean |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in the page report to the database at runtime. Choose an option from the drop-down list.  * **default** Select to apply the setting for the Push Down Group Query property of the query each data component in the report uses correspondingly. * **true** Select to push down group level summary computations to the database if it can do the computations; otherwise, Logi Report Engine performs the computations itself. * **false** Select to let Logi Report Engine perform group level summary computations itself.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533514391-Export-Page-Setting-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties)
