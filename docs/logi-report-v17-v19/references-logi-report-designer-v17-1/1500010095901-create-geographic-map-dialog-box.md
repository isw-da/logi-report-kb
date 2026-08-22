---
title: "Create Geographic Map Dialog Box"
id: 1500010095901
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095901-Create-Geographic-Map-Dialog-Box
updated_at: 2021-07-23T19:15:10Z
---

# Create Geographic Map Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058362-Create-Data-Mapping-File-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058382-Create-KPI-Chart-Dialog-Box)

# Create Geographic Map Dialog Box

You can use the Create Geographic Map dialog box to [insert a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500010094781-Inserting-Geographic-Maps-in-a-Report) into a report. This topic describes the options in the dialog box.

Designer displays the Create Geographic Map dialog box when you select Insert > Map > Geographic Map, or drag the Geographic Map icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/4404856991127/icon_geomap.gif) from the Components panel into a report, and provides you with different options in the dialog box according to the type of the report into which you are inserting the geographic map: [web report/library component](#Web) or [page report](#Page).

## Create Geographic Map Dialog Box - For Web Report and Library Component

When you use the Create Geographic Map dialog box for creating a geographic map in a web report or library component, you see the following screens in the dialog box:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Filter Screen](#Filter)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating the geographic map and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the business view using which to create the geographic map. You can select from all the predefined business views in the current catalog.

![Create Geographic Map - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856991511/crtgmp_dt_wb.gif)

### Display Screen

Use this screen to specify the data fields that you want to display in the geographic map.

![Create Geographic Map - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848597911/crtgmp_dsply_wb.gif)

**Map Type**

The drop-down list contains the types using which you can create the geographic map. Select the type you need.

* **OpenStreetMap - Standard**  
  This type displays the street map.
* **OpenCycleMap - Cycle Map**  
  This type displays the cycle route map.
* **OpenCycleMap - Transport Map**  
  This type displays the transport map.
* **Google Maps - Roadmap**  
  This type displays Google road map.
* **Google Maps - Satellite**  
  This type displays Google Earth satellite images.
* **Google Maps - Terrain**  
  This type displays a physical map based on terrain information.

**Resources**

The box lists all the group objects and aggregation objects in the specified business view, as well as the dynamic formulas for the business view in the current report. You can use them to create the geographic map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the geographic map.

**Enable Marker**

Select to enable specifying the marker properties for all the groups.

**Enable Area**

Select to enable specifying the area properties for all the groups.

You must select one option between Enable Marker and Enable Area at least and Designer selects Enable Marker by default.

**Drill Path**

The box lists the group objects that you add to group data in the geographic map. Select a group and you can specify its marker and/or area properties.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified field from the geographic map.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the selected group level.

**Web Behaviors**

Designer displays the option when you use the dialog box for creating a geographic map in a library component. Select it to open the [Web Behaviors dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099141-Web-Behaviors-Dialog-Box) to specify web behaviors to the markers and/or areas of the selected group level.

**Marker Options**

Designer enables the options when you select Enable Marker. You can specify the marker properties for the selected group level.

* **Shape By**  
  The text box shows the field that you add to control the shapes of the markers for the selected group level. You can only add the group object that represents the currently selected group level, a group object of a higher level than the current level in the Drill Path box, or an aggregation object.
  You can also leave the text box blank.
  + ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404856923543/btn_shp.gif)  
    Select to specify the shapes of the markers.
    - If you do not add any field to control the shape, select a shape from the shape list, or select the Advanced checkbox and select Advanced to open the [Advanced dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058042-Advanced-Dialog-Box#Map) to specify an image as the shape of the markers.

      ![Shape List](https://devnet.logianalytics.com/hc/article_attachments/4404856923799/cmpnt_map_geo_inst_shplst.gif)
    - If you add a field to control the shape, Designer displays the [Edit Shapes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096401-Edit-Shapes-Dialog-Box) for you to specify the shapes for the markers.
* **Color By**  
  The text box shows the field that you add to control the colors of the markers for the selected group level. You can only add the group object that represents the currently selected group level, group objects of higher levels than the current level in the Drill Path box, or an aggregation object. When you add more than one group object, you can adjust their order by dragging and dropping them in the text box.
  You can also leave the text box blank.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856924055/btn_colr.gif)  
    Select to specify the colors of the markers.
    - If you do not add any field to control the color, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) for the markers.
    - If you add one or more group objects to control the color, Designer displays the [Edit Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096201-Edit-Color-Dialog-Box) for you to specify colors for the markers.
    - If you add an aggregation object to control the color, Designer displays the [Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058742-Edit-Gradient-Color-Dialog-Box) for you to specify a gradient color for the markers.
