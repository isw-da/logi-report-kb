---
title: "Obtaining Detailed Information from a Banded Object"
id: 1500009605442
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605442-Obtaining-Detailed-Information-from-a-Banded-Object
updated_at: 2021-07-24T16:05:24Z
---

# Obtaining Detailed Information from a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605462-Embedding-Data-Components-in-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects)

# Obtaining Detailed Information from a Banded Object

In a banded object which contains group information, you may only care about the details in a certain group. To meet your expectation, Logi Report provides a function: go-to-detail. It applies to banded objects in page reports created using query resource.

This topic includes the following sections:

* [Going to Detail from a Field/Label/Image](#Field)
* [Going to Detail from a Map](#Map)
* [Going to Detail from a Chart](#Chart)

## Going to Detail from a Field/Label/Image

If a banded object contains group information, then a field (DBField, parameter, formula, summary, special field), label, or image in a group header/footer panel of the banded object, including the case that the field, label or image is in a tabular cell or text box which is in the banded object's group header/panel panel, can be used to obtain information of that group. To do this:

1. Open a page report which contains a grouped banded object.
2. Select the object which will be used for going to detail, set its property Go to Detail to **true** in the Report Inspector.
3. Find the property [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties#Target), then from its value drop-down list, select the target window or frame in which to display the detailed information.
4. Publish the page report to Logi Report Server and run it in Page Report Studio.
5. Right-click the object and select **Go to Detail**, then the related group information will be displayed.

## Going to Detail from a Map

A map in a grouped banded object can also be used for going to detail with the following preconditions:

* The map inherits dataset from the banded object.
* The banded object has at least two groups.
* The map is inserted in the group header/footer panel that is not the lowest level group of the banded object.

**To go to detail from a map:**

1. Open a page report which contains a grouped banded object with a map.
2. Select the map, then in the Report Inspector set its property Go to Detail to **true**, from the Detail Target Frame value drop-down list, select the target window or frame in which to display the detailed information.
3. Publish the page report to Logi Report Server and run it in Page Report Studio.
4. Right-click the map and select **Go to Detail**, then the related group information will be displayed.

## Going to Detail from a Chart

A chart in a banded object that is created using query resource can also be used for going to detail, however, some preconditions must be met:

* The value axis of the chart shows summary information.
* The chart inherits dataset from the banded object and has no data container link with the banded object.
* In the case that FieldA and FieldB are respectively displayed on the series and category axes of the chart, then the two fields must be group fields of the banded objects, and FieldA is one-level higher than FieldB, and the chart must be inserted into the header/footer panel of the group which is one-level higher than FieldA (if FieldA is the highest group level in the banded object, then the chart should be inserted into the banded header/footer panel). In the case that the chart only shows FieldB as category information (no series axis), then FieldB must be a group field of the banded object, and the chart must be inserted into the header/footer panel of the group which is one-level higher than FieldB, or the banded header/footer panel if FieldB is the highest level.

The following example shows how to obtain detailed information from a chart:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) based on the query WorldWideSales in Data Source 1 of the catalog. The banded object displays the following detail fields: the DBFields Product Name, Unit Price, Discount and Quantity and the formula Total, is grouped by Country, State and Category (Country is the highest level and Category the lowest), and applies the Classic style.
3. In the Data panel, select **<New Summary...>** from the Summaries node and create a summary named Sum\_Total, which uses the function Sum, sums on the formula Total, and applies to the Category group level, then drag the summary to the footer panel of the Category group level in the banded object.
4. [Insert a Bar 3-D chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report) into the header panel of the Country group level. The chart inherits the dataset from the banded object (make sure to select the **Current Dataset** radio button in the Data screen of the Create Chart wizard), and displays Category on the category axis, State on the series axis and Sum\_Total on the value axis.
5. In the Report Inspector, select the node that represents the chart from the resource tree and set its Go to Detail property to **true**.
6. Save the report and select **View** > **Preview As** > **Page Report Result** to preview it in Page Report Studio.
7. Turn to page around 24 to view records in the USA country.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404904470039/cmpnt_bdobj_detail1.gif)
8. Now point to the bar of State=CA and Category=Bold, the mouse pointer will become a hand. Select the bar and the result will be regenerated.

   ![Result of State=CA and Category=Bold](https://devnet.logianalytics.com/hc/article_attachments/4404904470295/cmpnt_bdobj_detail2.gif)
9. If you select a label on the category axis of the chart, you will go to detailed information concerned with the product category represented by that label; if you select a series axis label, detailed information about the state indicated by the label will be displayed.

**Notes:**

* The Go to Detail property is enabled by default for summaries on the group header/footer panel of a banded object. This is the same case when the formulas on the group header/footer panel of a banded object are group level formulas.
* Go-to-detail from a summary or group level formula in a banded object can also be performed in view mode in Logi Report Designer, and in HTML/PDF report outputs.
* For a chart, its Hyperlink, X Hyperlink, and Z Hyperlink properties allow you to set a URL for the graphic objects (such as bars, benches, and so on), category axis labels, and series axis labels respectively. If you have set any of the three properties, the corresponding object will no longer support the go-to-detail function in Page Report Studio, and selecting it will go to the URL. If Interactive is set to true and you have set Hyperlink, X Hyperlink, and/or Z Hyperlink, double-clicking the corresponding part of the chart will go to the URL you set.
* If there is no other actions bound on the object which is enabled with the go-to-detail action, you can also directly select the object to get the detail information at runtime. If there is other actions bound on the object, you can select the object to obtain the detail information only when the go-to-detail action is specified with the highest [Select priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Priority).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605462-Embedding-Data-Components-in-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects)
