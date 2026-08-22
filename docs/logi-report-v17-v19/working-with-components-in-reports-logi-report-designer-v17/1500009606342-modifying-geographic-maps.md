---
title: "Modifying Geographic Maps"
id: 1500009606342
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606342-Modifying-Geographic-Maps
updated_at: 2021-07-24T16:05:14Z
---

# Modifying Geographic Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606322-Example-Using-Geographic-Map)

# Modifying Geographic Maps

For any geographic map in a report, you can further modify it at any time. For example you can change and filter the data displayed in the geographic map, apply conditional formats on the map markers to highlight important values.

This topic introduces modifying a geographic map as follows:

* [Editing a Geographic Map with Wizard](#Edit)
* [Adding Conditional Formats to the Map Markers](#Format)

## Editing a Geographic Map with Wizard

Once a geographic map has been created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the geographic map. For example, you can change the data source the geographic map uses, edit the data displayed on the map, and so on.

1. Right-click the geographic map and select **Geographic Map Wizard** from the shortcut menu to display the [Geographic Map Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009608742-Geographic-Map-Wizard-Dialog).
2. In the Data screen, you can specify a new data source for the geographic map.
3. For a geographic map in a web report or library component, edit the data displayed on the map in the Display screen.

   For a geographic map in a page report, edit the group settings, layout mode and marker properties in the Group, Layout and Marker screens respectively.
4. Select **Finish** to accept the changes.

For more detailed information about defining a geographic map, refer to [Inserting Geographic Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report).

## Adding Conditional Formats to the Map Markers

After a geographic map is created, each value in a group is bound with a marker. You can add conditional formats to the markers, then when a specified condition is fulfilled, the format bound with the condition will be applied to the markers automatically. This is very useful to highlight values that might need to be acted on by the end user.

**To add conditional formats to the markers in a geographic map:**

1. Select the geographic map and then do one of the following:
   * Select **Format** > the **Conditional Formatting** button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404904160663/btn_cndtnlfmt.gif).
   * Right-click the geographic map and select **Conditional Formatting**  from the shortcut menu.

   The [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009630061-Conditional-Formatting-Dialog#GMap) dialog appears.

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904386327/cndtnlfmt_gmp.gif)
2. Select a group level from the Geographic Map box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Condition box. The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904187799/edtcndtn.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the condition will be based.
5. Choose the operator with which to compose the condition expression from the operator drop-down list.
6. From the value drop-down list, select the value of how to build the condition. You can also type in the value manually.

   ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

   The newly added condition is then displayed in the Condition box of the Conditional Formatting dialog.
9. In the Marker box, specify the settings which will be applied to the marker of the selected group level when the condition is fulfilled, including the image, the shadow image, and their width and height. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, select **Constrain Proportion**.
10. Repeat the above steps to add more conditions and define the marker properties for each condition.

    To edit a condition, select the condition from the Condition box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif), then edit the condition in the Edit Conditions dialog.

    To adjust the priority of the conditions, select a condition and select the **High** or **Low** button.

    To remove a condition and the corresponding marker properties, select the condition from the Condition box and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
11. Select **OK** to save and apply the settings.

**Note:** For a geographic map in a web report or library component, the conditional format settings have higher priority than the settings defined for the Shape By, Color By and Size By options in the map wizard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606322-Example-Using-Geographic-Map)
