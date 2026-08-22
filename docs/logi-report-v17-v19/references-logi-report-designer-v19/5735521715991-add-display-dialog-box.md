---
title: "Add Display Dialog Box"
id: 5735521715991
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521715991-Add-Display-Dialog-Box
updated_at: 2022-11-02T04:14:11Z
---

# Add Display Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513001239-Add-Collection-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564900247-Add-Driver-Dialog-Box)

# Add Display Dialog Box

You can use the Add Display dialog box to add available display text keys in the current report and catalog for the target language to [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/5735568330007-Creating-NLS-Property-Files). This topic describes the options in the dialog box.

Designer displays the Add Display dialog box when you select Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) in the Display tab of the [NLS Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523913495-NLS-Editor-Dialog-Box#Display).

![Add Display dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476317463/adddsply.gif)

Designer displays these options:

**Available Display**

This box lists all the available display text keys in the current report and catalog.

**Search box**

Type the keyword in the box and Designer lists the keys containing the matched text.

**Scope**

This column shows the scope of the keys. You can select the column header to sort the items by scope in an ascending or descending order.

* **Catalog**  
  This option indicates that the key is from the catalog NLS resource.
* **Report**  
  This option indicates that the key is from the report NLS resource.

**Type**

This column shows the types of the display text keys. You can select the column header to sort the items by type in an ascending or descending order.

Designer classifies the display text in different objects into different types.

* **Column**  
  It indicates that the type of the display text key is Column, which only applies to reports running in Page Report Studio.
* **DisplayName**  
  It indicates that the type of the display text key is Display Name.
* **Label**  
  This type is for the display text in labels, some web controls, and UDOs.
* **Metadata**  
  This type is mainly for the display text in catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.
* **Prompt**  
  This type is for the display text in the prompt values of parameters.
* **Title**  
  This type is for the display text in filter controls and library components.
* **TOC**  
  This type is for the display text in the TOC tree.

**Key**

This column shows the display text keys in the original language. You can select the column header to sort the items by key in an ascending or descending order.

**Scope of Keys**

Specify the scope of the keys to list in the Available Display box.

* **Current Catalog**  
  Select to list keys from the current catalog.
* **Current Report**  
  Select to list keys from the current report.

**OK**

Select to add the specified keys to the Display tab of the NLS Editor dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513001239-Add-Collection-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564900247-Add-Driver-Dialog-Box)
