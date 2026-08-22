---
title: "Working with DBFields"
id: 1500010057202
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields
updated_at: 2021-07-23T19:14:45Z
---

# Working with DBFields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields)

# Working with DBFields

In a query-based report, the DBFields or database fields refer to fields directly from databases, user data sources, hierarchical data sources, or other data resources; in a business view-based report, they are the group and details objects in the business view. This topic introduces how you can insert DBFields in a report and use the DBField features.

For the DBFields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting DBFields in a Report](#Insert)
* [Adding Summaries for DBFields](#Add)
* [Adding Conditional Formats to DBFields](#Format)
* [Searching for DBFields in a Report](#Find)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the DBField component example, open `<install_root>\Demo\Reports\SampleComponents\ForDBField.cls`.

## Inserting DBFields in a Report

You can insert DBFields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).

* **For a business view-based report**  
  Select the group or detail object in the **Data** panel and drag it to the destination.
* **For a query-based report**  
   You have two ways to insert a DBField into a query-based report.
  + **By dragging and dropping**   
    Select a dataset from the dataset drop-down list in the Data panel, then select the required DBField and drag it to the destination.
  + **Using dialog box**
    1. Position the mouse pointer at the destination where you want to insert the DBField.
    2. Select **Insert** > **DBField** or **Home** > **Insert** > **DBField**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box).

       ![Insert Fields dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848523671/instfld.gif)
    3. Select a dataset from the dataset drop-down list. Designer then lists all resources in the selected dataset in the **DBField List** box.
    4. Select the required DBField and specify its layout in the **Insert Layout** box. You can select them one by one with the Ctrl key, or you can make a continuous selection with the Shift key.
    5. Select the **Insert** button to insert the DBField into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You cannot use the Insert Fields dialog box to insert a DBField into a crosstab.
* If you insert a DBField into the detail panel of a banded object or table, Designer adds the name of the DBField automatically into the corresponding header panel; otherwise, Designer places the field and its name label in the same panel. If you do not want Designer to insert the name label automatically, you can clear **Insert field name label with field** in the Options dialog box (File > Options > Component > Insert field name label with field).

## Adding Summaries for DBFields

In a query-based page report, you can add summaries for DBFields as follows:

1. Select a DBField, then do one of the following:
   * Select **Insert** > **Summary**.
   * Right-click the DBField and select **Summary Function** from the shortcut menu.

   Designer displays the [Insert Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059642-Insert-Summary-Dialog-Box).

   ![Insert Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856918167/instsum.gif)
2. From the **Aggregate Function** drop-down list, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) of the summary. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box.
3. If the report is grouped, select to which group level you want to apply the summary from the **Group By** drop-down list. If you select **None**, Designer adds the summary based on the whole report.
4. Select the **Insert** button.

   Designer then creates a summary with the default name "Function\_DBFieldName" in the current catalog. The summary is also available under the Summaries node in the Data panel. You can [drag it to use in the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields#Insert).

## Adding Conditional Formats to DBFields

You can add conditional formats to DBFields in a report, then when a specified condition is fulfilled, Logi Report applies the format defined on the condition to the field values automatically. This is very useful to highlight values that the report users may need to act on at runtime.

**To add conditional formats to a DBField:**

1. Select the DBField and then do one of the following:
   * Select the **Conditional Formatting** button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404856793111/btn_cndtnlfmt.gif) on the Format tab.
   * Right-click the DBField and select **Conditional Formatting**  from the shortcut menu.

   Designer displays the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058242-Conditional-Formatting-Dialog-Box).

   ![Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857004055/cndtnlfmt.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif). Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box).

   ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856829207/edtcndtn.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the condition is based. You can also select the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" or **Page Number** to compose the condition. If you select Page Number, Logi Report applies the format to the field values on the pages that meet the condition at runtime.
5. Choose the operator with which to compose the condition expression from the operator drop-down list.
6. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually.

   When you are adding conditional format to a DBField in a crosstab, you can also select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) and then select an object from the drop-down list to use its value in the condition. Designer provides the following objects that are of the same data type as the field on which the condition is based in the drop-down list:

   * [Crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010094701-Using-Crosstab-Formulas) if the crosstab uses a query resource
   * [Dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) and aggregation objects if the crosstab uses a business view

   You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
7. Repeat steps 3 to 6 to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

   To group some condition lines, select them and select the **Group** button, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select the **Up** or **Down** button; to delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

   Designer then displays and highlights the newly added condition in the **Condition** box in the Conditional Formatting dialog box.
9. In the **Format** box, set the format you want to apply to values of the DBField when the specified condition is fulfilled, such as the font face, font size, and font color. Select **Blinking Text** if you want to make the values blink, then in the **Duration** text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings can work in Designer view mode, in the HTML output of the report, and at runtime.
10. Repeat the above steps to add more conditions and define the format for each condition.

    To edit a condition, select the condition from the Condition box, select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif), then edit the condition in the Edit Conditions dialog box.

    To adjust the priority of the conditions, select a condition and select the **High** or **Low** button.

    To delete a condition and the corresponding format, select the condition in the Condition box and then select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
11. Select **OK** to save the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) To make the blink settings of a conditional format take effect in HTML output or at runtime, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, Chrome, and Internet Explorer 10 or above.

## Searching for DBFields in a Report

When a report has many DBFields, you may find it difficult to locate where a certain field is. To easily find out the field you have lost track of in your report, you can make use of the Find DBField feature.

**To find a DBField in a report:**

1. Select **Home**> **Find**. Designer displays the [Find dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096801-Find-Dialog-Box).

   ![Find dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848577559/find.gif)
2. Select the field you want to locate from the **Find What** drop-down list.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Besides DBFields, Designer also lists the [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields) used in the report in the Find What drop-down list, so you can also use this dialog box to locate a formula in a report.
3. Specify the criteria with which to find the field.
   * **Root**  
     Select to search for the field from the top node.
   * **Current Node**  
     Select to search for the field from the current node.
4. Select the **Find Next** button and Designer selects the specified field in the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields)
