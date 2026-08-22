---
title: "Modifying Geographic Maps"
id: 1500010057362
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057362-Modifying-Geographic-Maps
updated_at: 2021-07-23T19:14:47Z
---

# Modifying Geographic Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094781-Inserting-Geographic-Maps-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057322-Example-Using-Geographic-Map)

# Modifying Geographic Maps

For any geographic map in a report, you can further modify it at any time. This topic introduces how you can change the data displayed in a geographic map, and apply conditional formats on the map markers to highlight important values.

This topic contains the following sections:

* [Editing a Geographic Map with Wizard](#Edit)
* [Adding Conditional Formats to the Map Markers](#Format)

## Editing a Geographic Map with Wizard

You can further modify a geographic map by accessing its shortcut menu wizard which contains a set of screens that are similar to the wizard screens used to create the geographic map. For example, you can change the data source the geographic map uses, edit the data displayed on the map, and so on.

1. Right-click the geographic map and select **Geographic Map Wizard** from the shortcut menu. Designer displays the [Geographic Map Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059462-Geographic-Map-Wizard-Dialog-Box).
2. In the **Data** screen, you can specify a new data source for the geographic map.
3. For a geographic map in a web report or library component, edit the data displayed on the map in the **Display** screen.

   For a geographic map in a page report, edit the group settings, layout mode and marker properties in the **Group**, **Layout**, and **Marker** screens respectively.
4. Select **Finish** to accept the changes.

For more information about defining a geographic map, refer to [Inserting Geographic Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010094781-Inserting-Geographic-Maps-in-a-Report).

## Adding Conditional Formats to the Map Markers

Each value in a group of a geographic map is bound with a marker. You can add conditional formats to the markers, then when a specified condition is fulfilled, Logi Report applies the format bound with the condition to the markers automatically. This is very useful to highlight the values that the report users may need to act on.

**To add conditional formats to the markers in a geographic map:**

1. Select the geographic map and then do one of the following:
   * Select **Format** > the **Conditional Formatting** button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404856793111/btn_cndtnlfmt.gif).
   * Right-click the geographic map and select **Conditional Formatting**  from the shortcut menu.

   Designer displays the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058242-Conditional-Formatting-Dialog-Box#GMap).

   ![Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848624663/cndtnlfmt_gmp.gif)
2. Select a group level in the **Geographic Map** box.
3. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif). Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box).

   ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856829207/edtcndtn.gif)
4. Select the **Add Condition** button to add a condition line.
5. From the field drop-down list, select the field on which the condition is based.
6. Choose the operator with which to compose the condition expression from the operator drop-down list.
7. From the value drop-down list, select the value of how to build the condition. You can also type the value manually.

   You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
8. Repeat steps 4 to 7 to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

   To group some condition lines, select them and select the **Group** button, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select the **Up** or **Down** button; to delete a condition line, select it and select the **Delete** button.
9. Select **OK** to save the condition and close the dialog box.

   Designer displays the newly added condition in the **Condition** box of the Conditional Formatting dialog box.
10. In the **Marker** box, specify the settings which you want to apply to the marker of the selected group level when the condition is fulfilled, including the image, the shadow image, and their width and height. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, select **Constrain Proportion**.
11. Repeat the above steps to add more conditions and define the marker properties for each condition.

    To edit a condition, select the condition from the Condition box, select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif), then edit the condition in the Edit Conditions dialog box.

    To adjust the priority of the conditions, select a condition and select the **High** or **Low** button.

    To delete a condition and the corresponding marker properties, select the condition from the Condition box and then select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
12. Select **OK** to save and apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) For a geographic map in a web report or library component, the conditional format settings have higher priority than the settings defined for the Shape By, Color By, and Size By options in the map wizard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094781-Inserting-Geographic-Maps-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057322-Example-Using-Geographic-Map)
