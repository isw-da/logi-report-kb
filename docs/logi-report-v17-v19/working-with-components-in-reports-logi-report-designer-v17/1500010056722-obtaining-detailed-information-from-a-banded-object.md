---
title: "Obtaining Detailed Information from a Banded Object"
id: 1500010056722
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object
updated_at: 2021-07-23T19:14:35Z
---

# Obtaining Detailed Information from a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056742-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects)

# Obtaining Detailed Information from a Banded Object

In a banded object which contains group information, you may only care about the details in a certain group. To meet your expectation, Logi Report provides the Go to Detail feature. This topic describes how you can enable the Go to Detail feature on different objects in the group panels of a banded object to get the details of the groups.

You can obtain group details for banded objects in page reports that use query resource only.

This topic contains the following sections:

* [Going to Detail from a Field/Label/Image](#Field)
* [Going to Detail from a Map](#Map)
* [Going to Detail from a Chart](#Chart)

## Going to Detail from a Field/Label/Image

If a banded object contains group information, you can use a field (DBField, parameter, formula, summary, special field), label, or image in a group header/footer panel of the banded object, including the case that the field, label, or image is in a tabular cell or text box which is in the banded object's group header/panel panel, to obtain information of that group. To do this:

1. Open a page report which contains a grouped banded object.
2. Select the object which you want to use for going to detail, set its property **Go to Detail** to **true** in the Report Inspector.
3. Find the property [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#Target), then from its value drop-down list, select the target window or frame in which to display the detailed information.
4. Publish the page report to Server and run it in Page Report Studio.
5. Right-click the object and select **Go to Detail**, you can then get the related group information.

## Going to Detail from a Map

You can use a map in a grouped banded object to obtain detailed information with the following preconditions:

* The map inherits dataset from the banded object.
* The banded object has at least two groups.
* The map is in the group header/footer panel that is not the lowest level group of the banded object.

**To go to detail from a map:**

1. Open a page report which contains a grouped banded object with a map.
2. Select the map, then in the Report Inspector set its property **Go to Detail** to **true**, from the **Detail Target Frame** value drop-down list, select the target window or frame in which to display the detailed information.
3. Publish the page report to Server and run it in Page Report Studio.
4. Right-click the map and select **Go to Detail**, you can then get the related group information.

## Going to Detail from a Chart

You can also use a chart in a banded object for going to detail, however, some preconditions must be met:

* The value axis of the chart shows summary information.
* The chart inherits dataset from the banded object and has no data container link with the banded object.
* In the case that FieldA and FieldB are respectively displayed on the series and category axes of the chart, then the two fields must be group fields of the banded objects, and FieldA is one-level higher than FieldB, and the chart must be in the header/footer panel of the group which is one-level higher than FieldA (if FieldA is the highest group level in the banded object, then the chart should be in the banded header/footer panel). In the case that the chart only shows FieldB as category information (no series axis), then FieldB must be a group field of the banded object, and the chart must be in the header/footer panel of the group which is one-level higher than FieldB, or the banded header/footer panel if FieldB is the highest level.

The following example shows how to obtain detailed information from a chart:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) based on the **WorldWideSales** query in Data Source 1 as follows: add the following detail fields to display: the DBFields **Product Name**, **Unit Price**, **Discount**, and **Quantity**, and the formula **Total**; group the banded object by **Country**, **State**, and **Category** (Country is the highest level and Category the lowest), and apply the **Classic** style.
3. In the **Data** panel, select **<New Summary...>** from the **Summaries** node and create a summary named "Sum\_Total", which uses the function **Sum**, sums on the formula **Total**, and applies to the **Category** group level, then drag the summary to the footer panel of the **Category** group level in the banded object.
4. [Insert a Bar 3-D chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report) into the header panel of the **Country** group level. The chart inherits the dataset from the banded object (make sure to select the **Current Dataset** radio button in the Data screen of the Create Chart wizard), and displays **Category** on the category axis, **State** on the series axis, and **Sum\_Total** on the value axis.
5. In the Report Inspector, select the node that represents the chart from the resource tree and set its **Go to Detail** property to **true**.
6. Save the report and select **View** > **Preview As** > **Page Report Result** to preview it in Page Report Studio.
7. Turn to page around 24 to view records in the USA country.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404848698647/cmpnt_bdobj_detail1.gif)
8. Now point to the bar of "State=CA" and "Category=Bold", the mouse pointer becomes a hand. Select the bar and Page Report Studio regenerates the result.

   ![Result of State=CA and Category=Bold](https://devnet.logianalytics.com/hc/article_attachments/4404857067671/cmpnt_bdobj_detail2.gif)
9. If you select a label on the category axis of the chart, you go to detailed information concerned with the product category represented by that label; if you select a series axis label, Page Report Studio displays detailed information about the state indicated by the label.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The Go to Detail property is enabled by default for summaries on the group header/footer panel of a banded object. This is the same case when the formulas on the group header/footer panel of a banded object are group level formulas.
* You can also perform the go-to-detail operation from a summary or group level formula in a banded object in Designer view mode, and in the HTML/PDF report outputs.
* For a chart, its Hyperlink, X Hyperlink, and Z Hyperlink properties enable you to set a URL for the data markers (such as bars, benches, and lines), category axis labels, and series axis labels respectively. If you have set any of the three properties, the corresponding object no longer supports the go-to-detail function in Page Report Studio and selecting it goes to the URL. If Interactive is set to true and you set Hyperlink, X Hyperlink, and/or Z Hyperlink, double-clicking the corresponding element of the chart goes to the URL you set.
* If there is no other actions bound on the object for which you enable the go-to-detail action, the report users can also directly select the object to get the detail information at runtime. If there is other actions bound on the object, the report users can select the object to obtain the detail information only when the go-to-detail action has the highest [Click Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Priority).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056742-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects)
