---
title: "Adding and Modifying Elements"
id: 1500009562642
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements
updated_at: 2021-07-24T05:56:15Z
---

# Adding and Modifying Elements

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562622-Editing-a-Business-View)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters)

# Adding and Modifying Elements

This topic introduces how to add or modifying business view elements. After you have selected data resources such as tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources to use in a business view, the data resources will be listed with their DBFields in the Resource Objects panel on the left in the Business View Editor, as well as the formulas and summaries in the current catalog data source that are valid to the data resources. You can use the resources to create view elements in the business view.

Below is a list of the sections covered in this topic:

> * [Adding Elements by Dragging](#Drag)
> * [Creating a Category](#Add)
> * [Creating a View Element](#Element)
> * [Editing a Category](#EditCategory)
> * [Editing a View Element](#EditElement)
> * [Adjusting Element Order](#Order)
> * [Renaming an Element](#Rename)
> * [Deleting an Element](#Delete)

## Adding Elements by Dragging

In the Business View Editor, a data resource is displayed as a folder containing their DBFields. You can drag DBFields, a whole data resource folder with all its DBFields, formulas, and summaries from the Resource Objects panel on the left to the business view or a category displayed in the Business View panel on the right. Multiple selection is supported.

Logi JReport then converts the resources into corresponding view elements in the business view. The conversion is as follows:

* DBFields and formulas are added as group elements.
* A whole data resource folder with all its DBFields is added as a category with group elements.
* Summaries are added as aggregations based on the same sum-on fields and summary functions.

If necessary, you can convert the group elements to detail elements via the [Edit View Element](#EditElement) dialog.

## Creating a Category

1. In the Business View Editor, select the business view or an existing category in the Business View panel, then do any of the following:
   * Right-click and select **New Category** from the shortcut menu.
   * Select the **New Category** on the toolbar.
   * Select **Menu** > **New** > **Category**.

   The [Category Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009564982-Category-Property-Dialog) dialog appears.

   ![Category Property dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404893932311/ctgryprpty_gnrl.gif)
2. In the General tab, set the display name of the category in the Display Name text field.
3. Type a description for the category in the Description text box if required to help others get an idea about it. The description will be shown when end users hover the mouse pointer over the category in the resources panel of Web Report Studio and Page Report Studio.
4. Select the **Security** tab and [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security) if needed.
5. Select **OK**. A new category will be added to the business view or the selected category. You can then New View Elements to it.

## Creating a View Element

1. In the Business View Editor, select the business view or any existing category into which you want to add the view element in the Business View panel, then do any of the following:
   * Right-click and select **New View Element**  from the shortcut menu.
   * Select **New Group**, **New Aggregation**, or **New Detail** on the toolbar.
   * Select **Menu** > **New**  > **Group**/**Aggregation**/**Detail**.

   The [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009588021-New-View-Element-Dialog) dialog appears.

   ![Add View Element dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889327383/nwvwelmnt_gen.gif)
2. In the General tab, decide the type of the view element by selecting the corresponding item from the Type drop-down list.
3. Select the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the Mapping Name text field to specify the mapping field of the view element.
4. Specify the display name of the view element in the Display Name text field.

   By default, the display name is the same as the mapping name. You can change it according to your requirements.
5. If you choose to create an aggregation object, select the **Aggregate Function** drop-down list to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions) with which to summarize the mapping field. Check the **Customized** option if you want to create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements#CA), then select the **Settings** button to open the Formula Editor to [compose the expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) using resources in the current business view.
6. Specify the tooltip and description of the view element in the Tip and Description text boxes respectively if required to help others get an idea about it. The tooltip and description will be shown when end users hover the mouse pointer over the view element in the resources panel of Web Report Studio and Page Report Studio.
7. Select the **Security** tab and [configure business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security) if needed.
8. When done, select **OK** to close the dialog.

## Editing a Category

1. In the Business View Editor, select the category you want to edit from the business view resource tree in the Business View panel, right-click it and select **Edit Category** from the shortcut menu. The Category Property dialog appears.
2. In the General tab, edit the general information of the category.
3. In the Security tab, edit the [security information](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security).
4. When done, select **OK** to accept the changes.

## Editing a View Element

1. In the Business View Editor, select the view element you want to edit from the business view resource tree in the Business View panel, right-click it and select **Edit** from the shortcut menu. The [Edit View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009586641-Edit-View-Element-Dialog) dialog appears.
2. In the General tab, edit the general information of the view element.

   You can convert a group element to a detail element and vice versa by selecting Detail or Group from the Type drop-down list.
3. In the Security tab, edit the [security information](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security).
4. When done, select **OK** to accept the changes.

If you want to apply the same tooltip and description for multiple view elements at a time, you can select them and then use the Edit View Element dialog to edit the Tip and Description settings, and when the selected view elements are all of the Group or Detail type, you can change their element type to Detail or Group if needed.

## Adjusting Element Orders

In the Business View Editor, you can change the position of the elements in any category or the categories in the business view in the resource tree of the Business View panel. The position here determines the display order of the elements and categories in any UI that shows the business view. You can place the elements and categories alphabetically or based on their using frequency to help others easily locate the desired one.

There are the following methods to change the position:

* Select a view element or a category and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) on the toolbar.
* Right-click a view element or a category and select **Move Up** or **Move Down** on the shortcut menu.

You can also drag a view element or a category and drop it to another category node to change its position. By doing this the view element or category is placed at the end of the target category. However when you drag a group element or category to another category, the group or groups in the selected category will be removed from [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/1500009583021-Defining-Hierarchies) that contain these groups and you need to add them from the target category to the hierarchies again.

## Renaming an Element

To rename a view element or a category, that is to change its display name, in the Business View panel of the Business View Editor, right-click the element or category and select **Rename** from the shortcut menu, or select on the name twice. The name text field then becomes editable. Input a new name and select outside of the text field to accept the change.

## Deleting an Element

When a view element or category is not required you can remove it from the business view. To do this, in the Business View panel of the Business View Editor, select the element or category, then,

* Select **Delete** on the toolbar.
* Right-click and select **Delete** from the shortcut menu.
* Drag and drop it to the Resource Objects panel on the left.

You can select multiple elements and delete them at one time.

**Tip:** From the Data tab of the Catalog Manager you can also create, edit, rename or delete an element in a business view by using the corresponding command on the element's shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562622-Editing-a-Business-View)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters)
