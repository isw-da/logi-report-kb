---
title: "Obtaining the Group Details in a Banded Object"
id: 4405661346583
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object
updated_at: 2022-01-27T20:34:22Z
---

# Obtaining the Group Details in a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664366615-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects)

# Obtaining the Group Details in a Banded Object

In a banded object which contains groups, you may only care about the details in a certain group. To meet your expectation, Logi Report provides the Go to Detail feature. This topic describes how you can use different objects in the group panels of a banded object to get detail information of the groups.

This topic contains the following sections:

* [Going to Detail from a Field/Label/Image](#Field)
* [Going to Detail from a Shape Map](#Map)
* [Going to Detail from a Chart](#Chart)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) You can obtain group details for banded objects that use query resources only.

## Going to Detail from a Field/Label/Image

If a banded object contains groups, you can use a field (DBField, parameter, formula, summary, special field), label, or image in a group header/footer panel of the banded object, including the case that the field, label, or image is in a tabular cell or text box which is in the banded object's group header/panel panel, to obtain the detail information of that group. To do this:

1. Open a page report which contains a grouped banded object.
2. Select the object you want to use for going to detail.
3. In the Report Inspector, edit its **Go to Detail** property to **true**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) The Go to Detail property is "true" by default for the summaries in the group header/footer panel of a banded object; it is the same case if the formulas in the group header/footer panel of a banded object are group level formulas.
4. From the value drop-down list of [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/4405661852055-DBField-Properties#Target), select the target window or frame to display the detail information at runtime.
5. Publish the page report to Server and run it in Page Report Studio.
6. Select the object and you can get the detail information of the corresponding group. For fields

You can also go to the details of a group from a summary or group level formula in the group's header/footer panel when [previewing the banded object in Logi Report format](https://devnet.logianalytics.com/hc/en-us/articles/4405664696343-Previewing-Reports#GoToDetail), and in the HTML/PDF output of the banded object if you select [Drilldown](https://devnet.logianalytics.com/hc/en-us/articles/4405661756567-Exporting-to-PDF#Drilldown) while specifying the export options.

## Going to Detail from a Shape Map

If a shape map in a grouped banded object meets the following preconditions, you can set its Go to Detail property to "true" to obtain the group details from the shape map in Page Report Studio.

* The shape map inherits dataset from the banded object.
* The banded object has at least two groups.
* The shape map is in the group header/footer panel that is not the lowest level group of the banded object.

## Going to Detail from a Chart

You can also use a chart in a banded object for going to detail; however, the chart should satisfy some prerequisites.

* The value axis of the chart shows summary information.
* The chart inherits dataset from the banded object and has no data container link with the banded object.
* In the case that the chart shows FieldA and FieldB respectively on the series and category axes, then the two fields must be group-by fields of the banded objects, and FieldA is one level higher than FieldB, and the chart must be in the header/footer panel of the group which is one level higher than FieldA (if FieldA is the highest group level in the banded object, the chart should be in the banded header/footer panel). In the case that the chart only shows FieldB as the category field (no series axis), then FieldB must be a group-by field of the banded object, and the chart must be in the header/footer panel of the group which is one level higher than FieldB, or the banded header/footer panel if FieldB is the highest level.

The following example shows how to obtain detail information from a chart.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Page Report** to
   create a page report with a banded object in its first report tab.
3. [Define the banded object](https://devnet.logianalytics.com/hc/en-us/articles/4405661347735-Inserting-Banded-Objects-in-a-Report#Query) as follows:
   1. Use the query **WorldWideSales** in Data Source 1 of the catalog.
   2. Display these detail fields: the DBFields **Product Name**, **Unit Price**, **Discount**, and **Quantity**, and the formula **Total**
   3. Group it by **Country**, **State**, and then **Category**.
   4. Apply the **Classic** style.
4. In the **Data** panel of the main window, select **<New Summary...>** in the **Summaries** node.
5. [Create the summary](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Predefine)**Sum\_Total** which uses the aggregate function **Sum**, summarizes on the formula **Total**, and applies to the **Category** group level.

   ![Create the Summary](https://devnet.logianalytics.com/hc/article_attachments/4420402612759/cmpnt_bdobj_detail1.gif)
6. Select the footer panel of the Category group in the banded object and drag the summary to it.
7. Resize the header panel of the Country group, then [insert a Bar 3-D chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report) into it. The chart inherits the dataset from the banded object (make sure to select **Current Dataset** in the Data screen of the Create Chart dialog box), and displays the DBField **Category** on the category axis, **State** on the series axis, and the summary **Sum\_Total** on the value axis.

   ![Insert Chart in Banded Group Panel](https://devnet.logianalytics.com/hc/article_attachments/4420394937367/cmpnt_bdobj_detail2.gif)
8. In the Report Inspector, select the node **Chart Object**, then set its **Go to Detail** property to **true**.
9. Save the report.
10. Navigate to **View** > **Preview As** > **Page Report Result** to preview the report in Page Report Studio.
11. Turn to page around 34 to view records in USA.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4420402613143/cmpnt_bdobj_detail3.gif)
12. Point to the bar of "Category=Bold" and "State=CA", the mouse pointer then becomes a hand. Select the bar and Page Report Studio regenerates the result.

    ![Result of State=CA and Category=Bold](https://devnet.logianalytics.com/hc/article_attachments/4420394937879/cmpnt_bdobj_detail4.gif)
13. If you select a data label on the category axis of the chart, you go to the detail information about the product category that label represents; if you select a series axis data label, Page Report Studio displays the details about the state indicated by the label.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) Users can select the object for which you enable the go-to-detail action to get the group details in Page Report Studio, if there is no other actions bound on the object. If you have bound other actions to the object, they can select the object to obtain the detail information only when you give the go-to-detail action the highest [Click Priority](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Priority).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664366615-Embedding-Data-Components-in-a-Banded-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects)
