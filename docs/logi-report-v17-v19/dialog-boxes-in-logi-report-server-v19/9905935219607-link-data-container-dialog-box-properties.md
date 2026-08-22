---
title: "Link Data Container Dialog Box Properties"
id: 9905935219607
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9905935219607-Link-Data-Container-Dialog-Box-Properties
updated_at: 2022-10-31T17:15:19Z
---

# Link Data Container Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905935179159-Insert-Summary-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425879831-JDashboard-Dialog-Boxes)

# This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Link Data Container Dialog Box Properties

This topic describes how you can use the Link Data Container dialog box to [set up data relation between two data components](https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio#DataContainerLink) that are in a parent-child relationship and apply different datasets.

Server displays the Link Data Container dialog box when you right-click a child data component that uses a different dataset from its parent's and select **Data Container Link** from the shortcut menu.

This topic contains the following sections:

* [Condition Tab Properties](#Condition)
* [Parameter Tab Properties](#Parameter)
* [Return Value Tab Properties](#ReturnValue)

You see these elements on all the tabs:

**Target Component**

The child data component that you selected to open this dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**OK**

Select to apply any changes you made here and close the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905902377623/btn_lrstd_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905880426903/btn_lrstd_delete.gif)**Close button**

Select to close the dialog box without saving any changes.

## Condition Tab Properties

Specify link conditions between the two parent-child data components.

![Link Data Container - Condition](https://devnet.logianalytics.com/hc/article_attachments/9905931138071/lnkdtcntnr_cndtn.gif)

**Resources box**

The box on the left lists the data fields in and related to the data resource from which the dataset the parent data component uses is created.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905931174039/btn_lrstd_add.gif)**Add button**

Select to add the specified field in the resources box (parent field) to set up a link condition based on the field.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905931197719/btn_lrstd_remove.gif)**Remove button**

Select to remove the specified field from the Field box.

**Field box**

This box lists the fields in both the parent and child data components on which the link conditions are based.

* **Fields (Parent)**  
  This column shows the fields of the parent data component that you add to set up the link conditions.
* **OP**  
  This column shows the operators that you select to set up the link conditions. You can select from these operators:
  + **=**  
    Equal to
  + **<>**  
    Not equal to
  + **<**  
    Less than
  + **>**  
    Greater than
  + **<=**  
    Less than or equal to
  + **>=**  
    Greater than or equal to
  + **in**  
    The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).
* **Fields (Child)**  
  This column shows the fields that you select from the child data component to set up the link conditions. Once you add a parent field, Server automatically displays the DBFields in the dataset of the child data component which are of the same data type in the drop-down list of the column. Select a child field to set up the link condition.

## Parameter Tab Properties

Server enables the Parameter tab when the child data component applies parameters. You can use it to assign values of the same-typed fields in the parent data component to the parameters.

![Link Data Container - Parameter](https://devnet.logianalytics.com/hc/article_attachments/9905902848407/lnkdtcntnr_prmtr.gif)

**Parameters (Child)**

This column lists all parameters the dataset of the child data component applies.

**Value (Parent)**

This column shows the fields of the parent data component (parent fields) that you select to assign values to parameters of the child data component. For each parameter, Server displays the DBFields, formulas, summaries, and parameters in the dataset of the parent data component that are of the same data type in the drop-down list of the column. Select a parent field to assign its values to the parameter.

## Return Value Tab Properties

Server enables the Return Value tab when the parent data component is in a page report and it applies parameters. You can use it to specify same-typed fields in the child data component to return their values to parameters of the parent data component.

![Link Data Container - Returen Value](https://devnet.logianalytics.com/hc/article_attachments/9905902881047/lnkdtcntnr_value.gif)

**Left box**

This box lists the available fields in the child data component that you can use to return values to parameters of the parent data component.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905931174039/btn_lrstd_add.gif)**Add button**

Select to add the specified field in the left box to use its value for a parameter of the parent data component.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905931197719/btn_lrstd_remove.gif)**Remove button**

Select to remove the specified field from the right box.

**Right box**

This box lists the fields of the child data component that you add to return values to parameters of the parent data component.

* **Fields (Child)**  
  This column shows the fields that you add from the child data component.
* **Parameters (Parent)**  
  This column shows the parameters in the parent data component that you select to get values from the specified fields in the child data component. Once you add a field from the child data component, Server automatically displays the parameters in the parent data component that are of the same data type in the drop-down list of the column. Select a parameter to obtain its values from the child field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905935179159-Insert-Summary-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425879831-JDashboard-Dialog-Boxes)
