---
title: "Creating a Motion Chart"
id: 1500009563262
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563262-Creating-a-Motion-Chart
updated_at: 2021-07-24T05:56:04Z
---

# Creating a Motion Chart

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583361-Creating-a-Back-to-back-Bench-Chart)

# Creating a Motion Chart

You can make a chart move at runtime based on the value changes of a specified motion field. This kind of chart is called motion chart. For a motion chart, a motion control section will be added on its platform, which contains the following elements:

![Motion chart diagram](https://devnet.logianalytics.com/hc/article_attachments/4404893999127/cmpnt_cht_mtn1.gif)

* A play button allowing you to make the chart play its dynamic trend or to be static.
* A motion bar which contains a defined motion field. The chart will update its dynamic trend based on the value changes of the motion field.
* A speed control. The moving speed of the chart can be controlled by dragging the slider on the speed control.
* For a bubble chart, there is also a trail control, which allows you to make the chart show trails of bubbles or lines (when null values appear, the trails of bubbles or lines will not be available).

Currently, motion charts is not supported in page reports that are created using query resources. Meanwhile to have a better and stable performance for motion charts, you are recommended to use the Google Chrome web browser.

**To insert a motion chart into a report:**

1. Position the mouse pointer at the destination where you want to insert the chart.
2. Do one of the following to open the [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009564882-Create-Chart-Dialog-Business-View-Based-) wizard:
   * Drag the desired chart type button from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.
3. In the Data screen, select a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) in the current catalog on which the chart will be created.
4. In the Type screen, specify the type of the chart which can only be single chart of bar, bench or bubble type.
5. In the Display screen, specify a title for the chart in the Title text field. Add the required fields from the Resources box to be displayed on the category axis, series axis and value axis of the chart, and define some [special group](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#Special) and [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#SelectN) on the category/series field if required. You can also add [additional values](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Additional) including constant values and average values to be displayed on the value axis of the chart.

   If you select the bubble chart type, you need to specify the fields to be shown on the bubble X axis, Y axis and the value you want to show as the bubble size in the value box. When a value is added for the bubble X axis, this value will be displayed on the category axis instead of the one specified in the Bubble box, however, the value defined in the Bubble box will still be included in data calculation.

   Check the **Motion Bar for Playable Chart** checkbox, then from the Resources box add a field which is of Integer, Date or Time data type as the motion field. When the field is of the Date data type, you can define some [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#Group) on it.
6. In the Filter screen, select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) of the specified business view if there is from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).
7. In the Layout screen, specify the layout of the chart.
8. In the Style screen, select a style for the chart.
9. Select **Finish** to insert the chart.

When a motion chart is published to Logi JReport Server, you can then run it in Report Studio or JDashboard. Then, you can use the motion control section to make the chart move. Select the play button and the chart will show its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. You can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, you can control whether the chart will be moving in bubble or line trail.

## Example of creating a motion chart

This example illustrates how to create a motion chart in a web report and play it in Web Report Studio.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. Select **Insert** > **Chart**. The Create Chart wizard appears.
4. In the Data screen of the wizard, select **WorldWideSalesBV** from Data Source 1. Select **Next**.
5. Select **Bubble 2-D** in the Type screen. Select **Next**.
6. In the Display screen, add the field **Product Type** to the Bubble box and and **Region** to the Color box.

   In the value box, add the field **Sum\_MTotal**, **Total Cost**  and **Total Sales**  respectively as the value of X-Axis, Y-Axis and Size. Note that when you specify a value for X axis, this value is displayed as the category value instead of Category that is specified in the Bubble box. Although Category is displayed as the category value, it is also included in the data calculation.

   Check **Motion Bar for Playable Chart**, add the field **Sales Year**  as the motion field.

   ![Create Chart wizard - Display in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893999511/cmpnt_cht_mtn_dsply.gif)
7. Select **Finish** to create the motion chart.
8. Save the report and select **View** > **Preview As** > **Web Report Result**, the report will show as follows:

   ![Motion chart in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893999767/cmpnt_cht_mtn2.gif)
9. Check the **Bubbles** and **Lines** checkboxes, and select the play button, then the value of the motion field will change, and the bubbles in the chart will move based on the value change of the motion field in line trail. See the result below, when the value of the motion field is changed to 2016, the display value of the bubble also changes accordingly.

   ![Motion chart in Wen Report](https://devnet.logianalytics.com/hc/article_attachments/4404894000279/cmpnt_cht_mtn3.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583361-Creating-a-Back-to-back-Bench-Chart)
