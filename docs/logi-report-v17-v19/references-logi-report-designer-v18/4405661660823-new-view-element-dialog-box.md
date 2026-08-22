---
title: "New View Element Dialog Box"
id: 4405661660823
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661660823-New-View-Element-Dialog-Box
updated_at: 2022-01-27T20:38:13Z
---

# New View Element Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661659543-New-User-Defined-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661661975-New-XML-Hierarchical-Data-Source-Dialog-Box)

# New View Element Dialog Box

You can use the New View Element dialog box to [add a new view element](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Element) into a business view. This topic describes the options in the dialog box.

Designer displays the New View Element dialog box when you perform one of the following:

* In the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661463063-Business-View-Editor-Dialog-Box):
  + Navigate to Menu > New > Group/Aggregation/Detail.
  + Select New Group, New Aggregation, or New Detail.
  + Right-click the business view or a category and select New View Element from the shortcut menu.
* In the Catalog Manager, right-click a business view or a category and select New View Element on the shortcut menu.

The dialog box contains the following tabs:

* [General Tab](#General)
* [Security Tab](#Security)

You see these buttons in the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify the general properties of the view element.

![New View Element - General](https://devnet.logianalytics.com/hc/article_attachments/4420556110103/nwvwelmnt_gen.gif)

**Display Name**

Specify the display name of the view element. An intuitive display name can help users easily understand the element.

**Mapping Name**

Specify the mapping field to which you want to map the view element. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to select the field.

**Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements) of the view element: Group, Aggregation, or Detail.

**By Expression**

Designer displays this option when you select Group as the type of the view element. Select it if you want to use an expression to retrieve values for the group object. After you select this option, Designer disables the Mapping Name text box.

* **Settings**  
   Select to open the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664483735-Formula-Editor-Dialog-Box) to compose the expression.

**Aggregate Function**

Designer displays the drop-down list only when the view element is an aggregation. It contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) that you can use for the aggregation object. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box).

**Customized**

Designer displays this option when you select Aggregation as the type of the view element. Select it if you want to create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements#CA) by writing a formula.

* **Settings**  
  Select to open the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664483735-Formula-Editor-Dialog-Box) to compose a formula using resources in the current business view, which can return an aggregation.

**Tip**

Specify the tool tip of the view element, which displays when users hover over it in the business view resource tree at runtime.

**Description**

Specify the description of the view element.

## Security

Use this tab to specify user accessibility to elements of the business views in the current catalog data source.
For more information about options in the tab, see the [Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661506455-Edit-Business-View-Security-Dialog-Box).

![New View Element - Security](https://devnet.logianalytics.com/hc/article_attachments/4420550876439/nwvwelmnt_scrty.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661659543-New-User-Defined-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661661975-New-XML-Hierarchical-Data-Source-Dialog-Box)