* **Size By**  
  The text box shows the field that you add to control the size of the markers for the selected group level. You can only add one aggregation object.
  + ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404856924311/btn_size.gif)  
    Select to specify the size of the markers.

    ![Size Zooming Bar](https://devnet.logianalytics.com/hc/article_attachments/4404848529943/cmpnt_map_geo_inst_size.gif)

    - **Zoom percentage bar**  
      Specify the zoom percentage based on the default size.
    - **Reset**  
      Select to restore the default size.
* **Label By**  
  Specify the field to control the labels shown above the markers for the selected group level. You can add more than one field. If you add several fields, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404856924823/btn_lbl.gif)  
    Select to specify the font format of the label text.

    ![Font Properties dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848530199/cmpnt_map_geo_inst_label.gif)

    - ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404856791447/btn_fntface.gif)  
      Select the font of the label text.
    - ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404856791703/btn_fntsize.gif)  
      Select the font size of the label text.
    - ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404848369815/btn_bold.gif)  
      Select to bold the label text.
    - ![Itelic button](https://devnet.logianalytics.com/hc/article_attachments/4404856792087/btn_italic.gif)  
      Select to make the label text italic.
    - ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404856792343/btn_underline.gif)  
      Select to underline the text.
    - ![Font Color button](https://devnet.logianalytics.com/hc/article_attachments/4404848530455/btn_fntcolr.gif)  
      Select to specify the color of the label text.
    - ![Font Format button](https://devnet.logianalytics.com/hc/article_attachments/4404856925591/btn_fntfmt.gif)  
      Designer enables the button when you select a field in the preview box below. Select it and select the data format of the field values to display in the label from the drop-down menu. If you have added more than one field to control the label, you can select the fields from the preview box and select the button to set their value format one by one.
      * **Auto Scale in Number**  
        Designer displays the option when the selected field is of the Number data type. You can use it to specify whether to automatically scale the field values that fall into the following two ranges:
        + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
        + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

        By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the geographic map in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010100421-Geo-Map-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
    - **Preview box**  
      The box displays the fields that you have added to control the label with the specified font format effects.
    - **OK**  
      Select to apply the specified font format and close the dialog box.
* **Marker Tip**  
  The text box shows the tip information that you specify for the markers. Select in the text box and type the tip. The tip displays when the report users hover the mouse on the markers at runtime.
  + ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
    Select it and select a field or a formula from the drop-down list to control the tip.

**Area Options**

Designer enables the options when you select Enable Area. You can specify the area properties for the selected group level.

* **Fill By**  
  The text box shows the fields that you add to control the colors used to fill the areas of the selected group level. You can only add the group object that represents the currently selected group level, group objects of higher levels than the current level in the Drill Path box, or an aggregation object. When you add more than one group object, you can adjust their order by dragging and dropping them in the text box.
  You can also leave the text box blank.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856924055/btn_colr.gif)  
    Select to specify the colors to fill the areas.
    - If you do not add any field to control the color, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) for the areas.
    - If you add one or more group objects to control the colors, Designer displays the [Edit Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096201-Edit-Color-Dialog-Box) for you to specify colors for the areas.
    - If you add an aggregation object to control the colors, Designer displays the [Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058742-Edit-Gradient-Color-Dialog-Box) for you to specify a gradient color for the areas.
