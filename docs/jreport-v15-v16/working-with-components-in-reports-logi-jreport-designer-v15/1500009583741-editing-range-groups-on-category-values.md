---
title: "Editing Range Groups on Category Values"
id: 1500009583741
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583741-Editing-Range-Groups-on-Category-Values
updated_at: 2021-07-24T05:56:04Z
---

# Editing Range Groups on Category Values

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583661-Labeling-Time-Series-Data-by-Constant-Interval)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583781-Creating-a-Scrollable-Chart)

# Editing Range Groups on Category Values

Data on the category axis of a chart can be divided into different range groups and separated by separating lines, and you can customize the data labels displayed for each range group.

The following example shows the usage in detail:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. [Insert a chart in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Web) which is based on WorldWideSalesBV in Data Source 1, displays in the Clustered Bar 2-D chart type, shows Sales Month on X-Axis and Total Sales on Bar Length.
4. View the chart and it appears as follows:

   ![Clustered Bar 2-D in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404889420695/cmpnt_cht_range2.gif)

14. Select the **Design** tab to return to the design mode.
15. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu. The Format Category (X) Axis dialog appears.
16. Go to the **Range** > **Properties** tab, check the **Enable Range** option and then select the **Special Group** button to display the User Defined Group dialog.
17. Define two range groups as follows and select **OK**.

    ![User Defined Group dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893997335/cmpnt_cht_range3.gif)
18. In the Gridline box, specify the line color as **#FF0000** and thickness as **2 px** for the separating line, then in the Fill box, specify the background colors of the 2015 and 2016 range groups as **#FFFFCC** and **#CCFFFF**.

    ![Format Category (X) Axis dialog - Range - Properties](https://devnet.logianalytics.com/hc/article_attachments/4404889420951/cmpnt_cht_range4.gif)
19. Select the **Data Label**  sub tab, check the **Show Data Label** option and then select the **Edit Data Labels** button to display the [Data Label Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009565062-Data-Label-Editor-Dialog). You can see there are three data labels which represent the category ranges, the summary field names and values respectively by default. Select **OK**.

    ![Data Label Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893997591/cmpnt_cht_range5.gif)
20. Select **value and percent** from the Value Label Type drop-down list. Select **OK**.
21. Select the **View** tab to preview the chart. The category values are now divided into two range groups with different background colors. In each range group, the data labels display the year information and the total sales of each year as well as the percentage of the total sales each year occupies.

    ![Ckustered bar 2-D in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404889421207/cmpnt_cht_range7.gif)
22. Select the **Design** tab to return to the design mode. This time we will format some properties of the areas that display the data labels on the range groups and make the data labels show total sales of each month instead.
23. Right-click the chart and select **Format Axes** > **Format Category (X) Axis** from the shortcut menu to open the Format Category (X) Axis dialog again.
24. Go to the **Range** > **Data Label**  tab, in the Border box, specify Color as **#606060**, select the first item from the Line Style drop-down list, set Thickness to **2 px**.

    ![Format Category (X) Axis dialog - Range - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889421463/cmpnt_cht_range6.gif)
25. Select the **Edit Data Labels** button to display the Data Label Editor.
26. Select **[Category]** from the first drop-down list of the last iterator.
27. Select on the right of the last drop-down list to select the last iterator, then right-click the iterator and
    select **Chart Iterator** from the shortcut menu to display the Chart Iterator dialog.

    ![Data Label Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893998103/cmpnt_cht_range8.gif)
28. Check the **Category** option in the Iterated By box and select **OK**.

    ![Chart Iterator dialog - Iteration](https://devnet.logianalytics.com/hc/article_attachments/4404893998359/cmpnt_cht_range9.gif)
29. Select **OK** in the Data Label Editor and Format Category (X) Axis dialog respectively to close them and apply the settings.
30. Resize the chart and save the report.
31. Select the **View** tab to view the chart again.
    The border of the data label areas is displayed and the data labels now show the total sales of each month and the percentage each month occupies. You can put the mouse over the data labels when they cannot be completely displayed to get the full text.

    ![Clustered Bar 2-D in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893998615/cmpnt_cht_range10.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583661-Labeling-Time-Series-Data-by-Constant-Interval)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583781-Creating-a-Scrollable-Chart)
