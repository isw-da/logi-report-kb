---
title: "Filtering the Data Components in a Dashboard"
id: 45203859352589
section: "Introduction to the JDashboard and Visual Analysis Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203859352589-Filtering-the-Data-Components-in-a-Dashboard
updated_at: 2026-04-30T14:08:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Filtering the Data Components in a Dashboard 

You can use filter controls to filter one or more data components in a dashboard. The filters you create via filter controls are on-screen filters. This topic describes how you can insert different types of filter controls in a dashboard, specify values in the filter controls, and save default filter values into a dashboard.

JDashboard supports four types of filter controls:

- 
Text List enables you to pick one or more random values from a list and is used with categorical or nominal variables. You can choose one or more values from anywhere in the list and there is no mean or median value calculation.

- 
Drop-down List functions basically the same as Text List. It differs from the Text List type by listing values in a drop-down list so that it takes less space in a dashboard. In a drop-down list filter control, Server places checkboxes ahead of the values for easy selection of multiple values.

- 
Single Value Slider enables you to select one single value from a list and suitable for displaying a few values like quarters. 

- 
Range Slider enables you to pick multiple sequential values from a list and is used for interval variables such as dates, times, quantity, and currency variables where the slider represents the scale from lowest to highest values and the middle represents the median value.

This topic contains the following sections:

- Filtering Scenarios and Filter Logic

- Link Relationship Between Filter Controls

- Inserting a Filter Control in a Dashboard

- Saving and Using Default Values in Filter Controls

## 
Filtering Scenarios and Filter Logic

Filtering based on one field is a common usage. Bind a field to a filter control, and then based on the field to filter the data components created from the same business view as the field. Another special usage is to filter data components created using different business views. In this case you need to choose a common field all the business views contain and select the common field from all the business views to bind them to the filter control. The names of the fields do not need to be the same, but the data returned needs to be similar.

After you select values in one or more filter controls in a dashboard, a filter condition based on the selected values of the specified fields will be applied to the designated data components in the dashboard, with each field affecting only the data components based on the same business view as the field. The value selection logic is: 

- When one value of one field is selected, the filter condition is Field1=SelectedValue1, for example, Country=USA. The filter condition will be applied to the data components that are created using the same business view as the field. 

- When multiple values of multiple fields in one business view are selected, the filter condition uses AND logic between the fields: (Field1=SelectedValue1 or Field1=SelectedValue2) and (Field2=SelectedValue3 or Field2=SelectedValue4)..., for example, (Country=USA or Country=China) and (Year=2017 or Year=2018). The filter condition will be applied to the data components that are created using the business view. 

- When multiple values of multiple fields in different business views are selected, the filter condition uses OR logic between the fields: (Field1=SelectedValue1 or Field1=SelectedValue2) or (Field2=SelectedValue3 or Field2=SelectedValue4)..., for example, (Country=USA or Country=China) or (Year=2017 or Year=2018). The filter condition will be applied to all the data components that are created using these business views.

When you bind a filter control with multiple different fields in different data resources, such as Country, P_Country, and S_Country, be sure the list of values in each field match so that when you select a value, it will match the appropriate country field in each data resource. That is because in cases like this Report applies the logic OR for the values, that is Country=SelectedValue1 or P_Country=SelectedValue1 or S_Country=SelectedValue1. Therefore, when Country, P_Country, and S_Country are used in different data components you will see the records correctly in each component. If you bind a filter control with multiple different fields in different business views which do not contain the same list of values such as Country, Region, and Territory, after you select a value in the filter control, the report will have no matching records for two of the fields and therefore the data components using the same data resources as the two fields will become blank components.

## 
Link Relationship Between Filter Controls

By default, all the filter controls applied to the same data components in a dashboard are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one filter control will result in that values which do not belong to the selected value, contain the selected value or relate to the selected value are grayed in all the other linked filter controls for distinguishing. For example, there is a filter control based on the field Country and another on City and they both are applied to the same table. When you select USA in the Country filter control, the values in the City filter control will change as follows: if the City filter control has a scroll bar, the cities belong to USA are displayed in the upper area of the filter control and the other cities are put in the lower area and grayed out; if it has no scroll bar, all the values remain their positions and the values not belonging to USA are grayed out. In both cases all the values are still selectable.

When using a filter control, you can determine whether to make the filter control apply the link relationship via the Link to Other Filters option.

See an example showing the logic of other linked filters:

When:

- Filter1 is applied to DC1, DC2, and DC3.

- Filter2 is applied to DC1.

- Filter3 is applied To DC2.

- Filter4 is applied to DC2 and DC3.

The result: 

- For Filter1, other linked filters are Filter2, Filter3, and Filter4.

- For Filter2, another linked filter is Filter1.

- For Filter3, other linked filters are Filter1 and Filter4.

- For Filter4, other linked filters are Filter1 and Filter3

## 
Inserting a Filter Control in a Dashboard 

- In the Resources panel of JDashboard, expand the Toolbox node (select Show Resources to display the Resources panel if it is closed). 

- Drag Filter Control to the destination in the dashboard body. Server displays the Insert Filter Control dialog box.
    

- In the Title text box, type a title for the filter control which will be displayed on the title bar of the filter control.

- From the Control Type drop-down list, select the type of the filter control.

- The Select Fields drop-down list lists all the group and detail objects in the business views used by data components in the current dashboard. Select the objects of the same data type to bind to the filter control, and then select outside of the drop-down list to close it.
    

