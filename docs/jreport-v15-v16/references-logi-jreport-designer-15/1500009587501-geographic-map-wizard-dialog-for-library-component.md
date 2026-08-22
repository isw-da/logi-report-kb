---
title: "Geographic Map Wizard Dialog (for Library Component)"
id: 1500009587501
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587501-Geographic-Map-Wizard-Dialog-for-Library-Component
updated_at: 2021-07-24T05:55:09Z
---

# Geographic Map Wizard Dialog (for Library Component)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566262-Geographic-Map-Wizard-Dialog-for-Page-Report-)

# Geographic Map Wizard Dialog (for Library Component)

The Geographic Map Wizard dialog for library component appears when you right-click a geographic map and then select Geographic Map Wizard from the shortcut menu. It helps you modify a [geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map) that has been created.

The wizard consists of the following screens:

* [Data](#Data)
* [Display](#Display)

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

## Data

Specifies the business view used by the geographic map. [See the screen](javascript:%20void(null)).

![Geographic Map Wizard for Library Component - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889336727/gmpwzd_dt_wb.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

## Display

Specifies the data fields that you want to display in the geographic map. [See the screen](javascript:%20void(null)).

![Geographic Map Wizard for Library Component - Display](https://devnet.logianalytics.com/hc/article_attachments/4404889338263/gmpwzd_dsply_lc.gif)

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

Lists all the available data resources. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected field to the geographic map.

**Enable Marker**

Enables specifying the marker properties for all the groups.

**Enable Area**

Enables specifying the area properties for all the groups.

One option between Enable Marker and Enable Area must be checked at least and Enable Marker is checked by default.

**Drill Path**

Lists the fields that are used to group data in the geographic map.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected fields that are not required from the geographic map.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition for the selected group level.

**Web Behaviors**

Opens the [Web Behaviors](https://devnet.logianalytics.com/hc/en-us/articles/1500009567882-Web-Behaviors-Dialog) dialog to specify some web behaviors to the markers and areas of the selected group level.

**Marker Options**

Specifies the marker properties of the selected group in the Drill Path box. Available only when Enable Marker is checked.

* **Shape By**  
   Specifies the field used to control the shapes of the markers for the selected group level. Only the group field that represents the currently selected group level, or a group field of a higher level than the current level in the Drill Path box, or an aggregation field can be added.
  + ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif)  
     Specifies the shapes of the markers.
    - If no field is added, select a shape from the shape list, or check and select the Advanced option to open the [Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009564522-Advanced-Dialog#Map) dialog to specify an image as the shape of the markers.
    - If a field is added, opens the [Edit Shapes](https://devnet.logianalytics.com/hc/en-us/articles/1500009565382-Edit-Shapes-Dialog) dialog to specify shapes for the markers.
* **Color By**  
   Specifies the field used to control the colors of the markers for the selected group level. Only the group field that represents the currently selected group level, or group fields of higher levels than the current level in the Drill Path box, or an aggregation field can be added. When more than one group field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif)  
     Specifies the colors of the markers.
    - If no field is added, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) for the markers.
    - If one or more group fields are added, opens the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565222-Edit-Color-Dialog) dialog to specify colors for the markers.
    - If an aggregation field is added, opens the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565282-Edit-Gradient-Color-Dialog) dialog to specify a gradient color for the markers.
* **Size By**  
   Specifies the field used to control the size of the markers for the selected group level. Only an aggregation field can be added.
  + ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404893879191/btn_size.gif)  
     Specifies the size of the markers.
    - **Zoom percentage bar**  
       Specifies the zoom percentage based on the default size.
    - **Reset**  
       Specifies whether to restore the default size.
* **Label By**  
   Specifies the field to control the labels shown above the markers for the selected group level. When there are more than one field, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404893879447/btn_lbl.gif)  
     Specifies the font format of the label text.
    - ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404893794583/btn_fntface.gif)  
       Specifies the font of the label text.
    - ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404893794839/btn_fntsize.gif)  
       Specifies the font size of the label text.
    - ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404889279511/btn_bold.gif)  
       Specifies whether to make the label text bold.
    - ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404889279767/btn_italic.gif)  
       Specifies whether to make the label text italic.
    - ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404893795095/btn_underline.gif)  
       Specifies whether to underline the text.
    - ![Text color button](https://devnet.logianalytics.com/hc/article_attachments/4404889337495/btn_fntcolr.gif)  
       Specifies the color of the label text.
    - ![Text format button](https://devnet.logianalytics.com/hc/article_attachments/4404893879831/btn_fntfmt.gif)  
       Specifies the format for the field you currently select from the preview box below.
    - **Preview box**  
       Displays the specified font format effects.
    - **OK**  
       Applies the specified font format and closes the dialog.
* **Marker Tip**  
   Specifies the tip information when you hover the mouse on the markers at runtime.

**Area Options**

Specifies the area properties of the selected group in the Drill Path box. Available only when Enable Area is checked.

* **Fill By**  
   Specifies the field to control the colors that are used to fill the areas of the selected group level. Only the group field that represents the currently selected group level, or group fields of higher levels than the current level in the Drill Path box, or an aggregation field can be added. When more than one group field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
  + ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif)  
     Specifies the colors to fill the areas.
    - If no field is added, select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) for the areas.
    - If one or more group fields are added, opens the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565222-Edit-Color-Dialog) dialog to specify colors for the areas.
    - If an aggregation field is added, opens the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565282-Edit-Gradient-Color-Dialog) dialog to specify a gradient color for the areas.
* **Label By**  
   Specifies the field to control the labels shown above the areas for the selected group level. When more than one field is added, you can adjust the orderof the fields by dragging and dropping.
  + ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404893879447/btn_lbl.gif)  
     Specifies the font format of the label text.
    - ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404893794583/btn_fntface.gif)  
       Specifies the font of the label text.
    - ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404893794839/btn_fntsize.gif)  
       Specifies the font size of the label text.
    - ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404889279511/btn_bold.gif)  
       Specifies whether to make the label text bold.
    - ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404889279767/btn_italic.gif)  
       Specifies whether to make the label text italic.
    - ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404893795095/btn_underline.gif)  
       Specifies whether to underline the text.
    - ![Text color button](https://devnet.logianalytics.com/hc/article_attachments/4404889337495/btn_fntcolr.gif)  
       Specifies the color of the label text.
    - ![Text format button](https://devnet.logianalytics.com/hc/article_attachments/4404893879831/btn_fntfmt.gif)  
       Specifies the format for the field you currently selected from the preview box below.
    - **Preview box**  
       Displays the specified font format effects.
    - **OK**  
       Applies the specified font format and closes the dialog.
* **Area Tip**   
   Specifies the tip information when you hover the mouse on the areas at runtime.

**Location Info**

Specifies the mapping location of the markers or areas for the selected group by field in the Drill Path box. For each group level that you want to show on the map, specify a DBfield or formula that contains the value matching the folder name in `<install_root>\gisinfo\geocode` used by the geographic map. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566262-Geographic-Map-Wizard-Dialog-for-Page-Report-)
