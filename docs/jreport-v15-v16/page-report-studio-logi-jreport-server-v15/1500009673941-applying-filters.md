---
title: "Applying Filters"
id: 1500009673941
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673941-Applying-Filters
updated_at: 2021-07-24T20:53:54Z
---

# Applying Filters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649402-Adding-Conditional-Formats-to-Fields)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements)

# Applying Filters

You can apply filters to a page report so as to narrow down the data displayed in the report. The filters can be applied to the business views used by data components such as banded objects, tables, crosstabs and charts in the report, or to the data components themselves.

Below is a list of the sections covered in this topic:

* [Applying Filters to Business Views](#QueryFilter)
* [Filtering the Data Components in a Report](#Component)

## Applying Filters to Business Views

For data components created on business views or converted to use business views in a page report, you can apply filters to the business views they use to narrow down the data scope of the business views. Filters for business views are defined into two categories in Page Report Studio: predefined filters and user-defined filters. As the name suggests, predefined filters are defined on business views in advance in Logi JReport Designer, and user-defined filters are created on business views while they are used in Page Report Studio.

Business view filters are defined on the component level in Page Report Studio, which means each time you create a component, you can apply a filter to the business view it applies without affecting other components based on the same business view.

A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

**To apply a filter to the business view a data component uses:**

1. Select the component by selecting anywhere in it, and then selecting the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) at the upper left corner of the component.
2. Select **Menu** > **Report** > **Query Filter**, or right-click the component and select **Query Filter** from the shortcut menu to display the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009645642-Query-Filter) dialog.

   All the predefined filters of the business view the data component uses are listed in the Query Filter drop-down list. Choose the one you want to apply. If you want to further edit the filter, select the **Edit** button and then redefine the filter as required. The edited filter will then be saved as a user-defined filter to the business view.

   If you prefer to define a filter on your own, select **User-Defined** from the Query Filter drop-down list, then define the filter according to your requirements.

   There are basic and advanced modes of the dialog for you to define either simple or complex filter expressions.

   * **To define a filter using simple expressions:**
     1. Make sure the dialog is in the basic mode.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404920465559/qryfltr_basic.gif)
     2. From the field drop-down list, select the field on which the filter is based.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. If you want to filter the field by another field, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926680855/btn_pgrpt_field.gif) next to the value drop-down list, then the fields and parameters of the same data type as the specified field and the special field User Name will be available in the drop-down list. Select the required one to use. To go back to filter the field by value, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920465943/btn_pgrpt_value.gif). You can also enter the value manually in the text box and when you type the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
        + To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

        Repeat this to add more filter expressions if required. To delete a condition line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398359/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Switch the dialog to the advanced mode.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404920466199/qryfltr_advc.gif)
     2. Select the **Add Condition** button to add a condition line.
     3. From the field drop-down list, select the field on which the filter is based.
     4. From the operator drop-down list, set the operator with which to compose the filter expression.
     5. The values of the specified field are available in the value drop-down list. Select the required one by which to filter the field. If you want to filter the field by another field, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926680855/btn_pgrpt_field.gif) next to the value drop-down list, then the fields and parameters of the same data type as the specified field and the special field User Name will be available in the drop-down list. Select the required one to use. To go back to filter the field by value, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920465943/btn_pgrpt_value.gif). You can also enter the value manually in the text box and when you type the value, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
     6. To add another condition line, select the **Add Condition** button and define the expression as required. Then, select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     7. Repeat the above steps to add more filter expressions if necessary.

        To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

        To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

        To delete a condition line or a group, select it and select the **Delete** button.
3. Select **OK** and the specified filter will be applied to the business view. Only data that meet the filter condition are fetched from the business view and displayed on the data component.

   If the special field User Name is used in the filter condition, the user name used to log onto Logi JReport Server will be applied to compose the filter expression; if a parameter is used, after selecting the OK button you will be prompted to specify the parameter value to dynamically define the filter condition.

You can also apply a filter to the business view a data component uses in the Query Filter screen of the report wizard while [creating the data component](https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Filtering the Data Components in a Report

When applying filters to the data components themselves in a page report, there are the following ways you can take: using the [Filter](#Dialog) dialog, using [filter controls](#Control), and using [shortcut menu](#Menu).

### Using the Filter Dialog

**To set the filtering conditions using the Filter dialog:**

1. Select **Menu** > **Report** > **Filter**, or the **Filter** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359831/btn_filter.gif) on the toolbar. The [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009645102-Filter) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920466967/filter_basic.gif)
2. Select the component on which the filtering will be based from the Apply to drop-down list.
3. [Define the filter](#Filter) using either simple or complex filter expressions. Filtering by field is not supported here.
4. Select **OK** to make the filter take effect and return to the report.

### Using Filter Controls

A filter control is a web control used to filter one or more data components in a report using the same data source. A filter control can do filtering based on one field or multiple fields of the same data type. For details, see [Using Filter Control to Filter Report Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009674041-Applying-Web-Controls#Filter).

### Using Shortcut Menu

You can use filter-related commands on the shortcut menu to filter the data in a banded object or table. To do this, point to any value of a field other than the group by field by which you want to filter data, then right-click to show the shortcut menu. You will see the Filter item which provides a submenu containing the following commands:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920467479/pgrpt_edit_fltr_menu.gif)

* **Remove Filter**  
   This command is enabled after you have applied filtering on the field. You can select it to remove the filter ever defined on it.
* **Top N**  
   Shows the [Top N](https://devnet.logianalytics.com/hc/en-us/articles/1500009645922-Top-N) dialog with which you can filter the field to display only its top N values.
* **Bottom N**  
   Shows the [Bottom N](https://devnet.logianalytics.com/hc/en-us/articles/1500009669441-Bottom-N) dialog with which you can filter the field to display only its bottom N values.
* **Field values**  
   "Field values" is not the name for a command on the Filter submenu, but represents some items which are the values of the field you right-click on. Select a value and the field will be filtered to show only the specified value.
* **More**  
   This command is enabled if the Filter submenu cannot list all values of the specified field. When it is enabled, selecting it brings up the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009645722-Select-Values) dialog. Select one value in the dialog and the field will be filtered to show only the selected value.

After a filter is applied using the Filter shortcut menu, if you open the Filter dialog you can find that the corresponding filter expression displays in the dialog.

**Tip:** You can customize the following filter-related features for a page report using Logi JReport Designer:

* Bind a label in a banded object or table with a field used in the banded object or table to enable the Filter shortcut menu on the label, and show the filter button beside the label which provides a filter list containing All, Top N, Bottom N, Custom Filter, the field values and More (if there are too many distinct values for the bound field) for easy filtering. For details, see "Enabling Sort and Filter on Labels" in the *Logi JReport Designer User's Guide*.
* Customize the items available on the Filter submenu of a field or label with the Filter Options property. For details, see "Setting Filter Options for an Object" in the *Logi JReport Designer User's Guide*.
* Specify the default selected component and available components in the Apply to drop-down list of the Filter dialog via the Default for Filter and Invisible for Filter Dialogs properties of the components.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649402-Adding-Conditional-Formats-to-Fields)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements)
