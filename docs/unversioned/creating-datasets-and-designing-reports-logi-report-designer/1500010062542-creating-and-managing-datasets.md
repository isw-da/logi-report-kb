---
title: "Creating and Managing Datasets"
id: 1500010062542
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets
updated_at: 2021-07-23T19:16:45Z
---

# Creating and Managing Datasets

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062742-Designing-Your-Reports)

# Creating and Managing Datasets

A dataset is the set of data built from the result of a data resource: [query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries), [stored procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures), [imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs), [imported APE](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs), [user-defined data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources), [hierarchical data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010057602-Using-Hierarchical-Data-Sources), or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views), and can optionally have filters applied to it. A dataset built on data resource other than a business view can contain all the DBFields in the data resource, as well as the parameters and valid formulas of these DBFields in the same catalog data source as the data resource; a dataset created from a business view can contain only view elements and dynamic resources. When you create a [data component](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports) in a report, you can select the data resource to create a new dataset from it or use an existing dataset in the report. This topic describes how you can create and manage the datasets in a report.

This topic contains the following sections:

* [Creating Datasets in a Report](#Create)
* [Managing the Datasets in a Report](#Manage)
* [Setting Properties of the Datasets in a Report](#Property)
* [Customizing Field Display Names for Datasets in a Report](#Customize)

## Creating Datasets in a Report

You have the following methods to create datasets in a report:

* **Creating a dataset from the report wizard** 

  When you create a data component by selecting a data resource in the report wizard, Designer creates a dataset at the same time, either empty or containing some data fields, depending on whether you add data fields to the data component.
* **Creating a dataset via the Data panel** 
  (you can use this method for query-based page reports only)
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010101501-Data-Panel), choose **<Choose Data from...>** from the dataset drop-down list.

     ![Create Dataset from Data Panel](https://devnet.logianalytics.com/hc/article_attachments/4404848437143/dtset_crt.gif)

     Designer displays the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

     ![New Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848437527/nwdtst.gif)
  2. Select the data resource in the current catalog on which to create the dataset. If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use.
  3. In the **New Dataset Name** text box, type the name of the dataset.
  4. Select **OK**. Designer creates an empty dataset.
* [Creating a dataset from the Manage Datasets dialog box](#CrtMng)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You are recommended to make different data components in the same report share the datasets in the report whenever possible, which will have a dramatic effect on the performance of your reports in the runtime environment. This is because each dataset is created by running a query against the database, and that is the most expensive part of running a report in terms of execution time. Even when two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
* If you create a dataset on a hierarchical data source, when you use the dataset to create data components, you need to pay attention to the [unique features of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010095141-Developing-Reports-from-Hierarchical-Data-Sources).

## Managing the Datasets in a Report

You can manage the datasets in a report with the [Manage Datasets dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059762-Manage-Datasets-Dialog-Box), for example, you can add more data fields to the datasets, filter the datasets, rename the datasets, and so on; however, Designer supports this feature only for query-based page reports and library components.

To manage the datasets in a report, [open the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010062782-Opening-Reports), then select **Report** > **Manage Datasets** to display the Manage Datasets dialog box.

![Manage Datasets dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848438039/mngdtst.gif)

You can manage the datasets in a report as follows:

* **Creating a dataset**
  1. Select the **New** button (Designer enables the button for query-based page reports only).
  2. In the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box), select the data resource in the current catalog on which to create the dataset. If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use.
  3. In the **New Dataset Name** text box, type the name of the dataset.
  4. Select **OK**. Designer creates an empty dataset.
  5. Add data fields to the dataset as shown below.
* **Adding/Removing data fields in a dataset**  
  For any dataset, Designer automatically adds fields to it when you add fields to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components, therefore, there generally is no need to ever add or remove fields from a dataset specifically. However, in the Manage Datasets dialog box, you can still manually add or remove data fields from a dataset. To do this, in the **Dataset List** box, select the dataset you want to edit, then in the **Data** tab:
  + To add more data fields to the dataset, from the **Available Resource** box, select the fields from the source on which the dataset is created and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the dataset. You can also select a field and drag and drop it into the **Dataset** box.
  + To remove an unnecessary data field from the dataset, select it in the Dataset box and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif). You can only remove the fields which are not used by any data component created on the dataset, either directly or indirectly. To remove all the data fields in a dataset, select the **Remove All** button ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404848392215/btn_rmvall.gif), however, when you select the button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can find that the data fields used by data components created on the dataset still display in the Dataset box.
  + Use the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to adjust the order of the added fields in the Dataset box.
* **Filtering data fields in a dataset**
  1. In the Dataset List box, select the dataset you want to filter.
  2. Select the **Filter** tab.
  3. If the dataset is created on a business view, Designer displays the **Filter** drop-down list, which contains all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply to the dataset, or select **User Defined** in the list to define a new filter.
  4. Add the filter conditions. Based on the data resource type from which the dataset is created, a business view or a query resource, the way to create a filter for the dataset varies.

     If the dataset is created on a business view, you can add filter condition for it in the same way as you [add conditions for a predefined filter in the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#AddCondition).

     **To add filter conditions for a dataset created from a query resource:**

     1. Select the **Add Condition** button to add a condition line.

        ![Filter Query Based Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404848438295/dtset_fltr.gif)
     2. From the field drop-down list, select the field to be filtered. The field can be any DBField in the query resource, or a parameter or valid formula of these DBFields in the same catalog data source as the query resource.
     3. From the operator drop-down list, select the operator with which to compose the filter expression.
     4. Select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to specify the value of how to filter the field in the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058942-Expressions-Dialog-Box) or type the value in the value text box manually. You can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" or a parameter to filter the dataset dynamically. For the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#FilterQuery).

        When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

        You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
     5. Repeat the above steps to add more condition lines and define the logic relationship between the condition lines: "And" or "Or".

        To group some condition lines, select them and select the **Group** button, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select the **Up** or **Down** button; to delete a condition line, select it and select the **Delete** button.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

  + A dataset is created based on another data resource and the data resource itself can also be applied with a filter. You may want to know the differences between the filters. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Filter) for more information.
  + You can also add/remove the data fields in a dataset or filter a dataset while creating a data component using a query resource with the report wizard. To do this, select the **More Options** button and select the **Existing Dataset** radio button in the Data screen of the wizard, then select an existing dataset and select the **Edit** button. In the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), edit the dataset as required.
  + You can also filter a dataset created from a query resource by selecting the [Dataset Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010058642-Dataset-Filter-Dialog-Box) button ![](https://devnet.logianalytics.com/hc/article_attachments/4404856803479/btn_filter.gif) on the toolbar of the Data panel.
  + You cannot filter the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.
* **Optimizing a dataset**  
  You can enlarge or decrease the scope of retrieved data for a dataset, and therefore make a balanceable decision between better performance and special usage cases/demands. However, you cannot apply this feature to datasets created from business views; for these datasets, you can make use of the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500010099841-Business-View-Properties#Prefetch) property on the business views for similar purpose.
  1. In the Dataset List box, select the dataset that you want to optimize.
  2. Select the **Optimize Dataset** button. Designer displays the Optimize Dataset dialog box.

     ![Optimize Dataset dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848438807/dtset_optmz.gif)
  3. Choose a retrieved data scope for the dataset.
     + **Only Columns Used in Report**  
       Select it if you only want to retrieve data columns used in the current report at runtime. This way ensures the best performance since the least data is retrieved. This is always the default for page reports.
     + **All Columns in Dataset**  
       Select it if you want to retrieve all data columns defined in the dataset at runtime. Unless you [manually added columns to the dataset](#Add), this is the same as Only Columns Used in Report.
     + **All Columns in Query**  
       Select it if you want to retrieve all data columns in the query on which the dataset is based at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more columns to the report.
  4. Select **OK** to optimize the dataset.
* **Renaming a dataset**
  1. In the Dataset List box, select the dataset that you want to modify.
  2. Double-click in the **Name** text box of the dataset.
  3. Type a new name in the text box and press **Enter** to apply the changes.
* **Removing a dataset**
  1. In the Dataset List box, select the dataset that you want to remove.
  2. Select the **Remove** button.
  3. Select **Yes** in the prompted message box to confirm the removal.

     You cannot remove any dataset that is used by a data component; if you want to do this, you need to first remove the data component which references this dataset.

## Setting Properties of the Datasets in a Report

Each dataset in a query-based page report and library component has its own node in the Report Inspector. You can edit the properties there to make the dataset better serve the data components created on it.

**To edit properties of a dataset in a report:**

1. In the Report Inspector, select the name of the dataset under the **Datasets** node for a page report or **Data Source** node for a library component.

   ![Datasets in Report Inspector](https://devnet.logianalytics.com/hc/article_attachments/4404848439191/dtset_prpty.gif)
2. In the **Properties** sheet, edit the [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010062082-Dataset-Properties) of the dataset as required.

   For example, you can apply a [cached query result file](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results) to the dataset, specify the data buffer size for the dataset to improve performance, and apply [Record Level Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094241-Applying-RLS-at-Report-Scope) for the data components using the dataset.

## Customizing Field Display Names for Datasets in a Report

For datasets created on query resources in a page report, Designer enables you to customize the display names of the data fields in the datasets, so that when the report users run the page report in Page Report Studio and perform operations such as Sort and Filter on data components in the page report, they will be able to work with intuitive field names. You can also specify the actions in which the customized display names will participate for each data component in the page report.

1. Open the query-based page report.
2. Select **Report** > **Edit Display Name**. Designer displays the [Edit Display Name dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096221-Edit-Display-Name-Dialog-Box).

   ![Edit Display Name](https://devnet.logianalytics.com/hc/article_attachments/4404848439447/edtdsplynm.gif)
3. From the **Report Dataset** drop-down list, which contains all datasets used in the page report, select a dataset and Designer displays all the data fields in the dataset in the mapping name box.
4. To make the resource names sort automatically, select the **Auto Sort** checkbox.
5. Specify the display names for the data fields in the **Display Name** column. You can also select a formula as the display name of the data field.
6. Select another dataset and repeat the above steps to edit the display names of data fields in it.
7. You can select the **Advanced** button to further customize the display names for data components in the page report using the [Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096241-Edit-Display-Name-for-Component-Dialog-Box).

   ![Edit Display Name for Component](https://devnet.logianalytics.com/hc/article_attachments/4404856849431/edtdsplynmcmpnt.gif)
8. From the **Component** drop-down list, select the data component in the page report that you want to customize.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can also right-click a data component that uses a query resource in a page report and then select **Edit Display Name** from the shortcut menu to display the Edit Display Name for Component dialog box (if you open the dialog box in this way, Designer only lists the component that you right-click on in the Component drop-down list).
9. In the action columns, select the corresponding checkboxes to indicate whether the actions are enabled for the data fields. Select the checkbox on the action column header if you want the corresponding action to be enabled for all data fields. If any action is not supported on the selected data component, Designer disables the corresponding column.

   When you select an action for a data field, the field's display name instead of mapping name will be shown in the corresponding dialog box or submenu in Page Report Studio. If you clear the box for any field in any action column, the field will not be available for the action. Moreover, if you set the display name of any field to be blank in the Edit Display Name dialog box, all actions will be disabled for the field, which means the report users will not be able to perform all these actions on the field in Page Report Studio.
10. Select **OK** to accept the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you set the display name of any data field to be blank, the field will not be shown in the lists where display names are used in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062742-Designing-Your-Reports)
