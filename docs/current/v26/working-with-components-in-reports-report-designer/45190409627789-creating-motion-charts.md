---
title: "Creating Motion Charts"
id: 45190409627789
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190409627789-Creating-Motion-Charts
updated_at: 2026-04-30T15:12:14Z
source_host: logi-report-v26.insightsoftware.com
---
# Creating Motion Charts

A motion chart is a chart moving at runtime based on the value changes of a specified motion field. In a motion chart, you can get a motion control section on its platform, which enables you to make the chart move. This topic introduces the elements in the motion control section of a motion chart and presents an example to show you how to create a motion chart.

 You cannot use motion charts in page reports that use query resources. Meanwhile, to have a better and stable performance for motion charts, you should use the Google Chrome web browser.

This topic contains the following sections:

- The Motion Control Section

- Example: Creating a Motion Chart

## 
The Motion Control Section

The motion control section of a motion chart contains the following elements:

- A play button to make the chart play its dynamic trend or to be static.

- A motion bar which contains a defined motion field. The chart updates its dynamic trend based on the value changes of the motion field.

- A speed control to determine the moving speed of the chart.

- For a bubble chart, there is also a trail control to make the chart show trails of bubbles or lines.

At runtime, users can use the motion control section to make the chart move. Select the play button and the chart shows its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. Users can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, users can control whether the chart is moving in bubble or line trail (when null values appear, the trails of bubbles or lines are not available).

## 
Example: Creating a Motion Chart

The following example shows how you can create a motion chart in a web report and play it in Web Report Studio.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- Navigate to File > New > Web Report to create a web report.

- Navigate to Insert > Chart. Designer displays the Create Chart dialog box.

- In the Data screen, select WorldWideSalesBV in Data Source 1. Select Next.

- In the Type screen, select Bubble 2-D. Select Next.

- In the Display screen, add the group objects Product Type to the Bubble (Category) box and Region to the Series box.

- In the Color (Show Values) box, add the aggregation objects Sum_MTotal, Total Cost, and Total Sales  respectively to X-Axis, Y-Axis, and Size. Note that, when you add a value for the bubble X axis, the chart displays this value  on the category axis instead of the one specified in the Category box, while it still includes the value defined in the Category box in data calculation.

- Select Motion Bar for Playable Chart, then add the group object Sales Year as the motion field.
    

- Select Finish to create the motion chart.

- Save the report.

- Navigate to View > Preview As > Web Report Result to run the report in Web Report Studio.

- Select Bubbles and Lines, and select the play button, then the value of the motion field changes, and the bubbles in the chart move based on the value change of the motion field in line trail. In the following result, when the value of the motion field changes to 2016, the value of the bubble also changes accordingly.
