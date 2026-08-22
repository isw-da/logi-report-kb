---
title: "Making Simple Modifications to Components"
id: 1500009675241
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components
updated_at: 2021-07-24T20:53:35Z
---

# Making Simple Modifications to Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components)

# Making Simple Modifications to Components

This topic introduces the general actions that you can perform on the report components.

Below is a list of the sections covered in this topic:

* [Moving a Component](#Move)
* [Resizing a Component and Its Elements](#Resize)
* [Hiding/Showing a Component](#Hide)
* [Editing a Component](#Edit)
* [Modifying Component Properties](#Property)
* [Changing the Position Property of Components](#Position)
* [Deleting a Component](#Delete)

## Moving a Component

When the [Position](#Position) property of a component is absolute, it can be moved to another place in the current container freely. To move a component, hover the mouse pointer on the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appear at the top right, drag the icon to the destination and then drop.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Resizing a Component and Its Elements

To resize a component, select anywhere in the component, then you will see it is surrounded by a rectangle with resizing handles. Point to a handle, when the mouse pointer turns to a double-headed arrow, you can drag the handle to resize the component.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920382103/wbrpt_edt_mdfy_resize.gif)

To adjust the width of a column in a table, select anywhere in the column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Point to the left or right boundary of the column, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the column.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926641175/wbrpt_edt_mdfy_width.gif)

To adjust the row height in a table, select anywhere in the row, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920374423/btn_wbrpt_slctrow.gif) that appears at the leftmost on the row to select the row. Point to the upper or lower boundary of a row, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the row height. Then all the other rows of the same role will be resized too. For example, if a detail row is resized, all rows in the detail area will be resized. If a group row is resized, all rows of the group will be resized, while the other groups' rows keep unchanged.

To resize the column or row in a crosstab, drag the right or lower boundary. Then all the columns or rows of the same role will change too.

For a tabular, point to the boundary between two cells and the mouse pointer will become a double-headed arrow, you can then drag the boundary to adjust the size of the related cells.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Hiding/Showing a Component

To hide a component, right-click on the component, then select **Hide** on the shortcut menu.

To hide a row or a column in a table, select anywhere in the row or column and you can see the buttons ![](https://devnet.logianalytics.com/hc/article_attachments/4404920374423/btn_wbrpt_slctrow.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) appear at the leftmost on the row and on the column header. Select the corresponding button to select the row or column, then right-click and select **Hide** from the shortcut menu.

To show the hidden components, select **Menu** > **Edit** > **Unhide Components** and then select the desired components to show from the drop-down list.

You can also set the Invisible property in the Inspector panel to show or hide a component. To do this, select the node that represents the component in the report structure tree in the Inspector panel, then set its Invisible property as required. If the parent of the component has no data source, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) in the value cell and [select a formula](#Formula) from the value drop-down list, or select **<Edit Expression>** to create an expression with the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009671841-Formula-Editor) to control whether or not to show the component.

For any component whose parent doesn't have a data source, for example, a label in the tabular cell of a web report, you can also use the Show Objects dialog to show or hide them. To do this:

1. Select the **Show Objects** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926629655/btn_wbrpt_shwobjt.gif) on the toolbar. The [Show Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009647782-Show-Objects) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382999/shwobjt.gif)
2. Select true or false from the Invisible drop-down list to show or hide the corresponding component. You can also [use a formula to control whether or not to to show the component](#Formula).
3. When done, select **OK** to accept the settings.

**Using formulas to control showing or hiding components**

You can use formulas to control whether the components whose parents have no data source will be shown or not in a web report. However, before doing this, you need to first bind a data source to the web report, then create dynamic formulas of Boolean type based on this data source and use these formulas to control the Invisible property of the required components. A return value of true will hide the component.

To use formulas to control which components to show in a web report, follow the steps below:

1. Select **Menu** > **Edit** > **Bind Data**. The [Bind Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009647062-Bind-Data) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926641815/bddt.gif)
2. Select a business view in the current catalog.
3. Select **OK** to bind the business view to the web report.
4. Select any blank place in the report. The business view bound to the report will be displayed in the Resources panel.
5. Follow the steps in [Creating and using dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to create the formulas you need.
6. Do either of the following:
   * **Using dialog**
     1. Select the **Show Objects** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926629655/btn_wbrpt_shwobjt.gif) on the toolbar to display the Show Objects dialog.
     2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) beside the Invisible property of the component which you want to control by formula and select the required formula from the drop-down list. Repeat this to select formulas for other components.
     3. Select **OK** to confirm the settings.
   * **Using the Inspector panel**
     1. In the Inspector panel, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) on the upper right corner to show the report structure tree.
     2. Select the node that represents the component in the tree.
     3. In the Properties sheet, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) in the value cell of the Invisible property, then select the required formula from the drop-down list, or select **<Create Formula>** in the drop-down list and create a dynamic formula in the bound data source to control the property value.
     4. Repeat the above steps to specify the Invisible property of other components.

   Then whether the components will be shown or not will then be determined by the return value of the specified formulas.

If you set the Invisible property of a component to true using a formula, the object will not be listed in the Menu > Edit > Unhide Components drop-down list. You can show it only by using the Show Objects dialog. Meanwhile, once the Invisible property of a component in a web report is controlled by a formula, the data source bound to the web report cannot be changed unless you remove the relationship between the formula and the property.

For a web report created in Logi JReport Designer, if it has been bound with a data source before being published to Logi JReport Server, and some dynamic formulas have been created based on this data source:

* If any of the formulas is used by the web report in Logi JReport Designer, you cannot change the bound data source for the web report in Web Report Studio. However, you can use the formulas of Boolean type created in Logi JReport Designer or create new formulas based on this data source to control the Invisible property in the Show Objects dialog.
* If none of the formulas is used by the web report in Logi JReport Designer, you can change the bound data source for the web report in Web Report Studio as you want.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Editing a Component

* To edit a label, select in the text and update the content. You can also use the toolbar to format the font, background color and alignment of a label.
* To edit a table, crosstab, or chart, use the corresponding report wizard on the shortcut menu. For details, see [Manipulating Data Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components).
* **To edit an image:**
  1. Select on the image, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and select **Edit** on the shortcut menu. The [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009671681-Edit-Image) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383767/edtimg.gif)
  2. Specify another image to use.
     + To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
     + To use an image on a website, select **Web URL**, then input the image URL or paste the URL in the Image URL text field.
     + To use an image in the image library of the Web Report Studio, select **Library**, then select the image in the My Images box.
  3. Select **OK** to finish editing the image.
