---
title: "New Parameter Dialog Box"
id: 1500010098041
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098041-New-Parameter-Dialog-Box
updated_at: 2021-07-23T19:15:47Z
---

# New Parameter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098021-New-General-Hierarchical-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box)

# New Parameter Dialog Box

You can use the New Parameter dialog box to [create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#Predefine) in the current catalog, or [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to use in the current report. This topic describes the options in the dialog box.

Designer displays the New Parameter dialog box when you do one of the following:

* Right-click the Parameters node in the Catalog Manager and select New Parameter from the shortcut menu.
* Select the <New Parameter…> item where a parameter list is provided.
* In the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096921-Formula-Editor-Dialog-Box) or [User Defined Function Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box), select Menu > File > New Parameter.

![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848447255/nwprm.gif)

You see the following options in the dialog box:

**Name**

Specify the name of the parameter.

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

**Value**

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

You can specify the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#Options) for the parameter in this box.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098021-New-General-Hierarchical-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box)
