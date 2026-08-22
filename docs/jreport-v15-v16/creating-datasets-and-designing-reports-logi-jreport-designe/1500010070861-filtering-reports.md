---
title: "Filtering Reports"
id: 1500010070861
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports
updated_at: 2021-07-24T10:37:44Z
---

# Filtering Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports)

# Filtering Reports

To filter the data shown in a report, you can make use of the following filters:

* [Query filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#FilterQuery) (including filter on [SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010064341-Imported-SQL-Files) and filter on [APE](https://devnet.logianalytics.com/hc/en-us/articles/1500010064441-Imported-APEs)), which applies to all data components that use the query.
* [Dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets), which applies to the data components that use the dataset in the current report.
* Local filter on individual data component (Chart, Table, Crosstab, Banded Object, Geographic Map and KPI) defined via the report wizard or [using the Edit Filter dialog](#EditFilter). It applies to this individual data component and does not affect other components that use the same dataset.
* On-screen filter, that is the filter created via a [filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Filter). It applies to the data components that use the same data source as the filter control in the current report.

Dataset filters are passed along to the Query Engine the same as query filters. The two levels of filters are much more efficient since only the filtered data is returned to Logi JReport. Local filters on individual components are not passed to the Query Engine so all data is returned to Logi JReport and the component filters out the unnecessary data. This may be very inefficient so always use dataset filters or query filters whenever possible. However if you are using stored procedures, web services and other data sources, Logi JReport may not be able to pass the filter to the Query Engine.

The advantage of using a dataset filter instead of a query filter is that it only affects data components that use the dataset in the current report. It still passes the filter to the database but does not change the catalog thus does not affect any other reports.

For data share concern, local filters most often cannot be pushed down to the database even though the [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500010069181-JDBC-Hive-Connection-Properties#PushDown) feature is enabled, thus all data is returned and Logi JReport filters the data locally which will use a lot more computer resources. To get better performance, it is better to define the filter at the other two levels.

**To apply a local filter in a report using the Edit Filter dialog:**

1. Right-click a data component in the report to which the filter will be applied and select **Format Filter** to display the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

   ![Edit Filer](https://devnet.logianalytics.com/hc/article_attachments/4404909126551/edtfltr.gif)
2. If the data component is created using a business view, the Filter drop-down list is available, listing all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   If you have applied a filter to the data component when creating it via the Filter screen of the report wizard, the filter conditions are automatically displayed. You can remove or edit the conditions according to your requirements.
3. Add the filter conditions as required. Based on the data resource type from which the data component is created, a business view or a query resource, the way to format a filter for the data component differs.

   If the data component is created using a business view, you can add filter condition for it in the same way as you [add conditions for a predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#AddCondition) in the business view. Besides, you can use  [a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param)  as the value of a filter condition if needed.

   **To add filter conditions for a data component created using a query resource:**

   1. Select the **Add Condition** button to add a condition line.

      ![Filter Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4404901134871/rpt_fltr.gif)
   2. From the field drop-down list, select the field to be filtered. All the DBFields in the query resource the data component uses, as well as the parameters and valid formulas of these DBFields in the same catalog data source as the query resource are listed in the drop-down list. You can select any field to filter.
   3. From the operator drop-down list, set the operator with which to compose the filter expression.
   4. From the value drop-down list, select the value or values of how to filter the field depending on the selected operator.

      You can also type in the values manually in the text box if you are familiar with the values. Note that if multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
   5. Select **Add Condition** to add more condition lines and define the logic (And or Or) between the condition lines.

      To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

      To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

      To delete a condition line, select it and select the **Delete** button.
4. Select **OK** to create the filter.

   Then when you preview the report, only data satisfying the specified filter conditions are shown in the data component.

**Note:**

* The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.
* If a data component in a page report is created on an HDS, the filter conditions you define in the Edit Filter dialog for the data component will not be applied when the report runs due to the [specialty of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064261-Developing-Reports-from-Hierarchical-Data-Sources). Therefore if you want to apply local filters in such type of data components, you need to make use of the dataset filter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports)
