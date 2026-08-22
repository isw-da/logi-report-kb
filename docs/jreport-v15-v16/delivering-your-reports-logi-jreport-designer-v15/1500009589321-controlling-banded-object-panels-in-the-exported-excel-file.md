---
title: "Controlling Banded Object Panels in the Exported Excel File"
id: 1500009589321
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File
updated_at: 2021-07-24T05:54:41Z
---

# Controlling Banded Object Panels in the Exported Excel File

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel)

# Controlling Banded Object Panels in the Exported Excel File

You can control panels of a banded object in the exported Excel file by settings the following three properties:

* [Merge to Next Panel](#Merge): Merges current panel to the next panel. It applied to BandedHeader, BandedPageHeader, GroupHeader, and GroupFooter panels.
* [Repeat in Detail Panel](#Repeat): Repeats certain panel with the Detail panel. It applied to GroupHeader and BandedPageHeader panels.
* [Remove Blank Row](#Remove): Removes blank rows in the panel. It applied to BandedPageHeader, GroupHeader, and Detail panels.

The three properties take effect only when the Columned property of a report tab is set to true, and there is an operation order when those three properties work together: first, Merge to Next Panel; second, Repeat in Detail Panel; third, Remove Blank Row.

## Merging Panels in the Exported Excel File

You can specify to merge the BandedHeader, BandedPageHeader, GroupHeader, or GroupFooter panel in a banded object into the panel next to it in the exported Excel file. To do this:

1. Make sure the Columned property of the report that contains the banded object is set to true.
2. In the Report Inspector, select the node that represents the panel you want to merge.
3. Set the value of the Merge to Next Panel property to true.
4. Select **File** > **Export**  > **To Excel**.
5. In the Export to Excel dialog, select **Column Format**.
6. Set the other settings according to your requirements and select **OK** to start exporting.

   In the exported Excel file, you can find that the specified panel has been merged to the panel next to it.

Suppose there is a standard banded report which displays the fields Customer Name, Annual Sales, and is grouped by Customer\_Country and Customer\_Region.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893842839/frmt_expt_excl_pnl1.gif)

Then we set the Columned property of the report to true and Merge to Next Panel of the first GroupHeader panel to true as well, save the report and export it to Excel. We can see that the two group by panels are merged into one and fields in the two panels are put in one cell in the exported Excel file.

![](https://devnet.logianalytics.com/hc/article_attachments/4404889310103/frmt_expt_excl_pnl2.gif)

In order to improve the layout of the Excel result, now we specify the Column Index and Row Index properties of the objects as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4404889310359/frmt_expt_excl_pnl3.gif)

| Object | Column Index | Row Index |
| --- | --- | --- |
| A | 3 | 1 |
| B | 4 | 1 |
| C | 1 | 1 |
| D | 2 | 1 |
| E | 3 | 1 |
| F | 4 | 1 |

Save the report and export it to Excel again. We can see that fields in the Excel file are shown more clearly this time.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893843095/frmt_expt_excl_pnl4.gif)

**Notes:**

* When two or more objects in the to be merged panels have the same Row Index and Column Index property values, after merging the panels, in the exported Excel file, the objects will be merged into one cell, and they will be located in the cell based on this rule: the object whose X/Y property value is smaller than others will be put to front, and Y has higher priority than X. However, you can improve the appearance of the report by [relocating the objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File).
* Do not set the property Merge to Next Panel to true for the last GroupFooter panel. That will make the exported Excel file incorrect.
* Do not set the property Merge to Next Panel to true for the panel that contains crosstab or subreport.

## Repeating Objects in the GroupHeader or BandedPageHeader Panel in the Detail Panel

If you want to repeat objects in the GroupHeader panel or BandedPageHeader panel in the Detail panel of a banded object in the exported Excel file, follow the steps below:

1. Make sure the Columned property of the report that contains the banded object is set to true.
2. In the Report Inspector, select the node that represents the panel you want to repeat.
3. Set the value of the Repeat in Detail Panel property to true.
4. Select **File** > **Export**  > **To Excel**.
5. In the Export to Excel dialog, select **Column Format**.
6. Set the other settings according to your requirements and select **OK** to start exporting.

   In the exported Excel file, you can find that objects in the specified panel are repeated in the Detail panel.

**Notes:**

* When the objects in the GroupHeader/BandedPageHeader panel have the same Row Index and Column Index property values with those in the Detail panel, and you specify to repeat the GroupHeader/BandedPageHeader panel in the Detail panel, in the exported Excel file, the repeated objects will be put in the same cells with the ones in the Detail panel based on this rule: the object whose X/Y property value is smaller than others will be put to front, and Y has higher priority than X. However, you can improve the appearance of the report by [relocating the objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File).
* When you specify to repeat a GroupHeader panel, if there is a chart in the panel, the chart cannot be repeated.
* If a banded object contains more than one group by fields, that is to say, it has several GroupHeader panels, when you specify to repeat the first GroupHeader panel in the Detail panel, it will be repeated in the second GroupHeader panel as well.

## Removing Blank Row in a Panel

The property Remove Blank Row is provided to make the report look compact in the exported Excel file. It applied to BandedPageHeader, GroupHeader, and Detail panels of a banded object.

**To remove blank rows in the exported Excel file:**

1. Make sure the Columned property of the report that contains the banded object is set to true.
2. In the Report Inspector, select the node that represents the panel where blank rows may appear in the Report Inspector.
3. Set the value of the Remove Blank Row property to true.
4. Select **File** > **Export**  > **To****Excel**.
5. In the Export to Excel dialog, select **Column Format**.
6. Set the other settings according to your requirements and select **OK** to start exporting.

   In the exported Excel file, you can find that there will be no blank rows in the specified panel.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel)
