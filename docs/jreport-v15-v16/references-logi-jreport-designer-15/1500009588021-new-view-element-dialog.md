---
title: "New View Element Dialog"
id: 1500009588021
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009588021-New-View-Element-Dialog
updated_at: 2021-07-24T05:55:00Z
---

# New View Element Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566862-New-User-Defined-Data-Source-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566922-New-XML-Hierarchical-Data-Source-Dialog)

# New View Element Dialog

The New View Element dialog appears when you,

* Do any of the following in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009564622-Business-View-Editor-Dialog):
  + Select Menu > Insert > Group/Aggregation/Detail.
  + Select New Group, New Aggregation or New Detail on the toolbar.
  + Right-click the business view or a category and select New View Element from the shortcut menu.
* Right-click a business view or a category and select New View Element on the shortcut menu in the Catalog Manager resource tree.

It helps you to [add a new view element](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements) into a business view, and consists of the following tabs:

* [General](#General)
* [Security](#Security)

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

## General

Specifies properties of the view element. [See the dialog](javascript:%20void(null)).

![Add View Element dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889327383/nwvwelmnt_gen.gif)

**Display Name**

Specifies the display name of the view element which is intuitive to the end user.

**Mapping Name**

Specifies the mapping name of the field to which the view element is mapped. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to select the field.

**Type**

Specifies the type of the view element.

* **Group**  
   Group objects are the view elements that will become the basis for analyzing data in a report. They characteristically return text data or dates. For example they may return items like country, state and year to use for grouping data in reports. Group elements can also show detail data for a table. If you have any question if something should be a detail or a group make it a group. A group can be used everywhere a detail can be used.
* **Aggregation**  
   Aggregation objects are numeric view elements that are calculated at the time the report runs. The values they return are dependent on the group objects which they are used with. For example you may want a sales total by year. They are also used to count the number of records or the number of unique values. For example you may want a count of all orders and a count of all unique customers. Any value which is null will not be counted so be sure when using count to pick a field that will never be null.
* **Detail**  
   Detail objects provide additional information. They can be bound to DBFields and formulas. Detail objects are not used for analysis in charts and crosstabs but are useful in tables to show detail information such as addresses and phone numbers.

**Aggregate Function**

Available only when the type of the view element is defined as Aggregation. It specifies the function for the aggregation object. For details about each function, see [Math Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).

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

![Add View Element dialog - Security](https://devnet.logianalytics.com/hc/article_attachments/4404893863959/nwvwelmnt_scrty.gif)

For details about options in the tab, refer to [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009565182-Edit-Business-View-Security-Dialog) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566862-New-User-Defined-Data-Source-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566922-New-XML-Hierarchical-Data-Source-Dialog)
