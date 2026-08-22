---
title: "Creating and Managing Datasets"
id: 1500009635941
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets
updated_at: 2021-07-24T16:03:25Z
---

# Creating and Managing Datasets

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613242-Designing-Your-Reports)

# Creating and Managing Datasets

When you create [data components](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports) in a report, datasets are created. A dataset is the set of data built from the result of a [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries), [stored procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures), [imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements), [imported APE](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs), [user defined data source](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources), [hierarchical data source](https://devnet.logianalytics.com/hc/en-us/articles/1500009606722-Hierarchical-Data-Sources)  or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views), and can optionally have filters applied to it. A dataset has a name, which by default is the name of the data resource on which it is created. A dataset built on data resource such as query, stored procedure, imported SQL, imported APE, UDS and HDS can contain all the DBFields in the data resource, as well as the parameters and valid formulas of these DBFields in the same catalog data source as the data resource; a dataset created from a business view can contain only view elements and dynamic resources.

Datasets in a page report created using query resources and web report can be shared by different data components. Having data components in the same report use an existing dataset whenever possible will have a dramatic effect on the performance of your reports in the runtime environment. This is because each dataset is created by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same query Logi Report will still run the query separately for each dataset.

This topic includes the following sections:

* [Creating Datasets in a Report](#Create)
* [Managing the Datasets in a Report](#Manage)
* [Setting Properties of the Datasets in a Report](#Property)
* [Customizing Field Display Names for Datasets in a Report](#Customize)

## Creating Datasets in a Report

You have the following methods to create datasets in a report:

* **Creating a dataset from the report wizard** 

  When you create a data component using the report wizard, a dataset is created at the same time, either empty or containing some data fields, depending on whether data fields are added to the data component.
* **Creating a dataset via the Data panel** 
  (available to page reports created using query resources only)
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009636281-Data-Panel), choose **<Choose Data from...>** from the dataset drop-down list.

     ![Create Dataset from Data Panel](https://devnet.logianalytics.com/hc/article_attachments/4404911638295/dtset_crt.gif)
  2. In the New Dataset dialog, specify the data resource in the current catalog on which the dataset will be built.

     ![New Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904198423/nwdtst.gif)
  3. Type the name of the dataset in the New Dataset Name text box.
  4. Select **OK**, and an empty dataset will be created.
* [Creating a dataset from the Manage Datasets dialog](#CrtMng)

**Note:** If a dataset is created on a hierarchical data source, when you use the dataset to create data components, pay attention to the [unique features of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629521-Developing-Reports-from-Hierarchical-Data-Sources).

## Managing the Datasets in a Report

You can manage the datasets in a report with the [Manage Datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009632421-Manage-Datasets-Dialog) dialog, for example, you can add more data fields to the datasets, filter the datasets, rename the datasets, and so on. However this feature is supported only for query based page reports and library components.

To manage the datasets in a report, [open the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports), then select **Report** > **Manage Datasets** to display the Manage Datasets dialog.

![Manage Datasets dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911638551/mngdtst.gif)

You can manage the datasets in a report as follows:

* **Creating a dataset**
  1. Select the **New** button (the button is activated for page reports created using query resources only).
  2. In the New Dataset dialog, specify the data source on which the dataset will be built.
  3. Type the name of the dataset in the New Dataset Name text box.
  4. Select **OK**, and an empty dataset is created.
  5. [Add data fields to the dataset](#Add) as required.
* **Adding/Removing data fields in a dataset**  
   For any dataset, Logi Report automatically adds fields to it when fields are added to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components that use it. So there generally is no need to ever add or remove fields from a dataset specifically. However in the Manage Datasets dialog, you can still manually add or remove data fields from a dataset. To do this, in the Dataset List box select the dataset you want to edit, then in the Data tab:
  + To add more data fields to the dataset, from the Available Resource box, select the fields from the source on which the dataset is created and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add them to the dataset. You can also select a field and drag and drop it into the Dataset box.
  + To remove an unnecessary data field from the dataset, select it in the Dataset box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif). Only the fields which are not used by any data component created on the dataset, either directly or indirectly, can be removed. To remove all the data fields in a dataset, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404911605783/btn_rmvall.gif), however when you select the button, only the unused data fields will actually be removed. When you open the dialog the next time, you will find that the data fields used by data components created on the dataset will still display in the Dataset box.
  + Use ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the order of the added fields in the Dataset box.
* **Filtering data fields in a dataset**
  1. In the Dataset List box select the dataset you want to filter, then select the **Filter** tab.
  2. If the dataset is created on a business view, the Filter drop-down list is available, listing all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply to the dataset, or select **User Defined** in the list to define a new filter as required.
  3. Add the filter conditions as required. Based on the data resource type from which the dataset is created, a business view or a query resource, the way to create a filter for the dataset differs.

     If the dataset is created on a business view, you can add filter condition for it in the same way as you [add conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#AddCondition) for a predefined filter in the business view.

     **To add filter conditions for a dataset created from a query resource:**

     1. Select the **Add Condition** button to add a condition line.

        ![Filter Query Based Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404911638807/dtset_fltr.gif)
     2. From the field drop-down list, select the field to be filtered. The field can be any DBField in the query resource, or a parameter or valid formula of these DBFields in the same catalog data source as the query resource.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. In the value text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to specify the value of how to filter the field in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009631041-Expressions-Dialog) dialog or type in the value manually. You can also use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) or a parameter to filter the dataset dynamically. For the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery).

        When you type in the value, if multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

        ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
     5. Select **Add Condition** to add more condition lines and define the logic (And or Or) between the condition lines.

        To group some condition lines, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

        To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

        To delete a condition line, select it and select the **Delete** button.

  **Tips:**

  + A dataset is created based on another data resource and the data resource itself can also be applied with a filter. You may want to know the differences between the filters. [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports#Filter) for details.
  + You can also add/remove the data fields in a dataset or filter a dataset while creating a data component using a query resource with the report wizard. To do this, select the **More Options** button and select the **Existing Dataset** radio button in the Data screen of the wizard, then select an existing dataset and select the **Edit** button. In the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), edit the dataset as required.
  + A dataset created from a query resource can also be filtered by selecting the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607782-Dataset-Filter-Dialog) button ![](https://devnet.logianalytics.com/hc/article_attachments/4404911588119/btn_filter.gif) on the toolbar of the Data panel.

  **Note:** The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.
* **Optimizing a dataset**  
   You can enlarge or decrease the scope of retrieved data for a dataset, and therefore make a balanceable decision between better performance and special usage cases/demands. However, this feature is not supported on datasets created from business views so only works for page reports that are created using query resources. For datasets created on business views, you can make use of the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500009634581-Business-View-Properties#Prefetch) property on the business views.
  1. In the Dataset List box select the dataset with the name you want to optimize.
  2. Select the **Optimize Dataset** button. The Optimize Dataset dialog appears.

     ![Optimize Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904198679/dtset_optmz.gif)
  3. Choose a retrieved data scope for the dataset.
     + **Only Columns Used in Report**  
        Only data columns used in the current report are retrieved at runtime. This way ensures the best performance since the least data is retrieved. This is always the default for page reports.
     + **All Columns in Dataset**  
        All data columns defined in the dataset are retrieved at runtime. Unless you [manually added columns to the dataset](#Add), this is the same as Only Columns Used in Report.
     + **All Columns in Query**  
        All data columns in the query that the dataset is based on are retrieved at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more columns to the report.
  4. Select **OK** to optimize the dataset.
* **Renaming a dataset**
  1. In the Dataset List box select the dataset with the name you want to modify.
  2. Double-click in the Name text box of the dataset.
  3. Type a new name in the text box and press **Enter** to apply the changes.

     However, you should not rename a dataset that has been used by any data component. Renaming a referenced dataset will cause data components based on the dataset unable to work anymore.
* **Removing a dataset**
  1. In the Dataset List box select the dataset you want to remove.
  2. Select the **Remove** button to remove the specified dataset.
  3. Select **OK** to apply the change and close the dialog.

     However, if you remove a dataset directly in this way, any data components created based on the dataset will not work. So when you want to remove a dataset, it is recommended that you first remove the data components which reference this dataset.

## Setting Properties of the Datasets in a Report

Each dataset in a query based page report and library component has its own node in the Report Inspector. You can edit the properties there to make the dataset better serve the data components created on it.

**To edit properties of a dataset in a report:**

1. In the Report Inspector, select the name of the dataset under the Datasets node for a page report or Data Source node for a library component.

   ![Datasets in Report Inspector](https://devnet.logianalytics.com/hc/article_attachments/4404904199191/dtset_prpty.gif)
2. In the Properties sheet, edit the [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties) of the dataset as required.

   For example, you can apply a [cached query result file](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results) to the dataset, specify the data buffer size for the dataset to improve performance, apply [record level security](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security#Report) for the data components using the dataset.

## Customizing Field Display Names for Datasets in a Report

For datasets created on query resources in a page report, Logi Report allows you to customize the display names of the data fields in the datasets, so that when end users run the page report in Page Report Studio and perform operations such as Sort, Filter on data components in the page report, they will be able to work with intuitive field names. You can also specify the actions in which the customized display names will participate for each data component in the page report.

1. Open the page report that is created using query resources.
2. Select  **Report** > **Edit Display Name** to display the [Edit Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009630641-Edit-Display-Name-Dialog) dialog.

   ![Edit Display Name](https://devnet.logianalytics.com/hc/article_attachments/4404904199447/edtdsplynm.gif)
3. From the Report Dataset drop-down list, where all datasets used in the page report are listed, select a dataset and all the data fields in the dataset are then shown in the mapping name box.
4. To make the resource names sort automatically, select the **Auto Sort** checkbox.
5. Specify the display names for the data fields in the Display Name column. A formula can be selected as the display name of the data field.
6. Select another dataset and repeat the above steps to edit the display names of data fields in it.
7. You can select the **Advanced** button to further customize the display names for data components in the page report using the [Edit Display Name for Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009630661-Edit-Display-Name-for-Component-Dialog) dialog.

   ![Edit Display Name for Component](https://devnet.logianalytics.com/hc/article_attachments/4404904199703/edtdsplynmcmpnt.gif)
8. From the Component drop-down list, select the data component in the page report you want to customize.

   **Tip:** You can also right-click a data component created using query resource in a page report and then select Edit Display Name from the shortcut menu to display the Edit Display Name for Component dialog. However, if the dialog is opened in this way, only the component you right-click on will be listed in the Component drop-down list.
9. In the action columns, select the corresponding checkboxes to indicate whether the actions are enabled for the data fields. Select the checkbox on the action column header if you want the corresponding action to be enabled for all data fields. If any action is not supported on the selected data component, the corresponding column will be disabled.

   When an action is selected for a data field, the field's display name instead of mapping name will be shown in the corresponding dialog or submenu in Page Report Studio. If you clear the box for any field in any action column, the field will not be available for the action. Moreover, if you set the display name of any field to be blank in the Edit Display Name dialog, all actions will be disabled for the field, which means end users will not be able to perform all these actions on the field in Page Report Studio.
10. Upon finishing, select **OK** to accept the changes.

**Note:** If you set the display name of any data field to be blank, the field will not be shown in the lists where display names are displayed in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613242-Designing-Your-Reports)
