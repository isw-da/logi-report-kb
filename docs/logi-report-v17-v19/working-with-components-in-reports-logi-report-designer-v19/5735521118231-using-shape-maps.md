---
title: "Using Shape Maps"
id: 5735521118231
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps
updated_at: 2022-11-02T04:13:14Z
---

# Using Shape Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521085463-Example-Using-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)

# Using Shape Maps

A shape map is a special kind of image in Logi Report that contains a picture and certain areas bound with groups in a banded object. This topic introduces how you can create shape maps in a report, and bind data and add conditional formatting to shape maps.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)Logi Report supports the Shape Map feature only in query-based page reports and it works when the page reports run in HTML or in Page Report Studio.

This topic contains the following sections:

* [Creating Shape Maps in a Page Report](#Create)
* [Binding Data to Shape Maps](#BindData)
* [Adding Conditional Formatting to Shape Map Areas](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the shape map component example, open `<install_root>\Demo\Reports\SampleComponents\MapReport.cls`.

## Creating Shape Maps in a Page Report

1. Select a tabular cell, or the banded header/footer, group header/footer, or banded page header/footer of a banded object in the page report.
2. Do one of the following:
   * From the **Components** panel, drag the **Shape Map** icon ![Insert Shape Map icon](https://devnet.logianalytics.com/hc/article_attachments/9898478571159/icon_shpmap.gif) in the **Visual** category to the destination.
   * Navigate to **Insert** > **Map** > **Shape Map**.
   * Navigate to **Home** > **Insert** > **Map** > **Shape Map**.

   Designer displays the [Shape Map Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523889559-Shape-Map-Editor-Dialog-Box).

   ![Shape Map Editor window](https://devnet.logianalytics.com/hc/article_attachments/9898461533719/mpedtr.gif)
3. To use an image as background of the map, navigate to **Menu** > **Insert** > **Background Image**. In the Shape Map Background Image dialog box, select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the image and select **OK**.
4. Next is to add areas to the map. You can do this either by [importing predefined map areas](#Import), or by [drawing the areas manually](#Draw), or using a combination of these two.
   * To import map areas from an previously saved XML file or an ESRI file that contains area information, navigate to **Menu** > **File** > **Open**, then in the Import Shape Map Area dialog box, specify the .xml or .shp file that contains the required area information and select **Open** to import the areas. If you choose to import the map areas from a .shp file, Designer displays the [Select Area Name dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515425303-Select-Area-Name-Dialog-Box), prompting you to further specify the field in the ESRI shape file using which to define the area names and the fields from which to get the area tool tip. The tool tip displays when you hover the mouse over the areas when the report runs in HTML or in Page Report Studio.

     ![Select Area Name dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477981591/slctareanm.gif)

     **To define the tool tip of the map areas**
   1. Select a field from the field box the values of which you want to display in the tool tip and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif).
   2. Repeat the preceding step to add more fields.
   3. Adjust the order of the fields in the **Tips** box by selecting a field and selecting **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). The order of the fields determines the display sequence of their values in the tool tip.
   4. To delete a field from the tool tip, select it in the Tips box and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The area tool tip can display only when you set the [Alternate Content Type](https://devnet.logianalytics.com/hc/en-us/articles/5735554918935-Shape-Map-Properties#Type) property on the map object to "customized".

   * To draw the areas manually, select **Insert Mode** on the toolbar, or navigate to **Menu** > **Edit** and select **Insert Mode** to switch the Shape Map Editor to the mode.
     Then, to draw an area, select the left mouse button to pick the start point of the area. Move the mouse pointer and select the left mouse button to select the other points. Designer connects the points automatically. When you move the mouse pointer to the start point, a square appears indicating that the area is closed. Select the left mouse button to finish drawing the area. If you want to undo your last line, select the right mouse button.

     ![Draw an Area](https://devnet.logianalytics.com/hc/article_attachments/9898534547991/cmpnt_map_shp_inst.gif)
5. If you want to further change the shape or position of the areas, select **Insert Mode** on the toolbar again to switch the Shape Map Editor to edit mode.
   * To change the shape of an area, move the mouse pointer over the border or the points of the area. When it becomes a cross, choose a point on the line and drag it to create a new point. You can also choose a point of the area and drag it to a new position. If there are three points on one line, Designer deletes the middle point automatically.
   * To move an area, move the mouse pointer close its border. When it changes to a four-headed arrow, drag the area to a new position.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you have specified a background image for the map, and its size is not the same as that of the map object, you can navigate to Menu > Insert > Match Background Image in the Shape Map Editor dialog box to resize the map object to make it match the size of the background image.
6. [Bind data to the map areas](#BindData) so as to show values on the areas.
7. [Add conditional formatting to the map areas](#Format).
8. [Link the map areas to different targets](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report) (to add a link to a map area, right-click it and select **Link** from the shortcut menu).
9. In the **Map Area Inspector** panel, edit [properties](https://devnet.logianalytics.com/hc/en-us/articles/5735523889559-Shape-Map-Editor-Dialog-Box#Properties) of any area, label, summary, and line in the map. For labels and summaries, you can also edit their background color, foreground color, and font properties by using the corresponding buttons on the toolbar of the Shape Map Editor dialog box.
   * For areas, labels, and summary fields, you can specify the properties globally and apply the global settings to individual ones conveniently. To specify area, label, or summary field properties globally, select the corresponding subnode under the **Map Global Setting** node in the Map Area Inspector tree, then edit the property values accordingly.
   * To make a specific area, label, or summary field adopt the global settings, select it in the inspector tree, then set its **Use Global Setting** property to **true**.
   * To apply the global settings to all the areas, labels, or summary fields at a time, navigate to **Menu** >  **Edit** > **Reset All**, then in the [Reset All dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544182423-Reset-All-Dialog-Box), specify the properties according to your requirements.
10. To save the area information you have defined into a file for future use, navigate to **Menu** > **File** > **Save As** in the Shape Map Editor dialog box. In the Save Map Area dialog box, specify the directory where you want to save the file and a name for it, then select **Save**. Later when you create a report with a map, you can choose to import areas from the saved XML file.
11. Select **Save** to save the changes to the map and close the Shape Map Editor dialog box.
12. Select in the tabular cell or banded panel to insert the map.

Designer inserts the shape map in the specified destination. You can further edit it using the Shape Map Editor dialog box (to display the dialog box again, right-click the shape map and select **Format Shape Map** on the shortcut menu.

## Binding Data to Shape Maps

When you create a shape map, you can bind it with a dataset so you can show values on the map areas.

1. In the Shape Map Editor dialog box, select **Bind Data** on the toolbar, or navigate to **Menu** > **Insert** > **Bind Data**. Designer displays the [Shape Map Data Binding Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523877527-Shape-Map-Data-Binding-Wizard-Dialog-Box). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
2. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to bind to the
   shape map.

   ![Shape Map Data Binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898461576087/mpdtbdingwzd_dt.gif)
3. In the **Group** screen, add a field as the group-by field to group data of the specified dataset. You can add only one group for the dataset. You can specify the sort manner, special function, Select N condition, and filter condition on the group respectively. For more information, see related sections in [Grouping Data in Tables](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables).

   ![Shape Map Data Binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/9898461615511/mpdtbdingwzd_grp.gif)
4. In the **Summary** screen, add summaries to calculate data based on the specified group. To add a summary, select a field in the Resources box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif), then from the **Aggregate Function** drop-down list, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) you need. Designer then calculates data in each group based on the added field using the specified function, and displays the summary result accordingly on map areas the names of which match with values of the group-by field. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.

   ![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898461623703/mpdtbdingwzd_sum.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer adds the summaries created from the Summary screen to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Create).
5. In the **Filter** screen, filter the data to display on the map areas by adding conditions based on the group-by field and the summaries. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898461632279/mpdtbdingwzd_fltr.gif)
6. Select **Finish** to apply the settings and close the dialog box.

## Adding Conditional Formatting to Shape Map Areas

When a shape map is [bound with a dataset](#BindData), you can add conditional formatting to the map areas, so the areas that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight the values that users may need to act on at runtime.

1. In the Shape Map Editor dialog box, select **Conditional Formatting**![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/9898421373463/btn_cndtnlfmt.gif) on the toolbar, or navigate to **Menu** > **Format** > **Conditional Formatting**. Designer displays the [Shape Map Area Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514815511-Shape-Map-Area-Condition-Formatting-Dialog-Box).

   ![Shape Map Area Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478711063/mpcndtnlfmt.gif)
2. Select **Add**. Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box).

   ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457026967/edtcndtn.gif)
3. Select **Add Condition** to add a condition line.
4. From the field drop-down list, select the field on which the condition is based.
5. Choose the operator with which to compose the condition from the operator drop-down list.
6. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) next to the value box to specify the value of how to build the condition. You can also type the value manually.
   When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
7. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
   * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
   * To take out any condition or group from a group, select it and select **Ungroup**.
   * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
   * To delete a condition line, select it and select **Delete**.
8. Select **OK** to save the condition and close the dialog box. Designer displays the newly added condition and selects it in the **Map Area Condition** box in the Map Area Conditional Formatting dialog box.
9. In the **Format** box, specify the formatting you want to apply to the map areas that meet the condition, including the fill color, border color, border style, and border width.
10. Repeat the preceding steps to add more conditions and define the area formatting for each condition.
11. You can further modify the conditions.
    * To edit a condition, select the condition from the Map Area Condition box, select **Edit**, then edit the condition in the Edit Conditions dialog box.
    * To adjust the priority of the conditions, select a condition and select **High** or **Low**.
    * To remove a condition and the corresponding formatting, select the condition from the Map Area Condition box and then select **Remove**.
12. Select **OK** to save and apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The conditional formatting you specify to the shape map areas corresponds with some formulas. After you save the map and the corresponding catalog, and then load the catalog again, you can find that Designer creates some formulas in the catalog. You can edit the formulas, but Designer does not reflect the changes you make to the formulas in the Shape Map Area Conditional Formatting dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521085463-Example-Using-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)
