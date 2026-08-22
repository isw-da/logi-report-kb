---
title: "Filtering Datasets in a Report"
id: 5735555312279
section: "Manipulating Report Datasets - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report
updated_at: 2022-11-02T08:17:40Z
---

# Filtering Datasets in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report)

# Filtering Datasets in a Report

When you filter a dataset in a report, the filter conditions apply to all data components that use the dataset in the report. This topic describes how you can apply a filter to a dataset.

1. Do one of the following to specify the dataset you want to filter:
   * Navigate to **Report** > **Manage Datasets**, then in the [Manage Datasets dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543613335-Manage-Datasets-Dialog-Box), select the dataset in the **Dataset List** box and select the **Filter** tab.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")When working with a page or web report, in the dialog box where you can select to use an existing dataset in the report (for example, the [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565057943-Bind-Data-Dialog-Box), [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box), or the Data screen of the component wizard), select an existing dataset and select **Edit**, then in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box), select the **Filter** tab.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")When working with a page or web report, select a dataset from the dataset drop-down list of the Data panel or select a data component in the report to locate the dataset it applies in the Data panel, then select **Dataset Filter**![Filter button](https://devnet.logianalytics.com/hc/article_attachments/9898405009687/btn_filter.gif) on the toolbar of the panel. Designer displays the [Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508603927-Dataset-Filter-Dialog-Box) for you to define the filter conditions.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")In the component wizard when working with a web report or business view-based page report, select the dataset you want to use for the data component in the Data screen and then select the **Dataset Filter** screen.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")When working with a web report or business view-based page report, right-click a data component in the report and select **Edit Dataset Filter** from the shortcut menu. Designer displays the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522534039-Edit-Dataset-Filter-Dialog-Box) for you to define the filter conditions.

   The following shows a sample dialog box.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/9898475557271/dtset_fltr1.gif)
2. When the dataset is based on a business view, Designer displays the **Filter** drop-down list, which contains all [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply to the dataset, or select **User Defined** in the list to define a new filter.
3. Add the filter conditions. According to the data resource type from which the dataset is created, a business view or a query resource, the way to create a filter for the dataset varies.
   * For a business view-based dataset, you can add filter condition for it in the same way as you [add conditions for a predefined filter in the business view](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Filter). Besides, you can use [a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Param) as the value of a filter condition when editing the filter in the Dataset Filter or Edit Dataset Filter dialog box.
   * To add filter conditions for a query-based dataset:
     1. Select **Add Condition** to add a condition line.

        ![Filter Query Based Dataset](https://devnet.logianalytics.com/hc/article_attachments/9898475564439/dtset_fltr2.gif)
     2. From the field drop-down list, select the field you want to filter. The field can be any DBField in the query resource, or a parameter or valid formula of these DBFields in the same catalog data source as the query resource.
     3. From the operator drop-down list, select the operator with which to compose the filter expression.
     4. Specify the value of how to filter the field
     5. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the value of how to filter the field in the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529359895-Expressions-Dialog-Box) or type the value in the value text box. You can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" or a parameter to filter the dataset dynamically. For the usage of parameters in filter conditions, see the example in [Dynamically Filtering Queries](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#FilterQuery).
        + When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
        + When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
          If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement `Trim(@Field)` that transforms the spaces into empty string, then use the formula to replace the field itself in the condition.
     6. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And" or "Or".
        + To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
        + To take out any condition or group from a group, select it and select **Ungroup**.
        + To adjust the priority of the condition lines, select it and select **Up** or **Down**.
        + To delete a condition line, select it and select **Delete**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot filter the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report)
