---
title: "Subreport Dialog"
id: 1500009567722
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567722-Subreport-Dialog
updated_at: 2021-07-24T05:54:48Z
---

# Subreport Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567702-Style-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567602-Suppress-Column-Grand-Totals-Dialog)

# Subreport Dialog

This dialog appears when you select Insert > Subreport, or right-click a subreport and select Format Subreport from the shortcut menu. It helps you to insert a report into another report as its [subreport](https://devnet.logianalytics.com/hc/en-us/articles/1500009563582-Subreports), or to format an exsiting subreport.

The following are details about options in the dialog:

**Select Report**

Specifies the report that contains the report tab you want to use as the subreport. Select the Browse button to select the desired report.

**Report Tab**

Specifies the report tab as the subreport.

**Field tab**

Specifies some links between the primary report and subreport. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893851671/subrpt_fld.gif)

* **Component in Report Tab**  
  Lists the components in the subreport that will be interlinked with the primary report.
  + **Add**  
    Adds a component in the subreport to be interlinked with the primary report.
  + **Remove**  
    Removes the selected component from the Component in Report Tab box.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)  
  Adds a field of the primary report to set up links between the primary report and the subreport.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)  
  Removes the selected field.
* **Field**  
  Lists all the fields that are used in the link conditions.
  + **Fields(Primary)**  
    Lists the selected fields of the primary report.
  + **OP**  
    Specifies the operator to be the condition for setting up links between the primary report and the subreport.
  + **Fields(Subreport)**  
    Lists the DBFields in the datasets of the subreport which are of the same data type as the selected fields in the primary report.

**Parameters tab**

Available only when there is at least a parameter in the subreport. It helps you to specify values for all parameters in the subreport. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893851927/subrpt_prmtr.gif)

* **Parameters**  
  Lists all the parameters contained in the datasets of the subreport.
* **Value**  
  Lists all the DBFields and formulas in the dataset of the primary report which are of the same data type as the parameters of the subreport. Select the field the value of which you want to assign to parameter of the subreport from the drop-down list.

**Return Value tab**

Specifies values of the subreport fields to be returned as the primary report parameter values. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889319447/subrpt_value.gif)

* **Component in Report** **Tab**  
  Specifies the component in the subreport the fields of which will be used to return value to parameters of the primary report.
* **Fields in Subreport**  
  Lists the available fields used by the specified component in the subreport that can be used to return value to parameters of the primary report.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)  
  Adds a field that you want to assign to a parameter in the primary report.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)  
  Removes the selected field.
* **Return Value**  
  Lists the fields in the specified component of the subreport that will be used to return value to parameters of the primary report.
  + **Fields**  
    Lists all the selected fields from the specified component in the subreport.
  + **Parameters**  
    Lists all the parameters in the primary report which are of the same data type as the fields selected in the specified component of the subreport. Select the parameter to which the subreport field value will be returned from the drop-down list.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567702-Style-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567602-Suppress-Column-Grand-Totals-Dialog)
