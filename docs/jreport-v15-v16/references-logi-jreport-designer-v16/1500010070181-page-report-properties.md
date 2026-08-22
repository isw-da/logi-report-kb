---
title: "Page Report Properties"
id: 1500010070181
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070181-Page-Report-Properties
updated_at: 2021-07-24T10:37:53Z
---

# Page Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034302-Page-Header-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties)

# Page Report Properties

This topic lists the properties of a Page Report object.

A page report may contain one or more report tabs, and each report tab contains a report body. The Report Inspector enables you to focus on one of the three levels, namely the page report, report tab, and report body. By default, the root node in the Report Inspector represents the current report tab. You can select the Up button ![](https://devnet.logianalytics.com/hc/article_attachments/4404901115671/btn_up.gif) on the toolbar to show the page report as the root node (if the current root node represents the report body, you should select that button twice). After showing the page report node in the Report Inspector, you can set its properties:

| Property Name | Description |
| --- | --- |
| General (available for page reports created using query resources) | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Others | |
| Import Parameter Values | Specifies the name of a class file from which to import default values for parameters used in the report, for example, TestParamList. Then when viewing the report, the displayed Enter Parameter Values dialog will only list the imported default parameters. To make the property work, you need specify the Parameter List Auto property to false.  For more information, see [Importing Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010069021-Importing-Parameter-Values).  Data type: String |
| Parameter List Auto | Specifies whether to get the default values for parameters used in the report from values defined in the catalog.  * **true** - Gets parameter default values from values defined in catalog. * **false** - Gets parameter default values from the class file specified by the Import Parameter Values property.   Data type: Boolean |
| [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500010069181-JDBC-Hive-Connection-Properties#PushDown) | Specifies whether to push down group level summary computations in the page report to the DBMS at runtime. Choose an option from the drop-down list.  * **default** - The settings of the Push Down Group Query property for the queries on which the data components in the page report are created will be applied for each data component correspondingly. * **true** - Logi JReport will push down the group level summary computations to the DBMS if the DBMS can do the computations, otherwise, Logi JReport will do the computations itself. * **false** - Logi JReport will do the group level summary computations itself.   Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034302-Page-Header-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties)
