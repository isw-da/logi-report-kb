---
title: "Predefining Sort and Filter Conditions"
id: 1500009570962
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570962-Predefining-Sort-and-Filter-Conditions
updated_at: 2021-07-24T05:53:47Z
---

# Predefining Sort and Filter Conditions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels)

# Predefining Sort and Filter Conditions

You can predefine sort and filter conditions for the data components banded objects, tables, charts and crosstabs in page reports, so that when the page reports are published to Logi JReport Server and are loaded in Page Report Studio, data in the components will be displayed in the order you prefer, or be narrowed down as you desire.

**To predefine sort conditions for a data component:**

1. Select the component to which the sort conditions will apply.
2. Select **Report** > **Edit Sort & Filter** to show the [Edit Sort and Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565402-Edit-Sort-and-Filter-Dialog) dialog. The Sort tab is active by default.

   ![Edit Sort and Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893808023/edtsrtfltr_srt.gif)
3. In the Fields box, all the fields in the dataset the component uses are displayed. Select the field by which to sort the data from the box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Sort By box. To sort by two or more fields, select all of them and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif).
4. To modify the sorting direction for a field, select ![Sort Ascending dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893808279/btn_srtasnd.gif) (ascending) or ![Sort Descending dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893808535/btn_srtdsnd.gif) (descending) in the Direction column.
5. To change the sorting priority of the fields, select the field in the Sort By box, and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to move it up or down.
6. Select **OK** to accept the settings.

**To predefine filter conditions for a data component:**

1. Select the component to which the filter conditions will apply.
2. Select **Report** > **Edit Sort and Filter** to show the Edit Sort and Filter dialog, then switch to the **Filter** tab.

   ![Edit Sort and Filter dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893809047/edtsrtfltr_fltr.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the filter will be based.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value combo box, type the value of how to filter the field or select the value from the drop-down list.
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

**Notes:**

* If the Customize Display Name feature hasn't been applied to the dataset on which the component is created, when you open the Edit Sort and Filter dialog, there will be no fields displayed either in the Fields box of the Sort tab or the field drop-down list in the Filter tab, in which case, you need to select the Edit Display Name button in the dialog first to enable the feature on the dataset. You can also [modify the display names](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names) in the Edit Display Name dialog if desired.
* The predefined sort and filter conditions will also affect the preview result in Logi JReport Designer, and the result produced from being run in other formats besides Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels)
