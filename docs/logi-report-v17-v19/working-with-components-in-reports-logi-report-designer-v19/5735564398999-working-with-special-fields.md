---
title: "Working with Special Fields"
id: 5735564398999
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields
updated_at: 2022-11-02T04:13:18Z
---

# Working with Special Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars)

# Working with Special Fields

Special fields are defined by Logi Report. You can use them to easily obtain system information and report-related data. This topic introduces the special fields Logi Report provides, how you can insert them in a report, and add conditional formatting to the special fields.

For the special fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report) if you want.

This topic contains the following sections:

* [Special Fields Supported by Logi Report](#Field)
  + [Date-time Special Fields](#DateTime)
  + [Computed Special Fields](#Computed)
  + [System Special Fields](#System)
* [Inserting Special Fields in a Report](#Insert)
* [Adding Conditional Formatting to Special Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the special field example, open `<install_root>\Demo\Reports\SampleComponents\ForSpecialFields.cls`.

## Special Fields Supported by Logi Report

Logi Report classifies the special fields it supports into the following categories: [Date-time](#DateTime), [Computed](#Computed), and [System](#System).

### Date-time Special Fields

This category contains special fields of the DateTime type.

* **Print Date**  
  Displays today's date (or the current date from your computer).
* **Print Time**  
  Displays the current time from your computer.
* **Fetch Date**  
  Displays the date when Logi Report Engine retrieves the data from the database.
* **Fetch Time**  
  Displays the time when Logi Report Engine retrieves the data from the database.
* **Modified Date**  
  Displays the last modified date of the catalog.
* **Modified Time**  
  Displays the last modified time of the catalog.

### Computed Special Fields

This category contains special fields that Logi Report Engine computes based on the report.

* **Record Number**  
  Displays the record number (usually placed in the detail panel).
* **Group Name**  
  Displays the group name (usually placed in the group header/footer panel).
* **Total Records**  
  Displays the total number of records after Logi Report Engine performs all filter conditions, except the ones created in the Filter dialog box of Page Report Studio, and the Group Filter dialog box and Top N/Bottom N condition in Designer.
* **Total Fetched Records**  
  Displays the total number of records which take part in grouping calculation. The possible result of the special field is:
  + If you do not set any filter condition in the Filter dialog box of Page Report Studio, print the number of the record obtained after setting the Maximum Records property.
  + If you set filter conditions in the Filter dialog box of Page Report Studio, print the number of records obtained after performing the filter, even though you have set the Maximum Records property before specifying the filter.
* **Group Number**  
  Displays the group number (usually placed in the group header/footer).
* **Total Group Number**  
  Displays the total group number (usually placed in the group header/footer).
* **Page Number**  
  Displays the page number of the component which the special field is placed in.
* **Global Page Number**  
  Displays the global page number of the whole report wherever the special field is placed.
* **Total Page Number**  
  Displays the total number of pages of the component which the special field is placed in.
* **Global Total Page Number**  
  Displays the global total number of pages of the whole report wherever the special field is placed.
* **Page N of M**  
  Displays a specific page number out of the total page number of the component which the special field is placed in.

  You can specify the format of this special field. To do this, select this special field, then in the Report Inspector, find the **Format** property and choose an item from the value drop-down list. You can also customize the format by yourself. For example, if you want to display it as "This is page n of m pages", you can type the format string "This is page @PageNumber of @TotalPageNumber pages" in the Format value box.
* **Global Page N of M**  
  Displays a specific global page number out of the global total page number of the report. You can also specify the format of this special field in the Report Inspector.
* **SQL Statement**  
  Displays the SQL statements used to execute the query. This is often useful for resolving performance issues because you can see exactly what is passed to the database after Logi Report Engine applies all the parameter substitutions and filters.
* **Query Filter**   
  Displays in the report the condition of the [query filters](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#FilterQuery) applied to the parent data container of the special field.
* **Filter**  
  Displays in the report the filter expressions applied to the parent data container of the special field, which are created using the Filter dialog box and via the Filter option on a field’s shortcut menu.
* **On-screen Filter**  
  Displays in the report the on-screen filter expressions applied to the parent data container of the special field, which are created using filter controls and via the Filter panel in Web Report Studio.
* **Go To Filter**  
  Displays in the report the filter expressions applied to the parent data container of the special field, which are generated via the drill-down and drill-to-by-value actions.
* **TOC Page Number**  
  Displays in the report page number for the [table of contents](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) differently than the report pages. You can insert this special field in the header/footer of a TOC page panel only.
* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Export Page Number**  
  Displays in the report the number of each report page. You can insert this special field in the header/footer of a page panel only (including the TOC page panel).
* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Export Total Page Number**  
  Displays in the report the total number of the report pages. You can insert this special field in the header/footer of a page panel only (including the TOC page panel).

### System Special Fields

This category contains special fields that get values from the system.

* **User Name**  
  Displays the User ID. When viewing the report in Designer, it is the name specified for the User Name option in the General category of the Options dialog box; at runtime, it is the user name for signing in to Server.

  Besides using as a component in report directly, you can also use the User Name special field in the following cases:

  + [The PARAMETER string](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog#General) of general hierarchical data sources
  + [The PARAMETER string](https://devnet.logianalytics.com/hc/en-us/articles/5735499573911-Adding-User-Defined-Data-Sources-to-a-Catalog#Add) of user-defined data sources
  + [Parameters of stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/5735521490199-Using-Stored-Procedures#Parameter)
  + [Imported SQL statements](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs#Syntax)
  + [Aggregation pipeline expressions](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs#Expression) (APE) in MongoDB connections
  + [JSON connections](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog#Set)
  + [Elasticsearch connections](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections#Set)
  + [Formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog#RefSpecial)
  + Filter conditions of [query filter](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#Filter), [business view filter,](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Filter) and [dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report)
  + [Security conditions](https://devnet.logianalytics.com/hc/en-us/articles/5735527007767-Working-with-RLS-and-CLS-at-Data-Source-Scope#Condition) of Record Level Security (RLS) at data source scope

  You should use it as *username* in stored procedures and formulas, and as *@username* in HDS, UDS, Imported SQL, APE, JSON, filter conditions, and RLS security conditions.
* **Task ID**  
  Displays the internal task ID (a unique time stamp). This special field only works in the runtime environment. It returns a "NULL" value in Designer.
* **Report Path on Server**  
  Displays the full path of the report in the resource tree of Server. When the report is not running on Server, it returns the full disk path of the report. It returns a "NULL" value if the report is unsaved.
* **Report Path on Disk**  
  Displays the full disk path of the report. It returns a "NULL" value if the report is unsaved.
* **Catalog Path on Server**  
  Displays the full path of the report's catalog in the resource tree of Server. When the report is not running on Server, it returns the full disk path of the catalog. It returns a "NULL" value if the report is unsaved.
* **Catalog Path on Disk**   
  Displays the full disk path of the report's catalog. It returns a "NULL" value if the report is unsaved.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif) You can insert all special fields into web reports and library components in Designer. However, due to the characteristics of Web Report Studio and JDashboard, they can only render the following special fields at runtime: Modified Date, Modified Time, Print Date, Print Time, Fetch Date, Fetch Time, Record Number, Total Records, Group Number, Total Group Number, User Name, Report Path on Server, Report Path on Disk, Catalog Path on Server, Catalog Path on Disk, Query Filter, Filter, On-screen Filter, and Go To Filter.

## Inserting Special Fields in a Report

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the special field.
2. Navigate to **Insert** > **Special Fields** or **Home** > **Insert** > **Special Fields**, and then select the required field from the drop-down menu.

## Adding Conditional Formatting to Special Fields

You can add conditional formatting to the special fields Page Number and User Name in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to the special field Page Number/User Name, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars)
