---
title: "Filtering Component Data"
id: 1500009669261
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data
updated_at: 2021-07-24T20:55:18Z
---

# Filtering Component Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669341-Synchronizing-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values)

# Filtering Component Data

Filter controls are used to filter one or more data components in a dashboard. They can do filtering based on the fields in the data sources the data components are created from.

The filters created via filter controls are referred to as on-screen filters.

Below is a list of the sections covered in this topic:

* [Filter Control Types](#Type)
* [Filtering Scenarios](#Scenarios)
* [Link Relationship Between Filter Controls](#Link)
* [Inserting a Text List](#FilterControl)
* [Inserting a Single-Value Slider](#SingleSlider)
* [Inserting a Range Slider](#RangeSlider)
* [Saving and Using Default Values in Filter Controls](#Default)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Filter Control Types

There are three types of filter controls: text list, single value slider, and range slider.

Text lists allow you to pick one or more random values from a list and are used with categorical or nominal variables.  You can choose one or more values from anywhere in the list and there is no mean or median value calculation possible such as States and Countries.

Single value sliders allow you to select one single value from a list and suit for displaying a few values like quarters.

Range sliders allow you to pick multiple sequential values from a list and are used for interval variables such as dates, times, quantity and currency variables where the slider represents the scale from lowest to highest value and the middle represents the median value.

Think about what you need and choose the proper filtering tool.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Filtering Scenarios

Both sliders and text lists have the same filtering mechanism.

Filtering based on one field is a common usage. Bind a field to a filter control, and then based on the field to filter the data of the components created from the same data source as the field.

Another special usage is to filter components using different data sources. Choose a common field all the data sources contain and then bind a filter control with the common field in all the data sources, that is, select the common field under the nodes of all the data sources. The name of the field does not need to be the same, only the values need to be the same.

For example, there are two components containing data from different data sources, and you want to filter their data using one filter control. The precondition is that both data sources have the field values you want to filter. For example, you would like the two components to show the data of a specific country. In order to do this, insert a filter control into the dashboard, then select both the country fields from the two data sources (different data sources may use different names for the country field, for example, data source 1 uses "Country", data source 2 uses "P\_Country", in this case, you need to select both "Country" and "P\_Country"), then from the Apply To drop-down list, select the two components you want to filter, and then select OK. The filter control will be inserted in the dashboard, and you can see it lists country names which come from the two data sources. In the filter control select one or more countries, then the two target components will be filtered and only display the data of these selected countries.

When you bind a filter control with multiple different fields, be sure the list of values in each field match so that when you select a value, such as Country, P\_Country and S\_Country, it will match the appropriate country field in each data source. The logic is the values are OR that is *Field1=SelectedValue1 or Field2=SelectedValue1 or Field3=SelectedValue1.* Therefore, when Field1, Field2 and Field3 are used in different components you will see the records correctly in each components.

When you bind a filter control with multiple different fields which do not contain the same list of values such as Country, Region and Territory, at runtime after you select values in the filter control, the filter condition will use OR logic to apply the selected values to all the fields of the filter control, for example, *Field1=SelectedValue1 or Field2=SelectedValue1 or Field3=SelectedValue1*. In this case, when there are three fields but the list of values in each field do not match, the result will have no matching records for two of the components and therefore become blank components. We recommend that you use three different filter controls in cases like this.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Link Relationship Between Filter Controls

By default, all the filter controls applied to the same data components in a dashboard are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one on-screen filter will result in that values which do not belong to the selected value, contain the selected value or relate to the selected value are grayed in all the other linked filter controls for distinguishing. For example, there is a filter control based on the field Country and another on City and they both are applied to the same table. When you select USA in the Country filter control, the values in the City filter control will change as follows if the control has scrollbar: the cities belong to USA are displayed in the upper area of the filter control, and the other cities are put in the lower area and grayed out. If the City filter control has no scrollbar, all the values remain their positions and the values not belonging to USA are grayed out. In both cases all the values are still selectable.

When using a filter control, you can determine whether or not to make the filter control apply the link relationship via the Link to Other Filters option.

Below is an example showing the logic of other linked filters:

When

* Filter1 is applied to DC1, DC2, and DC3.
* Filter2 is applied to DC1.
* Filter3 is applied To DC2.
* Filter4 is applied to DC2 and DC3.

The result:

* For Filter1, other linked filters are Filter2, Filter3, and Filter4.
* For Filter2, other linked filter is Filter1.
* For Filter3, other linked filters are Filter1 and Filter4.
* For Filter4, other linked filters are Filter1 and Filter3

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Text List

**To insert a text list filter control to the dashboard body:**

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **Filter Control** to the destination in the dashboard body. The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009646122-Insert-Filter-Control) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926754711/insrtfltrctrl.gif)
3. In the Title text field, input a title for the filter control which will be displayed on the title bar of the filter control.
4. From the Select Fields drop-down list,select the fields of the same data type to bind to the filter control, and then select outside of the drop-down list to close it . The name of the first displayed field you select in the list will be displayed as the name of the filter control.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one filter control, find a common field these data sources contain, then select the field in each of the data sources.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920648343/dshbrd_fltr_slctfld.gif)
5. By default, all values of the selected fields are used in the filter control. If you want to customize the value list, check **Customize Initial Values** and then select **Fetch Data** to select the desired values in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009646082-Fetch-Data) dialog. You can also type in the values manually in the text box below.

   To enter a value, input it in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and so on are supported. You need to make sure of the accuracy of the formats and values.

   For fields of Date/Time type, you can also specify a value using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) button.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920648599/dshbrd_fltr_cstmz.gif)
6. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
7. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
8. Select **OK**.

A text list filter control bound with the specified fields will be inserted in the dashboard body. You can then specify values in the filter control to filter the specified components.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920648855/dshbrd_fltr_cntrl.gif)

