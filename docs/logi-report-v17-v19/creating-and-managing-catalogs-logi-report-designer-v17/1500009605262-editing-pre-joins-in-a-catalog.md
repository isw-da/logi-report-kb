---
title: "Editing Pre-joins in a Catalog"
id: 1500009605262
section: "Creating and Managing Catalogs - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605262-Editing-Pre-joins-in-a-Catalog
updated_at: 2021-07-24T16:05:26Z
---

# Editing Pre-joins in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605342-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog)

# Editing Pre-joins in a Catalog

After data resources such as tables, views, synonyms, queries, imported SQLs, imported APEs, stored procedures, and user defined data sources have been added to a catalog, you can use them to build reports. However, in your daily work, you may often be dealing with a set of data resources in your queries. You will have to define relationships and create joins among different data resources every time you create a new report.

Logi Report Designer provides you with the Pre-join feature which can be used for [creating/editing queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009636061-Using-Pre-joins-in-Queries). You can create distributed pre-joins between the data resources that are mashed up from different connections in a catalog. The pre-join information is one type of resource that is not stored in the catalog. It is saved in a standalone file with the extension .pre, and shares the same prefix as the catalog file. It is not used at report runtime. In Logi Report Designer, when you open a catalog, the pre-join file is opened at the same time. When you save the catalog, the pre-join file is also saved. Once you create a .pre in a folder, you can copy the .pre file to any other folders that use the same catalog.

This topic includes the following sections:

