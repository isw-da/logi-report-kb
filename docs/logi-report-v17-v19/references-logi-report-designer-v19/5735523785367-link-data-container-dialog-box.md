---
title: "Link Data Container Dialog Box"
id: 5735523785367
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735523785367-Link-Data-Container-Dialog-Box
updated_at: 2022-11-02T04:39:41Z
---

# Link Data Container Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551885847-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735551905815-Mailing-Label-Wizard-Dialog-Box)

# Link Data Container Dialog Box

You can use the Link Data Container dialog box to [set up data relation between two data containers](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report) that are in a parent-child relationship and apply different datasets. This topic describes the options in the dialog box.

Designer displays the Link Data Container dialog box when you right-click a child data container that applies a different dataset than its parent's and select Data Container Link from the shortcut menu in a page or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")web report.

This dialog box contains the following tabs:

* [Condition Tab](#Condition)
* [Parameter Tab](#Parameter)
* [Return Value Tab](#ReturnValue)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Condition Tab

Use this tab to specify link conditions between two data containers.

![Link Data Container - Condition](https://devnet.logianalytics.com/hc/article_attachments/9898478876183/lnkdtcntnr_cndtn.gif)

**Resource box**

The box on the left lists the data fields in and related to the data resource from which the dataset the parent data container uses is created.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the resource box (parent field) to set up a link condition based on the field.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Field box.

**Field box**

This box lists the fields in both the parent and child data containers on which the link conditions are based.

* **Fields (Parent)**  
  This column shows the fields of the parent data container that you add to set the link conditions.
* **OP**  
  This column shows the operators that you select to set up the link conditions. You can select from the following operators:

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
  This column shows the fields that you select from the child data container to set up the link conditions. Once you add a parent field, Designer automatically displays the DBFields in the dataset of the child data container which are of the same data type in the drop-down list of the column. Select a child field to set up the link condition.

## Parameter Tab

Designer enables the Parameter tab when the child data container applies parameters. You can use it to assign values of the same-typed fields in the parent data container to the parameters.

![Link Data Container - Parameter](https://devnet.logianalytics.com/hc/article_attachments/9898478889367/lnkdtcntnr_prmtr.gif)

**Parameters**

This column lists all parameters the dataset of the child data container applies.

**Value**

This column shows the fields of the parent data container (parent fields) that you select to assign values to parameters of the child data container. For each parameter, Designer displays the DBFields, formulas, summaries, and parameters in the dataset of the parent data container that are of the same data type in the drop-down list of the column. Select a parent field to assign its values to the parameter.

## Return Value Tab

Designer enables the Return Value tab when the parent data container is in a page report and it applies parameters. You can use it to specify same-typed fields in the child data container to return their values to parameters of the parent data container.

![Link Data Container - Returen Value](https://devnet.logianalytics.com/hc/article_attachments/9898478895511/lnkdtcntnr_value.gif)

**Field in Child Data Container**

This box lists the available fields in the child data container that you can use to return values to parameters of the parent data container.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Field in Child Data Container box to use its value for a parameter of the parent data container.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Return Value box.

**Return Value**

This box lists the fields of the child data container that you add to return values to parameters of the parent data container.

* **Fields**  
  This column shows the fields that you add from the child data container.
* **Parameters**  
  This column shows the parameters in the parent data container that you select to get values from the specified fields in the child data container. Once you add a field from the child data container, Designer automatically displays the parameters in the parent data container that are of the same data type in the drop-down list of the column. Select a parameter to obtain values for it from the child field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551885847-Line-Pattern-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735551905815-Mailing-Label-Wizard-Dialog-Box)
