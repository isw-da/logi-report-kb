---
title: "Making Simple Modifications to Components"
id: 1500009751521
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components
updated_at: 2021-07-25T07:18:33Z
---

# Making Simple Modifications to Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components)

# Making Simple Modifications to Components

This topic introduces the general actions that you can perform on the report components.

Select the following links to view the topics:

* [Moving a Component](#Move)
* [Resizing a Component and Its Elements](#Resize)
* [Hiding/Showing a Component](#Hide)
* [Editing a Component](#Edit)
* [Modifying Component Properties](#Property)

+ [Modifying Properties Using Dialog](#UseDialog)
+ [Modifying Properties in the Inspector Panel](#Inspector)

* [Changing the Position Property of Components](#Position)
* [Deleting a Component](#Delete)

## Moving a Component

When the [Position](#Position) property of a component is absolute, it can be moved to another place in the current container freely. To move a component, hover the mouse pointer on the component, when the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) appear at the top right, drag the icon to the destination and then drop.

## Resizing a Component and Its Elements

To resize a component, select anywhere in the component, then you will see it is surrounded by a rectangle with resizing handles. Point to a handle, when the mouse pointer turns to a double-headed arrow, you can drag the handle to resize the component. When the width or height of a component is fully displayed, the right or bottom boundary cannot be further enlarged.

![Resize Component](https://devnet.logianalytics.com/hc/article_attachments/4404942459543/wbrpt_edt_mdfy_resize.gif)

To adjust the width of a column in a table, select anywhere in the column, then select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Point to the left or right boundary of the column, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the column.

![Resize Column](https://devnet.logianalytics.com/hc/article_attachments/4404942459799/wbrpt_edt_mdfy_width.gif)

To adjust the row height in a table, select anywhere in the row, then select the button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404936724503/btn_wbrpt_slctrow.gif) that appears at the leftmost on the row to select the row. Point to the upper or lower boundary of a row, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the row height. Then all the other rows of the same role will be resized too. For example, if a detail row is resized, all rows in the detail area will be resized. If a group row is resized, all rows of the group will be resized, while the other groups' rows keep unchanged.

To resize the column or row in a crosstab, drag the right or lower boundary. Then all the columns or rows of the same role will change too.

To adjust the panel height in a banded object, select the panel and drag the lower boundary of the panel until the panel is at the required height.

For a tabular, point to the boundary between two cells and the mouse pointer will become a double-headed arrow, you can then drag the boundary to adjust the size of the related cells.

## Hiding/Showing a Component

To hide a component, right-click on the component, then select **Hide** on the shortcut menu.

To show the hidden components, select **Menu** > **Edit** > **Unhide Components** and then select the desired components to show from the drop-down list.

You can also set the Invisible property in the Inspector panel to show or hide a component. To do this, select the node that represents the component in the report structure tree in the Inspector panel, then set its Invisible property as required. If the parent of the component has no data source, you can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) in the value cell and [select a formula](#Formula) from the value drop-down list, or select **<Edit Expression>** to create an expression with the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009748461-Formula-Editor) to control whether or not to show the component.

For any component whose parent doesn't have a data source, for example, a label in the tabular cell of a web report, you can also use the Show Objects dialog box to show or hide them. To do this:

1. Select the **Show Objects** button ![Show Objects button](https://devnet.logianalytics.com/hc/article_attachments/4404942447127/btn_wbrpt_shwobjt.gif) on the toolbar. Report Server displays the [Show Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009749321-Show-Objects) dialog box.

   ![Show Objects dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942460439/shwobjt.gif)
2. Select true or false from the Invisible drop-down list to show or hide the corresponding component. You can also [use a formula to control whether or not to to show the component](#Formula).
3. When done, select **OK** to accept the settings.

**Using formulas to control showing or hiding components**

You can use formulas to control whether the components whose parents have no data source will be shown or not in a web report. However, before doing this, you need to first bind a data source to the web report, then create dynamic formulas of Boolean type based on this data source and use these formulas to control the Invisible property of the required components. A return value of true will hide the component.

To use formulas to control which components to show in a web report, follow the steps below:

1. Select **Menu** > **Edit** > **Bind Data**. Report Server displays the [Bind Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009721222-Bind-Data) dialog box.

   ![Bind Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936733207/bddt.gif)
2. Select a business view in the current catalog.
3. Select **OK** to bind the business view to the web report.
4. Select any blank place in the report. The business view bound to the report will be displayed in the Resources panel.
5. Follow the steps in [Creating and using dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to create the formulas you need.
6. Do either of the following:
   * **Using dialog box**
     1. Select the **Show Objects** button ![Show Objects button](https://devnet.logianalytics.com/hc/article_attachments/4404942447127/btn_wbrpt_shwobjt.gif) on the toolbar to display the Show Objects dialog box.
     2. Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) beside the Invisible property of the component which you want to control by formula and select the required formula from the drop-down list. Repeat this to select formulas for other components.
     3. Select **OK** to confirm the settings.
   * **Using the Inspector panel**
     1. In the Inspector panel, select ![Show Report Structure Tree](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) on the upper right corner to show the report structure tree.
     2. Select the node that represents the component in the tree.
     3. In the Properties sheet, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) in the value cell of the Invisible property, then select the required formula from the drop-down list, or select **<Create Formula>** in the drop-down list and create a dynamic formula in the bound data source to control the property value.
     4. Repeat the above steps to specify the Invisible property of other components.

   Then whether the components will be shown or not will then be determined by the return value of the specified formulas.

If you set the Invisible property of a component to true using a formula, the object will not be listed in the Menu > Edit > Unhide Components drop-down list. You can show it only using the Show Objects dialog box. Meanwhile, once the Invisible property of a component in a web report is controlled by a formula, the data source bound to the web report cannot be changed unless you remove the relationship between the formula and the property.

For a web report created in Logi Report Designer, if it has been bound with a data source before being published to Logi Report Server, and some dynamic formulas have been created based on this data source:

* If any of the formulas is used by the web report in Logi Report Designer, you cannot change the bound data source for the web report in Web Report Studio. However, you can use the formulas of Boolean type created in Logi Report Designer or create new formulas based on this data source to control the Invisible property in the Show Objects dialog box.
* If none of the formulas is used by the web report in Logi Report Designer, you can change the bound data source for the web report in Web Report Studio as you want.

## Editing a Component

* To edit a label, double-click the text and update the content. You can also use the toolbar to format the font, background color and alignment of a label.
* To edit a table, crosstab, chart or banded object, use the corresponding report wizard on the shortcut menu. For details, see [Manipulating Data Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components).
* **To edit an image:**
  1. Right-click on the image and select **Edit** from the shortcut menu. Report Server displays the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009748281-Edit-Image) dialog box.

     ![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942460695/edtimg.gif)
  2. Specify another image to use.
     + To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
     + To use an image on a website, select **Web URL**, then type the image URL or paste the URL in the Image URL text box.
     + To use an image in the image library of Web Report Studio, select **Library**, then select the image in the My Images box.
  3. Select **OK** to finish editing the image.
* **To edit a multimedia object:**
  1. Right-click on the multimedia object and select **Edit** from the shortcut menu. Report Server displays the [Edit Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009748301-Edit-Multimedia) dialog box.

     ![Edit Multimedia dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936733719/edtmultmda.gif)
  2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
  3. In the File Name/URL text box, specify the full path of the multimedia object you want to insert or use the Browse button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
  4. The Plug-in page text box provides a default URL from which to download the player to play the inserted multimedia object on a web page.
  5. In the Properties box, specify the properties for the multimedia object as required.
  6. Select **OK** to finish editing the multimedia object.
* For a tabular, you can edit it as follows:
  + **Merging tabular cells**  
     Adjacent cells in a tabular which form a rectangle can be merged into one cell.

    To merge adjacent cells, select them one by one while holding the Ctrl key, then select **Menu** > **Format** > **Merge** or select ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404942447639/btn_wbrpt_merge.gif) on the toolbar, and these cells will be merged into one cell.
  + **Splitting a tabular cell**  
     To split a tabular cell, select the cell and select **Menu** > **Format**> **Split**, then in the [Split Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009722322-Split-Cell) dialog box, specify the number of rows and columns and select **OK**. You can also select ![Split button](https://devnet.logianalytics.com/hc/article_attachments/4404942447895/btn_wbrpt_split.gif) on the toolbar to split the cell vertically or horizontally.

## Modifying Component Properties

You can modify the component properties with either the corresponding properties dialog box or the Inspector panel.

For some properties you may see a button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) on the right of the value cell which means that the property value can be controlled by a formula dynamically. Select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936733975/btn_fmla.gif) and then select the drop-down arrow in the value cell, a drop-down list will be displayed. You can then select an existing formula in the list or select **<Edit Expression>** to create an expression with the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009748461-Formula-Editor) as the property value.

### Modifying Properties Using Dialog

To edit the properties of a component in a report, right-click it and select **Properties** from the shortcut menu (for a table row you need to first select anywhere in the row and then select the button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404936724503/btn_wbrpt_slctrow.gif) that appears at its leftmost to select the row, then you can right-click on the row to get the Properties command on the shortcut menu). In the corresponding properties dialog box, specify the settings as required. For detailed explanation about options in the properties dialog boxes, refer to the specific topics in [Web Report Studio Dialogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009721162-Web-Report-Studio-Dialogs).

If you want to format the properties of the report, select **Menu** > **Edit** > **Report Body Properties**, then in the [Report Body Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749281-Report-Body-Properties) dialog box, configure the properties as required.

### Modifying Properties in the Inspector Panel

The Inspector panel of Web Report Studio is for managing properties of the objects in a web report (to display the panel, select **Menu** > **View** > **Inspector**).

To edit the properties of an object with the Inspector panel, first select the object in the report, or select ![Show Report Structure Tree](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) on the upper right corner of the Inspector panel to show the report structure tree and then select it from the tree. All properties of the selected object are displayed in the Properties sheet which contains two columns: Name and Value. Each type of object has its own set of properties. Depending on the object type, the properties that a certain object holds may greatly differ from those of another. You can change how an object appears and behaves by editing its property values. For details about properties of each object, see [Web Report Object Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009750621-Web-Report-Object-Property-Reference).

When a report contains a lot of objects, you can make use of the search bar at the top of the report structure tree panel to easily locate an object in the tree.

The following shows the options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404936734231/btn_srchtlbr.gif)

* **Text box**  
  Type in the text you want to search in the text box and the values containing the matched text will be listed.
* **X**  
  Closes the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404942460951/btn_srchtlbr_adv.gif)  
  Lists more search options.
  + **Highlight All**   
    Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Specifies whether to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734487/btn_srchtlbr_prv.gif)  
  When Highlight All is selected, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734743/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

## Changing the Position Property of Components

Report templates in Web Report Studio use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, tabular cells themselves in Web Report Studio can also act as flow layout containers.

In a flow layout model, objects are positioned relative to one another or absolutely. The Position property controls the position of components in the flow layout container. Components placed in other areas such as table cells, are not affected by the Position property.

The Position property can be one of the following values:

* **Static**  
   The component will be positioned at the location in which it is inserted. The X and Y coordinate properties are disabled. The position of the component cannot be moved other than by having its insertion point moved. This can happen when the text flow preceding the insertion point expands.
* **Absolute**  
   The component will be located at the position specified by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance it is not affected by having text inserted before it.

To change the position property of a component, select on the component to select it, then:

* Right-click on the component and on the shortcut menu, select the required item from the Position submenu.
* In the Inspector panel, set its Position property value as required.

**Note:** The position of an object in a banded object can only be Absolute.

## Deleting a Component

A component can be removed from the report if it is no longer required. To delete a component, right-click on the component and select **Delete** from the shortcut menu. If a message prompts asking for your confirmation, select **Yes** to confirm the removal.

You can also remove a KPI chart from its KPI by right-clicking the KPI and then selecting **Remove KPI Chart** from the shortcut menu.

**Note:** In a web report, there must be one and only one tabular, so you cannot either insert another tabular or delete the current tabular.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components)
