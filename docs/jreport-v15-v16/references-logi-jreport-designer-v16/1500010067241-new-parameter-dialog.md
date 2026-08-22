---
title: "New Parameter Dialog"
id: 1500010067241
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog
updated_at: 2021-07-24T10:38:34Z
---

# New Parameter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067221-New-General-Hierarchical-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog)

# New Parameter Dialog

The New Parameter dialog helps you to [create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Predefine)  in the current catalog, or [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param)  to use in the current report. It appears when you do one of the following:

* Right-click the Parameters node in the Catalog Manager and select New Parameter from the shortcut menu.
* Select the <New Parameter…> item where a parameter list is provided.
* In the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010066181-Formula-Editor-Dialog) or [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010032902-User-Defined-Function-Editor-Dialog), select Menu > File > New Parameter.

![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909139223/nwprm.gif)

The following are details about options in the dialog.

**Name**

Specifies the name of the parameter.

**Value Setting**

Specifies the parameter type.

* **Type-in Parameter**  
   Using this type you can predefine parameter values by typing manually.
* **Bind with Single Column**  
   Using this type the parameter can be bound with a DBField. The values of the DBField will be retrieved as the parameter values.
* **Bind with Cascading Columns**  
   Using this type you can create a group of cascading parameters so as to achieve the function of filtering parameters with parameters in a simple way. Not available when the parameter is in a catalog data source that contains only XML connections.

**Value Type**

Specifies the data type of the parameter.

**Value**

The section after Value Type varies with the type you select from the Value Setting drop-down list.

* **For Type-in Parameter**
  + **Value List**  
     Lists the predefined parameter values.
  + **Prompt Values** [format hint]  
     Predefines the parameter values. The [format hint] shows what the predefined values should look like.

    There can be more than one prompt value. All the prompt values must be of the same type as specified in the Value Type field.

    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
       Adds a new prompt value to the list. double-click in the value line to edit the value. If the parameter is of Date, DateTime, or Time type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) to [set a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values#Date) in the calendar dialog.
    - ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
       Removes the selected prompt value.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
       Adjusts the display sequence of selected value by moving it up a step.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
       Adjusts the display sequence of selected value by moving it down a step.
* **For Bind with Single Column**  
  + **Source**  
     Specifies the source type from which to retrieve the DBFields which can be used to bind with the parameter. The available source types are: Tables and Views (including synonyms), Stored Procedures, Imported SQLs, and User Defined. However, when the parameter is in a catalog data source that contains only MongoDB connections, only Tables and User Defined are available in the Source drop-down list.
  + **Bind Column**  
     Specifies the DBField to be bound with the parameter.
  + **Display Column**  
     Specifies the DBField the values of which will be displayed for specifying the parameter value at runtime.
* **For Bind with Cascading Columns**
  + **Data Source**  
     Specifies the data source from which to retrieve the columns which can be used to bind with the parameters. The available data sources are tables, views, synonyms, stored procedures, imported SQLs, and user defined data sources in the same catalog data source as the parameter. However, when the parameter is in a catalog data source that contains only MongoDB connections, only tables and user defined data sources are available.
  + **Value List**  
     Defines a group of cascading parameters.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
       Adds a new parameter.
    - ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
       Removes the selected parameter.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
       Adjusts the parameter level by moving it up a step. The higher the position is, the higher the level is. The lower level field values are controlled by the higher level field values.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
       Adjusts the parameter level by moving it down a step.
    - **Bind Column**  
       Specifies the DBField to be bound with the parameter.
    - **Display Column**  
       Specifies the DBField the values of which will be displayed for specifying the parameter value at runtime.
    - **Parameter**  
       Specifies whether to set a group of Bind Column and Display Column as a parameter which will become a member of the cascading parameter group. All parameters in the cascading group will be created as independent parameters.

      The parameter name is provided by Logi JReport automatically, and the format is *[The name specified as parameter name]-[Bind Column name]*.

**Options**

Specifies [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Options) for the parameter.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067221-New-General-Hierarchical-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog)
