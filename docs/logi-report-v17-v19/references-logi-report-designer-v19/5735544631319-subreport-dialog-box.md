---
title: "Subreport Dialog Box"
id: 5735544631319
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735544631319-Subreport-Dialog-Box
updated_at: 2022-11-02T07:52:13Z
---

# Subreport Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515733399-Style-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515626135-Suppress-Column-Grand-Totals-Dialog-Box)

# Subreport Dialog Box

You can use the Subreport dialog box to insert a report into another report as its [subreport](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports), or to edit an existing subreport. This topic describes the options in the dialog box.

Designer displays the Subreport dialog box when you navigate to Insert > Subreport, or right-click a subreport and select Format Subreport from the shortcut menu.

This dialog box contains the following tabs:

* [Field Tab](#Field)
* [Parameters Tab](#Parameters)
* [Return Value Tab](#ReturnValue)

Designer displays these options in all the tabs:

**Select Report**

Specify the page report that contains the report tab you want to use as the subreport. Select **Browse** to select the report.

**Report Tab**

Select the report tab in the specified page report as the subreport.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Field Tab

Use this tab to specify the link relationship between the primary report and the subreport.

![Subreport - Field](https://devnet.logianalytics.com/hc/article_attachments/9898460670743/subrpt_fld.gif)

**Component in Report Tab**

This box lists the components in the subreport that you select to interlink with the primary report.

* **Add**  
  Select to add components in the subreport to interlink with the primary report.
* **Remove**  
  Select to remove the specified components from the Component in Report Tab box.

**Primary report field box**

The box on the left lists the fields in and related to the query resource the primary report uses, which you can add to set link conditions between the primary report and the specified components in the subreport.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add a field of the primary report to set up links between the primary report and the specified components in the subreport.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified link condition from the Field box.

**Field**

This box lists the link conditions that you specify between the primary report and the specified components in the subreport.

* **Fields (Primary)**  
  This column shows the fields that you add from the primary report to set up the link conditions.
* **OP**  
  This column shows the operators that you select for setting up the link conditions.
* **Fields (Subreport)**  
  This column shows the fields that you select from the subreport to set up the link conditions. Once you add a field from the primary report, Designer automatically displays the DBFields in the datasets of the subreport which are of the same data type in the drop-down list of the column. Select a field to link with the primary field.

## Parameters Tab

Designer enables the tab when there is at least one parameter in the subreport. You can use it to assign values of the same-typed fields in the primary report to the parameters.

![Subreport - Parameters](https://devnet.logianalytics.com/hc/article_attachments/9898477784215/subrpt_prmtr.gif)

**Parameters**

This column shows all parameters in the datasets of the subreport.

**Value**

This column shows the fields in the primary report that you select to assign values to the subreport parameters. For each subreport parameter, Designer automatically lists the DBFields and formulas in the dataset of the primary report which are of the same data type in the drop-down list of the column. Select a field to assign its values to the subreport parameter.

## Return Value Tab

Use this tab to specify same-typed fields in the subreport to return their values to parameters of the primary report.

![Subreport - Return Value](https://devnet.logianalytics.com/hc/article_attachments/9898460686871/subrpt_value.gif)

**Component in Report Tab**

Select the component in the subreport the fields of which you want to use to return values to the primary report parameters.

**Fields in Subreport**

This box lists the available fields used by the specified component in the subreport that you can use to return values to the primary report parameters.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Fields in Subreport box to use its values for a parameter in the primary report.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the Return Value box.

**Return Value**

This box lists the fields that you add from the specified component of the subreport to return values to the primary report parameters.

* **Fields**  
  This column shows the fields that you add from the specified component in the subreport.
* **Parameters**  
  This column shows the primary report parameters that you select to get values from the specified subreport fields. Once you add a field from the subreport, Designer automatically displays the parameters in the primary report which are of the same data type in the drop-down list of the column. Select a parameter to obtain values for it from the subreport field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515733399-Style-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515626135-Suppress-Column-Grand-Totals-Dialog-Box)
