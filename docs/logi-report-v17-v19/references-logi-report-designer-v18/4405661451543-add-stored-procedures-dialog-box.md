---
title: "Add Stored Procedures Dialog Box"
id: 4405661451543
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661451543-Add-Stored-Procedures-Dialog-Box
updated_at: 2022-01-27T20:35:45Z
---

# Add Stored Procedures Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661452695-Add-Role-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664425495-Add-Tables-Dialog-Box)

# Add Stored Procedures Dialog Box

You can use the Add Stored Procedures dialog box to [add stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures#Add) from the database to a catalog. This topic describes the options in the dialog box.

Designer displays the Add Stored Procedure dialog box when you right-click a JDBC connection node and then select Add Stored Procedure from the shortcut menu in the Catalog Manager, or in the dialog box where a stored procedure list is available, expand the Stored Procedures node in a catalog data source that contains only one JDBC connection and select <Add Stored Procedure...>.

![Add Stored Procedures dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550955799/addprcdr.gif)

You see the following options in the dialog box:

**Database Catalog**

This drop-down list displays all the catalogs in the database. Select the catalog that contains the stored procedures you need.

**Stored Procedures**

This box lists the stored procedures in the selected database catalog in a three-level tree. The top level is SQL-catalog, second is SQL-schema, and the third are stored procedures. Select one or more stored procedures to add to the catalog.

![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068375/btn_sort2.gif)**Sort icon**

Select to display the Sort drop-down menu to specify how to sort the stored procedures.

* **Ascending**  
  Select to sort the stored procedures in the ascending order.
* **Descending**  
  Select to sort the stored procedures in the descending order.
* **No Sort**  
  Select to keep the original order of the stored procedures as in the database.

Designer determines the default sort order according to the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/4405661667735-Options-Dialog-Box#Sort) option in the Catalog category of the Options dialog box. If you do not select Sort in the Options dialog box, Designer selects No Sort by default in the drop-down menu. In addition, the change of sort order is a one-off action which Designer does not remember after you exit the dialog box, meaning, each time when you open the dialog box, Designer always applies the default sort order.

![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068631/btn_srch.gif)**Search icon**

Select to open the search box to search for stored procedures. To start searching, type the text you want to search for in the search box and Designer lists the stored procedures containing the matched text.

You can use the following options in the search box:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4420550825111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  + **Highlight All**  
    Select to highlight all the matched text.
  + **Match Case**  
    Select to search for text that meets the case of the text you type.
  + **Match Whole Word**  
    Select to search for text that looks the same as the text you type.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420550826007/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

**Add**

Select to add the specified stored procedures to the catalog.

**Done**

Select to apply all changes and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661452695-Add-Role-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664425495-Add-Tables-Dialog-Box)
