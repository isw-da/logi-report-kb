---
title: "Setting Resource Properties"
id: 1500009583181
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583181-Setting-Resource-Properties
updated_at: 2021-07-24T05:56:13Z
---

# Setting Resource Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583121-Adding-Editing-and-Modifying-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583201-Searching-for-Resources)

# Setting Resource Properties

When you select a data resource and select Show Properties on the Catalog Manager toolbar, the property list of the selected data resource is displayed. See [Properties in the Catalog Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009590321-Catalog-Data-Object-Properties) for detailed explanation about properties of each data resource.

By default, the properties in the Catalog Manager cannot be edited. To make the properties editable:

1. On the Catalog Manager toolbar, select **Options**.
2. In the Options dialog, select **Catalog** in the Category box.
3. Uncheck the option **Forbid editing data object properties**, then select **OK** in the dialog to confirm the change.

## Setting default values for data resources

You can set the default values for the properties of data resources in the Catalog Manager, so that you do not need to set them each time you insert them into your report. The data resources that can have default values are formulas, parameters, summaries, table/view columns, SQL columns, procedure columns and user data source columns.Query columns do not support this feature. Data resources that are used in a business view inherit their properties from the underlying objects.

**To set default values for a data resource:**

1. Make sure that the property values are editable in the Catalog Manager.
2. Select the data resource with the properties you want to set, select **Show Properties** on the Catalog Manager toolbar, or right-click the data resource and select **Properties** from the shortcut menu.
3. The properties listed in the Properties sheet are the default values for the selected data resource. You can change the property values here, and the next time you insert the data resource into a report, the value you specify here will be used as the default value.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583121-Adding-Editing-and-Modifying-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583201-Searching-for-Resources)
