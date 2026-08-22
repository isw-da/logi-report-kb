---
title: "Link Data Container Dialog Box"
id: 1500010059702
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059702-Link-Data-Container-Dialog-Box
updated_at: 2021-07-23T19:15:42Z
---

# Link Data Container Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097841-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097861-Mailing-Label-Wizard-Dialog-Box)

# Link Data Container Dialog Box

You can use the Link Data Container dialog box to [set up link conditions between the child data component and its parent](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects). This topic describes the options in the dialog box.

Designer displays the Link Data Container dialog box when you right-click a child data component and select Data Container Link from the shortcut menu.

The dialog box contains the following tabs:

* [Condition Tab](#Condition)
* [Parameter Tab](#Parameter)
* [Return Value Tab](#ReturnValue)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Condition Tab

Use this tab to specify the link conditions between the parent and child data components.

![Link Data Container - Condition](https://devnet.logianalytics.com/hc/article_attachments/4404856914199/lnkdtcntnr_cndtn.gif)

**Resources box**

The box on the left lists the data fields in and related to the query resource that the parent data component uses. Add the fields to set up link conditions between the parent and child data components.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field of the parent data component to set up the link conditions between the parent and child data components.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Fields box.

**Field box**

The box lists the fields that you add to use in the link conditions between the parent and child data components.

* **Fields (Parent)**  
  The column shows the fields of the parent data component that you add to set the link conditions.
* **OP**  
  The column shows the operators that you select to set up the link conditions between the parent and child data component fields. You can select from the following operators:

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
+ **IN**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "IN" operator, you can use multiple values separated by comma (,).

* **Fields (Child)**  
  The column shows the fields that you select from the child data component to set up the link conditions. You can select from the DBFields in the dataset of the child data component which are of the same data type as the specified fields in the parent data component.

## Parameter Tab

Designer enables the Parameter tab if the child data component contains parameters. You can use it to assign values of the same-typed fields in the parent data component to the parameters.

![Link Data Container - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404856914455/lnkdtcntnr_prmtr.gif)

**Parameters**

The column lists all the parameters contained in the dataset of the child data component.

**Value**

The column shows the fields of the parent data component that you select to assign their values to the parameters of the child data component. You can select from the DBFields, formulas, summaries, and parameters in the dataset of the parent data component which are of the same data type as the parameters of the child data component.

## Return Value Tab

Designer enables the Return Value tab when the parent data component applies parameters. You can use it to specify the same-typed fields in the child data component to return their values to the parameters of the parent data component.

![Link Data Container - Returen Value](https://devnet.logianalytics.com/hc/article_attachments/4404848513943/lnkdtcntnr_value.gif)

**Field in Child Data Container**

The box lists all the fields included in the child data component.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the child data component to use its value for a parameter of the parent data component. You can only add fields that are of the same data type as the parameters of the parent data component.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Return Value box.

**Return Value**

The box lists the fields in the child data component that you add to return values to parameters of the parent data component.

* **Fields**  
  The column shows the fields that you add from the child data component.
* **Parameters**  
  The column shows the parameters in the parent data component which you select to use values of the specified fields in the child data component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097841-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097861-Mailing-Label-Wizard-Dialog-Box)
