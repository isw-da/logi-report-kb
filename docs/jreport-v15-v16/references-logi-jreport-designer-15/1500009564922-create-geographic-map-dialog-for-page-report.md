---
title: "Create Geographic Map Dialog (for Page Report)"
id: 1500009564922
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564922-Create-Geographic-Map-Dialog-for-Page-Report
updated_at: 2021-07-24T05:55:31Z
---

# Create Geographic Map Dialog (for Page Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564902-Create-Geographic-Map-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586081-Create-Geographic-Map-Dialog-for-Web-Report-)

# Create Geographic Map Dialog (for Page Report)

The Create Geographic Map dialog for page report appears when you select Insert > Map > Geographic Map, or drag the Geographic Map button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404889376407/btn_instgmp.gif) from the Components panel into a page report that is created using query resources. It helps you to [insert a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map) into the page report, and consists of the following screens:

* [Data](#Data)
* [Group](#Group)
* [Filter](#Filter)
* [Layout](#Layout)
* [Marker](#Marker)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the geographic map and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Data

Specifies the dataset that you want to use to create the geographic map. [See the screen](javascript:%20void(null)).

![Create Geographic Map wizard fot Page Report - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404893937687/crtgmp_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the geographic map.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the geographic map.

* **New Dataset**  
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the geographic map. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing****Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the geographic map. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current****Dataset**  
   If checked, the current dataset used by the parent object will be applied to the geographic map.

## Group

Specifies the data fields that are used to group the data in the geographic map. [See the screen](javascript:%20void(null)).

![Create Geographic Map wizard fot Page Report - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404889376919/crtgmp_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the geographic map.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

**Group By**

Lists the fields that are used to group data in the geographic map.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define grouping information.

  For example, if you placed a field named Region for grouping, and this field contains all 50 states of the United States; and if you want to see the data between Maryland (MD) and New York (NY), you can define the criteria by selecting the between operator to further define your grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

If the group by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field) for the field in the Special Function column to further specify to which level the data will be grouped by.

If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog) dialog will be displayed, in which you can set the function by your own.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog) dialog to specify the group filter condition.

## Filter

Specifies to filter the data used in the geographic map. [See the screen](javascript:%20void(null)).

![Create Geographic Map wizard fot Page Report - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893937943/crtgmp_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the geographic map elements. [See the screen](javascript:%20void(null)).

![Create Geographic Map wizard fot Page Report - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404893938199/crtgmp_layout.gif)

**Geographic Data**

Specifies the geographical data for the geographic map with an XML file. If the XML file that you specify does not exist it will be created in the <install\_root>\gisinfo directory. The geographic data XML file is used to map the geographic latitude and longitude coordinates from Google Maps, OpenStreetMap or OpenCycleMap based on the location information specified for each group in the Marker tab. When the location information key string of a group value matches the "nm" field in the XML file, you will get the related latitude and longitude value for this group value.

You can also import an XML file which contains predefined geographic data including latitude and longitude for the specific "nm" field. By default, the XML file is located in the `<install_root>\gisinfo` directory, if not, the file will be copied to this directory after it is imported. When you publish the report from Designer you can specify the gisinfo files to publish to the Server from the Geographic Information tab.

If you do not publish the geographical information it will be created automatically when you first run the report.

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

## Marker

Specifies properties of the markers bound with the group levels. [See the screen](javascript:%20void(null)).

![Create Geographic Map wizard fot Page Report - Marker screen](https://devnet.logianalytics.com/hc/article_attachments/4404893938455/crtgmp_mkr.gif)

**Geographic Map**

Lists all group levels defined for the geographic map.

**Location Info**

Specifies the mapping location of the markers for the selected group level. For each group level that you want to show on the map, specify a DBfield or formula that contains the value matching the "nm" field in the geographic data XML file used by the geographic map. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

**Marker Tip**

Specifies the tip information for the markers of the selected group level, which will be displayed when you hover the mouse on the markers at runtime.

**Default Icon**

Specifies to use the default icon for the markers of the selected group level. If you want to customize the icon, uncheck the option.

**Image**

Specifies the image for the markers of the selected group level. Input the URL for a web image or select Browse button to specify a local image.

* **Width**  
   Specifies the width of the image.
* **Height**  
   Specifies the height of the image.

**Shadow**

Specifies the shadow image for the markers of the selected group level. Input the URL for a web image or select Browse button to specify a local image. Only available for Google Maps types.

* **Width**  
   Specifies the width of the shadow image.
* **Height**  
   Specifies the height of the shadow image.

**Constrain Proportions**

Specifies whether to change the width and height for the marker image/shadow at the same time in a certain proportion. If checked, when the width/height is changed, the height/width will also be changed in a certain proportion.

**Hide Markers**

Specifies whether to show or hide the markers of the selected group level.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564902-Create-Geographic-Map-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586081-Create-Geographic-Map-Dialog-for-Web-Report-)
