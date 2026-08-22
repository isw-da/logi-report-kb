---
title: "Page Report Properties"
id: 4405664668695
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664668695-Page-Report-Properties
updated_at: 2022-01-27T20:35:56Z
---

# Page Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664666903-Page-Header-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties)

# Page Report Properties

This topic describes the properties of a Page Report object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) A page report may contain one or more report tabs. By default, the root node in the report structure tree represents the current report tab. You can select **Forward**![](https://devnet.logianalytics.com/hc/article_attachments/4420550817175/btn_forwd.gif) on the Report Inspector toolbar to show the page report as the root node (if the current root node represents the report body of the current report tab, you need to select the button twice). After showing the page report node in the Report Inspector, you can select the node to set its properties.

| Property Name | Description |
| --- | --- |
| General (available for page reports created using query resources) | |
| Class Type | Shows the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Others | |
| Constrained Data | Specifies whether to constrain users to use the business views the page report applies only, if they need to add more data components into the report at runtime. Data type: Boolean |
| Import Parameter Values | Specifies the name of a class name with the full package name, from which to import default values for parameters the page report applies. This property takes effect when you set Parameter List Auto of the report to "false". For more information, see [Importing Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/4405664613783-Importing-Parameter-Values).  Data type: String |
| Parameter List Auto | Specifies where to get the default values for the parameters the page report applies. If "true", Logi Report Engine gets the default values from values defined in the catalog; if "false", it gets the default values from the class file specified by the Import Parameter Values property. Data type: Boolean |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/4405664629143-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in the page report to DBMS at runtime. Choose an option from the drop-down list.  * **default** - Select to apply the setting for the Push Down Group Query property of the query each data component in the report uses correspondingly. * **true** - Select to push down group level summary computations to DBMS if the DBMS can do the computations; otherwise, Logi Report Engine performs the computations itself. * **false** - Select to let Logi Report Engine perform group level summary computations itself.   Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664666903-Page-Header-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties)
