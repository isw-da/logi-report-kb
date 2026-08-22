---
title: "Creating Business Views in a Catalog"
id: 4405664681111
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog
updated_at: 2022-08-02T04:00:05Z
---

# Creating Business Views in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters)

# Creating Business Views in a Catalog

Designer includes the interactive Business View Editor to help you create any business views you need. This topic introduce how you can create and edit business views in a catalog using the functions the editor provides.

This topic contains the following sections:

* [Creating a Business View](#Create)
* [Adding and Modifying Elements in a Business View](#AddElement)
  + [Adding Elements by Dragging](#Drag)
  + [Creating and Editing View Elements with Dialog](#Element)
  + [Adjusting the Order of the Elements](#Order)
  + [Renaming an Element](#Rename)
  + [Deleting an Element](#Delete)

* [Defining Hierarchies in a Business View](#Hierarchy)
* [Creating Predefined Filters for a Business View](#Filter)
* [Customizing Filter Resources for a Business View](#FilterResource)

## Creating a Business View

To create a business view in a catalog, take the following steps:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open), then do either of the following:
   * In the Catalog Manager, expand the data source to create the business view, then select the **Business Views**  node or any existing business view in the data source and select **New Business View**  on the Catalog Manager toolbar, or right-click the **Business Views**  node in the data source and select **New Business View**  from the shortcut menu.
   * Navigate to **Home** > **New** > **Business View**  or **File** > **New** > **Business View**, specify the data source to create the business view, then select **OK**.
2. In the Enter Business View Name dialog box, provide a name for the business view and select **OK**. Designer displays the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661454359-Add-Tables-Views-Queries-Dialog-Box).

   ![Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556109207/addtbvwqy.gif)
3. In the **All Tables/Views/Queries** box, expand the resource nodes to add the corresponding resources based on which to create the business view to the **Selected Tables/Views/Queries** box, then select **OK**.

   If the catalog data source is connected with multiple connections, you can mash up multiple data resources for the business view that come from all these connections, including [tables, views, synonyms](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms), [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs), [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures), [queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries), and [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/4405661435031-Using-User-Defined-Data-Sources). When you add a query, imported SQL, imported APE, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns. When two resources (for example, a table and a view) use the same name, you cannot add them at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

   If the current catalog data source contains JDBC connections, the **Show Tables/Views Already Added** option is available. Select it if you want to show the tables, views, and synonyms in the resource tree in the All Tables/Views/Queries box, which you have already added to the Selected Tables/Views/Queries box. You can then add the tables, views, and synonyms of the JDBC connections for the business view as many times as you want by providing different names for the tables, views, and synonyms each time you add them.
4. If you add more than one data resource for the business view, Designer displays the Query Editor dialog box, in which you can edit the data resources you select for the business view in the same way you would do for a query. You can:
   * Select the columns in each table that you want to use for the business view. To select all columns in a table, select **\*** at the top of the table. However, for tables from MongoDB connections, you cannot select all columns by selecting **\***, because you cannot use the PrimaryKey and ForeignKey columns in such table for a business view.
   * [Add or delete the data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#AddTable) used for creating the business view.
   * [Set up joins between the data resources](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#Join).
   * [Create formula fields](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#FormulaField) to use in the business view.
   * [Add filters](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#FilterQuery) to narrow data used in the business view.

   After making the necessary changes, select **OK** at the bottom of the Query Editor dialog box to apply them. You can also navigate to **Menu** > **Query** > **Save As** to save the data resources as a query.
5. Designer displays the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661463063-Business-View-Editor-Dialog-Box). All the resources that you have selected for the business view, and the formulas and summaries in the current catalog data source that are valid for the selected resources are available in the Resource Objects panel on the left of the editor.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4420550840727/bvedtr.gif)
6. [Add elements](#AddElement) to the business view based on the available resources.
7. [Define hierarchies](#Hierarchy) on the business view to allow users to drill report data to particular groups at runtime.
8. [Create predefined filters](#Filter) on the business view for users to choose when using the business view to create reports.
9. [Configure security for the business view](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security) to limit user access to the view elements.
10. Select **Save** on the toolbar to save the business view.
11. Navigate to **Menu** > **File** > **Close** to close the Business View Editor dialog box and add the business view to the catalog.

## Adding Elements to a Business View

Designer lists the data resources that you have selected for a business view with their DBFields, and the formulas and summaries in the current catalog data source that are valid to the data resources, in the Resource Objects panel in the Business View Editor. You can use the resources to create view elements in the business view.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) In the Catalog Manager, you can also create, edit, rename, or delete an element in a business view by using the corresponding command on the element's shortcut menu.

### Adding Elements by Dragging

In the Business View Editor, a data resource displays as a folder containing their DBFields. You can drag DBFields, a whole data resource folder with all its DBFields, formulas, and summaries from the Resource Objects panel to the business view or a category in the Business View panel. You can select multiple resources and drag them all at a time. Designer then converts the resources into corresponding view elements in the business view based on the following rules:

* DBFields and formulas are added as group objects.
* A whole data resource folder with all its DBFields is added as a category with group objects.
* Summaries are added as aggregations based on the same sum-on fields and summary functions.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You can convert the group objects to detail objects using the [Edit View Element dialog box](#EditElement) if you prefer to use them as detail objects.

When you drag a DBField of the Timestamp/DateTime data type, Designer displays the [Select Time Interval dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661715607-Select-Time-Interval-Dialog-Box) for you to specify how you want to create the group object. By default, Designer selects **Keep Original** in the dialog box which means to create a group object based on the DBField itself. If you also want to create a group object which uses an expression to retrieve the years/quarters/months/weeks/days of the DBField as its values, select the corresponding checkbox. In the meantime, you can use the **Auto Create Hierarchy** option to specify whether to create a [hierarchy](#Hierarchy) in the business view automatically and edit the name of the hierarchy. The hierarchy contains all the group objects you have specified to create from the DBField, with the group objects listed based on the order of the corresponding checkboxes in the dialog box. You can further edit the hierarchy.

![Select Time Interval dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556109591/slcttmintvl.gif)

If you drag multiple DBFields of the Timestamp/DateTime data type, Designer displays the Select Time Interval dialog box multiple times for you to specify the settings for each DBField.

### Creating and Editing Categories with Dialog

**To create a category in a business view using dialog box**

1. In the Business View Editor dialog box, select the business view or an existing category in the Business View panel, then do any of the following:
   * Right-click and select **New Category** from the shortcut menu.
   * Select **New Category** on the toolbar.
   * Navigate to **Menu** > **New** > **Category**.

   Designer displays the [Category Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664450071-Category-Property-Dialog-Box).

   ![Category Property dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550841239/ctgryprpty_gnrl.gif)
2. In the **General** tab, set the display name of the category in the **Display Name** text box.
3. In the **Description** text box, type a description for the category to help others get an idea about it. The description displays when users point to the category in the resources panel of Web Report Studio and Page Report Studio.
4. You can select the **Security** tab to [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security).
5. Select **OK**. Designer adds a new category to the business view or the selected category. You can then add elements to it.

**To edit a category**

1. In the Business View Editor dialog box, select the category from the business view resource tree in the Business View panel, right-click it and select **Edit Category** from the shortcut menu.
2. In the Category Property dialog box, edit its general information in the General tab and [security information](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security) in the Security tab.
3. Select **OK** to confirm the changes.

### Creating and Editing View Elements with Dialog

**To create a view element in a business view using dialog box**

1. In the Business View Editor dialog box, select the business view or any existing category into which you want to add the view element in the Business View panel, then do any of the following:
   * Right-click and select **New View Element**  from the shortcut menu.
   * Select **New Group**, **New Aggregation**, or **New Detail** on the toolbar.
   * Navigate to **Menu** >  **New** > **Group**/**Aggregation**/**Detail**.

   Designer displays the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661660823-New-View-Element-Dialog-Box).

   ![Add View Element dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556110103/nwvwelmnt_gen.gif)
2. In the **General** tab, decide the type of the view element by selecting the corresponding item from the **Type** drop-down list.
3. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to specify the mapping field of the view element.

   When creating a group object, if you want to write an expression to retrieve values for it, select **By Expression**, then select **Settings**. In the Formula Editor dialog box, [compose the expression](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog) using resources in the current catalog data source. The expression should follow the [record level pass one formula](https://devnet.logianalytics.com/hc/en-us/articles/4405664602263-Formula-Levels#PassOne) syntax.
4. In the **Display Name** text box, specify the display name of the view element. By default, the display name is the same as the mapping name.
5. If you choose to create an aggregation, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) to calculate the mapping field from the **Aggregate Function** drop-down list. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box) dialog box. Select **Customized** if you want to create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements#CA), then select **Settings** to open the Formula Editor dialog box to [compose the expression](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog) using resources in the current business view.
6. Specify the tool tip and description of the view element in the **Tip** and **Description** text boxes respectively to help others get an idea about it. The tool tip displays when users point to the view element in the business view resource tree at runtime.
7. You can select the **Security** tab to [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security).
8. Select **OK** to create the view element and close the dialog box.

**To edit a view element**

1. In the Business View Editor dialog box, select the view element from the business view resource tree in the Business View panel, right-click it and select **Edit** from the shortcut menu.
2. In the [Edit View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661533079-Edit-View-Element-Dialog-Box), edit its general information in the General tab and [security information](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security) in the Security tab.

   You can convert a group object to a detail object and vice versa, by selecting **Detail** or **Group** from the **Type** drop-down list in the General tab.
3. Select **OK** to confirm the changes.

You can also select multiple view elements of the Group and Detail types and edit them at a time using the Edit View Element dialog box to apply the same Tip and Description settings to them, and change their element type to Detail or Group.

### Adjusting the Order of the Elements

In the Business View Editor dialog box, you can change the position of the view elements in any category or the categories in the business view in the resource tree of the Business View panel. The position here determines the display order of the elements and categories in any UI that shows the business view, except that in the Catalog Manager resource tree which applies its own [sort](https://devnet.logianalytics.com/hc/en-us/articles/4405664358679-Managing-the-Data-Resources-in-a-Catalog#Sort) rule. You can place the elements and categories alphabetically or based on their using frequency to help others easily locate the desired one.

You can use the following methods to change the position:

* Select one or more categories or elements in a category and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif).
* Right-click one or more categories or elements in a category and select **Move Up** or **Move Down** on the shortcut menu.
* Select the **Sort** icon ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420542068375/btn_sort2.gif) at the upper right corner of the Business View panel and select **Ascending** or **Descending** from the drop-down menu to display the resources excluding the elements in [hierarchies](#Hierarchy) in either ascending or descending order.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) The No Sort item in the Sort drop-down menu is always grayed out. It is selected by default each time you open the Business View Editor. However, this does not cancel the ascending or descending order if you have applied one to the elements the last time you were working in the editor, in other words, once you have selected the ascending or descending order and saved the business view, when you open the editor the next time, Designer displays the elements in the specified order although No Sort is selected on the drop-down menu. You may also find that No Sort is selected automatically when the elements apply neither the ascending nor descending order, for example, you adjust the element order by moving them up or down.

You can also drag a view element or a category and drop it to another category node to change its position. When you perform this operation, Designer always places the view element or category at the end of the target category. However, when you drag a group object or category to another category, Designer automatically removes the group object or group objects in the selected category from [hierarchies](#Hierarchy) that contain these group objects; therefore, you need to add the group object from the target category to the hierarchies again if you still need them in the hierarchies.

### Renaming an Element

To rename a view element or a category, that is, to change its display name, take the following steps:

1. In the Business View panel of the Business View Editor dialog box, right-click the element or category and select **Rename** from the shortcut menu, or select on the name twice. The name text box then becomes editable.
2. Type a new name and select outside of the text box to accept the change.

### Deleting an Element

To delete an unwanted element or category, select it in the **Business View** panel of the Business View Editor dialog box, then:

* Select **Delete** on the toolbar.
* Right-click and select **Delete** from the shortcut menu.
* Drag it to the **Resource Objects** panel on the left.

You can select multiple elements and delete them at one time.

## Defining Hierarchies in a Business View

You can regard a hierarchy as a category that contains group objects sharing a hierarchical relationship in the order from the highest level to the lowest. Hierarchies enable users to drill report data up and down to particular groups at runtime. For example, you can add these group objects into one hierarchy called "Dates": Sales Year, Sales Quarter, Sales Month, and Sales Date. When you use any of these group objects to group data in a table, crosstab, or chart, users can use the context menu to drill up or down to the next level. You can create any number of hierarchies such as dates, times, geography, and product types.

The group objects added in a hierarchy are just references to the real group objects and therefore cannot be edited.

**To create hierarchies in a business view**

1. In the Business View Editor dialog box, do any of the following:
   * Select **New Hierarchy** on the toolbar.
   * Navigate to **Menu** > **New** > **Hierarchy**.
   * Right-click the business view root node or any category in the Business View panel and select **New Hierarchy** from the shortcut menu.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You can add a hierarchy to any category in a business view and it does not make any difference where you place the hierarchy. For easy look-up, you can put them under the root category.
2. In the New Hierarchy dialog box, provide a name for the hierarchy and select **OK**. Designer adds a blank hierarchy to the business view resource tree.
3. You can now drag group objects from the business view resource tree to the hierarchy as hierarchical groups. Where Designer places a group object in the hierarchy depends on the position you drag it to:
   * When you drag the group object to the hierarchy root node, Designer place it at the bottom of the hierarchy.
   * When you drag the group object to an existing hierarchical group, Designer places it below this hierarchical group.
   * When you drag the group object between two hierarchical groups, Designer places it between them.

   You can also drag fields from the Resource Objects panel to the hierarchy. Then if you have not added any of the selected fields as group objects in the business view, Designer automatically adds them to the business view and places them at the bottom of the business view resource tree.

   To adjust the position of the group objects in the hierarchy, select a group object and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif). The higher a group object is placed, the higher its level is in the hierarchy.

   To remove a group object from the hierarchy, select it, then right-click and select **Remove from Hierarchy** on the shortcut menu, or drag it to the **Resource Objects** panel.
4. Repeat the preceding three steps to create more hierarchies in the business view.

   To rename a hierarchy, select it from the business view resource tree, then right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text box becomes editable, type in a new name and select outside of the text box to accept the change.

   To remove a hierarchy, select it from the business view resource tree, then right-click it and select **Delete** on the shortcut menu, or select **Delete** on the toolbar. You can select multiple hierarchies and remove them all at a time.
5. Save the business view to save the hierarchies into it.

You can also add and manage hierarchies in a business view from the Catalog Manager.

* **Adding a hierarchy**
  1. In the Catalog Manager resource tree, right-click a category in the business view and select **New Hierarchy** from the shortcut menu.
  2. In the New Hierarchy dialog box, provide a name for the hierarchy and select **OK**. Designer then adds the hierarchy in the business view.
  3. Right-click the business view and select **Edit** on the shortcut menu to open the Business View Editor.
  4. [Drag group objects](#DragGroup) to the hierarchy to define its hierarchical groups.
  5. Save the business view to save the hierarchy.
* **Removing a hierarchical group from a hierarchy**  
  In the Catalog Manager resource tree, locate the group in the hierarchy, then right-click it and select **Remove from Hierarchy** on the shortcut menu.
* **Renaming a hierarchy**  
  In the Catalog Manager resource tree, locate the hierarchy in the business view, right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text box becomes editable, type in a new name and select outside of the text box to accept the change.
* **Removing a hierarchy**  
  In the Catalog Manager resource tree, locate the hierarchy in the business view, then right-click it and select **Delete** on the shortcut menu, or select **Delete** on the Catalog Manager toolbar.

## Creating Predefined Filters for a Business View

You can predefine filters in a business view for users to choose when they design or modify data components that use the business view, so as to filter out the unnecessary data in the data components.

If you want to filter the data to use in a business view, you need to define [query filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#FilterQuery) while specifying the data resources for the business view.

**To create predefined filters in a business view**

1. In the Business View Editor dialog box, select **Predefined Filter** on the toolbar or navigate to **Menu** > **Tools** > **Predefined Filter**. Designer displays the [Predefined Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664546967-Predefined-Filter-Dialog-Box).
2. Select **New** to add a filter.

   ![Predefined Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550841495/prdfndfltr.gif)
3. In the **Filters** box, double-click in the **Name** and **Description** text boxes to edit the name and description of the filter.
4. In the **Condition** panel, select **Add Condition** to add a condition line.

   ![Condition panel](https://devnet.logianalytics.com/hc/article_attachments/4420556110359/bv_crt_fltr.gif)
5. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the field text box (the first text box), then in the View Element Resources dialog box, locate the element you want to filter and double-click it, or select the element and select **OK**. You can also type in the name of the view element manually as *@ElementName* in the text box.
6. From the operator drop-down list, select the operator with which to compose the filter expression.
7. In the value text box, specify the value of how to filter the element. You can apply an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0).

   To specify the value, select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the value text box (the second text box), then in the Values dialog box, switch to the **Value** tab. The tab contains all values of the selected element. Double-click the required one, and then close the dialog box. However, if you choose to manually specify the element name in step 5, you need to select the element in the **Fields** tab of the Values dialog box once again to get its value list. You can also select the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" or a parameter in the Fields tab as the value to filter the element dynamically (for the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661801239-Parameter-Application-Cases#FilterQuery)).

   If you are familiar with the values of the selected view element, you can also type in the value manually (when the selected operator requires multiple values, you have to specify the values manually). When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
8. Repeat steps 4 to 7 to add more condition lines and define the logic relationship between the condition lines: "And" or "Or".

   To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select **Up** or **Down**; to delete a condition line, select it and select **Delete**.
9. Repeat steps 2-8 to add more filters and define the filter conditions. To remove a filter, select it from the Filters box and select **Delete** on the right of the box.
10. Select **OK** to save the filters.
11. Save the business view to save the filters into it.

You can then apply the filters when creating or editing reports based on the business view in Designer or at runtime after you publish the corresponding catalog to Server.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* If you remove the resources that you have used in some predefined filters from the business view, the next time when you open the Predefined Filter dialog box, Designer displays warning messages and automatically removes the filters from the dialog box.
* You cannot filter the following SQL types of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.

## Customizing Filter Resources for a Business View

When you use a business view to create a report and want to filter the business view to narrow down data shown in the reports, by default, Logi Report lists all the view elements the business view contains for you to choose to define the filter. In the case when a business view contains a large number of view elements, you may find it difficult to locate the element you need to focus on. To avoid such inconvenience, you can customize which view elements you prefer to be available as the filter resources of the business view when creating the business view.

**To customize filter resources for a business view**

1. In the Business View Editor dialog box, select **Select Filter Resources** on the toolbar. Designer displays the [Select Filter Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661710999-Select-Filter-Resources-Dialog-Box).

   ![Select Filter Resources dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542087319/slctfltrrsc.gif)
2. By default, Designer selects all the view elements in the resource box. Clear the view elements you do not want to use in filters. To deselect all the view elements, clear the top checkbox; to deselect the view elements in a category, clear the category.
3. Select **OK** to apply the settings.

You can also access the Select Filter Resources dialog box in the following way: in the Catalog Manager resource tree, right-click the business view and select **Select Filter Resources** on the shortcut menu.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you define filters during [creating a link](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports) or [sending/receiving a message](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components), the available resources are always all the view elements in the corresponding business view.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters)
