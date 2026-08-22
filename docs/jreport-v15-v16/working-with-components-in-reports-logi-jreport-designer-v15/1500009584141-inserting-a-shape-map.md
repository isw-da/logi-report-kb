---
title: "Inserting a Shape Map"
id: 1500009584141
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584141-Inserting-a-Shape-Map
updated_at: 2021-07-24T05:55:59Z
---

# Inserting a Shape Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563502-Shape-Maps)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map)

# Inserting a Shape Map

A shape map can be inserted into a tabular cell or the banded header/footer, group header/footer, or banded page header/footer panel of a banded object in a page report.

**To insert a shape map into a page report:**

1. Select a tabular cell, or the appropriate banded panel of a banded object in the page report.
2. Do any of the following:
   * Drag the **Insert Shape Map** button ![Insert Shape Map button](https://devnet.logianalytics.com/hc/article_attachments/4404893865367/btn_instmap.gif) from the Components panel to the destination.
   * Select **Insert** > **Map** > **Shape Map**.
   * Select **Home** > **Insert** > **Map** > **Shape Map**.

   The [Shape Map Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog) appears.

   ![Shape Map Editor window](https://devnet.logianalytics.com/hc/article_attachments/4404893865623/mpedtr.gif)
3. To use an image as background of the map, select **Menu****> Insert** > **Background****Image**. In the Shape Map Background Image dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the image and select **OK**.
4. Next is to add areas to the map. You can do this either by importing from an previously saved XML file or an ESRI file which has been defined with some area information, or by drawing the areas manually, or using a combination of these two.
   * To import the predefined map areas, select **Menu > File** > **Open**, then in the Import Shape Map Area dialog, specify the .xml file or .shp file that contains the required area information and select **Open** to import the areas. If you choose to import the map areas from a .shp file, you need to further specify a field in the ESRI shape file to define area name of the map, and if required, you can also select fields from the ESRI shape file to define the area tooltips (for more information, see [Select Area Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009567382-Select-Area-Name-Dialog) dialog).
   * To draw the areas manually, select **Insert Mode** on the toolbar, or **Menu** > **Edit** > **Insert Mode** to switch the Shape Map Editor to the mode.

     To draw an area, select the left mouse button to pick the start point of the area. Move the mouse pointer and select the left mouse button to select the other points. The points will be connected automatically. When you move the mouse pointer to the start point, a square appears indicating that the area will be closed. Select the left mouse button to finish drawing the area. If you want to undo your last line, select the right mouse button.

     ![Shape Map Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889407127/cmpnt_map_shp_inst.gif)
5. If you want to further change the shape or position of the areas, select  **Insert Mode** on the toolbar again to switch the Shape Map Editor to edit mode.

   To change the shape of an area, move the mouse pointer over the border or the points of the area. When it becomes a cross, choose a point on the line and drag it to create a new point. You can also choose a point of the area and drag it to a new position. If there are three points on one line, the middle point will be deleted automatically.

   To move an area, move the mouse pointer close its border. When it changes to a four-headed arrow, drag the area to a new position.

   **Tip:** If you have specified a background image for the map, and the size of it is not the same as that of the map object, you can select **Menu** > **Insert** > **Match Background Image** in the Shape Map Editor to resize the map object so as to make it match the size of the background image.
6. [Bind data to the map areas](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map) so as to show values on the areas.
7. [Add some conditional formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009563522-Adding-Conditional-Formats-to-Shape-Map-Areas) to the map areas.
8. [Make the map areas link to different targets](https://devnet.logianalytics.com/hc/en-us/articles/1500009584161-Binding-Links-to-Shape-Map-Areas).
9. In the Map Area Inspector panel, edit properties of any [area](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map), [label](https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map), [summary field](https://devnet.logianalytics.com/hc/en-us/articles/1500009591581-Properties-of-Summary-Field-in-Page-Report-Shape-Map) and [line](https://devnet.logianalytics.com/hc/en-us/articles/1500009569682-Properties-of-Line-in-Page-Report-Shape-Map) in the map if necessary. Select ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404893807511/btn_srch.gif) to search for the required property using the [quick search toolbar](https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog#Search) if needed.

   For areas, labels and summary fields, you can specify the properties globally and apply the global settings to individual ones conveniently. To specify area, label or summary field properties globally, select the corresponding sub node under the Map Global Setting node in the Map Area Inspector tree, then edit the property values accordingly.

   To make a specific area, label or summary field adopt the global settings, select it in the inspector tree, then set its Use Global Setting property to **true**. If you want the global settings to be applied to all the areas, labels or summary fields at a time, select **Menu > Edit** > **Reset All**, then in the [Reset All](https://devnet.logianalytics.com/hc/en-us/articles/1500009567262-Reset-All-Dialog) dialog, specify the properties according to your requirements.
10. If you want to save the area information you have defined in a file for future use, select **Menu** > **File** > **Save As** in the Shape Map Editor. In the Save Map Area dialog, specify the directory where you want to save the file and a name for it, then select **Save**. Later when you create a report with a map, you can choose to import areas from the saved XML file.
11. Select **Save** to save the changes to the map and close the Shape Map Editor.
12. Select the mouse button in the tabular cell, or banded panel to insert the map.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563502-Shape-Maps)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map)
