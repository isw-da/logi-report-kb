---
title: "Geographic Map Wizard Dialog"
id: 1500009608742
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608742-Geographic-Map-Wizard-Dialog
updated_at: 2021-07-24T16:04:31Z
---

# Geographic Map Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631241-Formula-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog)

# Geographic Map Wizard Dialog

The Geographic Map Wizard helps you to [edit an existing geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009606342-Modifying-Geographic-Maps#Edit). It appears when you right-click a geographic map in a report and select Geographic Map Wizard from the shortcut menu.

The wizard varies with the report type: [web report/library component](#Web) and [page report](#Page).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes modifying the geographic map and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Geographic Map Wizard - for web report and library component

When the wizard is used for editing a geographic map in a web report or library component, it consists of the following screens: [Data](#Data) and [Display](#Display).

### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the geographic map.

![Geographic Map Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904275223/gmpwzd_dt_wb.gif)

### Display

Specifies the data fields that you want to display in the geographic map.

![Geographic Map Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904275479/gmpwzd_dsply_wb.gif)

**Map Type**

Specifies the type for the geographic map from the drop-down list.

* **OpenStreetMap - Standard**  
   Displays the street map.
* **OpenCycleMap - Cycle Map**  
   Displays the cycle route map.
* **OpenCycleMap - Transport Map**  
   Displays the transport map.
* **Google Maps - Roadmap**  
   Displays Google road map.
* **Google Maps - Satellite**  
   Displays Google Earth satellite images.
* **Google Maps - Terrain**  
   Displays a physical map based on terrain information.

**Resources**

Lists all the group objects and aggregation objects in the specified business view, as well as the dynamic formulas for the business view in the current report. You can use them to edit the geographic map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected field in the Resources box to the geographic map.

**Enable Marker**

Enables specifying the marker properties for all the groups.

**Enable Area**

Enables specifying the area properties for all the groups.

One option between Enable Marker and Enable Area must be selected at least and Enable Marker is selected by default.

**Drill Path**

Lists the fields that are used to group data in the geographic map.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the specified group one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected field from the geographic map.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition for the selected group level.

**Web Behaviors**

Opens the [Web Behaviors](https://devnet.logianalytics.com/hc/en-us/articles/1500009633981-Web-Behaviors-Dialog) dialog to specify web behaviors to the markers and areas of the selected group level. Available only when editing the geographic map in a library component.

**Marker Options**

Specifies the marker properties of the selected group in the Drill Path box. Available only when Enable Marker is selected.

* **Shape By**  
   Specifies the field used to control the shapes of the markers for the selected group level. Only the group field that represents the currently selected group level, or a group field of a higher level than the current level in the Drill Path box, or an aggregation field can be added.
  + ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404904275735/btn_shp.gif)  
     Specifies the shapes of the markers.
    - If no field is added, select a shape from the shape list, or select the Advanced option to open the [Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009607222-Advanced-Dialog#Map) dialog to specify an image as the shape of the markers.
    - If a field is added, opens the [Edit Shapes](https://devnet.logianalytics.com/hc/en-us/articles/1500009607982-Edit-Shapes-Dialog) dialog to specify shapes for the markers.
* **Color By**  
   Specifies the field used to control the colors of the markers for the selected group level. Only the group field that represents the currently selected group level, or group fields of higher levels than the current level in the Drill Path box, or an aggregation field can be added. When more than one group field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif)  
     Specifies the colors of the markers.
    - If no field is added, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) for the markers.
    - If one or more group fields are added, opens the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009630621-Edit-Color-Dialog) dialog to specify colors for the markers.
    - If an aggregation field is added, opens the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009630701-Edit-Gradient-Color-Dialog) dialog to specify a gradient color for the markers.
* **Size By**  
   Specifies the field used to control the size of the markers for the selected group level. Only an aggregation field can be added.
  + ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404904276375/btn_size.gif)  
     Specifies the size of the markers.
    - **Zoom percentage bar**  
       Specifies the zoom percentage based on the default size.
    - **Reset**  
       Specifies whether to restore the default size.
