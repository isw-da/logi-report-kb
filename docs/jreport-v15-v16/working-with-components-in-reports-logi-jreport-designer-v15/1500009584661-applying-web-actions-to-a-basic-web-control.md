---
title: "Applying Web Actions to a Basic Web Control"
id: 1500009584661
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control
updated_at: 2021-07-24T05:55:52Z
---

# Applying Web Actions to a Basic Web Control

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563922-Binding-a-Link-to-a-Basic-Web-Control)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584681-Making-Basic-Web-Controls-Work-in-a-Form)

# Applying Web Actions to a Basic Web Control

A web action can be bound to a basic web control, and then when the trigger event, such as select occurs, the web action will be performed. This allows you to customize a web control to make it respond to some events, and execute corresponding actions, such as sorting and filtering. For example, you can insert a button in Logi JReport Designer and associate an action with the button's onclick event. Then, when you view the report at runtime and select the button, the defined operation will be executed.

**To bind web actions to a basic web control:**

1. Right-click the web control and select **Display Type** from the shortcut menu.
2. In the Web Behaviors box of the Display Type dialog, choose an event from the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box.
3. In the Web Action List dialog, select the required action and then select **OK**.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) in the Display Type dialog to add more web behavior lines and specify the events and actions accordingly. If a web behavior is not required, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.
5. Adjust the order of the added web actions by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif). Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
6. When done , select **OK** to accept the settings.

For more information about web actions, see [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

## Example of Applying Web Actions

In the following example, a sample report is built for guiding you through the process of using web controls and applying web actions step by step.

**Step 1: Create the sample report**

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report)  which is based on the query WorldWideSales in Data Source 1 of the catalog, shows the following detail fields: Country, Product Type Name, Product Name, Unit Price, Quantity, Discount, and the formula Total ( `@"Unit Price" * @Quantity - @"Unit Price" * @Quantity * @Discount/100`), applies the filter "COUNTRY = China AND PRODUCT TYPE NAME = Decaf", and uses the Classic style.
3. [Insert a crosstab into the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab) and place it below the banded object. The crosstab shares the same dataset with the banded object, comprises the column field: Product Type Name, row field: Category, and aggregate field: Total (aggregate function: Sum) and applies the Classic style.
4. Select **View** > **Page Header** to have this panel visible, then set its Height property to **1.0** in the Report Inspector to hold all the web controls that will be inserted in the report later.
5. Save the report.

**Step 2: Apply a web action without parameters**

First, we want to allow the report user to select a button in the report to show the Search dialog of Page Report Studio. To achieve this:

1. Select the page header panel and select **Insert** > **Web Controls** >  **Button** to insert a Button web control in it.
2. Right-click the button, and select **Display Type** from the shortcut menu.
3. In the Web Behaviors box of the Display Type dialog, specify event to **Select**, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box.
4. In the Web Action List dialog, choose **user\_showSearchDialog** to be web action of the button, then confirm the settings.
5. Go to the Report Inspector and set the Text property of this button to **Search**.
6. Save the report.

**Step 3: Apply a web action with parameters**

Now we want to allow the report user to rotate the crosstab in the report and to change the report style.

1. Insert another Button web control in the page header panel of the report and place it next to the Search button.
2. Specify the **Select** event and **user\_rotateCrosstab** action to the button as explained above, then set **&CT Crosstab** to be the value of the action parameter instanceName (CT Crosstab is the name of the crosstab we can see in the report structure panel of the Report Inspector, and here the symbol & shall be prefixed to the crosstab name).
3. In the Report Inspector, edit the Text property of the button to **Rotate Crosstab**.
4. Insert a Label object in the page header panel and place it below the two buttons, then resize the label and edit its text to "**Change Report Style To:**".
5. Insert a Drop-down List web control next to the label.
6. Right-click the drop-down list and select **Display Type** shortcut menu.
7. In the Display Type dialog, add these items and corresponding values to the drop-down list (to add an item line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)):

   | Item Label | Value |
   | --- | --- |
   | Classic | Classic |
   | Classic Blue | ClassicBlue |
   | Classic Green | ClassicGreen |
   | Default | Default |
   | None | None |

   Then, in the Web Behaviors box of the dialog, set Event to **Data Change**, Action to **user\_changeStyleTo**, and specify the value for the web action parameter styleName to **this.value**.

   ![Web Cintrol Action parameter](https://devnet.logianalytics.com/hc/article_attachments/4404893973911/cmpnt_wbcntrl_basic_actn_eg0.gif)
8. Save the report.

**Step 4: Apply a web action with the Builder Wizard**

The actions Filter, Sort and Parameter have a Builder Wizard. Now we would like to use the wizard to allow the report user to sort records in the banded object by one of the specified fields.

1. Insert another Drop-down List web control into the page header panel, and place it below the above web controls. The drop-down list is displayed as MultiValueContainer1 in the Report Inspector.
2. Right-click the drop-down list and select **Display Type** shortcut menu.
3. In the Display Type dialog, add these items and corresponding values to the drop-down list:

   | Item Label | Value |
   | --- | --- |
   | Unit Price | UNIT PRICE |
   | Quantity | QUANTITY |
4. Insert a List web control next to the drop-down list. The list is displayed as MultiValueContainer2 in the Report Inspector.
5. In the Display Type dialog for this list, add these items and corresponding values:

   | Item Label | Value |
   | --- | --- |
   | Ascending | Ascending |
   | Descending | Descending |
6. Insert a Button web control and place it next to the list, then right-click the button and select **Display Type** on the shortcut menu.
7. In the Display Type dialog, specify Event to **Select** and Action to **Sort**, then in the Sort - Web Action Builder dialog, select **MultiValueContainer1** from the Sort On column, and **MultiValueContainer2** from the Sort Value column. Confirm the settings, and go to the Report Inspector to modify the Text property of the button to **Sort**.
8. Save the report.

**Step 5: Preview the report in Page Report Studio and applying the web actions**

1. Select **View** > **Preview As** > **Page Report Result** to preview this report in Page Report Studio.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893974167/cmpnt_wbcntrl_basic_actn_eg1.gif)
2. Select the **Search** button and the Search dialog appears.
3. Select the **Rotate Crosstab** button, the columns and rows of the crosstab are rotated.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893974423/cmpnt_wbcntrl_basic_actn_eg2.gif)
4. Select a style from the Change Report Style To drop-down list, for example, select **Classic Green**, and the report style now changes to the selected one. It affects both the banded object and the crosstab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893974807/cmpnt_wbcntrl_basic_actn_eg3.gif)

   **Note:** You may notice that the value of the drop-down list does not change to the selected one after the report style is updated. To update the drop-down list value to the current report style, you need to append another action user\_changeCompProperty to the event Data Change to the drop-down list.
5. Select a field name from the third drop-down list and then the sorting direction from the list. Here we select **Unit Price** and **Descending** respectively, then select the **Sort** button.

   The records in the banded object now are sorted based on the Unit Price values descending.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889400215/cmpnt_wbcntrl_basic_actn_eg4.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563922-Binding-a-Link-to-a-Basic-Web-Control)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584681-Making-Basic-Web-Controls-Work-in-a-Form)