* **To edit a multimedia object:**
  1. Select on the multimedia object, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and select **Edit** on the shortcut menu. The [Edit Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009671721-Edit-Multimedia) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926642327/edtmultmda.gif)
  2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
  3. In the File Name/URL text field, specify the full path of the multimedia object you want to insert or use the Browse button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
  4. The Plug-in page text field provides a default URL from which to download the player to play the inserted multimedia object on a web page.
  5. In the Properties box, specify the properties for the multimedia object as required.
  6. Select **OK** to finish editing the multimedia object.
* For a tabular, you can edit it as follows:
  + **Merging tabular cells**  
     Adjacent cells in a tabular which form a rectangle can be merged into one cell.

    To merge adjacent cells, select them one by one while holding the Ctrl key, then select **Menu** > **Format** > **Merge** or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363031/btn_wbrpt_merge.gif) on the toolbar, and these cells will be merged into one cell.
  + **Splitting a tabular cell**  
     To split a tabular cell, select the cell and select **Menu** > **Format**> **Split**, then in the [Split Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009647842-Split-Cell) dialog, specify the number of rows and columns and select **OK**. You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363287/btn_wbrpt_split.gif) on the toolbar to split the cell vertically or horizontally.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Modifying Component Properties

You can modify the object properties with either the corresponding properties dialog or the Inspector panel.

**Modifying component properties using the properties dialog**

To edit the properties of an object in a report, right-click the object and select **Properties** from the shortcut menu. In the corresponding properties dialog, specify the settings as required. For detailed explanation about options in the properties dialogs, refer to the specific topics in [Web Report Studio Dialogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009647022-Web-Report-Studio-Dialogs).

For a table group header/footer, table detail, or table header/footer, you need to first select anywhere in the corresponding row, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920374423/btn_wbrpt_slctrow.gif) that appears to select the row, right-click on the row and select **Properties** from the shortcut menu.

If you want to format the properties of the report, select **Menu** > **Edit** > **Report Body Properties**, then in the [Report Body Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009672461-Report-Body-Properties) dialog, configure the properties as required.

**Modifying component properties in the Inspector panel**

Properties of the objects in a web report are shown in the Inspector panel when Web Report Studio (to display the Inspector panel, select **Menu** > **View** > **Inspector**). The Inspector panel lists all the objects in the report in a tree structure with their properties. By selecting an object in the tree you also select it in the report.

To edit the properties of an object, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) on the upper right corner of the Inspector panel to show the report structure tree, select the object in the tree, then all properties of the selected object are displayed in the Properties sheet which contains two columns: Name and Value. Each type of object has its own set of properties. Depending on the object type, the properties that a certain object holds may greatly differ from those of another. You can change how an object appears and behaves by editing its property values. For details about properties of each object, see [Web Report Object Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009649522-Web-Report-Object-Property-Reference).

When a report contains a lot of objects, you can make use of the quick search toolbar at the top of the report structure tree panel to easily locate an object in the tree.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920384023/btn_srchtlbr.gif)

* **Text box**  
   The quick search toolbar treats the display names of the objects in the report structure tree as strings and searches by consecutive text. Type in the text you want to search for in the text box and the objects containing the matched text will be listed.
* **X**  
   Clears the text in the search text box.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384279/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384535/btn_srchtlbr_prv.gif)  
   When Highlight All is selected, you can use this button to go to the previous matched text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384791/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

### Changing the Position Property of Components

Report templates in Logi JReport use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, tabular cells themselves in Logi JReport can also act as flow layout containers.

In a flow layout model, objects are positioned relative to one another or absolutely. The Position property controls the position of components in the flow layout container. Components placed in other areas such as table cells, are not affected by the Position property.

The Position property can be one of the following values:

* **Static**  
   The component will be positioned at the location in which it is inserted. The X and Y coordinate properties are disabled. The position of the component cannot be moved other than by having its insertion point moved. This can happen when the text flow preceding the insertion point expands.
* **Absolute**  
   The component will be located at the position specified by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance it is not affected by having text inserted before it.

**To change the position property of a component:**

* Select on the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and on the shortcut menu, select the required item from the Position submenu.
* In the Inspector panel, select the node which represents the component, then set its Position property value as required.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Deleting a Component

A component can be removed from the report if it is no longer required. To delete a component, right-click on the component and select **Delete** from the shortcut menu, or select on the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, right-click on the icon and on the shortcut menu select **Delete**. If a message prompts asking for your confirmation, select **Yes** to confirm the removal.

To delete a table column, select anywhere in the column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Right-select on the column and select **Delete** from the shortcut menu. In the Confirm dialog, select **Yes** to confirm the removal.

You can also remove a KPI chart from its KPI component by right-clicking the KPI component and then selecting **Remove KPI Chart** from the shortcut menu.

**Note:** In a web report, there must be one and only one tabular, so you cannot either insert another tabular or delete the current tabular.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components)
