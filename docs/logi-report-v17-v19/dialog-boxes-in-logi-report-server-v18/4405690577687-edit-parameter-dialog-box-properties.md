---
title: "Edit Parameter Dialog Box Properties"
id: 4405690577687
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690577687-Edit-Parameter-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:14Z
---

# Edit Parameter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690576791-Edit-Multimedia-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683814423-Enter-Parameter-Values-Dialog-Box-Properties)

# Edit Parameter Dialog Box Properties

This topic describes how you can use the Edit Parameter dialog box to [edit a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405684037271-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#Param) for a report.

Server displays the dialog box when you select the parameter button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4420461506455/btn_dshbrd_prm.gif) in the Value text box of the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683872023-Query-Filter-Dialog-Box-Properties) or [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties), select a local parameter from the Local Parameters node of the drop-down list, right-click it, and select **Edit** from the shortcut menu.

![Edit Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453584663/edtprm.gif)

**Name**

Specifies the name of the parameter.

**Value Setting**

Specifies the parameter type.

* **Type-in Parameter**  
   Using this type you can predefine parameter values by typing manually.
* **Bind with Single Column**  
   Using this type the parameter can be bound with a DBField. The values of the DBField will be retrieved as the parameter values.
* **Bind with Cascading Columns**  
   Using this type you can create a group of cascading parameters so as to achieve the function of filtering parameters with parameters in a simple way.

**Value Type**

Specifies the data type of the parameter.

**Values**

The section after Value Type varies with the type you select from the Value Setting drop-down list.

* **For Type-in Parameter**
  + **Value List**  
     Lists the predefined parameter values.
  + **Prompt Values** [format hint]   
     Predefines the parameter values. The [format hint] shows what the predefined values should look like.

    There can be more than one prompt value. All the prompt values must be of the same type as specified in the Value Type field.

    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif)  
       Adds a new prompt value to the list. Double-click in the value line to edit the value. If the parameter is of Date, DateTime, or Time type, you can also select the **Calendar** icon ![](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif) to set a date and time value using the calendar.
    - ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)  
       Removes the selected prompt value.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)  
       Adjusts the display sequence of selected value by moving it up a step.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)  
       Adjusts the display sequence of selected value by moving it down a step.
* **For Bind with Single Column**  
  + **Source**  
     Specifies the business view in the current data source from which to retrieve data for the parameter.
  + **Bind Column**  
     Specifies the group or detail object in the selected business view to be bound with the parameter.
  + **Display Column**  
     Specifies the group or detail object in the selected business view the values of which will be displayed for specifying the parameter value.
* **For Bind with Cascading Columns**
  + **Source**  
     Specifies the business view in the current data source from which to retrieve data for the parameter.
  + **Value List**  
     Defines a group of cascading parameters.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif)  
       Adds a new parameter.
    - ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)  
       Removes the selected parameter.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)  
       Adjusts the parameter level by moving it up a step. The higher the position is, the higher the level is. The lower level field values are controlled by the higher level field values.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)  
       Adjusts the parameter level by moving it down a step.
    - **Bind Column**  
       Specifies the group or detail object in the selected business view to be bound with the parameter.
    - **Display Column**  
       Specifies the group or detail object in the selected business view the values of which will be displayed for specifying the parameter value.
    - **Parameter**  
       Specifies whether to set a group of Bind Column and Display Column as a parameter which will become a member of the cascading parameter group. All parameters in the cascading group will be created as independent parameters.

      The parameter name is provided by Logi Report automatically, and the format is *[The name specified as parameter name]-[Bind Column name]*.

**Options**

Specifies options for the parameter. For more information, see [Options](https://devnet.logianalytics.com/hc/en-us/articles/4405683788823-Add-Parameter-Dialog-Box-Properties#Options).

**OK**

Applies all changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683787799-Add-Aggregation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683814423-Enter-Parameter-Values-Dialog-Box-Properties)
