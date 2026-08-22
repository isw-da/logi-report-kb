---
title: "Link Data Container Dialog Box"
id: 4405661638423
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661638423-Link-Data-Container-Dialog-Box
updated_at: 2022-01-27T20:35:47Z
---

# Link Data Container Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664529047-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661639575-Mailing-Label-Wizard-Dialog-Box)

# Link Data Container Dialog Box

You can use the Link Data Container dialog box to [set up link conditions between the child data component and its parent](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects). This topic describes the options in the dialog box.

Designer displays the Link Data Container dialog box when you right-click a child data component and select Data Container Link from the shortcut menu.

The dialog box contains the following tabs:

* [Condition Tab](#Condition)
* [Parameter Tab](#Parameter)
* [Return Value Tab](#ReturnValue)

You see these buttons in the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Condition Tab

Use this tab to specify the link conditions between the parent and child data components.

![Link Data Container - Condition](https://devnet.logianalytics.com/hc/article_attachments/4420556147735/lnkdtcntnr_cndtn.gif)

**Resource box**

This box on the left lists the data fields in and related to the query resource that the parent data component uses. Add the fields to set up link conditions between the parent and child data components.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the resource box to set up the link conditions between the parent and child data components.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Field box.

**Field box**

This box lists the fields that you add to use in the link conditions between the parent and child data components.

* **Fields (Parent)**  
  This column shows the fields of the parent data component that you add to set the link conditions.
* **OP**  
  This column shows the operators that you select to set up the link conditions between the parent and child data component fields. You can select from the following operators:

+ **=**  
  Equal to
+ **>=**  
  Greater than or equal to
+ **>**  
  Greater than
+ **<**  
  Less than
+ **<=**  
  Less than or equal to
+ **!=**/**<>**  
  Not equal to
+ **in**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).

* **Fields (Child)**  
  This column shows the fields that you select from the child data component to set up the link conditions. Once you add a field from the parent data component, Designer automatically displays the DBFields in the dataset of the child data component which are of the same data type in the drop-down list of the column for you to select to set up the link condition.

## Parameter Tab

Designer enables the Parameter tab if the child data component contains parameters. You can use it to assign values of the same-typed fields in the parent data component to the parameters.

![Link Data Container - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4420556148119/lnkdtcntnr_prmtr.gif)

**Parameters**

This column lists all the parameters contained in the dataset of the child data component.

**Value**

This column shows the fields of the parent data component that you select to assign values to the parameters of the child data component. For each parameter, Designer displays the DBFields, formulas, summaries, and parameters in the dataset of the parent data component which are of the same data type in the drop-down list of the column for you to select to assign values to the parameter.

## Return Value Tab

Designer enables the Return Value tab when the parent data component applies parameters. You can use it to specify the same-typed fields in the child data component to return their values to the parameters of the parent data component.

![Link Data Container - Returen Value](https://devnet.logianalytics.com/hc/article_attachments/4420556148375/lnkdtcntnr_value.gif)

**Field in Child Data Container**

This box lists the available fields in the child data component that you can use to return values to the parameters of the parent data component.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Field in Child Data Container box to use its value for a parameter of the parent data component.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Return Value box.

**Return Value**

This box lists the fields of the child data component that you add to return values to parameters of the parent data component.

* **Fields**  
  This column shows the fields that you add from the child data component.
* **Parameters**  
  This column shows the parameters in the parent data component that you select to get values from the specified fields in the child data component. Once you add a field from the child data component, Designer automatically displays the parameters in the parent data component which are of the same data type in the drop-down list of the column for you to select to obtain values from the field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664529047-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661639575-Mailing-Label-Wizard-Dialog-Box)
