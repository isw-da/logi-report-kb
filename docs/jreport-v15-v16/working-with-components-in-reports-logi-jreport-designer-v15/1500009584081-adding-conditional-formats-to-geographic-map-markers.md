---
title: "Adding Conditional Formats to Geographic Map Markers"
id: 1500009584081
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers
updated_at: 2021-07-24T05:56:00Z
---

# Adding Conditional Formats to Geographic Map Markers

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563482-Example-of-Using-Geographic-Map)

# Adding Conditional Formats to Geographic Map Markers

After a geographic map is created, each value in a group is bound with a marker. You can add conditional formats to the markers, then when a specified condition is fulfilled, the format bound with the condition will be applied to the markers automatically. This is very useful to highlight values that might need to be acted on by the end user.

However, for geographic maps in web reports and library components, the conditional formats are applied based on the [advanced settings of the Shape By option](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map#Image), in other words, when the marker shape is controlled by image. If you apply conditional formats to a geographic map the shape of which is controlled by field or shape, the field or shape that you specified to the Shape By option will be ignored after the conditional formats take effect.

**To add conditional formats to geographic map markers:**

1. Select the geographic map and then do one of the following:
   * Select **Format** > the **Conditional Formatting** button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404889280535/btn_cndtnlfmt.gif).
   * Right-click the geographic map and select **Conditional Formatting**  from the shortcut menu.

   The [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009585901-Conditional-Formatting-Dialog#GMap) dialog appears.

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893948951/cndtnlfmt_gmp.gif)
2. Select a group level from the Geographic Map box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the Condition box. The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893926679/edtcndtn.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the condition will be based.
5. Choose the operator with which to compose the condition expression from the operator drop-down list.
6. From the value drop-down list, select the value of how to build the condition. You can also type in the value manually.
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

   The newly added condition is then displayed in the Condition box of the Conditional Formatting dialog.
9. In the Marker box, specify the settings which will be applied to the marker of the selected group level when the condition is fulfilled, including the image, the shadow image, and their width and height. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, check **Constrain Proportion**.
10. Repeat the above steps to add more conditions and define the marker properties for each condition.

    To edit a condition, select the condition from the Condition box, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif), then edit the condition in the Edit Conditions dialog.

    To adjust the priority of the conditions, select a condition and select the **High** or **Low** button.

    To remove a condition and the corresponding marker properties, select the condition from the Condition box and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).
11. When done, select **OK** to save and apply the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563482-Example-of-Using-Geographic-Map)
