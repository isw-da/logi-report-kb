---
title: "Add Stored Procedures Dialog"
id: 1500009607142
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607142-Add-Stored-Procedures-Dialog
updated_at: 2021-07-24T16:05:02Z
---

# Add Stored Procedures Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629861-Add-Role-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607162-Add-Tables-Dialog)

# Add Stored Procedures Dialog

The Add Stored Procedures dialog displays all the stored procedures in the database, and allows you to [add the required stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures#Add) to a catalog. It appears when you right-click a JDBC connection node and then select Add Stored Procedure from the shortcut menu in the Catalog Manager.

![Add Stored Procedures dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904399511/addprcdr.gif)

The following are details about options in the dialog:

**Database Catalog**

Lists all the catalogs in the database.

**Stored Procedures**

Lists all the stored procedures in a three level tree. The top level is SQL-catalog, second is SQL-schema and the third are stored procedures. You can select one or more stored procedures to add to the catalog.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif)

Displays the Sort drop-down menu to sort the stored procedures in the ascending or descending order. The default sort order is controlled by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Sort) option in the Catalog category of the Options dialog. When Sort is not selected in the Options dialog, No Sort is selected by default in the drop-down menu which means the stored procedures are listed in their original order in the database. The change of sort order here is a one-off action and will not be remembered after you exit the dialog.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif)**Search**

Opens the search box to search for stored procedures. To start the search, type in the text you want to search for and the stored procedures containing the matched text will be listed.

In the search box, there are the following options:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404911683351/btn_srchbox_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404904186775/btn_close1.gif)  
   Closes the search box and cancels the search.

**Add**

Adds the selected stored procedures to the catalog.

**Done**

Applies all changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629861-Add-Role-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607162-Add-Tables-Dialog)