To easily locate the values you want in the filter control, select the Sort ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404920370327/btn_sort1.gif) button on the field name bar to sort the values in the ascending or descending order. You can also make use of the quick search toolbar to search for the desired values. To display the toolbar, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) on the field name bar. The button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920369559/btn_clear.gif) on the field name bar is used to cancel the selection of values in the filter control. For detailed usage about the quick search toolbar, refer to [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009670521-Select-Values) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Single-Value Slider

**To insert a single value slider to the dashboard body:**

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **Filter Control** to the destination in the dashboard body. The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009646122-Insert-Filter-Control) dialog appears.
3. In the Title text field, input a title for the slider which will be displayed on the title bar of the slider.
4. From Control Type drop-down list, choose **Single Value Slider**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926780951/dshbrd_fltr_sgl.gif)
5. From the Select Fields drop-down list, select the fields of the same data type to bind to the slider, and then select outside of the drop-down list to close it. The name of the first displayed field you select in the list will be displayed as the name of the filter control.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one slider, find a common field these data sources contain, then select the field in each of the data sources.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920648343/dshbrd_fltr_slctfld.gif)
6. By default, all the values of the selected fields will be available to the slider, which may be too many for a slider. If you want to customize the value list, check **Customize Initial Values** and then select **Fetch Data** to select the desired values in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009646082-Fetch-Data) dialog. You can also type in the values manually in the text box below.

   To enter a value, input it in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and so on are supported. You need to make sure of the accuracy of the formats and values.

   For fields of Date/Time type, you can also specify a value using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) button and specify a special function.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920649111/dshbrd_fltr_cstmzsgl.gif)
7. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
8. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
9. Select **OK**. A slider bound with the specified fields will be inserted in the dashboard body. You can then specify a value in the slider to filter the specified components.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Range Slider

**To insert a range slider to the dashboard body:**

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag Filter Control to the destination in the dashboard body. The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009646122-Insert-Filter-Control) dialog appears.
3. In the Title text field, input a title for the slider which will be displayed on the title bar of the slider.
4. From Control Type drop-down list, choose **Range Slider**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920649367/dshbrd_fltr_rng.gif)
5. From the Select Fields drop-down list, select the fields of the same data type to bind to the slider, and then select outside of the drop-down list to close it. The name of the first displayed field you select in the list will be displayed as the name of the filter control.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one slider, find a common field these data sources contain, then select the field in each of the data sources.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920648343/dshbrd_fltr_slctfld.gif)
6. By default, all the values of the selected fields will be available to the slider, which may be too many for a slider. If you want to customize the value list, check **Customize Initial Values** and then select the start value of the slider from the From drop-down list and the end value from the To drop-down list. For fields of Date/Time type, you can also specify a value using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) button and specify a special function.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920649623/dshbrd_fltr_rngcus.gif)
7. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
8. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
9. Select **OK**. A slider bound with the specified fields will be inserted in the dashboard body. You can then specify a value range in the slider to filter the specified components.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## [Saving and Using Default Values in Filter Controls](#Default)

When the [Use Default On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#OnScreenFilter) feature is enabled for dashboards, each end user can save the values specified to the filter controls in a dashboard as the default values for the dashboard and for him. Next time when the user runs the dashboard, the saved values will be applied to the filter controls by default. The default values in filter controls work on a user-dashboard basis.

* To save values specified to the filter controls in a dashboard as the default values, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar, go to **On-screen Filter Values** and then select **Save as Default**.
* To clear the default values that have been saved to the filter controls in a dashboard, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar, go to **On-screen Filter Values** and then select **Clear Default**.
* To replace the values specified in the filter controls in a dashboard with the saved default values, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar, go to **On-screen Filter Values** and then select **Restore to Default**.

**Notes:**

* When there are more than 300 values in a filter control, Logi JReport will use Big Data Loading logic. In this case, the Shift Key for multiple selection cannot work.
* Sometimes, when the position of a filter control is changed due to layout change, the advanced search toolbar in the filter control may not follow the filter control but stay where it is.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669341-Synchronizing-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values)
