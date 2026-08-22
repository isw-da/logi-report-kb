---
title: "Using Filter Control to Filter Data"
id: 1500009584601
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584601-Using-Filter-Control-to-Filter-Data
updated_at: 2021-07-24T05:55:53Z
---

# Using Filter Control to Filter Data

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563862-Using-Navigation-Control-to-Undo-Redo-Value-Selection-in-Filter-Controls)

# Using Filter Control to Filter Data

Filter controls are used to filter one or more data components in a report or library component. They can do filtering based on the fields in the data sources the data components are created from. After inserting filter controls, you can also insert a navigation control for undoing/redoing the value selection in the filter controls. For details about the usage of navigation control, see [Using Navigation Control to Undo/Redo Value Selection in Filter Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009563862-Using-Navigation-Control-to-Undo-Redo-Value-Selection-in-Filter-Controls).

Below is a list of the sections covered in this topic:

> * [Filter Control Types](#Type)
> * [Filtering Scenarios](#scenario)
> * [Inserting a Text List](#FilterControl)
> * [Inserting a Single Value Slider](#SingleSlider)
> * [Inserting a Range Slider](#RangeSlider)
> * [Editing Filter Controls](#Edit)

## Filter Control Types

There are three types of filter controls: text list, single value slider, and range slider.

Text lists allow you to pick one or more random values from a list and are used with categorical or nominal variables.  You can choose one or more values from anywhere in the list and there is no mean or median value calculation possible such as States and Countries.

Single value sliders allow you to select one single value from a list and suitable for displaying a few values like quarters.

Range sliders allow you to pick multiple sequential values from a list and are used for interval variables such as dates, times, quantity and currency variables where the slider represents the scale from lowest to highest value and the middle represents the median value.

Think about what you need and choose the proper filtering tool.

## Filtering Scenarios

Both sliders and text lists have the same filtering mechanism.

Filtering based on one field is a common usage. Bind a field to a filter control, and then based on the field to filter the data of the components created from the same data source as the field.

Another special usage is to filter components using different data sources. Choose a common field all the data sources contain and then bind a filter control with the common field in all the data sources, that is, select the common field under the nodes of all the data sources. The name of the fields do not need to be the same but the data returned needs to be similar.

For example, there are two components containing data from different data sources, and you want to filter their data using one filter control. The precondition is that both data sources have the field you want to filter. For example, you would like the two components to show the data of a specific country. In order to do this, insert a filter control into the report, then select both the country fields from the two data sources (different data sources may use different names for the country field, for example, data source 1 uses "Country", data source 2 uses "P\_Country", in this case, you need to select both "Country" and "P\_Country"), then from the Apply To drop-down list, select the two components you want to filter, and then select OK. The filter control will be inserted in the report, and you can see it lists country names which come from the two data sources. In the filter control select one or more countries, then the two target components will be filtered and only display the data of these selected countries.

When you bind a filter control with multiple different fields, be sure the list of values in each field match so that when you select a value, such as Country, P\_Country and S\_Country, it will match the appropriate country field in each data source. The logic is the values are OR that is *Field1=SelectedValue1 or Field2=SelectedValue1 or Field3=SelectedValue1.* Therefore, when Field1, Field2 and Field3 are used in different components you will see the records correctly in each component.

When you bind a filter control with multiple different fields which do not contain the same list of values such as Country, Region and Territory, at runtime after you select values in the filter control, the filter condition will use OR logic to apply the selected values to all the fields of the filter control, for example, *Field1=SelectedValue1 or Field2=SelectedValue1 or Field3=SelectedValue1*. In this case, when there are three fields but the list of values in each field do not match, the result will have no matching records for two of the components and therefore become blank components. We recommend that you use three different filter controls in cases like this.

## Inserting a Text List

**To insert a text list filter control into a report or a library component:**

1. Do any of the following:
   * Drag the **Filter Control**  button ![Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404889334551/btn_instfltrcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Filter Control**, then select the mouse button in the destination.

   The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009566462-Insert-Filter-Control-Dialog-for-Report-) dialog appears.

   ![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889334807/instfltrctrl.gif)
2. From the Select Fields drop-down list, select the fields of the same data type to bind to the filter control, and then select outside of the drop-down list to close it. The name of the first displayed field you select in the list will be displayed as the name of the filter control.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one filter control, find a common field these data sources contain, then select the field in each of the data sources.

   ![Select Fileds](https://devnet.logianalytics.com/hc/article_attachments/4404893975319/instfltrctrl_slctfld.gif)
3. By default the selected fields use all of their values in the filter control. You can customize the default value list by selecting **Customize Initial Values**. Then type in values directly in the below text box, or select Fetch Data to select values from the database in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009587481-Fetch-Data-Dialog) dialog.
   For fields of Date/Time type, you can also specify a value using the ![Select Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889335063/btn_slctdt.gif) button.

   In the text box, input one value in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and etc. are supported. You need to make sure the accuracy of the formats and values.

   ![Initial Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404889400727/instfltrctrl_cstmz.gif)
4. By default, all filter controls that are applied to the same data components are linked. Selecting a value in one filter control, for example, USA, will result in that all the other linked filter controls respond to gray the values that do not belong to USA or that do not contain USA or that are not related to USA like London. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
5. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
6. When done, select **OK** to insert the filter control. Then at runtime, all values or the customized values of the specified fields will be listed in the filter control. End users can select one or more values to apply.

## Inserting a Single Value Slider

**To insert a single value slider to a library component:**

1. Drag **Filter Control** button**![Filter Control button](https://devnet.logianalytics.com/hc/article_attachments/4404889334551/btn_instfltrcntrl.gif)** from the Components panel to the destination. Then the [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009587601-Insert-Filter-Control-Dialog-for-Library-Component-) dialog appears.
2. From Control Type drop-down list, choose Single Value Slider.

   ![Insert Filter Control dialog - Single Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404889400983/instfltrctrl_sgl.gif)
3. From the Select Fields drop-down list, select the fields of the same data type to bind to the slider, and then select outside of the drop-down list to close it.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one slider, find a common field these data sources contain, then select the field in each of the data sources.

   ![Select fields value](https://devnet.logianalytics.com/hc/article_attachments/4404893975319/instfltrctrl_slctfld.gif)
4. By default, all the values of the selected fields will be available to the slider, which may be too many for a slider. However you can customize the values to show by selecting **Customize Initial Values**. Then type in values directly in the below text box, or select Fetch Data to select values from the database in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009587481-Fetch-Data-Dialog) dialog.

   In the text box, input one value in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and etc. are supported. You need to make sure the accuracy of the formats and values.

   For fields of Date/Time type, you can also specify a value using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404889335063/btn_slctdt.gif) button and specify a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field).

   ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404893975575/instfltrctrl_cstmzsgl.gif)
5. By default, all filter controls that are applied to the same data components are linked. Selecting a value in one filter control, for example, USA, will result in that all the other linked filter controls respond to gray the values that do not belong to USA or that do not contain USA or that are not related to USA like London. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
6. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
7. When done, select **OK** to insert the slider. Then at runtime, end users can select a value on the slider to filter the specified data components.

## Inserting a Range Slider

**To insert a range slider to a library component:**

1. Drag **Filter Control**  from the Components panel to the destination. Then the [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009587601-Insert-Filter-Control-Dialog-for-Library-Component-) dialog appears.
2. From Control Type drop-down list, choose Range Slider.

   ![Insert Filter Control dialog - Range Slider](https://devnet.logianalytics.com/hc/article_attachments/4404889401495/instfltrctrl_rng.gif)
3. From the Select Fields drop-down list, select the fields of the same data type to bind to the slider, and then select outside of the drop-down list to close it.

   To filter components created from the same data source, select a field in the data source.

   To filter components created from different data sources via one slider, find a common field these data sources contain, then select the field in each of the data sources.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893975319/instfltrctrl_slctfld.gif)
4. By default, all the values of the selected fields will be available to the slider, which may be too many for a slider. However you can customize the values to show by selecting **Customize Initial Values**. Then select the start value of the slider from the From drop-down list and the end value from the To drop-down list. For fields of Date/Time type, you can also specify a value using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404889335063/btn_slctdt.gif) button and specify a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field).

   ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404893975959/instfltrctrl_rngcus.gif)
5. By default, all filter controls that are applied to the same data components are linked. Selecting a value in one filter control, for example, USA, will result in that all the other linked filter controls respond to gray the values that do not belong to USA or that do not contain USA or that are not related to USA like London. If you do not want the filter control to be affected by other on-screen filters, unselect **Link to Other Filters**.
6. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
7. When done, select **OK** to insert the slider. Then at runtime, end users can select a value range on the slider to filter the specified data components.

## Editing Filter Controls

You can further modify the filter controls inserted into a report if you want.

To edit a filter control, right-click the filter control and select **Edit Filter Control** from the shortcut menu. In the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009586441-Edit-Filter-Control-Dialog-for-Library-Component-) dialog, edit the filter control settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584621-Using-Parameter-Form-Control-to-Run-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563862-Using-Navigation-Control-to-Undo-Redo-Value-Selection-in-Filter-Controls)
