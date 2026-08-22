---
title: "Realigning Objects for a Better Appearance in the Exported Excel File"
id: 1500009589341
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File
updated_at: 2021-07-24T05:54:42Z
---

# Realigning Objects for a Better Appearance in the Exported Excel File

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File)

# Realigning Objects for a Better Appearance in the Exported Excel File

Normally, when a report is exported to an Excel file, the position and size of the objects in the original report are automatically rearranged by Logi JReport Designer. However, you can also arrange most objects manually, especially for exporting to Excel, so that they can be well-aligned in the exported Excel file.

Before you can resize or reposition an object, you should set the Columned property of the report to true, then:

> * [Relocating an Object for Exporting to Excel](#Relocate)
> * [Resizing an Object for Exporting to Excel](#Resize)

## Relocating an Object for Exporting to Excel

1. Select the node that represents the object in the Report Inspector.
2. In the Properties sheet, set the [Column Index and Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Excel) properties. The values you specify here determine the object's location in the exported Excel file.

   **Note:** If the Position property of an object is set to static, its Column Index and Row Index properties will not take affect when the report is exported to Excel result.
3. Select **File** > **Export**  > **To****Excel**.
4. In the Export to Excel dialog, select **Column Format**.
5. Set the other options as required and select **OK** to start exporting.

The object in the exported Excel file will then be located according to its Column Index and Row Index property values.

Alignment for drawing objects is different from other objects. The following explains the difference in detail:

1. Select the node that represents the drawing object in the Report Inspector, a box for example.
2. In the Properties sheet, set the following properties as required: [Top Attach Column, Top Attach Row, Bottom Attach Column, Bottom Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009591181-Properties-of-Box-in-Page-Report#Excel). These four properties together determine the coordinates and size of the drawing object.

   The first pair of the properties (Top Attach Column, Top Attach Row) locates a cell and uses its upper left corner as the upper left corner of the drawing object, while the second pair (Bottom Attach Column, Bottom Attach Row) locates another cell and uses its upper left corner as the lower right corner of the drawing object.

   For example, if the properties for an oval are set as:

   Top Attach Column: 1, Top Attach Row: 2, Bottom Attach Column: 3, Bottom Attach Row: 4

   Then, the upper left cell will be A2 and the lower right cell will be C4.

   **Notes:**

   * The value you set for the Top Attach Column (Top Attach Row) property should be always larger than that for the Bottom Attach Column (Bottom Attach Row) property.
   * The arc object cannot be shown in Excel and therefore these four properties for arc does not work.
3. Select **File** > **Export**  > **To****Excel**.
4. In the Export to Excel dialog, select **Column Format**.
5. Set the other options as required and select **OK** to start exporting.

The drawing object in the exported Excel file will then be aligned according to the four property values.

## Resizing an Object for Exporting to Excel

1. Select the node that represents the object in the Report Inspector.
2. In the Properties sheet, set the [Column Number and Row Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009591201-Properties-of-Box-in-Page-Report#Number) properties as required. The values you specify here determine the object's size in the exported Excel file, and only a few objects, such as images, charts, and user-defined objects, have these two properties.
3. Select **File** > **Export**  > **To Excel**.
4. In the Export to Excel dialog, select **Column Format**.
5. Set the other options as required and select **OK** to start exporting.

The object in the exported Excel file will then be resized according to its Column Number and Row Number property values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File)
