---
title: "Query Filter Dialog Box Properties"
id: 4405690522007
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:48Z
---

# Query Filter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690518423-Printable-Version-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690521111-Quick-Schedule-Dialog-Box-Properties)

# Query Filter Dialog Box Properties

You can use the Query Filter dialog box to [apply a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/4405683956247-Applying-Filters-to-Page-Report#BV) that the specified data component uses, to narrow down its data scope. This topic describes the properties in the dialog box.

**Advanced/Basic**

Select to switch between [advanced mode](#Advanced) or [basic mode](#Basic).

You see these elements in both modes:

**Query Filter**

Select the filter you want to apply to the business view.

* **User Defined**  
   Select to create a user defined filter to apply to the business view.
* **Predefined filters**  
   Server lists the names of the predefined filters which you created using the business view in Logi Report Designer. You can choose one of them to apply.
  + **Edit**  
     Select to edit the selected predefined filter. Once you edit a predefined filter, Server saves it as a user defined filter in the business view.
  + **Description**  
     Server displays the description of the selected predefined filter.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Basic Mode

You can create simple filter conditions using the AND/OR logic.

![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4420447158039/qryfltr_basic.gif)

![Delete Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4420447089175/btn_pgrpt_no.gif)**Remove button**

Select to delete the current condition line.

**Field**

Select the field you want to filter.

**Operator**

Select the [operator](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties#Operator) to compose the filter expression.

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the list. Select the **Toggle to Field** button ![Filter By Field](https://devnet.logianalytics.com/hc/article_attachments/4420453494807/btn_pgrpt_field.gif) or **Toggle to Value** button ![Filter By Value](https://devnet.logianalytics.com/hc/article_attachments/4420447158295/btn_pgrpt_value.gif) to filter the field by either field or value.

**Logic**

Select a logic operator.

* **AND**  
   Select to connect this line with the next line using the **AND** logic.
* **OR**  
   Select to connect this line with the next line using the **OR** logic.
* **END**  
   Select to end the whole condition expression.

## Advanced Mode

You can build more complex filter conditions by grouping conditions.

![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4420453495447/qryfltr_advc.gif)

**Add Condition**

Select to add a new condition line. Each condition line contains an expression which is composed of a field, an operator, and a value.

**Delete**

Select to delete the selected condition lines or groups.

**Group**

Select to make the selected condition lines become a group. A group can only have one logic operator to connect all its condition lines. For example, a group contains three conditions lines, which are expression A, B, and C, and the group's logic operator is OR, then the group's expression is: A OR B OR C.

You can also add condition lines to an existing group. Select the condition lines and the group while selecting **Ctrl**, and then select **Group**.

**Ungroup**

Select to move the selected condition lines and groups out of a group or disband a group.

**Up**

Select to move the selected condition line or group higher.

**Down**

Select to move the selected condition line or group lower.

**Logic**

Specify the logic operator of a condition group. Each time you select the logic button, Server displays the next item following the order below.

* **AND**  
   Select to connect all the condition lines and groups in the group using the **AND** logic.
* **OR**  
   Select to connect all the condition lines and groups in the group using the **OR** logic.
* **AND NOT**   
   Select to connect all the condition lines and groups in the group using the **AND NOT** logic.
* **OR NOT**   
   Select to connect all the condition lines and groups in the group using the **OR NOT** logic.

**Field**

Select the field you want to filter.

**Operator**

Select the [operator](https://devnet.logianalytics.com/hc/en-us/articles/4405683818007-Filter-Dialog-Box-Properties#Operator) to compose the filter expression.

**Value**

Specify the value of the field. You can either type the value manually in the text box or select a value from the list. Select the **Toggle to Field** button ![Filter By Field](https://devnet.logianalytics.com/hc/article_attachments/4420453494807/btn_pgrpt_field.gif) or **Toggle to Value** button ![Filter By Value](https://devnet.logianalytics.com/hc/article_attachments/4420447158295/btn_pgrpt_value.gif) to filter the field by either field or value.

**Condition Expression**

Server displays the SQL statement of the filter condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690518423-Printable-Version-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690521111-Quick-Schedule-Dialog-Box-Properties)
