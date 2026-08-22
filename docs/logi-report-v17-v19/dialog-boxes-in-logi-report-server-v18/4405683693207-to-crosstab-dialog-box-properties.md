---
title: "To Crosstab Dialog Box Properties"
id: 4405683693207
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683693207-To-Crosstab-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:51Z
---

# To Crosstab Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683692055-To-Chart-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683691031-Turn-to-Page-Dialog-Box-Properties)

# To Crosstab Dialog Box Properties

You can use the To Crosstab dialog box to [convert a chart into a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/4405683959319-Manipulating-Data-Components-in-Page-Report#ToCrosstab). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Display Tab Properties](#Display)
* [Style Tab Properties](#Style)

You see these elements on both tabs:

**Back**

Select to go to the previous tab.

**Next**

Select to go to the next tab.

**OK**

Select to convert the chart to a crosstab.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Display Tab Properties

Specify the data fields you want to display in the crosstab.

![To Crosstab dialog box - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4420447148183/tocrstb_dsply.gif)

**Resources**

Server displays all the view elements used in the chart. Select a field, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif) beside the Columns, Rows, or Summaries box to add it into the corresponding box.

**Columns/Rows**

* **Field**  
   Server lists the group objects you added to display on the column/row headers of the crosstab. To remove an object from a box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.
* **Display Name**  
   Specify the labels for the column/row headers. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Sort**  
   Select the sort order of a group object.
* **![Add Compound Group](https://devnet.logianalytics.com/hc/article_attachments/4420453504151/btn_pgrpt_addparal.gif) Add Compound Group button**  
  Select to add a column/row compound group.

**Summaries**

* **Field**  
   Server lists the aggregation objects you added as the aggregate fields of the crosstab. To remove an object from the box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.
* **Display Name**  
   Specify the labels for the aggregations. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Style Tab Properties

Specify the style of the crosstab. Server hides this tab when there is only one style available.

![To Crosstab dialog box - Style tab](https://devnet.logianalytics.com/hc/article_attachments/4420447299223/tocrstb_style.gif)

**Style**

Select the style you want to apply to the component.

* **Custom**  
   There is no style information in this style. Server only uses it to support reports you created in previous versions when they do not bind any style or their styles are not in the style list.

**Preview**

Server displays a diagram to illustrate the effect of the selected style on the component.

**Inherit Style**

Select to take the style of the parent component. The property is available when the chart is in a table or banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683692055-To-Chart-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683691031-Turn-to-Page-Dialog-Box-Properties)