* **Label By**  
   Specifies the field to control the labels shown above the markers for the selected group level. You can add more than one field. When several fields are added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404904276631/btn_lbl.gif)  
     Specifies the font format of the label text.

    ![Label By](https://devnet.logianalytics.com/hc/article_attachments/4404916787735/geomap_labelby.gif)

    - ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404911579799/btn_fntface.gif)  
       Specifies the font of the label text.
    - ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404911580055/btn_fntsize.gif)  
       Specifies the font size of the label text.
    - ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404904159639/btn_bold.gif)  
       Specifies whether to make the label text bold.
    - ![Itelic button](https://devnet.logianalytics.com/hc/article_attachments/4404911580695/btn_italic.gif)  
       Specifies whether to make the label text italic.
    - ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404904159895/btn_underline.gif)  
       Specifies whether to underline the text.
    - ![Font Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276887/btn_fntcolr.gif)  
       Specifies the color of the label text.
    - ![Font Format button](https://devnet.logianalytics.com/hc/article_attachments/4404904277143/btn_fntfmt.gif)  
       Activated when a field is selected from the preview box below. It specifies the value format of the field to be displayed in the label. When more than one field is added to control the label, you can select the fields from the preview box and select the button to set the format one by one.
      * **Auto Scale in Number**  
         Available when the selected field is of the Number data type. It specifies whether to automatically scale the field values that fall into the two ranges:
        + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
        + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

        By default it is set to auto which means that the setting follows [that of the geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009635401-Geo-Map-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.
    - **Preview box**  
       Displays the specified font format effects.
    - **OK**  
       Applies the specified font format and closes the dialog.
* **Marker Tip**  
   Specifies the tip information when you hover the mouse on the markers at runtime.

**Area Options**

Specifies the area properties of the selected group in the Drill Path box. Available only when Enable Area is selected.

* **Fill By**  
   Specifies the field to control the colors that are used to fill the areas of the selected group level. Only the group field that represents the currently selected group level, or group fields of higher levels than the current level in the Drill Path box, or an aggregation field can be added. When more than one group field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif)  
     Specifies the colors to fill the areas.
    - If no field is added, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) for the areas.
    - If one or more group fields are added, opens the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009630621-Edit-Color-Dialog) dialog to specify colors for the areas.
    - If an aggregation field is added, opens the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009630701-Edit-Gradient-Color-Dialog) dialog to specify a gradient color for the areas.
* **Label By**  
   Specifies the field to control the labels shown above the areas for the selected group level. You can add more than one field. When several fields are added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404904276631/btn_lbl.gif)  
     Specifies the [font format](#LabelBy) of the label text.
* **Area Tip**   
   Specifies the tip information when you hover the mouse on the areas at runtime.

**Location Info**

Specifies the mapping location of the markers or areas for the selected group-by field in the Drill Path box. For each group level that you want to show on the map, specify the view element or dynamic formula that contains the value matching the folder name in `<install_root>\gisinfo\geocode` used by the geographic map. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

## Geographic Map Wizard - for page report

When the wizard is used for editing a geographic map in a page report, it consists of the following screens: [Data](#PageData), [Group](#PageGroup), [Layout](#PageLayout), and [Marker](#PageMarker).

### Data

Specifies the dataset for the geographic map.

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the geographic map.

**More Options**/**Less Options**

![Geographic Map Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904277399/gmpwzd_dt.gif)Shows or hides the dataset selection panel to choose a dataset for the geographic map.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Group

Specifies the data fields that are used to group data in the geographic map.

![Geographic Map Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904278039/gmpwzd_grp.gif)

**Resources**

Lists the DBFields in the specified data resource, as well as the valid formulas and parameters for these DBFields in the current catalog that can be used as group-by fields in the geographic map.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box as the group-by field in the geographic map.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected group-by field from the geographic map.

**Group By**

Lists the group-by fields of the geographic map.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog to define grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009607602-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

For a group-by field of the Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Function) for it to specify to which level data will be grouped by. Select Customize to set the function in the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog) dialog.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sort manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631861-Group-Filter-Dialog) dialog to specify the group filter condition.

### Layout

Specifies the layout of the geographic map elements.

![Geographic Map Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904278423/gmpwzd_layout.gif)

**Geographic Data**

Specifies the geographical data for the geographic map using an XML file.

**Map Type**

Specifies the type for the geographic map from the drop-down list.

* **Google Maps - Roadmap**  
   Displays Google road map.
* **Google Maps - Satellite**  
   Displays Google Earth satellite images.
* **Google Maps - Terrain**  
   Displays a physical map based on terrain information.
* **OpenStreetMap - Standard**  
   Displays the street map.
* **OpenCycleMap - Cycle Map**  
   Displays the cycle route map.
* **OpenCycleMap - Transport Map**  
   Displays the transport map.

### Marker

Specifies properties of the markers bound with the group levels.

![Geographic Map Wizard - Marker](https://devnet.logianalytics.com/hc/article_attachments/4404904279063/gmpwzd_mkr.gif)

**Geographic Map**

Lists all group levels defined for the geographic map.

**Location Info**

Specifies the mapping location of the markers for the selected group level. For each group level that you want to show on the map, specify a DBfield or formula that contains the value matching the "nm" field in the geographic data XML file used by the geographic map. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

**Marker Tip**

Specifies the tip information for the markers of the selected group level, which will be displayed when you hover the mouse on the markers at runtime.

**Default Icon**

Specifies to use the default icon for the markers of the selected group level. If you want to customize the icon, clear the option.

**Image**

Specifies the image for the markers of the selected group level. Type the URL for a web image or select Browse button to specify a local image.

* **Width**  
  Specifies the width of the image.
* **Height**  
  Specifies the height of the image.

**Shadow**

Specifies the shadow image for the markers of the selected group level. Type the URL for a web image or select Browse button to specify a local image. Only available for Google Maps types.

* **Width**  
  Specifies the width of the shadow image.
* **Height**  
  Specifies the height of the shadow image.

**Constrain Proportions**

Specifies whether to change the width and height for the marker image/shadow at the same time in a certain proportion. If the option is selected, when the width/height is changed, the height/width will also be changed in a certain proportion.

**Hide Markers**

Specifies whether to show or hide the markers of the selected group level.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631241-Formula-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog)
