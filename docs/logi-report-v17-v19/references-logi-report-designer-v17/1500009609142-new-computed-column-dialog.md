---
title: "New Computed Column Dialog"
id: 1500009609142
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609142-New-Computed-Column-Dialog
updated_at: 2021-07-24T16:04:21Z
---

# New Computed Column Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632581-New-Catalog-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609182-New-CSS-Style-Dialog)

# New Computed Column Dialog

The New Computed Column dialog helps you to [create functions quickly and easily](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#ComputedColumn) instead of having to write formulas. It appears when you select Menu > Column > New Computed Column, or select New Computed Column on the toolbar in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).

![New Computed Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911636759/nwcmptclmn.gif)

The following are details about options in the dialog:

**Computed Column Name**

Specifies the name of the computed column.

**Functions**

The functions here are not from Logi Report system. They are from the connected database you are using. Thus, if you change your data source, some of these functions may no longer exist. For each database, the different supported functions list will be returned.

* **String**  
   Specifies String formulas to create a function.
* **Numeric**  
   Specifies Numeric formulas to create a function.
* **Time & Date**  
   Specifies Time or Date formulas to create a function.
* **+**  
   Adds the numbers or fields together in the Expression menu.
* **-**  
   Subtracts numbers or fields together in the Expression menu.
* **\***  
   Multiplies numbers or fields together in the Expression menu.
* **/**  
   Divides numbers or fields together in the Expression menu.
* **=**  
   Equates fields together.
* **"**  
   Places quotations on long character strings or names that have blanks in them. For example, you should place quotes on values such as "New York" or "Washington DC").
* **||**  
   Places fields together in the same Expression menu. For example, "New York" || "Washington DC").
* **()**  
   Places your fields in parentheses.

**Table/Column**

Lists all the tables and fields which are available for creating the computed column.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632581-New-Catalog-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609182-New-CSS-Style-Dialog)
