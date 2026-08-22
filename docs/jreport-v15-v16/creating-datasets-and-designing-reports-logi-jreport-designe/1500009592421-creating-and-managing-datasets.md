---
title: "Creating and Managing Datasets"
id: 1500009592421
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets
updated_at: 2021-07-24T05:53:55Z
---

# Creating and Managing Datasets

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562682-Modifying-the-Joins-Between-Data-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592661-Designing-Your-Reports)

# Creating and Managing Datasets

When you create [data components](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports) in a report, datasets are created. A dataset is the set of data built from the result of a [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries), [stored procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures), [imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files), [UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources), [HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources) or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views), and can optionally have filters applied to it. A dataset built on data resource such as query, stored procedure, imported SQL, UDS, and HDS contains all the DBFields in the data resource, as well as parameters and valid formulas in the catalog data source where the data resource is added; a dataset created from a business view contains only view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic).

A dataset has a name, which by default is the name of the resource on which it is created. For a page report, you can view items in a dataset by choosing the Dataset View mode from the toolbar of the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel).

Datasets in a page report can be shared by different data components. Having data components in the same page report use an existing dataset whenever possible will have a dramatic effect on the performance of your reports in the runtime environment. This is because each dataset is created by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same query Logi JReport will still run the query separately for each dataset.

Below is a list of the sections covered in this topic:

> * [Creating a Dataset](#Create)
> * [Managing Datasets](#Manage)

## Creating a Dataset

To create a dataset, take any of the following ways:

* **Creating a dataset from the report wizard** 

  When you create a data component using the report wizard, a dataset is created at the same time, either empty or containing some data fields, depending on whether data fields are added to the data component.
* **Creating a dataset via the Data panel** 
  (available to page report only)
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel), choose **<Choose Data from...>** from the dataset drop-down list.

     ![Data panel](https://devnet.logianalytics.com/hc/article_attachments/4404893825303/dtset.gif)
  2. In the New Dataset dialog, specify the data resource in the current catalog on which the dataset will be built.

     ![New Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889298327/nwdtst.gif)
  3. Enter the name of the dataset in the New Dataset Name field.
  4. Select **OK**, and an empty dataset will be created.
* [Creating a dataset from the Dataset Management](#CrtMng) dialog (available to page report only)

**Note:** If a dataset is created on a hierarchical data source, when you use the dataset to create data components, pay attention to the [unique features of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS).

## Managing Datasets

After you have created datasets in a report, you can manage them using the [Manage Datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009587781-Manage-Datasets-Dialog) dialog, for example, you can filter the datasets. To display the dialog, select **Report** > **Manage Datasets**.

![Manage Datasets dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889298711/mngdtst.gif)

### Adding/Removing data fields in a dataset

For any dataset, Logi JReport automatically adds fields to it when fields are added to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components that use it. So there generally is no need to ever add or remove fields from a dataset specifically. However, in the Dataset Management dialog, you can still manually add or remove data fields from a dataset.

1. In the Dataset List box of the Dataset Management dialog, select the dataset you want to edit.
2. In the Data tab of the dialog:
   * To add more data fields to the dataset, from the Available Resource box, select the fields from the source on which the dataset is created and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add them to the dataset. You can also select a field and drag and drop it into the Dataset box.
   * To remove an unnecessary data field from the dataset, select it in the Dataset box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif). Only the fields which are not used by any data component created on the dataset, either directly or indirectly, can be removed. To remove all the data fields in a dataset, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404889274263/btn_rmvall.gif), however, when you select the button, only the unused data fields will actually be removed. When you enter the dialog the next time, you will find that the data fields used by data components created on the dataset will still display in the Dataset box.
   * Use ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the added fields in the Dataset box.
3. When done, select **OK** to apply the changes and close the dialog box.

### Filtering data fields in a dataset

1. In the Dataset List box of the Dataset Management dialog, select the dataset with the data fields you want to filter, then select the **Filter** tab.
2. If the dataset is created on a business view, the Filter drop-down list is available, listing all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) of the business view. You can select one from the drop-down list to apply to the dataset, or select **User Defined** in the list to define a new filter as required.
3. Select the **Add Condition** button to add a condition line.
4. In the field drop-down list, specify the field on which the filter will be based.

   For a dataset created on a query, stored procedure, imported SQL, UDS, or HDS, you can filter on any DBField in the data resource, or a parameter or valid formula that is in the same catalog data source as the data resource. For a dataset created on a business view, you can only filter on a group or detail object in the business view.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value text field, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the value of how to filter the field in the displayed dialog or input the value manually. You can use a DBField or a formula as the value to filter the dataset, or the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009584241-Special-Fields#UserName) or a parameter to filter the dataset dynamically (for the usage of parameters in filter conditions, see the example in [Dynamically Filtering Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries)).

   When you type in the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To group some condition lines, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

