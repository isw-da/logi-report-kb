---
title: "Using Dynamic Resources"
id: 1500009649362
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649362-Using-Dynamic-Resources
updated_at: 2021-07-24T20:53:56Z
---

# Using Dynamic Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674001-Sorting-Report-Data)

# Using Dynamic Resources

When you drag view elements from the Resource View panel to [analyze data of a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements), sometimes you may find that the view elements that have been predefined in the business view cannot meet your requirements, in which case you can create dynamic resources including formulas and aggregations and use them in the report to get the desired data. Then when you save the report, the dynamic resources will be saved along with the report as its resources.

Dynamic resources are report tab level resources, which means they are only available to the report tab for which they are created.

A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

Below is a list of the sections covered in this topic:

* [Creating and Using Dynamic Formulas](#Formula)
* [Creating and Using Dynamic Aggregation Objects](#Agg)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula with no errors. To learn the formula syntax, refer to [Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/1500009672901-Formula-Syntax).

**To create a dynamic formula:**

1. In the Resource View panel, expand the **Dynamic Resources** > **Formulas** node, then select **<Add Formula…>**. The [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009669661-Formula-Editor) appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926681367/fmlaedtr.gif)
2. Enter a name for the formula in Formula Name text field.
3. By default, Logi JReport will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views) from the Use As drop-down list on the toolbar.

   Whether a dynamic formula can be used as a certain type depends on the following rules:

   * Any formula can be used as Detail.
   * Any formula that references a DBField and not an aggregation can be used as Group.
   * A formula that refers only to aggregations can be used as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * A formula that follows the custom aggregation expression can be used as Aggregation.
4. Compose the formula by selecting the required fields, functions and operators from the Fields, Functions and Operators boxes. You can also write the formula by yourself in the editing box.

   For details about the functions and operators, refer to [Built-in Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009672681-Built-In-Functions) and [Operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009648142-Operators).
5. Select the **Check** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920400791/btn_pgrpt_check.gif) to check whether or not the syntax of your formula is correct.
6. When done, select the **OK** button to create the formula.

Once a dynamic formula is created, you can then drag it from the Resource View panel to the desired position in the report for data analyzing. The formulas can also be used to [control object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009649442-Making-Simple-Modifications-to-Report-Objects#Property) if you are an [advanced user](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#AdvUser) and provided that the Use Dynamic Formula in Property is checked on the Report menu.

If you want to further edit an existing formula or remove any formula that is not required, right-click the formula and then select the corresponding command on the shortcut menu. However, if the formula has been used in the report or referenced by another formula, it cannot be deleted.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating and Using Dynamic Aggregation Objects

In Page Report Studio, you can also create dynamic aggregation objects by mapping them to the available resources which include group objects, detail objects in the current business view and the dynamic formulas that have been created in the report.

**To create a dynamic aggregation object:**

1. In the Resource View panel, expand the **Dynamic Resources** > **Aggregations** node, then select **<Add Aggregation…>**. The [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009669361-Add-Aggregation) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920468631/addmsr.gif)
2. In the Aggregation Name text field, specify the display name of the aggregation object.
3. Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385815/btn_chsr.gif) next to the Mapping Name text field. In the [Select Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009670001-Select-Resource) dialog, specify a field or a formula on which the aggregation object is based.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920468887/slctrsc.gif)
4. From the Aggregate Function drop-down list, specify the aggregate function for the aggregation object.
5. When done, select **OK** to create the aggregation object.

You can also create a dynamic aggregation object on a dynamic formula. To do this:

1. In the Resource View panel, right-click the formula in the Dynamic Resources > Formulas node, then select **Add Aggregation** from the shortcut menu.
2. In the Add Aggregation dialog, specify the display name of the aggregation object and the aggregate function as required.
3. When done, select **OK**.

Once a dynamic aggregation object is created, you can then drag it from the Resource View panel to the desired position in the report for data analyzing.

For any dynamic aggregation object, you can further modify if needed. To do this, right-click the aggregation object and select **Edit** from the shortcut menu. Then in the [Edit Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009645062-Edit-Aggregation) dialog, edit the aggregation object as required.

For dynamic aggregation objects that are on longer required, you can remove them. To delete an aggregation object, right-click it and select **Delete** on the shortcut menu. Aggregation objects that have been used in report cannot be deleted.

**Notes:**

* You can only use JDK (not JRE) to compile formulas created in Logi JReport and save a dynamic formula with no errors into a report.
* Currently, global variables are not supported in dynamic formulas.
* When formulas reference display names or mapping names, the names should not contain any of below characters if the names are not quoted by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Measure, when adding it to a formula, quote it as "Category.Measure" or "Category"."Measure".
* Now in Logi JReport, the display names of objects in a category in a business view cannot be duplicated. When you choose to create a dynamic formula/aggregation object on an object which was created in a previous version and it has the same display name as another object, you will be prompted with a message asking you to give a new name for the object in Logi JReport Designer first.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674001-Sorting-Report-Data)
