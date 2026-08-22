---
title: "Edit View Element Dialog"
id: 1500009586641
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586641-Edit-View-Element-Dialog
updated_at: 2021-07-24T05:55:22Z
---

# Edit View Element Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565422-Edit-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586661-Encrypt-Dialog)

# Edit View Element Dialog

The Edit View Element dialog appears when you right-click any view element of a business view and select Edit from the shortcut menu in the Catalog Manager. It helps you to [edit the specified view element](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements), and consists of the following tabs:

* [General](#General)
* [Security](#Security)

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

## General

Sets properties for the view element. [See the tab](javascript:%20void(null)).

![Edit View Element dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893921175/edtvwelmnt_gen.gif)

**Display Name**

Specifies the display name of the view element which is intuitive to the end user.

**Mapping Name**

Specifies the mapping name of the field to which the view element is mapped. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to select the field.

**Type**

Specifies the type of the view element.

* **Group**  
   Group objects are the view elements that will become the basis for analyzing data in a report. They characteristically return text data or dates. For example they may return items like country, state and year to use for grouping data in reports.
* **Aggregation**  
   Aggregation objects are numeric view elements that are calculated at the time the report runs. The values they return are dependent on the group objects which they are used with. For example you may want a sales total by year.
* **Detail**  
   Detail objects provide additional information. They can be bound to group, aggregation, or category elements. Detail objects are not used for analysis but are useful in tables to show detail information such as addresses and phone numbers.

**Aggregate Function**

Available only when the view element is an aggregation. It specifies the function for the aggregation object. For details about each function, see [Math Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).

**Customized**

Available only when the type of the view element is defined as Aggregation. If checked, you can create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements#CA) by writing a formula.

* **Settings**  
   Opens the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog) to compose a formula using resources in the current business view, which can return an aggregation.

**Tip**

Specifies the tooltip of the view element which will be shown when you hover the mouse pointer over the element in the Resources panel of Web Report Studio or the Data panel of Page Report Studio.

**Description**

Specifies the description of the view element.

## Security

Specifies user accessibility to members of the group objects in all the business views in current data source. [See the tab](javascript:%20void(null)).

![Edit View Element dialog - Security](https://devnet.logianalytics.com/hc/article_attachments/4404893921559/edtvwelmnt_scrty.gif)

For details about options in the tab, refer to [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009565182-Edit-Business-View-Security-Dialog) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565422-Edit-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586661-Encrypt-Dialog)