* **Label By**  
  The text box shows the field that you add to control the label shown above the areas for the selected group level. You can add more than one field. When you add several fields, you can adjust their display order in the label by dragging and dropping them in the text box.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404856924823/btn_lbl.gif)  
    Select to specify the [font format](#LabelBy) of the label text.
* **Area Tip**  
  The text box shows the tip information that you specify for the areas. Select in the text box and type the tip. The tip displays when the report users hover the mouse on the areas at runtime.
  + ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
    Select it and select a field or a formula from the drop-down list to control the tip.

**Location Info**

The text box shows the mapping location that you specify for the markers and/or areas of the selected group level. Select in the text box and type the location information.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Select it and select a field or a formula from the drop-down list to control the location information. You need to make sure the field contains values that match the folder names in `<install_root>\gisinfo\geocode`.

### Filter Screen

Use this screen to narrow down the data to display in the geographic map.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Create Geographic Map - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856991767/crtgmp_fltr_wb.gif)

## Create Geographic Map Dialog Box - For Page Report

When you use the Create Geographic Map dialog box for creating a geographic map in a page report, you see the following screens in the dialog box:

* [Data Screen](#PageData)
* [Group Screen](#PageGroup)
* [Filter Screen](#PageFilter)
* [Layout Screen](#PageLayout)
* [Marker Screen](#PageMarker)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating the geographic map and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the geographic map.

![Create Geographic Map - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856992279/crtgmp_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the geographic map.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the geographic map.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  A geographic map cannot inherit the dataset from its parent.

### Group Screen

Use this screen to specify the criteria for grouping data in the geographic map.

![Create Geographic Map - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848603927/crtgmp_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the geographic map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the geographic map.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the geographic map.

**Group By**

The column shows the group-by fields on which you select to group data in the geographic map.

**Sort**

The column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

The column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables the button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables the button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box) to specify the group filter condition.

### Filter Screen

Use this screen to filter the group-by fields that you add to the geographic map to reduce the data.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Create Geographic Map - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856992535/crtgmp_fltr.gif)

### Layout Screen

Use this screen to specify the layout of the geographic map elements.

![Create Geographic Map - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404848607255/crtgmp_layout.gif)

**Geographic Data**

Specify the geographical data for the geographic map using an XML file. Select the Browse button to select the XML file.

**Map Type**

The drop-down list contains the types using which you can create the geographic map. Select the type you need.

* **Google Maps - Roadmap**  
  This type displays Google road map.
* **Google Maps - Satellite**  
  This type displays Google Earth satellite images.
* **Google Maps - Terrain**  
  This type displays a physical map based on terrain information.
* **OpenStreetMap - Standard**  
  This type displays the street map.
* **OpenCycleMap - Cycle Map**  
  This type displays the cycle route map.
* **OpenCycleMap - Transport Map**  
  This type displays the transport map.

### Marker Screen

Use this screen to specify properties of the markers bound with the group levels.

![Create Geographic Map - Marker](https://devnet.logianalytics.com/hc/article_attachments/4404848607511/crtgmp_mkr.gif)

**Geographic Map**

The box lists all the groups that you add for the geographic map. Select a group to specify its marker properties.

**Location Info**

Specify the mapping location for the markers of the selected group level. Select in the text box and type the location information.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Select it and select a field or a formula from the drop-down list to control the location information. You need to make sure that the specified field contains the values matching the "nm" field in the geographic data XML file used by the geographic map.

**Marker Tip**

Specify the tip information for the markers of the selected group level. Select in the text box and type the tip. The tip displays when the report users hover the mouse on the markers at runtime.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Select it and select a field or a formula from the drop-down list to control the tip.

**Default Icon**

Select to use the default icon for the markers of the selected group level. If you want to customize the icon, clear the option.

**Image**

Specify the image for the markers of the selected group level. Type the URL for a web image or select the Browse button to specify a local image.

* **Width**  
  Specify the width of the image.
* **Height**  
  Specify the height of the image.

**Shadow**

Designer enables this option only when you select a Google Maps type for the geographic map. Type the URL for a web image or select the Browse button to specify a local image as the shadow image of the markers.

* **Width**  
  Specify the width of the shadow image.
* **Height**  
  Specify the height of the shadow image.

**Constrain Proportions**

If you select the option, when you set the width or height of the marker image/shadow, Designer adjusts the other accordingly in a certain proportion.

**Hide Markers**

Specify whether to show or hide the markers of the selected group level.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Select it and select a formula from the drop-down list to control whether or not to show the markers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058362-Create-Data-Mapping-File-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058382-Create-KPI-Chart-Dialog-Box)
