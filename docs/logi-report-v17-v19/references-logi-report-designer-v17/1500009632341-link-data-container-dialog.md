---
title: "Link Data Container Dialog"
id: 1500009632341
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632341-Link-Data-Container-Dialog
updated_at: 2021-07-24T16:04:24Z
---

# Link Data Container Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609002-Line-Pattern-List-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632361-Mailing-Label-Wizard-Dialog)

# Link Data Container Dialog

The Link Data Container dialog helps you to [set up link conditions between the child data component and its parent](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects). It appears when you right-click a child data component and select Data Container Link from the shortcut menu.

The following are details about options in the dialog:

**Condition tab**

Specifies the link conditions between the parent and child data components.

![Link Data Container - Condition](https://devnet.logianalytics.com/hc/article_attachments/4404904259095/lnkdtcntnr_cndtn.gif)

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)  
   Adds a field of the parent data component to set up links between the parent and child data components.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)  
   Removes the selected field.
* **Field**  
   Lists all the fields that are used in the link conditions.
  + **Fields (Parent)**  
     Lists the selected fields of the parent data component.
  + **OP**  
     Specifies the operator to setting up links between the parent and child data components. It can be =, <>, >, >=, <, <=, IN or NOT IN.
  + **Fields (Child)**  
     Lists the DBFields in the dataset of the child data component which are of the same data type as the selected fields in the parent data component.

**Parameter tab**

Specifies values for all parameters in the child data component.

![Link Data Container - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404904259479/lnkdtcntnr_prmtr.gif)

* **Parameters**  
   Lists all parameters contained in the dataset of the child data component.
* **Value**  
   Lists all the DBFields, formulas, summaries and parameters in the dataset of the parent data component which are of the same data type as the parameters of the child data component.

**Return Value tab**

Specifies values of the child data component fields which will be returned as the parent data component parameter values.

![Link Data Container - Returen Value](https://devnet.logianalytics.com/hc/article_attachments/4404904259735/lnkdtcntnr_value.gif)

* **Fields in Child Data Container**  
   Lists all the fields in the child data component.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)  
   Adds a field in the child data component whose value will be returned to a parameter of the parent data component.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)  
   Removes the selected field.
* **Return Value**  
   Lists all the fields in the child data component that will be used to return value to parameters of the parent data component.
  + **Fields**  
     Lists the selected fields in the child data component.
  + **Parameters**  
     Lists all the parameters in the parent data component which are of the same data type as the fields selected in the child data component.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609002-Line-Pattern-List-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632361-Mailing-Label-Wizard-Dialog)
