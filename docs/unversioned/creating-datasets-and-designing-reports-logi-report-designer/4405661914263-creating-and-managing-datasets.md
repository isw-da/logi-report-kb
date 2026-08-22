---
title: "Creating and Managing Datasets"
id: 4405661914263
section: "Creating Datasets and Designing Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets
updated_at: 2022-01-27T20:35:07Z
---

# Creating and Managing Datasets

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664689687-Designing-Your-Reports)

# Creating and Managing Datasets

A dataset is the set of data built from the result of a data resource: [query](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries), [stored procedure](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures), [imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs), [imported APE](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs), [user-defined data source](https://devnet.logianalytics.com/hc/en-us/articles/4405661435031-Using-User-Defined-Data-Sources), [hierarchical data source](https://devnet.logianalytics.com/hc/en-us/articles/4405664410263-Using-Hierarchical-Data-Sources), or [business view](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views), and can optionally have filters applied to it. A dataset built on data resource other than a business view can contain all the DBFields in the data resource, and the parameters and valid formulas of these DBFields in the same catalog data source as the data resource; a dataset created from a business view can contain only view elements and dynamic resources. When you create a data component in a report, you can select the data resource to create a new dataset from it or use an existing dataset in the report. This topic describes how you can create and manage the datasets in a report.

This topic contains the following sections:

* [Creating Datasets in a Report](#Create)
* [Managing the Datasets in a Report](#Manage)
  + [Creating a Dataset](#CrtMng)
  + [Adding/Removing Data Fields in a Dataset](#Add)
  + [Filtering Data Fields in a Dataset](#Filter)
  + [Optimizing a Dataset](#Optimize)
  + [Renaming a Dataset](#Rename)
  + [Removing a Dataset](#Remove)
* [Setting Properties of the Datasets in a Report](#Property)
* [Customizing Field Display Names for Datasets in a Report](#Customize)

## Creating Datasets in a Report

You have the following methods to create datasets in a report:

* **Creating a dataset from the component wizard**  
  When you select a data resource to create a data component using the component wizard, Designer creates a dataset at the same time, either empty or containing some data fields, depending on whether you add data fields to the data component.

  When creating a data component in a query-based page report, if you choose to use an existing dataset in the page report for the data component but the exiting ones are not what you want, you can also create a dataset directly to use for the data component.

  1. In the **Data** screen of the component wizard, select **More Options**.
  2. Select **Existing Dataset**, then select **<New Dataset...>** in the dataset box.

     ![Create Dataset from Data Panel](https://devnet.logianalytics.com/hc/article_attachments/4420550839319/dtset_wzd.gif)

     Designer displays the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661656087-New-Dataset-Dialog-Box).

     ![New Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556108439/nwdtst.gif)
  3. From the data source drop-down list, select the catalog data source that contains the data you need.
  4. Designer displays the data resources you have created in the specified catalog data source in the resource box. Select the data resource on which to create the dataset. You can also select the first item in a resource node to create a data resource of the type to use for the dataset.

     ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you select to add a new stored procedure or imported SQL for the dataset,

     + If the specified catalog data source contains only one connection other than the JDBC connection, Designer displays the [Get JDBC Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box) for you to [set up the JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog) first.
     + If the specified catalog data source contains more than one connection, Designer displays the [Choose JDBC Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4411769082647-Choose-JDBC-Connection-Dialog-Box) for you to select the JDBC connection in the data source, via which you want to add the stored procedure or imported SQL. You can also select **<Add JDBC Connection...>** in the dialog box to create a JDBC connection and then add the stored procedure or imported SQL from the new connection.
  5. In the **New Dataset Name** text box, type the name of the dataset.
  6. Select **OK** to create the dataset based on the specified data resource.
  7. Add data fields in and related to the data resource to display in the data component and Designer includes them in the dataset automatically. If you do not add any data field, the dataset is empty.
* **Creating a dataset when choosing or binding data for a report**  
  When you select the data for a report in the [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661466135-Choose-Data-Dialog-Box) or [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661458711-Bind-Data-Dialog-Box), you can also create a dataset based on a data resource in the current catalog using [the same method](#Wizard) as from the component wizard.
* [Creating a dataset from the Manage Datasets dialog box](#CrtMng)
* **Creating a dataset via the Data panel**
  (you can use this method for query-based page reports only)
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/4405661950871-Data-Panel), select **<Choose Data from...>** from the dataset drop-down list.

     ![Create Dataset from Data Panel](https://devnet.logianalytics.com/hc/article_attachments/4420550839575/dtset_crt.gif)
  2. In the New Dataset dialog box, [create the dataset](#ChooseData). Designer adds the dataset in the page report. You can then use the dataset for any report tab in the page report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* You should make different data components in the same report share the datasets in the report whenever possible, which has a dramatic effect on the performance of your reports in the runtime environment. This is because Logi Report Engine creates each dataset by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
* If you create a dataset on a hierarchical data source, when you use the dataset to create data components, you need to pay attention to the [unique features of HDS](https://devnet.logianalytics.com/hc/en-us/articles/4405664411159-Developing-Reports-from-Hierarchical-Data-Sources).

## Managing the Datasets in a Report

You can manage the datasets in a report with the [Manage Datasets dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661641879-Manage-Datasets-Dialog-Box), for example, you can add more data fields to the datasets, filter the datasets, rename the datasets, and so on; however, Designer supports this feature only for query-based page reports and library components.

To manage the datasets in a report, [open the report](https://devnet.logianalytics.com/hc/en-us/articles/4405664694551-Opening-Reports), then navigate to **Report** > **Manage Datasets** to display the Manage Datasets dialog box.

![Manage Datasets dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542084503/mngdtst.gif)

You can perform the following management tasks in the Manage Datasets dialog box.

### Creating a Dataset

1. Select **New** (Designer enables this button for query-based page reports only).
2. In the New Dataset dialog box, [create the dataset](#ChooseData) and select **OK**. Designer creates an empty dataset.
3. [Add the data fields](#AddField) you want to include in the dataset.

### Adding/Removing Data Fields in a Dataset

For any dataset, Designer automatically adds fields to it when you add fields to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components; therefore, there generally is no need to ever add or remove fields from a dataset specifically. However, in the Manage Datasets dialog box, you can still manually add or remove data fields from a dataset. To do this, in the **Dataset List** box, select the dataset you want to edit, then in the **Data** tab,

**To add more data fields to the dataset**

Select the fields in the **Available Resource** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif) to add them to the dataset. You can also select a field and drag it to the **Dataset Resources** box.

**To remove an unnecessary data field from the dataset**

Select the field in the **Dataset Resources** box and select **Remove**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif). You can only remove the fields which are not used by any data component created on the dataset, either directly or indirectly. To remove all the data fields in a dataset, select **Remove All**![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4420556095639/btn_rmvall.gif), however, when you select the button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can find that the data fields used by data components that apply the dataset still display in the Dataset box.

### Filtering Data Fields in a Dataset

1. In the Dataset List box, select the dataset you want to filter.
2. Select the **Filter** tab.
3. If the dataset is created on a business view, Designer displays the **Filter** drop-down list, which contains all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply to the dataset, or select **User Defined** in the list to define a new filter.
4. Add the filter conditions. Based on the data resource type from which the dataset is created, a business view or a query resource, the way to create a filter for the dataset varies.

   If the dataset is created on a business view, you can add filter condition for it in the same way as you [add conditions for a predefined filter in the business view](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#AddCondition).

   **To add filter conditions for a dataset created from a query resource**

   1. Select **Add Condition** to add a condition line.

      ![Filter Query Based Dataset](https://devnet.logianalytics.com/hc/article_attachments/4420542084759/dtset_fltr.gif)
   2. From the field drop-down list, select the field to be filtered. The field can be any DBField in the query resource, or a parameter or valid formula of these DBFields in the same catalog data source as the query resource.
   3. From the operator drop-down list, select the operator with which to compose the filter expression.
   4. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to specify the value of how to filter the field in the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664472599-Expressions-Dialog-Box) or type the value in the value text box manually. You can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" or a parameter to filter the dataset dynamically. For the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661801239-Parameter-Application-Cases#FilterQuery).

      When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

      You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
   5. Repeat the preceding steps to add more condition lines and define the logic relationship between the condition lines: "And" or "Or".

      To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select **Up** or **Down**; to delete a condition line, select it and select **Delete**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* A dataset is created based on another data resource and the data resource itself can also be applied with a filter. You may want to know the differences between the filters. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Filter) for more information.
* You can also add/remove the data fields in a dataset or filter a dataset while creating a data component using a query resource with the component wizard. To do this, select **More Options** and select **Existing Dataset** in the Data screen of the wizard, then select an existing dataset and select **Edit**. In the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), edit the dataset as required.
* You can also filter a dataset created from a query resource by selecting the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661502359-Dataset-Filter-Dialog-Box) button ![](https://devnet.logianalytics.com/hc/article_attachments/4420556086295/btn_filter.gif) on the toolbar of the Data panel.
* You cannot filter the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.

### Optimizing a Dataset

You can enlarge or decrease the scope of retrieved data for a dataset, and therefore make a balanceable decision between better performance and special usage cases/demands. However, you cannot apply this feature to datasets created from business views; for these datasets, you can use the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/4405664618903-Business-View-Properties#Prefetch) property on the business views for similar purpose.

1. In the Dataset List box, select the dataset that you want to optimize.
2. Select **Optimize Dataset**. Designer displays the Optimize Dataset dialog box.

   ![Optimize Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542085015/dtset_optmz.gif)
3. Choose a retrieved data scope for the dataset.
   * **Only Columns Used in Report**  
     Select it if you only want to retrieve data columns used in the current report at runtime. This way ensures the best performance since the least data is retrieved. This is always the default for page reports.
   * **All Columns in Dataset**  
     Select it if you want to retrieve all data columns defined in the dataset at runtime. Unless you [manually added columns to the dataset](#Add), this is the same as Only Columns Used in Report.
   * **All Columns in Query**  
     Select it if you want to retrieve all data columns in the query on which the dataset is based at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more columns to the report.
4. Select **OK** to optimize the dataset.

### Renaming a Dataset

1. In the Dataset List box, select the dataset that you want to modify.
2. Double-click in the **Name** text box of the dataset.
3. Type a new name in the text box and select **Enter** on the keyboard to apply the change.

### Removing a Dataset

1. In the Dataset List box, select the dataset that you want to remove.
2. Select **Remove**.
3. Select **Yes** in the prompted message box to confirm the removal.

   You cannot remove any dataset that is used by a data component; if you want to do this, you need to first remove the data component which references this dataset.

## Setting Properties of the Datasets in a Report

Each dataset in a query-based page report and library component has its own node in the Report Inspector. You can edit the properties there to make the dataset better serve the data components using it.

**To edit properties of a dataset in a report**

1. In the Report Inspector, select the name of the dataset under the **Datasets** node for a page report or **Data Source** node for a library component.

   ![Datasets in Report Inspector](https://devnet.logianalytics.com/hc/article_attachments/4420550840087/dtset_prpty.gif)
2. In the **Properties** sheet, edit the [properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664656919-Dataset-Properties) of the dataset as required.

   For example, you can apply a [cached query result file](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results) to the dataset, specify the data buffer size for the dataset to improve performance, and apply [Record Level Security](https://devnet.logianalytics.com/hc/en-us/articles/4405661343639-Applying-RLS-at-Report-Scope) for the data components using the dataset.

## Customizing Field Display Names for Datasets in a Report

For datasets created on query resources in a page report, Designer enables you to customize the display names of the data fields in the datasets, so that when users run the page report in Page Report Studio and perform operations such as Sort and Filter on data components in the page report, they will be able to work with intuitive field names. You can also specify the actions in which the customized display names will participate for each data component in the page report.

**To customize the field display names for datasets in a query-based page report**

1. Open the page report.
2. Navigate to **Report** > **Edit Display Name**. Designer displays the [Edit Display Name dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661508887-Edit-Display-Name-Dialog-Box).

   ![Edit Display Name dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556108951/edtdsplynm.gif)
3. From the **Report Dataset** drop-down list, which contains all datasets used in the page report, select a dataset and Designer displays all the data fields in the dataset in the mapping name box.
4. To make the resource names sort automatically, select **Auto Sort**.
5. Specify the display names for the data fields in the **Display Name** column. You can also select a formula as the display name of the data field.
6. Select another dataset and repeat the preceding steps to edit the display names of data fields in it.
7. You can select **Advanced** to further customize the display names for data components in the page report using the [Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664457879-Edit-Display-Name-for-Component-Dialog-Box).

   ![Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542085911/edtdsplynmcmpnt.gif)
8. From the **Component** drop-down list, select the data component in the page report that you want to customize.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You can also right-click a data component that uses a query resource in a page report and then select **Edit Display Name** from the shortcut menu to display the Edit Display Name for Component dialog box (if you open the dialog box in this way, Designer only lists the component that you right-click on in the Component drop-down list).
9. In the action columns, select the corresponding checkboxes to indicate whether the actions are enabled for the data fields. Select the checkbox on the action column header if you want the corresponding action to be enabled for all data fields. If any action is not supported on the selected data component, Designer disables the corresponding column.

   When you select an action for a data field, the field's display name instead of mapping name will be shown in the corresponding dialog box or submenu in Page Report Studio. If you clear the box for any field in any action column, the field will not be available for the action. Moreover, if you set the display name of any field to be blank in the Edit Display Name dialog box, all actions will be disabled for the field, which means users will not be able to perform all these actions on the field in Page Report Studio.
10. Select **OK** to accept the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you set the display name of any data field to be blank, the field will not be shown in the lists where display names are used in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664689687-Designing-Your-Reports)
