---
title: "Creating Motion Charts"
id: 1500010057082
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057082-Creating-Motion-Charts
updated_at: 2021-07-23T19:14:42Z
---

# Creating Motion Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057122-Creating-Real-Time-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056862-Creating-Dynamic-Charts-in-Excel)

# Creating Motion Charts

A motion chart is a chart moving at runtime based on the value changes of a specified motion field. In a motion chart, you can get a motion control section on its platform, which enables you to make the chart move. This topic introduces the elements in the motion control section of a motion chart and presents an example to show you how to create a motion chart.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You cannot use motion charts in page reports that use query resources. Meanwhile, to have a better and stable performance for motion charts, you are recommended to use the Google Chrome web browser.

This topic contains the following sections:

* [The Motion Control Section](#Section)
* [Example of Creating a Motion Chart](#Create)

## The Motion Control Section

The motion control section of a motion chart contains the following elements:

![Motion Chart Diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857059095/cmpnt_cht_mtn.gif)

* A play button to make the chart play its dynamic trend or to be static.
* A motion bar which contains a defined motion field. The chart updates its dynamic trend based on the value changes of the motion field.
* A speed control to determine the moving speed of the chart.
* For a bubble chart, there is also a trail control to make the chart show trails of bubbles or lines.

At runtime, the report users can use the motion control section to make the chart move. Select the play button and the chart shows its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. The report users can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, the report users can control whether the chart is moving in bubble or line trail (when null values appear, the trails of bubbles or lines are not available).

## Example of Creating a Motion Chart

The following example shows how you can create a motion chart in a web report and play it in Web Report Studio.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. Select **Insert** > **Chart**. Designer displays the Create Chart wizard.
4. In the Data screen of the wizard, select **WorldWideSalesBV** from Data Source 1. Select **Next**.
5. Select **Bubble 2-D** in the Type screen. Select **Next**.
6. In the Display screen, add the group objects **Product Type** to the Bubble (Category) box and **Region** to the Color (Series) box.
7. In the value box, add the aggregation objects **Sum\_MTotal**, **Total Cost**, and **Total Sales**  respectively on X-Axis, Y-Axis, and Size. Note that, when you add a value for the bubble X axis, the chart displays this value on the category axis instead of the one specified in the Category box, while it still includes the value defined in the Category box in data calculation.
8. Select **Motion Bar for Playable Chart**, add the group object **Sales Year** as the motion field.

   ![Add Field for the Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848689175/cmpnt_cht_mtn_eg1.gif)
9. Select **Finish** to create the motion chart.
10. Save the report and select **View** > **Preview As** > **Web Report Result**. The chart shows as follows:

    ![Preview the Report as Web Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404848689559/cmpnt_cht_mtn_eg2.gif)
11. Select the **Bubbles** and **Lines** checkboxes, and select the play button, then the value of the motion field changes, and the bubbles in the chart move based on the value change of the motion field in line trail. See the result below, when the value of the motion field changes to 2016, the display value of the bubble also changes accordingly.

    ![Motion Chart Result with Bubbles and Lines](https://devnet.logianalytics.com/hc/article_attachments/4404848689815/cmpnt_cht_mtn_eg3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057122-Creating-Real-Time-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056862-Creating-Dynamic-Charts-in-Excel)
