---
title: "Edit Parameter Dialog"
id: 1500010065721
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065721-Edit-Parameter-Dialog
updated_at: 2021-07-24T10:38:56Z
---

# Edit Parameter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065701-Edit-Operation-Calling-Property-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030522-Edit-Pre-join-Paths-Dialog)

# Edit Parameter Dialog

The Edit Parameter dialog helps you to [edit the selected parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog). It appears when you right-click a parameter and select Edit Parameter from the shortcut menu in the Catalog Manager or the Data panel.

![Edit Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909223319/edtprm.gif)

The following are details about options in the dialog:

**Name**

Displays the name of the parameter.

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
       Adds a new prompt value to the list. double-click in the value line to edit the value. If the parameter is of Date, DateTime, or Time type, you can also select the calendar button ![](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) to [set a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values#Date) in the calendar dialog.
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

      **Note:**
      This feature is only useful when the default SQL generated by Logi JReport returns the correct values for the bound parameters. When you need more complex SQL you must use Bind With Single Column and manually enter the SQL to reference the higher level parameter in each lower level. For example, you may have State and City, the City parameter can reference the State parameter such as SELECT City FROM Customers WHERE Customers.State = @State.

**Options**

Specifies [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Options) for the parameter.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065701-Edit-Operation-Calling-Property-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030522-Edit-Pre-join-Paths-Dialog)
