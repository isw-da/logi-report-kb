---
title: "Working with DBFields"
id: 5735507243031
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields
updated_at: 2022-11-02T04:28:14Z
---

# Working with DBFields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields)

# Working with DBFields

In a query-based report, the DBFields or database fields refer to fields directly from databases, user data sources, hierarchical data sources, or other data resources; in a business view-based report, they are the group and details objects in the business view. This topic introduces how you can insert DBFields in a report and use the DBField features.

For the DBFields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report) if you want.

This topic contains the following sections:

* [Inserting DBFields in a Report](#Insert)
* [Adding Summaries for DBFields](#Add)
* [Adding Conditional Formatting to DBFields](#Format)
* [Searching for DBFields in a Report](#Find)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the DBField component example, open `<install_root>\Demo\Reports\SampleComponents\ForDBField.cls`.

## Inserting DBFields in a Report

You can insert DBFields in the report areas listed in [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type).

**For a business view-based report**

In the **Data** panel, select the group or detail object and drag it to the destination.

**For a query-based report**

You can insert a DBField into a query-based report using either of the following two methods:

* **By dragging and dropping**  
  In the **Data** panel, select a dataset from the dataset drop-down list, then select the DBField and drag it to the destination.
* **Using dialog box**
  1. Position the mouse pointer at the destination where you want to insert the DBField.
  2. Navigate to **Insert** > **DBField** or **Home** > **Insert** > **DBField**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530158487-Insert-Fields-Dialog-Box).

     ![Insert Fields dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898462184727/instfld.gif)
  3. Select a dataset from the dataset drop-down list. Designer then lists all resources in the specified dataset. However, if you are inserting DBFields into a data component, you should not change the dataset. You can only apply one dataset in a data component.
  4. Select the DBField you need. You can select multiple DBFields to insert them all at a time.
  5. When you select multiple DBFields, in the **Insert Layout** box, specify the layout of the DBFields in the report. By default, Designer arranges them in the default layout. You can arrange the DBFields horizontally or vertically by selecting **Horizontal** or **Vertical**, and customize the space between them.
  6. When you select multiple fields, specify how to arrange these fields in the **Insert Layout** box.
  7. Select **Insert** to insert the DBFields into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You cannot use the Insert Fields dialog box to insert a DBField into a crosstab.
* If you insert a DBField into the detail panel of a banded object or table, Designer adds the name of the DBField automatically into the corresponding header panel; otherwise, Designer places the field and its name label in the same panel. If you do not want Designer to insert the name label automatically, clear "Insert field name label with field" in the Component category of the Options dialog box.

## Adding Summaries for DBFields

In a query-based page report, you can add summaries for DBFields.

1. Select a DBField, then do one of the following:
   * Navigate to **Insert** > **Summary**.
   * Right-click the DBField and select **Summary Function** from the shortcut menu.

   Designer displays the [Insert Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551821719-Insert-Summary-Dialog-Box).

   ![Insert Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898462075159/instsum.gif)
2. From the **Aggregate Function** drop-down list, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) of the summary. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) next to the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.
3. When the report is grouped, select to which group level you want to apply the summary from the **Group By** drop-down list. If you select **None**, Designer adds the summary based on the whole report.
4. Select **Insert**.

Designer then creates a summary with the default name "Function\_DBFieldName" in the current catalog. The summary is also available under the Summaries node in the Data panel. You can [drag it to use in the report](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields#Insert).

## Adding Conditional Formatting to DBFields

You can add conditional formatting to DBFields in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

**To apply conditional formatting to a DBField**

1. Select the DBField and do one of the following:
   * Select **Conditional Formatting**![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/9898421373463/btn_cndtnlfmt.gif) in the Format ribbon.
   * Right-click the DBField and select **Conditional Formatting**  from the shortcut menu.

   Designer displays the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499987863-Conditional-Formatting-Dialog-Box).

   ![Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898532989335/cndtnlfmt.gif)
2. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif). Designer displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box).

   ![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457026967/edtcndtn.gif)
3. Select **Add Condition** to add a condition line.
4. From the field drop-down list, select the field on which to create the condition. You can also select the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" or **Page Number** to compose the condition. If you select Page Number, Server applies the formatting to the field values on the pages that meet the condition at runtime.
5. Choose the operator with which to compose the condition from the operator drop-down list.
6. From the value drop-down list, specify the value of how to build the condition. You can also type the value by yourself.
   * When you are adding conditional formatting to a DBField in a crosstab, you can select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and then select an object from the drop-down list to use its value in the condition. Designer provides the following objects that are of the same data type as the field on which the condition is based in the drop-down list:
     + [Crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas) if the crosstab uses a query resource
     + [Dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) and aggregation objects if the crosstab uses a business view
   * When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
     If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement `Trim(@Field)` that transforms the spaces into empty string, then use the formula to replace the field itself in the condition.
7. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
   * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
   * To take out any condition or group from a group, select it and select **Ungroup**.
   * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
   * To delete a condition line, select it and select **Delete**.
8. Select **OK** to save the condition. Designer displays and selects the newly added condition in the **Condition** box in the Conditional Formatting dialog box.
9. In the **Format** box, specify the formatting you want to apply to the field values that meet the condition, such as the font face, font size, and font color. Select **Blinking Text** if you want to make the values blink, then in the **Duration** text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings can work in Designer view mode, in HTML output, and at runtime.
10. Repeat steps 2 to 9 to add more conditions and specify the formatting for each condition.
    * To edit a condition, select the condition from the Condition box, select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif), then edit the condition in the Edit Conditions dialog box.
    * To adjust the priority of the conditions, select a condition and select **High** or **Low**.
    * To delete a condition and the corresponding formatting, select the condition in the Condition box and then select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
11. Select **OK** to save the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) To make the blink settings take effect in HTML output and at runtime, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, and Chrome.

## Searching for DBFields in a Report

When a report has many DBFields, you may find it difficult to locate where a certain field is. To easily find out the field you have lost track of in your report, you can use the Find DBField feature.

**To find a DBField in a report**

1. Navigate to **Home** > **Find**. Designer displays the [Find dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522918039-Find-Dialog-Box).

   ![Find dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898464365719/find.gif)
2. Select the field you want to locate from the **Find What** drop-down list.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Besides DBFields, Designer also lists the [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) used in the report in the Find What drop-down list, so you can also use this dialog box to locate a formula in a report.
3. Specify the criteria with which to find the field.
   * **Root**  
     Select to search for the field from the top node.
   * **Current Node**  
     Select to search for the field from the current node.
4. Select **Find Next** and Designer selects the specified field in the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields)
