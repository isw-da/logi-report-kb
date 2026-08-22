---
title: "New View Element Dialog Box"
id: 5735530525975
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735530525975-New-View-Element-Dialog-Box
updated_at: 2022-11-02T07:53:14Z
---

# New View Element Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735543814807-New-User-Defined-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515004311-New-XML-Hierarchical-Data-Source-Dialog-Box)

# New View Element Dialog Box

You can use the New View Element dialog box to [add a new view element](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Element) into a business view. This topic describes the options in the dialog box.

Designer displays the New View Element dialog box when you perform one of the following:

* In the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box):
  + Navigate to Menu > New > Group/Aggregation/Detail.
  + Select New Group, New Aggregation, or New Detail.
  + Right-click the business view or a category and select New View Element from the shortcut menu.
* In the Catalog Manager, right-click a business view or a category and select New View Element on the shortcut menu.

This dialog box contains the following tabs:

* [General Tab](#General)
* [Security Tab](#Security)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify the general properties of the view element.

![New View Element - General](https://devnet.logianalytics.com/hc/article_attachments/9898458626711/nwvwelmnt_gen.gif)

**Display Name**

Specify the display name of the view element. An intuitive display name can help users easily understand the element.

**Mapping Name**

Specify the mapping field to which you want to map the view element. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the field.

**Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements) of the view element: Group, Aggregation, or Detail.

**By Expression**

Designer displays this option when you select Group as the type of the view element. Select it if you want to use an expression to retrieve values for the group object. After you select this option, Designer disables the Mapping Name text box.

* **Settings**  
   Select to open the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box) to compose the expression.

**Aggregate Function**

Designer displays the drop-down list only when the view element is an aggregation. It contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you can use for the aggregation object. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

**Customized**

Designer displays this option when you select Aggregation as the type of the view element. Select it if you want to create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements#CA) by writing a formula.

* **Settings**  
  Select to open the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box) to compose a formula using resources in the current business view, which can return an aggregation.

**Tip**

Specify the tool tip that displays when users hover over the view element in the business view resource tree at runtime.

**Description**

Specify the description of the view element.

## Security

Use this tab to specify user accessibility to elements of the business views in the current catalog data source.
For more information about options in the tab, see the [Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565601559-Edit-Business-View-Security-Dialog-Box).

![New View Element - Security](https://devnet.logianalytics.com/hc/article_attachments/9898461455767/nwvwelmnt_scrty.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735543814807-New-User-Defined-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515004311-New-XML-Hierarchical-Data-Source-Dialog-Box)
