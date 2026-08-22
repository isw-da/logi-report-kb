---
title: "Add Stored Procedures Dialog Box"
id: 1500010057982
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057982-Add-Stored-Procedures-Dialog-Box
updated_at: 2021-07-23T19:15:01Z
---

# Add Stored Procedures Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box)

# Add Stored Procedures Dialog Box

You can use the Add Stored Procedures dialog box to [add stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures#Add) from the database to a catalog. This topic describes the options in the dialog box.

Designer displays the Add Stored Procedure dialog box when you right-click a JDBC connection node and then select Add Stored Procedure from the shortcut menu in the Catalog Manager.

![Add Stored Procedures dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848639895/addprcdr.gif)

You see the following options in the dialog box:

**Database Catalog**

The drop-down list displays all the catalogs in the database. Select the catalog that contains the required stored procedures.

**Stored Procedures**

The box lists all the stored procedures in the selected catalog in a three-level tree. The top level is SQL-catalog, second is SQL-schema, and the third are stored procedures. You can select one or more stored procedures to add to the catalog.

![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif)**Sort icon**

Select to display the Sort drop-down menu to sort the stored procedures in the ascending or descending order.

Designer controls the default sort order according to the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Sort) option in the Catalog category of the Options dialog box. When you do not select Sort in the Options dialog box, Designer selects No Sort by default in the drop-down menu, which means the stored procedures are listed in their original order in the database. The change of sort order here is a one-off action, meaning Designer does not save it after you exit the dialog box.

![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif)**Search icon**

Select to open the search box to search for stored procedures.

To start searching, type the text you want to search for in the search box and Designer lists the stored procedures containing the matched text.

You can make use of the following options in the search box:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  + **Highlight All**   
    Select to highlight all matched text.
  + **Match Case**   
    Select to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select to search for text that looks the same as the typed text.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

**Add**

Select to add the specified stored procedures to the catalog.

**Done**

Select to apply all changes and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box)
