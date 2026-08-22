---
title: "Working with Special Fields"
id: 4405664402327
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields
updated_at: 2022-01-27T20:34:33Z
---

# Working with Special Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars)

# Working with Special Fields

Special fields are defined by Logi Report. You can use them to easily obtain system information and report-related data. This topic introduces the special fields Logi Report provides, how you can insert them in a report, and add conditional formatting to the special fields.

For the special fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Special Fields Supported by Logi Report](#Field)
* [Inserting Special Fields in a Report](#Insert)
* [Adding Conditional Formatting to Special Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the special field example, open `<install_root>\Demo\Reports\SampleComponents\ForSpecialFields.cls`.

## Special Fields Supported by Logi Report

Logi Report classifies the special fields it supports into the following categories: Date-time, Computed, and System.

**Date-time**

Special fields of the DateTime type.

* **Print Date**  
  Prints today's date (or the current date from your computer).
* **Print Time**  
  Prints the current time from your computer.
* **Fetch Date**  
  Prints the date when Logi Report retrieves the data from the database.
* **Fetch Time**  
  Prints the time when Logi Report retrieves the data from the database.
* **Modified Date**  
  Prints the last modified date of the catalog.
* **Modified Time**  
  Prints the last modified time of the catalog.

**Computed**

Special fields that Logi Report computes based on the report.

* **Record Number**  
  Prints the record number (usually placed in the detail panel).
* **Group Name**  
  Prints the group name (usually placed in the group header/footer panel).
* **Total Records**  
  Prints the total number of records after Logi Report performs all the filter conditions, except the ones created in the Filter dialog box of Page Report Studio, and the Group Filter dialog box and Top N/Bottom N condition in Designer.
* **Total Fetched Records**  
  Prints the total number of records which take part in grouping calculation. The possible result of the special field is:
  + If you don't set any filter condition in the Filter dialog box of Page Report Studio, print the number of the record obtained after setting the property Maximum Records.
  + If you set filter conditions in the Filter dialog box of Page Report Studio, print the number of records obtained after performing the filters, even though you have set the property Maximum Records before setting the filters.
* **Group Number**  
  Prints the group number (usually placed in the group header/footer).
* **Total Group Number**  
  Prints the total group number (usually placed in the group header/footer).
* **Page Number**  
  Prints the page number of the component which it is placed in.
* **Global Page Number**  
  Prints the global page number of the whole report wherever it is placed.
* **Total Page Number**  
  Prints the total number of pages of the component which it is placed in.
* **Global Total Page Number**  
  Prints the global total number of pages of the whole report wherever the field is placed.
* **Page N of M**  
  Prints a specific page number out of the total page number of the component which the field is placed in.

  You can specify the format of this special field. To do this, select this special field, then in the Report Inspector, find the **Format** property and choose an item from the value drop-down list. You can also customize the format by yourself. For example, if you want to display it as "This is page n of m pages", you can type the format string "This is page @PageNumber of @TotalPageNumber pages" in the Format value box.
* **Global Page N of M**  
  Prints a specific global page number out of the global total page number of the report. You can specify the format of this special field in the Report Inspector. The operation is the same as Page N of M.
* **SQL Statement**  
  Prints the SQL statements used to execute the query. This is often useful for resolving performance issues as you can see exactly what is passed to the database after Logi Report applies all the parameter substitutions and filters.
* **Query Filter**   
  Prints in the report the condition of the [query filters](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#FilterQuery) applied to the parent data container of the special field.
* **Filter**  
  Prints in the report the filter conditions applied to the parent data container of the special field, which are created using the Filter dialog box and via the Filter option on a field’s shortcut menu.
* **On-screen Filter**  
  Prints in the report the on-screen filter conditions applied to the parent data container of the special field, which are created using filter controls and via the Filter panel in Web Report Studio.
* **Go To Filter**  
  Prints in the report the filter conditions applied to the parent data container of the special field, which are generated via the drill-down and drill-to-by-value actions.
* ![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420542050071/___newv18.3.jpg "New for version 18.3.")**TOC Page Number**  
  Prints in the report page numbers for the [Table of Contents](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) differently than your report pages. You can insert this special field in the page header/footer of a TOC page only.

**System**

Special fields which get values from the system.

* **User Name**  
  Prints the User ID. When viewing the report in Designer, it is the name specified for the User Name option in the General category of the Options dialog box; at runtime, it is the user name for signing in to Server.

  Besides using as a component in report directly, you can also use the "User Name" special field in the following cases:

  + [The PARAMETER string](https://devnet.logianalytics.com/hc/en-us/articles/4405661419159-Adding-Hierarchical-Data-Sources-to-a-Catalog#General) of general hierarchical data sources
  + [The PARAMETER string](https://devnet.logianalytics.com/hc/en-us/articles/4405661436055-Adding-User-Defined-Data-Sources-to-a-Catalog#Add) of user-defined data sources
  + [Parameters of stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures#Parameter)
  + [Imported SQL statements](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs#Syntax)
  + [Aggregation pipeline expressions](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs#Expression) (APE) in MongoDB connections
  + [JSON connections](https://devnet.logianalytics.com/hc/en-us/articles/4405661432343-Working-with-JSON-Connections-in-a-Catalog#Set)
  + [Elasticsearch connections](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections#Set)
  + [Formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog#RefSpecial)
  + Filter conditions of [query filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#Filter), [business view filter,](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) and [dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Filter)
  + [Security conditions](https://devnet.logianalytics.com/hc/en-us/articles/4405661342359-Working-with-RLS-and-CLS-at-Data-Source-Scope#Condition) of Record Level Security (RLS) at data source scope

  You should use it as *username* in stored procedures and formulas, and as *@username* in HDS, UDS, Imported SQL, APE, JSON, filter conditions, and RLS security conditions.
* **Task ID**  
  Prints the internal task ID (a unique time stamp). This special field only works in the Server environment. It returns a "NULL" value when running in Designer.
* **Report Path on Server**  
  Prints the full path of the report in the resource tree of Server. If the report is not running on Server, it returns the full disk path of the report. It returns a "NULL" value if the report is unsaved.
* **Report Path on Disk**  
  Prints the full disk path of the report. It returns a "NULL" value if the report is unsaved.
* **Catalog Path on Server**  
  Prints the full path of the report's catalog in the resource tree of Server. If the report is not running on Server, it returns the full disk path of the catalog. It returns a "NULL" value if the report is unsaved.
* **Catalog Path on Disk**   
  Prints the full disk path of the report's catalog. It returns a "NULL" value if the report is unsaved.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) You can insert all special fields into web reports and library components in Designer. However, due to the characteristics of Web Report Studio and JDashboard, they can only render these at runtime: Modified Date, Modified Time, Print Date, Print Time, Fetch Date, Fetch Time, Record Number, Total Records, Group Number, Total Group Number, User Name, Report Path on Server, Report Path on Disk, Catalog Path on Server, Catalog Path on Disk, Query Filter, Filter, On-screen Filter, and Go To Filter.

## Inserting Special Fields in a Report

You can insert special fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship).

**To insert a special field into a report**

1. Position the mouse pointer at the destination where you want to insert the special field.
2. Navigate to **Insert** > **Special Fields** or **Home** > **Insert** > **Special Fields**, and then select the required field from the drop-down menu.

## Adding Conditional Formatting to Special Fields

You can add conditional formatting to the special fields Page Number and User Name in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to the special field Page Number/User Name, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars)
