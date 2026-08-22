---
title: "Edit Parameter Dialog Box"
id: 1500010096341
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096341-Edit-Parameter-Dialog-Box
updated_at: 2021-07-23T19:15:18Z
---

# Edit Parameter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058802-Edit-Operation-Calling-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058822-Edit-Pre-join-Paths-Dialog-Box)

# Edit Parameter Dialog Box

You can use the Edit Parameter dialog box to [edit the specified parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog). This topic describes the options in the dialog box.

Designer displays the Edit Parameter dialog box when you right-click a parameter and select Edit Parameter from the shortcut menu in the Catalog Manager or in the Data panel.

![Edit Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848583191/edtprm.gif)

You see the following options in the dialog box:

**Name**

The option shows the name of the parameter.

**Value Setting**

Select the parameter type.

* **Type-in Parameter**  
  Select this type if you want to predefine parameter values by typing manually.
* **Bind with Single Column**  
  Select this type if you want to bind DBField with the parameter so as to retrieve the values of the DBField as the parameter values.
* **Bind with Cascading Columns**  
  Select this type if you want to create a group of cascading parameters so as to achieve the function of filtering parameters with parameters in a simple way. Designer does not display this type when the parameter is in a catalog data source that contains only XML connections.

**Value Type**

Select the data type of the parameter.

**Value section**

Designer displays different options in the section after Value Type according to the type you select from the Value Setting drop-down list.

* **For Type-in Parameter**
  + **Value List**  
    The box lists the values that you predefine for the parameter.
    - **Prompt Values** [format hint]   
      Specify the prompt values for the parameter. The [format hint] shows what the predefined values should look like.

      You can add more than one prompt value. All the prompt values must be of the same type as specified by Value Type.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
      Select to add a new prompt value to the list. Double-click in the value line to edit the value. If the parameter is of the Date, Time, or DateTime data type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to [set a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values#Date) from the calendar.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
      Select to delete the specified prompt value.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
      Select to move the specified value higher in the display sequence.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
      Select to move the specified value lower in the display sequence.
* **For Bind with Single Column**  
  + **Source**  
    Select the source type from which to retrieve the DBFields that you can use to bind with the parameter: Tables and Views (including synonyms), Stored Procedures, Imported SQLs, or User Defined.
  + **Bind Column**  
    Select the DBField to bind with the parameter.
  + **Display Column**  
    Select the DBField the values of which you want to display for specifying the parameter value at runtime.
* **For Bind with Cascading Columns**
  + **Data Source**  
    Select the data source from which to retrieve the columns which you can use to bind with the parameters.
  + **Value List**  
    Specify a group of cascading parameters.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
      Select to add a new parameter.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
      Select to delete the specified parameter.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
      Select to move the specified parameter to a higher level. The higher position a parameter has, the higher level it gets. Values of the lower-level parameters are controlled by values of the higher-level parameters.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
      Select to move the specified parameter to a lower level.
    - **Bind Column**  
      Select the DBField to bind with the parameter.
    - **Display Column**  
      Select the DBField the values of which you want to display for specifying the parameter value at runtime.
    - **Parameter**  
      Specify whether to set a group of Bind Column and Display Column as a parameter which becomes a member of the cascading parameter group.

**Options**

You can specify [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#Options) for the parameter in this box.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058802-Edit-Operation-Calling-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058822-Edit-Pre-join-Paths-Dialog-Box)
