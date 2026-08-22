---
title: "Adding, Editing, and Modifying Resources"
id: 1500009583121
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583121-Adding-Editing-and-Modifying-Resources
updated_at: 2021-07-24T05:56:13Z
---

# Adding, Editing, and Modifying Resources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583101-Managing-Data-Resources-in-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties)

# Adding, Editing, and Modifying Resources

It is easy for you to create data resources, and edit the existing data resources in a catalog using the Catalog Manager.

* **Adding a data resource**  
   Although there are a variety of data resources in a catalog, the ways you create them are fairly similar - select a data resource node of the type that you want to create, and then create them using either the Catalog Manager toolbar or context menu.
  1. In the Catalog Manager, expand the catalog data source where the resource will be added.
  2. Right-click the data resource node or a data resource of the type that you want to create and select **Add**/**New XXX**. The appropriate resource editor or dialog is then displayed.

     For example, if you want to create a formula, right-click the **Formulas** node and select **New Formula**. Enter a name for the formula in the displayed dialog and select **OK**. The Formula Editor appears. Create the formula in the editor.
* **Editing a data resource**  
   To edit any of the existing data resources in a catalog, locate the data resource in the Catalog Manager, then select **Edit** on the Catalog Manager toolbar or right-click it and select **Edit XXX** from the shortcut menu. In the corresponding editor or dialog, edit the resource as required.

  In most cases you can also edit a data resource by using its right-click Edit XXX menu command from the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel), which only shows data resources actually available for use in the selected report component.
* **Duplicating a data resource**  
   To copy a data resource, select it and select **Copy** on the Catalog Manager toolbar. To paste it, select **Paste** on the toolbar.
* **Renaming a data resource**  
   To rename a data resource, select on the resource name twice, the name text field will become editable, edit the resource name and then select outside the renaming box to confirm the change.

  You can also rename data resources by using the Properties sheet:

  1. Select the data resource, and select **Show Properties** on the Catalog Manager toolbar to show the Properties sheet.
  2. Select the property **Name**, type a new name in the Value field. You need to [enable the editable mode for the Properties sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties) before you can do this.

  **Note:** Renaming a data resource will impact the reports that use it. You can configure the [reference table](https://devnet.logianalytics.com/hc/en-us/articles/1500009583141-Using-a-Reference-Table-to-Clarify-Resource-Relationships)  then use right-click Reference Entities to show a list of the reports currently using this data resource so that you can update those reports.
* **Deleting a data resource**  
   To delete a data resource, select it and select **Delete** on the Catalog Manager toolbar, or right-click the data resource and select **Delete** from its shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583101-Managing-Data-Resources-in-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties)
