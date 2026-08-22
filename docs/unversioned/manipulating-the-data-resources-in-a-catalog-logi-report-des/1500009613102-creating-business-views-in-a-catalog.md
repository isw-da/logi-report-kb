---
title: "Creating Business Views in a Catalog"
id: 1500009613102
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog
updated_at: 2021-07-24T16:03:26Z
---

# Creating Business Views in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters)

# Creating Business Views in a Catalog

Logi Report Designer includes the interactive [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607342-Business-View-Editor-Dialog), with which you can create and edit any business views as you need.

This topic includes the following sections:

* [Creating a Business View](#Create)
* [Adding and Modifying Elements in a Business View](#AddElement)
  + [Adding Elements by Dragging](#Drag)
  + [Creating and Editing View Elements with Dialog](#Element)
  + [Adjusting the Order of the Elements](#Order)
  + [Renaming an Element](#Rename)
  + [Deleting an Element](#Delete)

* [Defining Hierarchies in a Business View](#Hierarchy)
* [Creating Predefined Filters for a Business View](#Filter)
* [![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Customizing Filter Resources for a Business View](#FilterResource)

## Creating a Business View

To create a business view in a catalog, take the following steps:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open), then do either of the following:
   * In the Catalog Manager, expand the data source in which you want to create the business view, then select the **Business Views**  node or any existing business view in the data source and select **New Business View**  on the Catalog Manager toolbar, or right-click the **Business Views**  node in the data source and select **New Business View**  from the shortcut menu.
   * Select **Home** > **New** > **Business View**  or **File** > **New** > **Business View**, specify the data source in which the business view will be created, then select **OK**.
2. In the Enter Business View Name dialog, provide a name for the business view and select **OK**. The [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009607182-Add-Tables-Views-Queries-Dialog) dialog is then displayed.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911634967/addtbvwqy.gif)
3. In the left box, expand the resource nodes to add the resources based on which to create the business view to the right box, then select **OK**.

   If the catalog data source is connected with multiple connections, you can mash up multiple data resources for the business view that come from all these connections, including tables, views, synonyms, queries, imported SQLs, imported APEs, stored procedures and user defined data sources. When a query, imported SQL, imported APE, stored procedure or user defined data source is added, it will be added as a single table with all of its columns. When two resources (for example, a table and a view) use the same name, they cannot be added at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

   If the current catalog data source contains JDBC connections, the Show Tables/Views Already Added option is available. Select it if you want to show the tables, views and synonyms in the resource tree in the left box, which have already been added to the right box. You can then add the tables, views and synonyms of the JDBC connections for the business view as many times as you want by providing different names for the tables, views and synonyms each time you add them.
4. If more than one data resource is added for the business view, the Query Editor appears, in which you can edit the data resources you select for the business view in the same way you would do for a query. You can:
   * Select the columns in each table that you want to use for the business view. To select all columns in a table, select **\*** at the top of the table. However for tables from MongoDB connections, you cannot select all columns by selecting \*. The PrimaryKey and ForeignKey columns in such table cannot be selected to a business view.
   * [Add or delete the data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#AddTable)  used for creating the business view.
   * [Set up joins between the data resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#Join).
   * [Create formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#FormulaField) to use in the business view.
   * [Add filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#FilterQuery) to narrow data used in the business view.

   When done, select the **OK** button at the bottom of the Query Editor to apply the changes. You can also select **Menu** > **Query** > **Save As** to save the data resources as a query.
5. The Business View Editor appears. All the resources you have selected for the business view, and the formulas and summaries in the current catalog data source that are valid for the selected resources are listed in the Resource Objects panel on the left of the editor.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404911639063/bvedtr.gif)
6. [Add elements](#AddElement) to the business view based on the available resources.
7. [Define hierarchies](#Hierarchy) on the business view to allow end users to drill report data to particular groups.
8. [Create predefined filters](#Filter) on the business view for users to choose when using the business view to create reports.
9. You can [Configure security for the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security).
10. Select **Save** on the toolbar to save the business view.
11. Select **Menu** > **File** > **Close** to close the window. The business view will now have been added to the catalog.

## Adding Elements to a Business View

After you have selected data resources such as tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources to use in a business view, the data resources will be listed with their DBFields in the Resource Objects panel on the left in the Business View Editor, as well as the formulas and summaries in the current catalog data source that are valid to the data resources. You can use the resources to create view elements in the business view.

**Tip:** In the Catalog Manager you can also create, edit, rename or delete an element in a business view by using the corresponding command on the element's shortcut menu.

### Adding Elements by Dragging

In the Business View Editor, a data resource is displayed as a folder containing their DBFields. You can drag DBFields, a whole data resource folder with all its DBFields, formulas, and summaries from the Resource Objects panel on the left to the business view or a category displayed in the Business View panel on the right. Multiple selection is supported.

Logi Report then converts the resources into corresponding view elements in the business view. The conversion is as follows:

* DBFields and formulas are added as group elements.
* A whole data resource folder with all its DBFields is added as a category with group elements.
* Summaries are added as aggregations based on the same sum-on fields and summary functions.

You can convert the group elements to detail elements via the [Edit View Element](#EditElement) dialog.

When dragging a DBField whose data type is Timestamp/DateTime, you will be prompted with the [Select Time Interval](https://devnet.logianalytics.com/hc/en-us/articles/1500009610402-Select-Time-Interval-Dialog) dialog to specify how to create the group element. By default, Keep Original is selected in the dialog which means a group element based on the DBField itself will be created. If you also want to create a group element which uses an expression to retrieve the years/quarters/months/weeks/days of the field as its values, select the corresponding checkbox. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")In the meantime, you can use the Auto Create Hierarchy checkbox to specify whether to create a [hierarchy](#Hierarchy) in the business view automatically and edit the name of the hierarchy. The hierarchy will contain all the group elements you have specified to create from the DBField, with the group elements listed based on the order of the corresponding checkboxes in the dialog. You can further edit the hierarchy.

![Select Time Interval dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911639703/slcttmintvl.gif)

When multiple DBFields of the Timestamp/DateTime data type are dragged, the Select Time Interval dialog will pop up multiple times for you to specify the settings for each DBField.

### Creating and Editing Categories with Dialog

**To create a category in a business view using dialog:**

1. In the Business View Editor, select the business view or an existing category in the Business View panel, then do any of the following:
   * Right-click and select **New Category** from the shortcut menu.
   * Select **New Category** on the toolbar.
   * Select **Menu** > **New** > **Category**.

   The [Category Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009630441-Category-Property-Dialog) dialog appears.

   ![Category Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911639959/ctgryprpty_gnrl.gif)
2. In the General tab, set the display name of the category in the Display Name text box.
3. You can type a description for the category in the Description text box to help others get an idea about it. The description will be shown when end users hover the mouse pointer over the category in the resources panel of Web Report Studio and Page Report Studio.
4. You can select the **Security** tab and [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security).
5. Select **OK**. A new category will be added to the business view or the selected category. You can then add elements to it.

**To edit a category:**

1. In the Business View Editor, select the category from the business view resource tree in the Business View panel, right-click it and select **Edit Category** from the shortcut menu.
2. In the Category Property dialog, edit its general information in the General tab and [security information](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security) in the Security tab.
3. Select **OK** to confirm the changes.

### Creating and Editing View Elements with Dialog

**To create a view element in a business view using dialog:**

1. In the Business View Editor, select the business view or any existing category into which you want to add the view element in the Business View panel, then do any of the following:
   * Right-click and select **New View Element**  from the shortcut menu.
   * Select **New Group**, **New Aggregation**, or **New Detail** on the toolbar.
   * Select **Menu** > **New**  > **Group**/**Aggregation**/**Detail**.

   The [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog) dialog appears.

   ![Add View Element dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904200215/nwvwelmnt_gen.gif)
2. In the General tab, decide the type of the view element by selecting the corresponding item from the Type drop-down list.
3. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the Mapping Name text box to specify the mapping field of the view element.

   When creating a group element, if you want to write an expression to retrieve values for the group element, select the **By Expression**  checkbox, then select **Settings** and in the Formula Editor [compose the expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog) using resources in the current catalog data source. The expression should follow the [record level pass one formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#PassOne) syntax.
4. Specify the display name of the view element in the Display Name text box.

   By default, the display name is the same as the mapping name. You can change it according to your requirements.
5. If you choose to create an aggregation element, select the **Aggregate Function** drop-down list to specify the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) with which to summarize the mapping field. When DistinctSum is selected, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog. Select the **Customized** option if you want to create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements#CA), then select the **Settings** button to open the Formula Editor to [compose the expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog) using resources in the current business view.
6. Specify the tooltip and description of the view element in the Tip and Description text boxes respectively to help others get an idea about it. The tooltip will be shown when end users hover the mouse pointer over the view element in the business view resource tree at server runtime.
7. You can select the **Security** tab and [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security).
8. Select **OK** to create the view element and close the dialog.

**To edit a view element:**

1. In the Business View Editor, select the view element from the business view resource tree in the Business View panel, right-click it and select **Edit** from the shortcut menu.
2. In the [Edit View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009630941-Edit-View-Element-Dialog) dialog, edit its general information in the General tab and [security information](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security) in the Security tab.

   You can convert a group element to a detail element and vice versa by selecting Detail or Group from the Type drop-down list in the General tab.
3. Select **OK** to confirm the changes.

You can also select multiple view elements of the Group and Detail types and edit them at a time using the Edit View Element dialog to apply the same Tip and Description settings to the view elements, and change their element type to Detail or Group.

### Adjusting the Order of the Elements

In the Business View Editor, you can change the position of the elements in any category or the categories in the business view in the resource tree of the Business View panel. The position here determines the display order of the elements and categories in any UI that shows the business view, except that in the Catalog Manager resource tree which applies its own [sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009605302-Managing-the-Data-Resources-in-a-Catalog#Sort) rule. You can place the elements and categories alphabetically or based on their using frequency to help others easily locate the desired one.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.") There are the following methods to change the position:

* Select one or more categories or elements in a category and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) on the toolbar.
* Right-click one or more categories or elements in a category and select **Move Up** or **Move Down** on the shortcut menu.
* Select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif) at the upper right corner of the Business View panel and select **Ascending** or **Descending** from the drop-down menu to make the resources excluding the elements in [hierarchies](#Hierarchy) display in either ascending or descending order.

  **Note:** The No Sort item in the Sort drop-down menu is always grayed out. It is selected by default each time you open the Business View Editor, however this does not cancel the ascending or descending order if you have applied one to the elements the last time you were working in the editor, in other words, once you have selected the ascending or descending order and saved the business view, when you open the editor the next time, the elements will be displayed in the specified order although No Sort is selected on the drop-down menu. You will also find No Sort is selected automatically when the elements apply neither the ascending nor descending order, for example you adjust the element order by moving them up or down.

You can also drag a view element or a category and drop it to another category node to change its position. By doing this the view element or category is placed at the end of the target category. However when you drag a group element or category to another category, the group or groups in the selected category will be removed from [hierarchies](#Hierarchy) that contain these groups and you need to add them from the target category to the hierarchies again.

### Renaming an Element

To rename a view element or a category, that is to change its display name, in the Business View panel of the Business View Editor, right-click the element or category and select **Rename** from the shortcut menu, or select on the name twice. The name text box then becomes editable. Type in a new name and select outside of the text box to accept the change.

### Deleting an Element

When a view element or category is not required you can remove it from the business view. To do this, in the Business View panel of the Business View Editor, select the element or category, then,

* Select **Delete** on the toolbar.
* Right-click and select **Delete** from the shortcut menu.
* Drag and drop it to the Resource Objects panel on the left.

You can select multiple elements and delete them at one time.

## Defining Hierarchies in a Business View

Hierarchies can be defined in a business view to allow end users to drill report data up and down to particular groups at runtime. A hierarchy can be regarded as a category that contains group elements sharing a hierarchical relationship in order from the highest level to the lowest. For example, these group elements can be added into one hierarchy called Dates: Sales Year, Sales Quarter, Sales Month, and Sales Date. When any of these group elements are used for grouping data in a table, crosstab or chart, end users can use the context menu to drill up or down to the next level. You can create any number of hierarchies such as dates, times, geography, product types, and so on.

The group elements added in a hierarchy are just references to the real group elements and therefore cannot be edited.

**To create hierarchies in a business view:**

1. In the Business View Editor, do any of the following:
   * Select **New Hierarchy** on the toolbar.
   * Select **Menu** > **New** > **Hierarchy**.
   * Right-click the business view root node or any category in the Business View panel and select **New Hierarchy** from the shortcut menu.

   **Tip:** Hierarchies can be added into any category in a business view and it does not make any difference where it is placed. For easy look-up, you can put them under the root category.
2. In the New Hierarchy dialog, provide a name for the hierarchy and select **OK**. A blank hierarchy is added to the business view resource tree.
3. You can now add group elements into the hierarchy as a hierarchical group by dragging and dropping. From the business view resource tree, select a required group element and then drop it into the hierarchy. Where the group will be placed in the hierarchy depends on the dropped position:
   * When you drop on the hierarchy root node, it will be placed to the bottom level of the hierarchy.
   * When on an existing hierarchical group, it will be placed below this hierarchical group.
   * When between two hierarchical groups, it will be placed between them.

   You can also drag objects from the Resource Objects panel to the hierarchy. Then those that have not been added as group elements in the business view will be automatically added to the business view and placed at the bottom of the business view resource tree.

   To adjust the position of the groups in the hierarchy, make use of the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) button. The higher a group is placed, the higher its level is in the hierarchy.

   To remove a group from the hierarchy, select it, then right-click and select **Remove from Hierarchy** on the shortcut menu, or drag and drop it to the Resource Objects panel.
4. Repeat the above three steps to create more hierarchies in the business view.

   To rename a hierarchy, select it from the business view resource tree, then right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text box becomes editable, type in a new name and select outside of the text box to accept the change.

   To remove a hierarchy, select it from the business view resource tree, then right-click it and select  **Delete** on the shortcut menu, or select **Delete** on the toolbar. You can select multiple hierarchies and remove them all at a time.
5. Save the business view to save the hierarchies into it.

You can also add and manage hierarchies in a business view from the Catalog Manager as follows:

* **Adding a hierarchy**
  1. In the Catalog Manager resource tree, right-click a category in the business view and select **New Hierarchy** from the shortcut menu.
  2. Provide a name in the New Hierarchy dialog and then select **OK**.
  3. A hierarchy will be added in the business view.
  4. Right-click the business view and select **Edit** on the shortcut menu to open the Business View Editor.
  5. [Drag and drop group elements](#DragGroup)  to the hierarchy to define its hierarchical groups.
  6. Save the business view to save the hierarchy.
* **Removing a hierarchical group from a hierarchy**  
  In the Catalog Manager resource tree, locate the group in the hierarchy, then right-click it and select **Remove from Hierarchy** on the shortcut menu.
* **Renaming a hierarchy**  
  In the Catalog Manager resource tree, locate the hierarchy in the business view, right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text box becomes editable, type in a new name and select outside of the text box to accept the change.
* **Removing a hierarchy**  
  In the Catalog Manager resource tree, locate the hierarchy in the business view, then right-click it and select  **Delete** on the shortcut menu, or select **Delete** on the Catalog Manager toolbar.

## Creating Predefined Filters for a Business View

You can predefine filters in a business view for users to choose when they design or modify data components that use the business view, so as to filter out the unnecessary data in the data components.

If you want to filter data used in a business view, you need to make use of the [query filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#FilterQuery) while defining the data resources to be used for the business view.

**To create predefined filters in a business view:**

1. In the Business View Editor, select **Predefined Filter** on the toolbar or select **Menu** > **Tools** > **Predefined Filter**. The [Predefined Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009609682-Predefined-Filter-Dialog) dialog appears.
2. Select the **New** button to add a filter.

   ![Predefined Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904200599/prdfndfltr.gif)
3. In the Filters box, double-click in the Name and Description text boxes to edit the name and description of the filter.
4. In the Condition panel, select the **Add Condition** button to add a condition line.

   ![Condition panel](https://devnet.logianalytics.com/hc/article_attachments/4404911640215/bv_crt_fltr.gif)
5. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the field text box, then in the View Element Resources dialog, locate the element you want to filter and double-click it, or select the element and select **OK**. You can also type in the name of the view element manually as *@ElementName* in the text box.
6. From the operator drop-down list, select the operator with which to compose the filter expression.
7. In the value text box, specify the value of how to filter the element.

   To specify the value, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the value text box, then in the Values dialog switch to the **Value** tab. All values of the selected element are listed. Double-click the required one, and then close the dialog. However if you choose to manually specify the element name in step 5, you need to select the element in the Fields tab of the Values dialog once again to get its value list. You can also select the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) or a parameter in the Fields tab as the value to filter the element dynamically (for the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery)).

   If you are familiar with the values of the selected view element, you can also type in the value manually (when the selected operator requires multiple values, you will have to specify the values manually). When you type in the value, if multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

   ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0).
8. Select **Add Condition** to add more condition lines, specify the condition in each line, and define the logic (And or Or) between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
9. Repeat steps 2-8 to add more filters and define the filter conditions. To remove a filter, select it from the Filters box and select the **Delete** button on the right.
10. Select **OK** to save the filters.
11. Save the business view to make the filters saved into it.

You can then apply the filters when creating or editing reports based on the business view in Logi Report Designer or at server runtime after you publish the corresponding catalog to Logi Report Server.

**Notes:**

* When the resources that are used in some predefined filters are removed from the business view, the next time when you open the Predefined Filter dialog, you will be prompted with warning messages showing the details and the filters will be removed automatically from the dialog as well.
* The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

## This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Customizing Filter Resources for a Business View

When a business view is used as the data source of reports and you want to filter the business view to narrow down data shown in the reports, by default all the view elements the business view contains will be listed for you to choose to define the filter. In the case when a business view contains a large number of view elements, you will find it difficult to locate the element you need to focus on. To avoid such inconvenience, you can customize which view elements you prefer to be available as the filter resources of the business view when creating the business view.

**To customize filter resources for a business view:**

1. In the Business View Editor, select **Select Filter Resources** on the toolbar. The [Select Filter Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009633541-Select-Filter-Resources-Dialog) dialog opens.

   ![Select Filter Resources dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911643671/slctfltrrsc.gif)
2. By default all the view elements are selected in the resource box. Clear the view elements you do not want to use in filters. To deselect all the view elements, clear the top checkbox; to deselect the view elements in a category, clear the category. You can also make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif) to display the view elements in the ascending or descending order for easy look-up, or the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif) to search for the required view elements.
3. Select **OK** to apply the settings.

The Select Filter Resources dialog can also be opened in the following way: in the Catalog Manager resource tree, right-click the business view and select **Select Filter Resources** on the shortcut menu.

**Note:** When defining filters during [creating a link](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports) or [sending/receiving a message](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-), the available resources are always all the view elements in the corresponding business view.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters)
