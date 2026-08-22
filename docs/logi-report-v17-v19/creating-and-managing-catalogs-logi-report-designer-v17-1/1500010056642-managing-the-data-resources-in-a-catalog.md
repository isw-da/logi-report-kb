---
title: "Managing the Data Resources in a Catalog"
id: 1500010056642
section: "Creating and Managing Catalogs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056642-Managing-the-Data-Resources-in-a-Catalog
updated_at: 2021-07-23T19:14:33Z
---

# Managing the Data Resources in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094041-Editing-Pre-joins-in-a-Catalog)

# Managing the Data Resources in a Catalog

The [Catalog Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500010101481-Catalog-Manager) of Designer provides a hierarchical view of the data resources in the current catalog. This topic describes how you can use the manager to add, remove, and modify the data resources in a catalog.

![Catalog Manager](https://devnet.logianalytics.com/hc/article_attachments/4404856807447/rptenv_ctlgmngr.gif)

This topic contains the following sections:

* [Adding Data Resources](#Add)
* [Editing Data Resources](#Edit)
* [Duplicating Data Resources](#Duplicate)
* [Renaming Data Resources](#Rename)
* [Deleting Data Resources](#Delete)
* [Setting Data Resource Properties](#Property)
  + [Setting Default Property Values for a Data Resource](#Default)
* [Filtering Data Resources](#Filter)
* [Searching for Data Resources](#Search)
* [Sorting Data Resources](#Sort)

## Adding Data Resources

Although there are a variety of data resources in a catalog, the ways you create them are fairly similar.

1. In the Catalog Manager, expand the catalog data source where you want to add the resource.
2. Select the data resource node of the type that you want to create, then right-click it and select **Add**/**New XXX** from the shortcut menu, or select the appropriate command on the Catalog Manager toolbar. Designer then displays the corresponding resource editor or dialog box.

   For example, if you want to create a summary, right-click the **Summaries** node and select **New Summary**. Designer then displays the New Summary dialog box for you to create the summary.

## Editing Data Resources

Select the data resource that you want to edit, then select **Edit** on the Catalog Manager toolbar or right-click it and select **Edit XXX** from the shortcut menu. In the corresponding editor or dialog box, edit the resource as required.

In most cases, you can also edit a data resource by using its right-click Edit XXX menu command from the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010101501-Data-Panel), which only shows data resources actually available for use in the selected report component.

## Duplicating Data Resources

Select the data resource you want to duplicate and select **Copy** on the Catalog Manager toolbar. To paste it, select **Paste** on the toolbar.

## Renaming Data Resources

Select twice on the name of the data resource you want to rename, when the name text box becomes editable, type the new name and select outside the name text box to confirm the change.

You can also rename data resources by editing their Name property in the Properties sheet.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Renaming a data resource impacts other resources that use it. You can configure the [reference table](https://devnet.logianalytics.com/hc/en-us/articles/1500010056662-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) to monitor the reference relationships between resources.

## Deleting Data Resources

Select the data resource you want to delete and select **Delete** on the Catalog Manager toolbar, or right-click the data resource and select **Delete** from its shortcut menu.

## Setting Data Resource Properties

When you select a data resource and select **Show Properties** on the Catalog Manager toolbar, Designer displays the property list of the data resource in the Properties sheet on the right. See [Catalog Data Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061302-Catalog-Data-Object-Properties) for detailed explanation about the properties of each data resource type.

### Setting Default Property Values for a Data resource

You can set the default values for the properties of data resources in the Catalog Manager, so that you do not need to set them each time you insert them into your report. The data resources that can have default values are formulas, parameters, summaries, table/view columns, SQL columns, stored procedure columns, and user-defined data source columns. Query columns do not support this feature. Data resources that are used in a business view inherit their properties from the underlying objects.

**To set default values for a data resource:**

1. Select the data resource with the properties you want to set, select **Show Properties** on the Catalog Manager toolbar, or right-click the data resource and select **Properties** from the shortcut menu.
2. The property values listed in the Properties sheet are the default values for the selected data resource. You can change the property values here, and the next time you insert the data resource into a report, Designer will use the values you specify here as the default values.

## Filtering Data Resources

You can filter the data resources in the Catalog Manager to show only the required resources.

1. In the Catalog Manager, select **Filter View** on the toolbar. Designer displays the [Filter View dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096881-Filter-View-Dialog-Box).

   ![Filter View dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856971031/fltrvw.gif)
2. Provide a filter condition in the **Filter Expression** text box. Use "\*" to stand for any string, and use "?" to stand for any character. You can also leave this text box blank.
3. Select the **Case Sensitive** checkbox if you want Designer to distinguish between uppercase and lowercase characters when filtering.
4. In the **Select the elements to include in the view** box, select the resource types you want to keep in the Catalog Manager resource tree. Select the **Select All**/**Deselect All** button to select/clear all the resource types.
5. Select the **OK** button to filter the resources.

   The filter result is the union of the resources that match the filter condition and the selected resource types.

## Searching for Data Resources

When there are many resources in a catalog, sometimes you may find that it is difficult to locate a resource. The Catalog Manager provides you with the search function which enables you to search resources in the leaf nodes of the catalog data resource tree.

You can search for data resources using either the quick way or advanced way.

**To perform quick search:**

Select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif) at the upper right corner of the Data Resource panel in the Catalog Manager. In the search box that appears, type the text you want to search for and Designer lists the resources containing the matched text in the data resource tree.

You can also specify the following search settings after selecting the drop-down icon![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404856853911/btn_srchtlbr_adv.gif) in the search box:

* **Highlight All**   
  Select to highlight all matched text.
* **Match Case**   
  Select to search for text that meets the case of the typed text.
* **Match Whole Word**   
  Select to search for text that looks the same as the typed text.

To close the search box and cancel the search, select the **Delete** icon ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif) in it. Designer then lists all resources in the tree.

**To perform advanced search using dialog box:**

1. In the Catalog Manager, select **Search** on the toolbar. Designer displays the [Search dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060622-Search-Dialog-Box).

   ![Search dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848377367/srch.gif)
2. Provide a search condition in the **Search Expression** text box. Use "\*" to stand for any string, and use "?" to stand for any character.
3. Select the **Case Sensitive** checkbox if you want Designer to distinguish between uppercase and lowercase characters when searching.
4. Specify the search scope:
   * **Selected Resources**: Specifies to search from the leaf nodes of the resource that you have selected in the Catalog Manager resource tree when you open the dialog box.
   * **Search In**: Specifies to search from the leaf nodes of the selected catalog data source. To search from all data sources, select **All**.

   For example, if you want to find the DBField Customer Name in the Queries node, select the node in the Catalog Manager, then in the Search dialog box, type **Customer Name** in the Search Expression text box and select the scope as **Selected Resource**.
5. Select **Search** to start searching.

   Designer lists all the matched results in the Search Result panel which has three columns: Resource Name, Resource Type, and Resource Path. You can sort the search results alphabetically by selecting any column header. When you select an item in the Search Result panel, Designer highlights the corresponding resource in the Catalog Manager.

   ![Search Result](https://devnet.logianalytics.com/hc/article_attachments/4404857080983/ctlg_mng_srch.gif)

## Sorting Data Resources

Resources in the leaf nodes of the catalog data resource tree can be sorted for easy management. To do this, select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif) at the upper right corner of the Data Resource panel in the Catalog Manager, then from the drop-down menu, choose how to sort the resources:

* **Ascending**  
  Sorts the resources in an ascending order.
* **Descending**  
  Sorts the resources in a descending order.
* **No Sort**  
  Keeps the original order of the resources as in the database.

The default sort order is controlled by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Sort) option in the Catalog category of the Options dialog box. When Sort is unselected in the Options dialog box, the default sort order is No Sort.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You cannot sort the logical folder nodes for categorizing the resources and elements in a business view [hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Hierarchy).
* The change of sort order is a one-off action, meaning Designer does not save it after you exit the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094041-Editing-Pre-joins-in-a-Catalog)
