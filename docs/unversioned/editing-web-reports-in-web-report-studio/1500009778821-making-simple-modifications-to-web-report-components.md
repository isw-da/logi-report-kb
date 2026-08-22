---
title: "Making Simple Modifications to Web Report Components"
id: 1500009778821
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components
updated_at: 2021-07-24T00:47:30Z
---

# Making Simple Modifications to Web Report Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report)

# Making Simple Modifications to Web Report Components

This topic describes the general actions that you can perform on the web report components: move, resize, show, hide, edit, and delete a component, and more.

This topic contains the following sections:

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

When the [Position](#Position) property of a component is **absolute**, you can move it to another place in the current container freely. To move a component, hover the mouse pointer on the component, when Server displays the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404880145943/btn_pgrpt_drag.gif) at the top right, drag the icon to the destination and then drop.

## Resizing a Component and Its Elements

To resize a component, select anywhere in the component, then you will see it is surrounded by a rectangle with resizing handles. Point to a handle, when the mouse pointer turns to a double-headed arrow, you can drag the handle to resize the component. When the width or height of a component is fully displayed, you cannot further enlarge the right or bottom boundary.

![Resize Component](https://devnet.logianalytics.com/hc/article_attachments/4404880159383/wbrpt_edt_mdfy_resize.gif)

To adjust the width of a column in a table, select anywhere in the column, then select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404880149783/btn_wbrpt_slctclmn.gif) that Server displays on the column header to select the column. Point to the left or right boundary of the column, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the column.

![Resize Column](https://devnet.logianalytics.com/hc/article_attachments/4404880159639/wbrpt_edt_mdfy_width.gif)

To adjust the row height in a table, select anywhere in the row, then select the button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404880149015/btn_wbrpt_slctrow.gif) that Server displays at the leftmost on the row to select the row. Point to the upper or lower boundary of a row, when the mouse pointer becomes a double-headed arrow, drag the handle to resize the row height. Then Server resizes all the other rows of the same role too. For example, if you resize a detail row, Server resizes all rows in the detail area. If you resize a group row, Server resizes all rows of the group, while the other groups' rows keep unchanged.

To resize the column or row in a crosstab, drag the right or lower boundary. Then all the columns or rows of the same role change too.

To adjust the panel height in a banded object, select the panel and drag the lower boundary of the panel until the panel is at the required height.

For a tabular, point to the boundary between two cells until the mouse pointer becomes a double-headed arrow, then drag the boundary to adjust the size of the related cells.

## Hiding/Showing a Component

To hide a component, right-click on the component, then select **Hide** on the shortcut menu.

To show the hidden components, go to **Menu** > **Edit** > **Unhide Components** drop-down list and then select the desired components to show.

You can also set the **Invisible** property in the **Inspector** panel to show or hide a component. To do this, select the node that represents the component in the report structure tree in the Inspector panel, then set its **Invisible** property to **false** or **true**. If the parent of the component has no data source, you can select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) in the value cell and [select a formula](#Formula) from the value drop-down list, or select **<Edit Expression>** to create an expression using the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties) to control whether to show the component.

**Using formulas to control showing or hiding components**

You can use formulas to control whether to show the components whose parents have no data source in a web report. However, before doing this, you need to first bind a data source to the web report, then create dynamic formulas of Boolean type based on this data source and use these formulas to control the Invisible property of the required components. A return value of true will hide the component.

To use formulas to control which components to show in a web report, follow the steps below:

1. Select **Menu** > **Edit** > **Bind Data**. Server displays the [Bind Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009774901-Bind-Data-Dialog-Box-Properties) dialog box.

   ![Bind Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880160151/bddt.gif)
2. Select a business view in the current catalog.
3. Select **OK** to bind the business view to the web report.
4. Select any blank place in the report. Server displays the business view bound to the report in the **Resources** panel.
5. Follow the steps in [Creating and using dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#DynamicFormula) to create the formulas you need.
6. In the **Inspector** panel, select the icon ![Show Report Structure Tree](https://devnet.logianalytics.com/hc/article_attachments/4404885328919/btn_mvdown1.gif) on the upper right corner to show the report structure tree.
7. Select the node that represents the component in the tree.
8. In the **Properties** sheet, select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) in the value cell of the **Invisible** property.
9. Select the required formula from the drop-down list, or select **<Create Formula>** in the drop-down list and create a dynamic formula in the bound data source to control the property value.
10. Repeat the above steps to set the **Invisible** property of other components.

Then the return values of the specified formulas determine whether to show the components.

If you set the **Invisible** property of a component to **true** using a formula, Server does not lists the component in the Menu > Edit > Unhide Components drop-down list. You can only show it by setting the **Invisible** property of the component to **false**. Meanwhile, once you control the Invisible property of a component in a web report by a formula, you cannot change the data source bound to the web report unless you remove the relationship between the formula and the property.

For a web report that you created in Logi Report Designer, if you have bound it with a data source before you published it to Logi Report Server, and you have created some dynamic formulas based on this data source:

* If the web report used any of the formulas in Logi Report Designer, you cannot change the bound data source for the web report in Web Report Studio. However, you can use the formulas of Boolean type created in Logi Report Designer or create new formulas based on this data source to control the Invisible property.
* If the web report used none of the formulas in Logi Report Designer, you can change the bound data source for the web report in Web Report Studio as you want.

## Editing a Component

* To edit a label, double-click the text and update the content. You can also use the toolbar to format the font, background color, and alignment of a label.
* To edit a table, crosstab, or chart, use the corresponding component wizard on the shortcut menu. For more information, see [Manipulating Data Components in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report).
* To edit a banded object, select it, select the **Edit Template** icon ![Edit Template button](https://devnet.logianalytics.com/hc/article_attachments/4404880142871/btn_wbrpt_edt.gif) on the visualization toolbar, and then modify the template. For more information, see [Manipulating Data Components in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report).
* **To edit an image:**
  1. Right-click on the image and select **Edit** from the shortcut menu. Server displays the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009775161-Edit-Image-Dialog-Box-Properties) dialog box.

     ![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885329431/edtimg.gif)
  2. Specify another image to use.
     + To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
     + To use an image on a website, select **Web URL**, then type the image URL or paste the URL in the **File URL** text box.
     + To use an image in the image library of Web Report Studio, select **Library**, then select the image in the **My Pictures** box.
  3. Select **OK** to finish editing the image.
* **To edit a multimedia object:**
  1. Right-click on the multimedia object and select **Edit** from the shortcut menu. Server displays the [Edit Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009747022-Edit-Multimedia-Dialog-Box-Properties) dialog box.

     ![Edit Multimedia dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880160791/edtmultmda.gif)
  2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
  3. In the **File Name/URL** text box, specify the full path of the multimedia object you want to insert or select the **Browse** button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
  4. The **Plug-in Page** text box provides a default URL from which to download the player to play the inserted multimedia object on a web page.
  5. In the **Properties** box, specify the properties for the multimedia object.
  6. Select **OK** to finish editing the multimedia object.
* For a tabular, you can edit it as follows:
  + **Merging tabular cells**  
    You can merge adjacent cells in a tabular which form a rectangle into one cell.

    To merge adjacent cells, select them one by one while holding the **Ctrl** key, then select **Menu** > **Format** > **Merge** or select the **Merge** button ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404880140567/btn_wbrpt_merge.gif) on the toolbar. Server merges these cells into one cell.
  + **Splitting a tabular cell**  
     To split a tabular cell, select the cell and select **Menu** > **Format** > **Split**. Server displays the [Split Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009748082-Split-Cell-Dialog-Box-Properties) dialog box. Type the number of rows and columns and select **OK**. You can also select the **Split** button ![Split button](https://devnet.logianalytics.com/hc/article_attachments/4404885310615/btn_wbrpt_split.gif) on the toolbar to split the cell into two cells vertically or horizontally.

## Modifying Component Properties

You can modify the component properties using either the corresponding properties dialog box or the Inspector panel.

For some properties you may see a formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) on the right of the value cell, which means that you can control the property value by a formula dynamically. Select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880161431/btn_fmla.gif) and then select the drop-down arrow in the value cell. Server displays a drop-down list. You can then select an existing formula in the list or select **<Edit Expression>** to create an expression with the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties) as the property value.

