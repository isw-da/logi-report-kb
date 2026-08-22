---
title: "Obtaining Detailed Information from a Banded Object"
id: 1500009592841
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object
updated_at: 2021-07-24T05:53:48Z
---

# Obtaining Detailed Information from a Banded Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570922-Configuring-Page-Reports-for-Specific-Page-Report-Studio-Features)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names)

# Obtaining Detailed Information from a Banded Object

In a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects) which contains group information, you may only care about the details in a certain group. To meet your expectation, Logi JReport provides a function: go-to-detail.

Below is a list of the sections covered in this topic:

> * [Going to Detail from a Field/Label/Image](#Field)
> * [Going to Detail from a Map](#Map)
> * [Going to Detail from a Chart](#Chart)

## Going to Detail from a Field/Label/Image

If a banded object contains group information, then a field (DBField, parameter, formula, summary, special field), label, or image in a group header/footer panel of the banded object, including the case that the field, label or image is in a tabular cell or text box which is in the banded object's group header/panel panel, can be used to obtain information of that group. To do this:

1. Open a page report which contains a grouped banded object.
2. Select the object which will be used for going to detail, set its property Go to Detail to **true** in the Report Inspector.
3. Find the property [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009591441-Properties-of-DBField-in-Page-Report#Target), then from its value drop-down list, select the target window or frame in which to display the detailed information.
4. Publish the page report to Logi JReport Server and run it in Page Report Studio.
5. Right-click the object and select **Go to Detail**, then the related group information will be displayed.

## Going to Detail from a Map

A map in a grouped banded object can also be used for going to detail with the following preconditions:

* The map inherits dataset from the banded object.
* The banded object has at least two groups.
* The map is inserted in the group header/footer panel that is not the lowest level group of the banded object.

**To go to detail from a map:**

1. Open a page report which contains a grouped banded object with a map.
2. Select the map, then in the Report Inspector set its property Go to Detail to **true**, from the Detail Target Frame value drop-down list, select the target window or frame in which to display the detailed information.
3. Publish the page report to Logi JReport Server and run it in Page Report Studio.
4. Right-click the map and select **Go to Detail**, then the related group information will be displayed.

## Going to Detail from a Chart

A chart in a banded object can also be used for going to detail, however, some preconditions must be met:

* The value axis of the chart shows summary information.
* The chart inherits dataset from the banded object, and has no data container link with the banded object.
* In the case that FieldA and FieldB are respectively displayed on the series and category axes of the chart, then the two fields must be group fields of the banded objects, and FieldA is one-level higher than FieldB, and the chart must be inserted into the header/footer panel of the group which is one-level higher than FieldA (if FieldA is the highest group level in the banded object, then the chart should be inserted into the banded header/footer panel). In the case that the chart only shows FieldB as category information (no series axis), then FieldB must be a group field of the banded object, and the chart must be inserted into the header/footer panel of the group which is one-level higher than FieldB, or the banded header/footer panel if FieldB is the highest level.

The following example shows how to obtain detailed information from a chart:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query WorldWideSales in Data Source 1 of the catalog. The banded object displays the following fields: the DBFields Product Name, Unit Price, Discount and Quantity and the formula Total, is grouped by Country, State and Category (Country is the highest level and Category the lowest), and applies the Classic style.
3. In the Data panel, select **<New Summary...>** from the Summaries node and create a summary named Sum\_Total, which uses the function Sum, sums on the formula Total, and applies to the Category group level, then drag the summary to the footer panel of the Category group level in the banded object.
4. [Insert a Bar 3-D chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart) into the header panel of the Country group level. The chart inherits the dataset from the banded object (make sure to check the **Current** radio button in the Data screen of the Create Chart wizard), and displays Category on the category axis, State on the series axis and Sum\_Total on the value axis.
5. In the Report Inspector, select the node that represents the chart from the resource tree and set its Go to Detail property to **true**.
6. Save the report and select **View** > **Preview As** > **Page Report Result** to preview it in Page Report Studio.
7. Turn to page around 24 to view records in the USA country.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893809815/rpt_pgrpt_dhtml_detail1.gif)
8. Now point to the bar of State=CA and Category=Bold, the mouse pointer will become a hand. Select the bar and the result will be regenerated.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893810071/rpt_pgrpt_dhtml_detail2.gif)
9. If you select a label on the category axis of the chart, you will go to detailed information concerned with the product category represented by that label; if you select a series axis label, detailed information about the state indicated by the label will be displayed.

**Notes:**

* The Go to Detail property is enabled by default for summaries on the group header/footer panel of a banded object. This is the same case when the formulas on the group header/footer panel of a banded object are group level formulas.
* Go-to-detail from a summary or group level formula in a banded object can also be performed in view mode in Logi JReport Designer, and in HTML/PDF report outputs.
* For a chart, its Hyperlink, X Hyperlink, and Z Hyperlink properties allow you to set a URL for the graphic objects (such as bars, benches, and so on), category axis labels, and series axis labels respectively. If you have set any of the three properties, the corresponding object will no longer support the go-to-detail function in Page Report Studio, and selecting it will go to the URL. If Interactive is set to true and you have set Hyperlink, X Hyperlink, and/or Z Hyperlink, double-clicking the corresponding part of the chart will go to the URL you set.
* If there is no other actions bound on the object which is enabled with the go-to-detail action, you can also directly select the object to get the detail information at runtime. If there is other actions bound on the object, you can select the object to obtain the detail information only when the go-to-detail action is specified with the highest [click priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Priority).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570922-Configuring-Page-Reports-for-Specific-Page-Report-Studio-Features)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names)