For a text list filter control, after the filter control is created the name of the first selected object will be displayed as the name of the filter control.

- By default, all values of the selected objects are used in the filter control except for the drop-down list filter control which can display 300 values at most. If you want to customize the value list, select Customize Initial Values and customize the values as you want.
    
- 
To customize the values for a text list, drop-down list or single value slider:
 Select Fetch Data to select the values you want in the Fetch Data dialog box. You can also type the values manually in the value text box.
        

Type a value in one row and then press Enter to start a new row. General text editing operations such as Copy, Paste, Cut, Backspace, and Delete are supported. You need to make sure of the accuracy of the formats and values. If the selected objects are of the Date/Time type, you can also select the Calendar icon  to specify a date and time value from the calendar.

- 
To customize the values for a range slider:
        Select the start value of the slider from the From drop-down list and the end value from the To drop-down list. If the selected objects are of the Date/Time type, you can also select the Calendar icon  to specify a date and time value from the calendar.
        

- By default, all filter controls that are applied to the same data components are linked. If you do not want the filter control to be affected by filter controls, clear Link to Other Filters.

- If you have selected a slider control type and the fields bound to the slider are of the Date/Time type, the Special Function drop-down list is available. You can apply a special function to the fields.
				
| Special Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| For each day | The records, of which the field values are in the same day, will be grouped together. |
| For each week | The records, of which the field values are in the same week, will be grouped together. |
| For each bi-week | The records, of which the field values are in the same bi-week, will be grouped together. |
| For each half month | The records, of which the field values are in the same half month, will be grouped together. |
| For each month | The records, of which the field values are in the same month, will be grouped together. |
| For each quarter | The records, of which the field values are in the same quarter, will be grouped together. |
| For each half year | The records, of which the field values are in the same half year, will be grouped together. |
| For each year | The records, of which the field values are in the same year, will be grouped together. |

- From the Apply To drop-down list, specify which data components in the dashboard the filter will be applied to.
    By default, Report applies the filter to all the data components created using the business views in which the selected objects are obtained. If you do not select the data components which are based on the same business view as any selected objects, these objects will not be used in the filter and thus their values will not be listed in the filter control.

- Select OK to insert the filter control. 

You can now select values from the filter control to filter the dashboard data. If the objects bound to the filter control have the same values, the values are distinctive in the filter control.

- For a text list filter control, select the values with which you want to filter the dashboard. A filter condition based on the selected values is then applied to the specified data components in the dashboard.  
               You can make use of the Ctrl or Shift key to select multiple values. If the values themselves have inter-relationship, after you make the selection, Report will deal with the rest values to put the related ones on the top and gray the ones that have no relationship with the selected values. The grayed values are still selectable.

To easily locate the values you want in the filter control, select  on the name bar to sort the values in the ascending or descending order. You can also make use of the search bar to search for the values you want. To display the search bar, select  on the name bar (for detailed usage about the search bar, see Search). The button  on the name bar is used to cancel the selection of values in the filter control. 

- For a drop-down list filter control, select the arrow button on the right to open the drop-down list, select or clear the values (<All> means all the values), and then select OK. A filter condition based on the selected values is then applied to the specified data components in the dashboard.

- For a single value slider, specify a value with which you want to filter the dashboard. A filter condition based on the selected value is then applied to the specified data components in the dashboard.

- For a range slider, specify a value range with which you want to filter the dashboard data. A filter condition based on the selected value range is then applied to the specified data components in the dashboard.

After you insert filter controls in a dashboard, you can further edit them. To edit a filter control, select  on the component title bar and then select Edit Setting from the drop-down menu. Server displays the Edit Filter Control dialog box for you to edit the filter control. 

- When there are more than 300 values in a text list filter control, Report uses Big Data Loading logic. In this case, the Shift Key for multiple selection cannot work.

- If you deleted all the data components in a dashboard that use a business view, Server removes the fields in the business view that have been added in the filter controls in the dashboard from the filter controls too.

- Sometimes when the position of a text list filter control changes due to layout change, the advanced search bar in the filter control may not follow the filter control but stay where it is.

## 
Saving and Using Default Values in Filter Controls

When you have enabled the Use Default On-screen Filter Values feature for dashboards, you can save the values that you specified to the filter controls as the default values for a dashboard and for yourself. Next time when you run the dashboard, Server applies the saved values to the filter controls by default. The default values in filter controls work on a user-dashboard basis. 

- To save values that you specified to the filter controls in a dashboard as the default values, select the Options button  on the toolbar, and navigate to On-screen Filter Values > Save as Default.

- To clear the default values that you have saved for the filter controls in a dashboard, select the Options button  on the toolbar, and navigate to On-screen Filter Values > Clear Default.

- To replace the values that you specified for the filter controls in a dashboard with the saved default values, select the Options button  on the toolbar, and navigate to On-screen Filter Values > Restore to Default.

- 
                To generate the dashboard data by applying all filters to the database, select the Options button  on the toolbar, and navigate to On-screen Filter Values > Push Down.

- Generally, for small data, setting Push Down as "false" can reduce the number of database accesses; for large data, setting Push Down as "true" can improve the performance by pushing down the execution to the database.

- On-Screen Filter Push-Down has higher priority than Business View Prefetch (See the Prefetch property in Business View Properties in the Report Designer Guide) and Dataset Reuse.

- On-Screen Filter Push-Down cannot work in reports that have used one of the following data resources: In-Memory Cube, Cached Report Data, and Query Result Set.