### Modifying Properties Using Dialog

To edit the properties of a component in a report, right-click it and select **Properties** from the shortcut menu (for a table row, you need to first select anywhere in the row and then select the button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404880149015/btn_wbrpt_slctrow.gif) that Server displays at its leftmost to select the row. Then you can right-click on the row to get the **Properties** command on the shortcut menu). In the corresponding properties dialog box, specify the settings. For more information about the properties dialog boxes, see the specific topics in [Web Report Studio Dialog Boxes](https://devnet.logianalytics.com/hc/en-us/articles/1500009746662-Web-Report-Studio-Dialog-Boxes).

If you want to format the properties of the report, select **Menu** > **Edit** > **Report Body Properties**. Server displays the [Report Body Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009776201-Report-Body-Properties) dialog box. Configure the properties as you want.

### Modifying Properties in the Inspector Panel

The Inspector panel of Web Report Studio is for managing properties of the objects in a web report. To display the panel, select **Menu** > **View** > **Inspector**.

To edit the properties of an object with the Inspector panel, first select the object in the report, or select the icon ![Show Report Structure Tree](https://devnet.logianalytics.com/hc/article_attachments/4404885328919/btn_mvdown1.gif) on the upper right corner of the Inspector panel to show the report structure tree and then select it from the tree. Server displays all properties of the selected object in the Properties sheet which contains two columns: **Name** and **Value**. Each type of object has its own set of properties. Depending on the object type, the properties that a certain object holds may greatly differ from those of another. You can change how an object appears and behaves by editing its property values. For more information, see [Web Report Object Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009749122-Web-Report-Object-Property-Reference).

When a report contains a lot of objects, you can make use of the search bar at the top of the report structure tree panel to easily locate an object in the tree.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

## Changing the Position Property of Components

Report templates in Web Report Studio use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, tabular cells themselves in Web Report Studio can also act as flow layout containers.

In a flow layout model, Server positions objects relative to one another or absolutely. The **Position** property controls the position of components in the flow layout container. It does not affect components in other areas such as table cells.

You can set the Position property to one of the following values:

* **Static**  
   Server positions the component at the location where you inserted it. It disables the X and Y coordinate properties. You cannot move the position of the component other than by having its insertion point moved. This can happen when the text flow preceding the insertion point expands.
* **Absolute**  
   Server locates the component at the position that you specified by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance by inserting text before it.

To change the position property of a component, select on the component to select it, then:

* Right-click on the component and on the shortcut menu, select the required item from the **Position** submenu.
* In the Inspector panel, set its **Position** property value.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The position of an object in a banded object can only be **Absolute**.

## Deleting a Component

You can remove a component from the web report if you no longer need it. To delete a component, right-click on the component and select **Delete** from the shortcut menu. If Server prompts a message asking for your confirmation, select **Yes** to confirm the removal.

You can also remove a KPI chart from its KPI by right-clicking the KPI and then selecting **Remove KPI Chart** from the shortcut menu.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)In a web report, when there is already one tabular, you cannot either insert another tabular or delete the current tabular.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report)