**Tips:**

* A dataset is created based on another data resource and the data resource itself can also be applied with a filter. You may want to know the differences between the filters. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data#FilterLevel) for details.
* In a page report, you can also add/remove the data fields in a dataset or filter a dataset while creating a data component with the report wizard. To do this, check the **Existing** radio button in the Data screen of the wizard, then select an existing dataset and select the **Modify** button. In the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog), edit the dataset as required.
* A dataset in a page report can also be filtered using the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565142-Dataset-Filter-Dialog) dialog, which is displayed by selecting the Dataset Filter button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893799575/btn_filter.gif) on the toolbar of the Data panel.

**Note:** The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

### Optimizing a dataset

You can enlarge or decrease the scope of retrieved data for a dataset, and therefore make a balanceable decision between better performance and special usage cases/demands. However, this feature is not supported on datasets created from business views so only works for page reports. For datasets created on a business views, you can make use of the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500009590341-Business-View-Properties#Prefetch) property on the business views.

1. In the Dataset List box of the Dataset Management dialog, select the dataset with the name you want to optimize.
2. Select the **Optimize Dataset** button. The [Optimize Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009566982-Optimize-Dataset-Dialog) dialog appears.

   ![Optimize Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889298967/optmzdtst.gif)
3. Choose a retrieved data scope for the dataset.
   * **Only Columns Used in Report**  
      Only data columns used in the current report are retrieved at runtime. This way ensures the best performance since the least data is retrieved. This is always the default for page reports.
   * **All Columns in Dataset**  
      All data columns defined in the dataset are retrieved at runtime. Unless you manually added columns to the dataset [with the above mentioned method](#Add), this is the same as Only Columns Used in Report.
   * **All Columns in Query**  
      All data columns in the query that the dataset is based on are retrieved at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more columns to the report.
4. Select **OK** to apply the settings and close the dialog.

### Creating a dataset

You can create datasets for a page report via the Dataset Management dialog. To do this:

1. In the Dataset Management dialog, select the **New** button.
2. In the New Dataset dialog, specify the data source on which the dataset will be built.
3. Enter the name of the dataset in the New Dataset Name field.
4. Select **OK**, and an empty dataset is created.
5. [Add data fields to the dataset](#Add) as required.

### Renaming a dataset

1. In the Dataset List box of the Dataset Management dialog, select the dataset with the name you want to modify.
2. Double-click the **Name** cell of the dataset.
3. Input a new name in the cell and press Enter to apply the changes.

   However, you should not rename a dataset that has been used by any data component. Renaming a referenced dataset will cause data components based on the dataset not to work.

### Removing a dataset

1. In the Dataset List box of the Dataset Management dialog, specify the dataset you want to remove.
2. Select the **Remove** button to remove the specified dataset.
3. When done, select **OK** to apply the changes and close the dialog.

   However, if you remove a dataset directly in this way, any data components created based on the dataset will not work. So, when you want to remove a dataset, it is recommended that you first remove the data components which reference this dataset.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562682-Modifying-the-Joins-Between-Data-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592661-Designing-Your-Reports)
