---
title: "Making Simple Modifications to Report Objects"
id: 1500009649442
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649442-Making-Simple-Modifications-to-Report-Objects
updated_at: 2021-07-24T20:53:54Z
---

# Making Simple Modifications to Report Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673961-General-Operations)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649262-Adding-Report-Objects)

# Making Simple Modifications to Report Objects

You can make simple modifications to report objects, such as move an object to a new position, resize an object, delete an object from the report and so on. However, except for the Show/Hide Object feature, a [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to use all the other features introduced in this document. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

Below is a list of the sections covered in this topic:

* [Moving an Object](#Move)
* [Resizing an Object](#Resize)
* [Hiding/Showing an Object](#Hide)
* [Splitting and Merging Cells in a Tabular](#Cell)
* [Modifying Object Properties](#Property)
* [Deleting an Object](#Delete)

## Moving an Object

A table, banded object, chart, crosstab, tabular, or image, can be easily moved to a new position. What you need to do is select anywhere in the object, then drag the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appearing at its upper left corner to the destination. After Page Report Studio has finished processing, the object will be redrawn in the new location.

For other objects, select it and move it to the new position.

**Note:** For page reports created in Logi JReport Designer, only the objects whose Position property value is absolute, and the DBFields or labels which have been defined as a view element can be moved in Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Resizing an Object

To resize an object, select anywhere in the object, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon to select the object, then you will see that it is surrounded by a rectangle with three resizing handles. Point to a handle, when the mouse pointer turns to a double-headed arrow, you can drag the handle to resize the object.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926674327/pgrpt_edit_mdfy_resize.gif)

To resize a panel in a banded object, select it and drag the resizing handle to the desired position.

To adjust the width/height of a column/row in a table, point to the right/lower boundary of the column/row, when the mouse pointer becomes a horizontal/vertical double-headed arrow, drag the handle and the width/height of the column/row will change. This will also resize all cells in the column or row.

For a crosstab, you can resize its rows and columns the same as you do with a table.

For a tabular, point to the boundary between two cells and the mouse pointer will become a double-headed arrow, you can then drag the boundary to adjust the size of the related cells.

To change the width and height of a field, select any value of this field to select it, then drag the right or lower resizing handle on its borders to a new position, and the width or height of the field will change. You can also do this for any label.

**Notes:**

* When resizing table rows:
  + If you resize the table header, only the height of the header will be changed. However, when you resize any row except the header, the height of all rows in the table will be changed at the same time.
  + If there are some groups in a table and the height of one group row is changed, the other group rows will not be resized.
* When resizing crosstab columns/rows:
  + If you resize the horizontal/vertical header of a crosstab, other rows/columns will not be affected.
  + If you resize the total column/row of a crosstab, other columns/rows will not be affected.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Hiding/Showing an Object

To hide a table, banded object, chart, crosstab, or tabular, select on the object, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and then select **Hide** from the shortcut menu. For other objects such as text boxes, drop-down lists, fields, and labels, right-click it and then select **Hide** to hide it.

To show a hidden object, right-click the object containing it, then on the shortcut menu, select the object name from the Show submenu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Splitting and Merging Cells in a Tabular

Adjacent cells in a tabular which can form a rectangle may be merged into one cell.

To merge adjacent cells, select them one by one while holding the Ctrl key, then select **Menu** > **Report** > **Merge**, and these cells will be merged into one cell.

**To split a cell:**

1. Select the cell and select **Menu** > **Report** > **Split**.
2. In the [Split](https://devnet.logianalytics.com/hc/en-us/articles/1500009645782-Split) dialog, specify the number of rows and columns.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920452503/split.gif)
3. Select **OK** and the cell will be split.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Modifying Object Properties

Page Report Studio allows you to modify object properties with the corresponding properties dialog. However for some objects, you must be an [advanced user](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#AdvUser) in order to edit their properties.

* To edit the properties of any object in a report, right-click on the object and select **Properties** from the shortcut menu. If it is a table, crosstab, chart, banded object, or tabular, select anywhere on it, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and select **Properties** on the shortcut menu. In the corresponding properties dialog, specify the settings as required. For a table, you can also right-click any field or cell in it and select **Table** from the shortcut menu to show the Table Properties dialog. For detailed explanation about options in the properties dialogs, refer to the specific topics in [Page Report Studio Dialogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009644902-Page-Report-Studio-Dialogs).
* You can right-click a group header/footer panel in a banded object, and then select **Group** to show the [Group Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009645202-Group-Properties) dialog in order to define the group properties.
* To edit the properties of a report tab, right-click the blank part of the report tab and select **Report** from the shortcut menu, then in the [Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009669961-Report-Tab-Properties) dialog, configure the properties as required.

**Tip:** If you just want to modify the text related properties for a field or label, for example, you want to change the text alignment or make the text bold, you can achieve it by simply selecting the field or label, then selecting the corresponding buttons on the toolbar.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Deleting an Object

An object can be removed from the report if it is no longer required. However, objects that are in a subreport cannot be deleted.

* To delete a table, banded object, chart, crosstab, tabular, or image, select on the object, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and select **Delete** from the shortcut menu, or you can drag the icon outside the report page. Then, a message box will prompt, asking for your confirmation. Select **OK** in the message box so as to remove the component.
* For a field, you can drag any value of the field outside the report page to remove it. You can also drag any label outside the report page to remove it. Right-selecting and then selecting Delete is another way to achieve this.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673961-General-Operations)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649262-Adding-Report-Objects)
