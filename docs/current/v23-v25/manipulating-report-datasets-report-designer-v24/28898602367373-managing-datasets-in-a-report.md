---
title: "Managing Datasets in a Report"
id: 28898602367373
section: "Manipulating Report Datasets - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898602367373-Managing-Datasets-in-a-Report
updated_at: 2024-09-30T09:13:16Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Managing Datasets in a Report

This topic describes how you can manage the datasets that a report applies, for example, create more datasets in the report, specify the data fields to include in the datasets, and filter the datasets.

This topic contains the following sections:

- Creating a Dataset

- Adding/Removing Data Fields in a Dataset

- Filtering a Dataset 

- Optimizing a Dataset

- Renaming a Dataset 

- Removing a Dataset        

To manage the datasets in a report, open the report, then navigate to Report > Manage Datasets to display the Manage Datasets dialog box.

## 
Creating a Dataset

 When you bind data to the report body or specify the data resource you want to use for a data component, you create a dataset implicitly in the corresponding report. In the Manage Dataset dialog box, you can also create datasets explicitly in a report so you can use them directly in the report.

- Select New (Designer disables this button for library components). Designer displays the New Dataset dialog box. 

- From the data source drop-down list, select the catalog data source that contains the data you need.

- Designer displays the data resources you have added in the specified catalog data source  in the resource box. Select the data resource on which to create the dataset. You can also select the first item in a resource node to create a data resource of the type to use for the dataset.  When you select to add a new stored procedure or imported SQL for the dataset,

- If the specified catalog data source contains only one connection other than the JDBC connection, Designer displays the Get JDBC Connection dialog box for you to set up the JDBC connection first.

- If the specified catalog data source contains more than one connection, Designer displays the Choose JDBC Connection dialog box for you to select the JDBC connection in the data source, via which you want to add the  stored procedure or imported SQL. You can also select <Add JDBC Connection...> in the dialog box to create a JDBC connection and then add the stored procedure or imported SQL from the new connection.

- In the New Dataset Name text box, type the name of the dataset.

- Select OK to create the dataset based on the specified data resource.

- Add the data fields you want to include in the dataset as shown in the next section.

## 
Adding/Removing Data Fields in a Dataset

For any dataset, Designer automatically adds fields to it when you add fields to the data components that use the dataset, and removes the fields from the dataset once you remove them from the data components; therefore,  there generally is no need to ever add or remove fields from a dataset specifically. However, you can still manually add or remove data fields from a dataset if you want. To do this, in the Dataset List box, select the dataset you want to edit, then in the Data tab,

To add more data fields to the dataset

Select the fields in the Available Resource box and select Add to add them to the dataset. You can also select a field and drag it to the Dataset Resources box. 

- A dataset built on a query data resource can contain all DBFields in the data resource, and the parameters and valid formulas of these DBFields in the same catalog data source.

- A dataset created from a business view can contain view elements and dynamic resources  of the business view.
            

To remove an unnecessary data field from the dataset

Select the field in the Dataset Resources box and select Remove. You can only remove the fields that are not used by any data component applying this dataset, either directly or indirectly. To remove all the data fields in a dataset, select Remove All, however, when you select the button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can find that the data fields used by data components that apply the dataset still display in the Dataset box.

## 
Filtering a Dataset

- In the Dataset List box, select the dataset you want to filter.

- Select the Filter tab.

- 
Define the filter conditions.

## 
Optimizing a Dataset

You can increase or decrease the scope of retrieved data for a dataset in a page or web report, and therefore make a balanceable decision between better performance and special usage cases/demands.

 You cannot apply the Optimize Dataset feature to datasets in a library component. For these datasets, you can use the Prefetch property on the business views for similar purpose.
  

- In the Dataset List box, select the dataset that you want to optimize.

- Select Optimize Dataset. Designer displays the Optimize Dataset dialog box.
      

- Choose a retrieved data scope for the dataset.
      
- 
Only Columns Used in Report
Select it if you only want to retrieve data resources used in the current report at runtime. This way ensures the best performance since the least data is retrieved. This is always the default. 

- 
All Columns in Dataset
Select it if you want to retrieve all data resources defined in the dataset at runtime. Unless you manually added data fields to the dataset, this is the same as Only Columns Used in Report. 

- 
All Columns in Query
Select it if you want to retrieve all data resources in the query on which the dataset is based  at runtime. This usually leads to lower performance and is not of any benefit unless you expect the users to often need to add more fields to the report.

When the dataset is based on a business view, the option names are Only Resources Used in Report, All Resources in Dataset, and All Resources in Business View respectively. 

- Select OK to optimize the dataset. 

## 
Renaming a Dataset

- In the Dataset List box, select the dataset that you want to modify.

- Double-click in the Name text box of the dataset.

- Type a new name in the text box and select Enter on the keyboard to apply the change.

## 
Removing a Dataset

- In the Dataset List box, select the dataset that you want to remove.

- Select Remove.

- Select Yes in the prompted message box to confirm the removal.

 You cannot remove any dataset that is used by a data component. If you want to do this, you need to  first remove the data component which references this dataset.

Previous Topic  Next Topic
