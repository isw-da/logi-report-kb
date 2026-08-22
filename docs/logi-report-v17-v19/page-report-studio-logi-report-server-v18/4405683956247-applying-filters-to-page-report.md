---
title: "Applying Filters to Page Report"
id: 4405683956247
section: "Page Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683956247-Applying-Filters-to-Page-Report
updated_at: 2022-01-27T07:59:43Z
---

# Applying Filters to Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683957271-Adding-Conditional-Formats-to-Fields-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690650263-Using-Dynamic-Resources-in-Page-Report)

# Applying Filters to Page Report

You can apply filters to a page report to narrow down the data in the report. This topic describes how you can filter business views and data components such as banded objects, tables, crosstabs, and charts in page reports.

This topic contains the following sections:

* [Applying Filters to Business Views](#BV)
* [Applying Filters to Data Components](#Component)
  + [Filtering Using the Filter Dialog](#Dialog)
  + [Filtering Using Shortcut Menu](#Menu)

## Applying Filters to Business Views

For data components created on business views or converted to use business views in a page report, you can apply filters to the business views they use to narrow down the data scope of the business views. Filters for business views are defined into two categories in Logi Report: predefined filters and user defined filters. As the name suggests, predefined filters are defined in advance when creating or editing the business views using Logi Report Designer, and user defined filters are created on the business views while they are used.

Business view filters are defined on the component level in Page Report Studio, which means each time you create a data component, you can apply a filter to the business view it applies without affecting other data components based on the same business view.

You need a [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683899543-Logi-Report-Licenses#ServerLive) to use this feature. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

**To apply a filter to the business view a data component uses:**

1. Select any object in the data component.
2. Do any of the following to open the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties) dialog box.
   * Select the Query Filter button ![Query Filter button](https://devnet.logianalytics.com/hc/article_attachments/4420453480087/btn_pgrpt_qryfltr.gif) on the toolbar.
   * Select **Menu** > **Report** > **Query Filter**.
   * Right-click on the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463703/btn_pgrpt_drag.gif) at the upper-left corner of the data component and select **Query Filter** from the shortcut menu.
3. Specify the filter to be applied to the business view.

   All the predefined filters of the business view the data component uses are listed in the Query Filter drop-down list. Choose the one you want to apply. If you want to further edit the filter, select the **Edit** button and then redefine the filter as required. The edited filter will then be saved as a user defined filter to the business view.

   If you prefer to define a filter on your own, select **User Defined** from the Query Filter drop-down list, then define the filter according to your requirements.

   The dialog box has the basic and advanced modes for you to define either [simple expressions](#Simple) or [complex expressions](#Complex).

   * **To define a filter using simple expressions:**
     1. Make sure the dialog box is in the basic mode.

        ![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4420447158039/qryfltr_basic.gif)
     2. From the field drop-down list, select the field on which the filter is based.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. You can also type the value manually in the text box and when you type multiple values, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also filter the field by another field by selecting ![Filter by Field](https://devnet.logianalytics.com/hc/article_attachments/4420453494807/btn_pgrpt_field.gif) and then selecting the field from the drop-down list. The provided field list contains the following: the group and detail information objects in the business view and the parameters in the current catalog which are of the same data type as the field to be filtered, and the special field User Name. To go back to filter the field by value, select ![Filter by Value](https://devnet.logianalytics.com/hc/article_attachments/4420447158295/btn_pgrpt_value.gif).
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
        + To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

        You can repeat this to add more condition lines. To delete a condition line, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420447089175/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Switch the dialog box to the advanced mode.

        ![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4420453495447/qryfltr_advc.gif)
     2. Select the **Add Condition** button to add a condition line.
     3. From the field drop-down list, select the field on which the filter is based.
     4. From the operator drop-down list, set the operator with which to compose the filter expression.
     5. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. You can also type the value manually in the text box and when you type multiple values, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also filter the field by another field by selecting ![Filter by Field](https://devnet.logianalytics.com/hc/article_attachments/4420453494807/btn_pgrpt_field.gif) and then selecting the field from the drop-down list. The provided field list contains the following: the group and detail information objects in the business view and the parameters in the current catalog which are of the same data type as the field to be filtered, and the special field User Name. To go back to filter the field by value, select ![Filter by Value](https://devnet.logianalytics.com/hc/article_attachments/4420447158295/btn_pgrpt_value.gif).
     6. To add another condition line, select the **Add Condition** button and define the expression as required. Then, select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     7. You can repeat the preceding steps to add more condition lines.

        To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

        To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

        To delete a condition line or a group, select it and select the **Delete** button.
4. Select **OK** to apply the filter to the business view. Only the data that meets the filter conditions will be fetched from the business view and displayed on the data component.

   If the special field User Name is used in the filter condition, the username used to sign in to Logi Report Server will be applied to compose the filter expression; if a parameter is used, after selecting the OK button you will be prompted to specify the parameter value to dynamically define the filter condition.

You can also apply a filter to the business view a data component uses in the Query Filter screen of the report wizard while [creating the data component](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports).

## Applying Filters to Data Components

When applying filters to the data components themselves in a page report, there are the following ways you can take: using the Filter dialog box, using shortcut menu, or using [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report#Filter).

### Filtering Using the Filter Dialog

1. Select **Menu** > **Report** > **Filter**, or the **Filter** button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4420447053335/btn_filter.gif) on the toolbar. Server displays the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405683629847-Filter-Dialog-Box-Properties) dialog box.

   ![Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4420453495959/filter_basic.gif)
2. From the Apply to drop-down list, select the data component in the report to which you want to apply the filter.

   **Tip:** For page reports created in Logi Report Designer, the default selected data component and available data components in the Apply to drop-down list are determined by the Default for Filter and Invisible for Filter Dialogs properties of the components.
3. Define the filter conditions using either [simple expressions](#Simple) or [complex expressions](#Complex) as you would do while filtering the business view of a data component. However, there are the following differences when you edit conditions to filter a data component:
   * You cannot filter a field by another field.
   * To specify an empty string (value length=0) as the value for a field of String type, type a pair of single quotes ('') in the text box and then click outside of the condition line to accept the condition.
4. Select **OK** to make the filter take effect and return to the report.

### Filtering Using Shortcut Menu

You can use filter-related commands on the shortcut menu to filter the data in a banded object or table. To do this, right-click any value of a field other than the group-by field by which you want to filter data, to show the shortcut menu. You will see the Filter submenu with these commands:

![Filter Item Submenu](https://devnet.logianalytics.com/hc/article_attachments/4420453496343/pgrpt_edit_fltr_menu.gif)

* **Remove Filter**  
  Select to remove the filter from the field. Server enables this command after you have filtered the field.
* **Top N**  
  Select to display the [Top N](https://devnet.logianalytics.com/hc/en-us/articles/4405690529943-Top-N-Dialog-Box-Properties) dialog box, with which you can filter the field to display only its top N values.
* **Bottom N**  
  Select to display the [Bottom N](https://devnet.logianalytics.com/hc/en-us/articles/4405690499479-Bottom-N-Dialog-Box-Properties) dialog box, with which you can filter the field to display only its bottom N values.
* **Field values**  
  "Field values" is not the name for a command on the Filter submenu, but represents the values of the field. Select a value, and the field will be filtered to show only the specified value.
* **More**  
  Server enables this command if the Filter submenu cannot list all values of the field. Select the command to display the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/4405683682839-Select-Values-Dialog-Box-Properties) dialog box. Then specify a value, and Server filters the field to show only the selected value.

After you apply a filter using the Filter shortcut menu, if you open the Filter dialog box you can find that the corresponding filter expression in the dialog box.

**Tip:** You can customize the following filter-related features for a page report using Logi Report Designer:

* Set the Bind Column property for labels in banded objects or tables to enable the Filter shortcut menu on the labels, and show the filter button beside the labels which provides a filter list containing All, Top N, Bottom N, Custom Filter, the field values and More (if there are too many distinct values for the bound field) for easy filtering.
* Customize the items available on the Filter submenu of a field or label with the Filter Options property.
* Specify the default selected component and available components in the Apply to drop-down list of the Filter dialog box via the Default for Filter and Invisible for Filter Dialogs properties of the components.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683957271-Adding-Conditional-Formats-to-Fields-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690650263-Using-Dynamic-Resources-in-Page-Report)