* [Creating Pre-joins](#Create)
  + [Outer Joins](#OuterJoin)
* [Defining Pre-join Paths](#Define)
* [Saving Pre-join Relationships Together with a Catalog](#Save)

## Creating Pre-joins

The Pre-join Editor is a convenient tool for you to predefine the relationships between data resources all at once in a catalog.

1. Open the catalog on which you want to define pre-join relationships.
2. In the Catalog Manager, select **Pre-join** on the toolbar.
3. In the Select Data Source dialog, select the catalog data source for which the joins will be created and select **OK**.

   The [Pre-join Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009632901-Pre-join-Editor-Dialog) appears.

   ![Pre-join Editor](https://devnet.logianalytics.com/hc/article_attachments/4404911688215/prjnedtr.gif)
4. Select **Add Tables** on the toolbar, then in the [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009607182-Add-Tables-Views-Queries-Dialog) dialog, select the data resources such as tables, views, synonyms, queries, imported SQLs, imported APEs, stored procedures, and user defined data sources in the specified catalog data source based on which to create the joins, and then select **OK**. The added data resources will be displayed as tables in the Pre-join Editor.

   When the selected catalog data source contains XML connections, tables from the XML connections will be automatically added in the Pre-join Editor, and when the [Generate the default pre-join path](https://devnet.logianalytics.com/hc/en-us/articles/1500009629721-Working-with-XML-Connections-in-a-Catalog#Prejoin) option is selected for the XML connections, if the parent and children nodes are transformed to different tables in an XML connection, joins will be embodied by the parent-child relationship by default, which is maintained by primary key and foreign key in the tables.
5. Select **Arrange** to organize the tables.
6. Create joins between the tables by using mouse drag and drop. You can make more than one join between two tables.
7. Point to one column in the source table, press and hold the mouse button, then move the pointer to the other column in the target table and release the mouse button. A green line with a join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404904196631/btn_join.gif) will be shown, linking the two columns. This represents that a join has been created.
8. If you want to further edit the join, double-click its join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404904196631/btn_join.gif). The [Join Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009608902-Join-Options-Dialog) dialog appears.

   ![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911635607/jnoptn.gif)
9. To make the join an [outer join](#OuterJoin), select the **Outer Join** option, then select either the **Left**, **Right** or **Full** radio button if you would like all rows of the left table, right table, or both tables to be retrieved.
   Regardless of where the tables are placed in the Pre-join Editor, left table is where the arrow starts and right table is where the arrow points.
10. Edit the join condition in the Condition panel according to your requirements.

    Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) beside the two text boxes to select a column in the two tables involved in the join, or a parameter or [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) in the current catalog data source and select the operator to compose the condition. You can also manually type the column, parameter, or formula name in the text boxes (parameters and formulas should be specified in the format *@FieldName* or *:FieldName*). When a parameter is referenced in a join condition, the Ignore Predicate If Parameter Value Is Null setting of the parameter will be ignored. Using parameters in the join conditions can dynamically change query results at runtime. It works similarly as in [query filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery).

    To add another condition line, select the **Add Condition** button and define the condition as required. Then from the logic drop-down list, specify the relationship between the two condition lines. You can repeat this to add more condition lines.

    To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of conditional expression. Conditions and groups together can be further grouped.

    To take any condition or group in a group out, select it and select **Ungroup**.

    To adjust the priority of the conditions, select it and select the **Up** or **Down** button.

    To delete a condition line, select it and select the **Delete** button.
11. Select the **OK** button to accept the changes and close the Join Options dialog.
12. Repeat steps 6 to 9 to create more joins.
13. If you want to delete any join, double-click its join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404904196631/btn_join.gif) and then select the **Delete Join** button in the Join Options dialog.
14. Select **Save** on the Pre-join Editor toolbar to the save the joins.

### Outer Joins

With conventional joins, records that do not satisfy the join condition are eliminated from the result. An outer join preserves these records in the result and replaces the missing values with nulls. SQL syntax uses the left outer join if the records in the left side table are preserved and right outer join if the records on the right side table are preserved. The left side is determined by where the arrow begins and the right side is determined by the side the arrow points to. It is independent of the location of the table in the Pre-join Editor or Query Editor. When you drag to make the join, you always drag logically from left to right even if your view in the query editor is right to left.

For example, consider the following two tables where the join arrow points from the Customer.C# to the Order.C#:

Table 1:

| Order | O# | C# |
| --- | --- | --- |
|  | 101 | 001 |
|  | 102 | 002 |
|  | 103 | 004 |

Table 2:

| Customer | C# | Name |
| --- | --- | --- |
|  | 001 | GE |
|  | 002 | IBM |
|  | 003 | DELL |

The inner join of `Customer.C# = Order.C#` will produce the following result:

| Join Result | O# | Customer.C# | Name |
| --- | --- | --- | --- |
|  | 101 | 001 | GE |
|  | 102 | 002 | IBM |

The left outer join on `Customer.C# = Order.C#` will produce the following result:

| Join Result | O# | Customer.C# | Name |
| --- | --- | --- | --- |
|  | 101 | 001 | GE |
|  | 102 | 002 | IBM |
|  | <null> | 003 | DELL |

The right outer join on `Customer.C# = Order.C#` will produce the following result:

| Join Result | O# | Order.C# | Name |
| --- | --- | --- | --- |
|  | 101 | 001 | GE |
|  | 102 | 002 | IBM |
|  | 103 | 004 | <null> |

The full outer join on `customer.C# = order.C#` will produce the following result:

| Join Result | O# | Order.C# | Customer.C# | Name |
| --- | --- | --- | --- | --- |
|  | 101 | 001 | 001 | GE |
|  | 102 | 002 | 002 | IBM |
|  | <null> | <null> | 003 | DELL |
|  | 103 | 004 | <null> | <null> |

## Defining Pre-join Paths

After you have created joins between the tables in the Pre-join Editor, you can then use them to define paths. To do this:

1. Select **Edit Paths**  on the Pre-join Editor toolbar. The [Edit Pre-join Paths](https://devnet.logianalytics.com/hc/en-us/articles/1500009630761-Edit-Pre-join-Paths-Dialog) dialog appears.

   ![Edit Pre-join Path dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916806295/edtprjnpth.gif)
2. Select the **New** button and type a name for the new path in the Enter Path Name dialog (by default the name will be Path1, Path2, and so on), and then select **OK**. The [Select Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500009633581-Select-Pre-join-Dialog) dialog appears.

   ![Select Pre-join dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904242071/slctprjn.gif)
3. You will see that all the joins you have created are displayed in the All Joins box. Choose the joins you want and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add them to the right box, then select **OK** to dismiss the dialog and return to the Edit Pre-join Paths dialog. The joins included in the path will be displayed in the Detail box.
4. Select the **New** button and follow the steps above to form a new path. You can select **Hide Joins Added in Other Paths** to hide the joins that have been used by the existing paths in the All Joins box.
5. For the paths you have defined, you can further edit, delete or rename them.

   To edit or delete a path, select it in the Pre-join Paths box, then select the **Edit** or **Delete** button.

   To rename a path, select it in the Pre-join Paths box, then in the **Rename** box, type the new name and then press **Enter** to confirm.
6. Upon finishing specifying the paths, select **OK** in the Edit Pre-join Paths dialog to confirm the settings.

You must define at least one path for the joins you create. If no path is defined, when you select Save on the Pre-join Editor toolbar:

* If there are no join loops among the joins, a default path named Path1 which includes all the joins you have created will be defined by Logi Report Designer. A message box will then be displayed to ask whether you accept the default path (select Yes), or you can modify the default path (select No).
* If there are join loops among the joins, the Edit Pre-join Paths dialog will appear for you to define at least one path.

## Saving Pre-join Relationships Together with a Catalog

You can save the relationships by selecting Save on the Pre-join Editor toolbar. Note that the pre-join information won't really be saved to disk until you save the catalog. After you have saved the catalog, you can then use the just created pre-join to develop reports.

**Notes:**

* You cannot make outer joins for XML data sources.
* When the tables in a query come from the same collection of a MongoDB database, the joins between them cannot be edited.
* Not all forms of joins are supported by all database systems. For example, MySQL does not support Full Outer Join so be sure to check your DBMS manuals.
* The joins in one path should never form a loop (any table in this path will have direct or indirect joins with all the other tables). If you specify a path which forms a loop, Logi Report Designer will prompt you to re-select the joins.
* You cannot define a path completely having all the same joins as with existing paths. If you have specified a path that is the same as an existing path, Logi Report Designer will prompt you to re-select the joins.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605342-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog)
