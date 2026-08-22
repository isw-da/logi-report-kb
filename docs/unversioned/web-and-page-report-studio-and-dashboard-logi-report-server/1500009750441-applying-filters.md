---
title: "Applying Filters"
id: 1500009750441
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750441-Applying-Filters
updated_at: 2021-07-25T07:18:53Z
---

# Applying Filters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750461-Adding-Conditional-Formats-to-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources)

# Applying Filters

You can apply filters to a page report so as to narrow down the data displayed in the report. The filters can be applied to the business views used by data components such as banded objects, tables, crosstabs, and charts in the report, or to the data components themselves.

Select the following links to view the topics:

* [Applying Filters to the Business Views for Data Components](#BV)
* [Applying Filters to the Data Components](#Component)
  + [Filtering Using the Filter Dialog](#Dialog)
  + [Filtering Using Shortcut Menu](#Menu)

## Applying Filters to the Business Views for Data Components

For data components created on business views or converted to use business views in a page report, you can apply filters to the business views they use to narrow down the data scope of the business views. Filters for business views are defined into two categories in Logi Report: predefined filters and user defined filters. As the name suggests, predefined filters are defined in advance when creating or editing the business views using Logi Report Designer, and user defined filters are created on the business views while they are used.

Business view filters are defined on the component level in Page Report Studio, which means each time you create a data component, you can apply a filter to the business view it applies without affecting other data components based on the same business view.

A [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

**To apply a filter to the business view a data component uses:**

1. Select any object in the data component.
2. Do any of the following to open the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719862-Query-Filter) dialog box.
   * Select the Query Filter button ![Query Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404936772503/btn_pgrpt_qryfltr.gif) on the toolbar.
   * Select **Menu** > **Report** > **Query Filter**.
   * Right-click on the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) at the upper left corner of the data component and select **Query Filter** from the shortcut menu.
3. Specify the filter to be applied to the business view.

   All the predefined filters of the business view the data component uses are listed in the Query Filter drop-down list. Choose the one you want to apply. If you want to further edit the filter, select the **Edit** button and then redefine the filter as required. The edited filter will then be saved as a user defined filter to the business view.

   If you prefer to define a filter on your own, select **User Defined** from the Query Filter drop-down list, then define the filter according to your requirements.

   The dialog box has the basic and advanced modes for you to define either [simple expressions](#Simple) or [complex expressions](#Complex).

   * **To define a filter using simple expressions:**
     1. Make sure the dialog box is in the basic mode.

        ![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404936785175/qryfltr_basic.gif)
     2. From the field drop-down list, select the field on which the filter is based.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. You can also type the value manually in the text box and when you type the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also filter the field by another field by selecting ![Filter by Field](https://devnet.logianalytics.com/hc/article_attachments/4404936785431/btn_pgrpt_field.gif) and then selecting the field from the drop-down list. The provided field list contains the following: the group and detail information objects in the business view and the parameters in the current catalog which are of the same data type as the field to be filtered, and the special field User Name. To go back to filter the field by value, select ![Filter by Value](https://devnet.logianalytics.com/hc/article_attachments/4404936785687/btn_pgrpt_value.gif).
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
        + To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

        You can repeat this to add more condition lines. To delete a condition line, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936748823/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Switch the dialog box to the advanced mode.

        ![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4404942494743/qryfltr_advc.gif)
     2. Select the **Add Condition** button to add a condition line.
     3. From the field drop-down list, select the field on which the filter is based.
     4. From the operator drop-down list, set the operator with which to compose the filter expression.
     5. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. You can also type the value manually in the text box and when you type the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also filter the field by another field by selecting ![Filter by Field](https://devnet.logianalytics.com/hc/article_attachments/4404936785431/btn_pgrpt_field.gif) and then selecting the field from the drop-down list. The provided field list contains the following: the group and detail information objects in the business view and the parameters in the current catalog which are of the same data type as the field to be filtered, and the special field User Name. To go back to filter the field by value, select ![Filter by Value](https://devnet.logianalytics.com/hc/article_attachments/4404936785687/btn_pgrpt_value.gif).
     6. To add another condition line, select the **Add Condition** button and define the expression as required. Then, select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     7. You can repeat the above steps to add more condition lines.

        To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

        To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

        To delete a condition line or a group, select it and select the **Delete** button.
4. Select **OK** to apply the filter to the business view. Only the data that meets the filter conditions will be fetched from the business view and displayed on the data component.

   If the special field User Name is used in the filter condition, the user name used to log onto Logi Report Server will be applied to compose the filter expression; if a parameter is used, after selecting the OK button you will be prompted to specify the parameter value to dynamically define the filter condition.

You can also apply a filter to the business view a data component uses in the Query Filter screen of the report wizard while [creating the data component](https://devnet.logianalytics.com/hc/en-us/articles/1500009750341-Creating-Page-Reports).

## Applying Filters to the Data Components

When applying filters to the data components themselves in a page report, there are the following ways you can take: using the Filter dialog box, using shortcut menu, or using [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009750541-Applying-Web-Controls#Filter).

### Filtering Using the Filter Dialog

1. Select **Menu** > **Report** > **Filter**, or the **Filter** button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404942446359/btn_filter.gif) on the toolbar. Report Server displays the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719322-Filter) dialog box.

   ![Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404936785943/filter_basic.gif)
2. From the Apply to drop-down list, select the data component in the report to which you want to apply the filter.

   **Tip:** For page reports created in Logi Report Designer, the default selected data component and available data components in the Apply to drop-down list are determined by the Default for Filter and Invisible for Filter Dialogs properties of the components.
3. Define the filter conditions using either [simple expressions](#Simple) or [complex expressions](#Complex) as you would do while filtering the business view of a data component. However there are the following differences when you edit conditions to filter a data component:
   * You cannot filter a field by another field.
   * ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To specify an empty string (value length=0) as the value for a field of String type, type a pair of single quotes ('') in the text box and then click outside of the condition line to accept the condition.
4. Select **OK** to make the filter take effect and return to the report.

### Filtering Using Shortcut Menu

You can use filter-related commands on the shortcut menu to filter the data in a banded object or table. To do this, point to any value of a field other than the group-by field by which you want to filter data, then right-click to show the shortcut menu. You will see the Filter item which provides a submenu containing the following commands:

![Filter Item Submenu](https://devnet.logianalytics.com/hc/article_attachments/4404936786199/pgrpt_edit_fltr_menu.gif)

* **Remove Filter**  
  This command is enabled after you have applied filtering on the field. You can select it to remove the filter ever defined on it.
* **Top N**  
  Shows the [Top N](https://devnet.logianalytics.com/hc/en-us/articles/1500009746641-Top-N) dialog box with which you can filter the field to display only its top N values.
* **Bottom N**  
  Shows the [Bottom N](https://devnet.logianalytics.com/hc/en-us/articles/1500009719122-Bottom-N) dialog box with which you can filter the field to display only its bottom N values.
* **Field values**  
  "Field values" is not the name for a command on the Filter submenu, but represents some items which are the values of the field you right-click on. Select a value and the field will be filtered to show only the specified value.
* **More**  
  This command is enabled if the Filter submenu cannot list all values of the specified field. When it is enabled, selecting it brings up the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009746341-Select-Values) dialog box. Select one value in the dialog box and the field will be filtered to show only the selected value.

After a filter is applied using the Filter shortcut menu, if you open the Filter dialog box you can find that the corresponding filter expression displays in the dialog box.

**Tip:** You can customize the following filter-related features for a page report using Logi Report Designer:

* Set the Bind Column property for labels in banded objects or tables to enable the Filter shortcut menu on the labels, and show the filter button beside the labels which provides a filter list containing All, Top N, Bottom N, Custom Filter, the field values and More (if there are too many distinct values for the bound field) for easy filtering.
* Customize the items available on the Filter submenu of a field or label with the Filter Options property.
* Specify the default selected component and available components in the Apply to drop-down list of the Filter dialog box via the Default for Filter and Invisible for Filter Dialogs properties of the components.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750461-Adding-Conditional-Formats-to-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources)
