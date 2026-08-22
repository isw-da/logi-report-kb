---
title: "Inserting Geographic Maps in a Report"
id: 1500010029142
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029142-Inserting-Geographic-Maps-in-a-Report
updated_at: 2021-07-24T10:39:20Z
---

# Inserting Geographic Maps in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029122-Geographic-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063861-Modifying-Geographic-Maps)

# Inserting Geographic Maps in a Report

With the geographic map wizard, it is easy to create geographic maps in a report, however the wizard varies with the report type: web report/library component and page report.

If you want to use geographic maps in a page report, you need to make sure the page report is created using query resources. Geographic map is not supported in page reports that are based on business views.

A geographic map can be inserted into the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-#Relationship). When it is inserted into a banded object, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500010028662-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the geographic map and its parent.

Below is a list of the sections covered in this topic:

* [Creating Geographic Maps in a Web Report/Library Component](#Web)
* [Creating Geographic Maps in a Page Report](#Page)

## Creating Geographic Maps in a Web Report/Library Component

1. Position the mouse pointer at the destination where you want to insert the geographic map.
2. Do either of the following:
   * Drag ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404909233175/btn_instgmp.gif) from the Visual category of the Components panel.
   * Select **Insert** > **Map** > **Geographic Map**.
   * Select **Home** > **Insert** > **Map** > **Geographic Map**.

   The [Create Geographic Map Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010065121-Create-Geographic-Map-Dialog#Web) appears, which contains a set of screens for helping you define a geographic map easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select a business view in the current catalog using which to create the geographic map.

   ![Create Geological Map wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901278487/crtgmp_dt_wb.gif)
4. In the Display screen, specify the map type from the Map Type drop-down list, it could be one of the following: OpenStreetMap - Standard, OpenCycleMap - Cycle Map, OpenCycleMap - Transport Map, Google Maps - Roadmap, Google Maps - Satellite and Google Maps - Terrain.

   ![Create Geological Map wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404909233431/crtgmp_dsply_wb.gif)
5. The Resources box lists all the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314071/bv_grp.gif) and aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404909272471/bv_agg.gif) in the specified business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314583/bv_dynfmla_grp.gif) and dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404909272727/bv_dynfmla_agg.gif) for the business view in the current report. You can use them to create the geographic map.

   In the Resources box, you can also further edit the business view and the objects as follows:

   * To edit the business view, right-click the business view or any object in it and select **Edit** from the shortcut menu, then [edit the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog) in the Business View Editor as required.
   * To change the display name of the business view or an object, right-click the business view or the object and select **Rename** from the shortcut menu. Enter the new name in the name text box and select outside of the box to confirm the new name.
   * To delete an object, right-click it and select **Delete** from the shortcut menu.
6. In the Drill Path box specify how data in the geographic map will be grouped.

   To add a group, select a group object or dynamic formulas used as Group in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the selected node in the Drill Path box; to remove an unwanted group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif) or drag and drop it out of the Drill Path box. Make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) above the Drill Path box to adjust the group levels. For any group, you can specify a Select N condition for it if needed (for details about the feature, see [Specifying Select N Conditions for the Groups)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#SelectN).

   **Tip:** When more than one groups are added to the Drill Path box, the go-down and go-up actions on the geographic map will follow this hierarchical path. By default, only values of the first group level are shown on the geographic map in Logi JReport Designer view mode, exported result, Web Report Studio and JDashboard.
7. To enable setting the marker and area properties for all groups, check the **Enable Marker** and **Enable Area** checkboxes (one of the two checkboxes must be checked at least and Enable Marker is checked by default).
8. Select each group level from the Drill Path box and specify its marker properties.
   1. Specify the shape of the markers in any of the following ways.
      * If you want to use a shape as the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404909190039/btn_shp.gif) next to the Shape By box and select a shape from the shape list, then select outside of the shape list to apply the selected shape.
      * If you want to use an image to be the shape of the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404909190039/btn_shp.gif), then check the checkbox ahead of the **Advanced** option in the shape list. A default image will then be applied as the shape of the markers. If you want to customize the image, after checking the checkbox, select **Advanced** to open the [Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500010064781-Advanced-Dialog#Map) dialog to specify the image.

        ![Shape Advanced dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901295767/advncd2.gif)

        1. Uncheck the **Default Icon** option.
        2. Input the URL for a web image in the Image text box, or select the **Browse** button to specify a local image.
        3. Specify the width and height of the image.
        4. If you want to change the width and height for the image at the same time in a certain proportion, check **Constrain Proportion**.
        5. If the map is of any Google Maps type, you can further specify a shadow image for the markers.
        6. When done, select **OK** to apply the images and return to the map wizard.
      * If you want to control the shapes of the markers by values, select the group object that represents the currently selected group level, or a group object of a higher level than the current level in the Drill Path box, or an aggregation object from the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the Shape By text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404909190039/btn_shp.gif) to open the [Edit Shapes](https://devnet.logianalytics.com/hc/en-us/articles/1500010065741-Edit-Shapes-Dialog) dialog to edit the shapes.

        ![Edit Shapes dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901266327/edtshp.gif)

        1. From the shape pattern drop-down list, select the required pattern. A preview of the shapes in the selected pattern will be displayed in the box below.
        2. The field values with the shapes in the selected pattern are listed in the Data Items box. You can change the shape for each value by selecting it and then selecting a shape in the preview box. Note that if an aggregation field has been added to control the shapes, the Data Items box will be blank. You cannot customize the shapes and the default shapes in the selected pattern will be applied at runtime.
        3. Select **OK** to apply the specified shapes to the markers and return to the map wizard.
   2. Specify the color of the markers in any of the following ways.
      * Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404901214487/btn_colr.gif) next to the Color By text box and select a color from the color palette or select **More Colors** on the color palette to open the Pick a Color dialog, with which you can set a full range of color.
      * If you want to control the colors of the markers by group values, select the group object that represents the currently selected group level, or a group object of a higher level than the current level in the Drill Path box from the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the Shape By text box. You can add more than one group objects and when several group objects are added, you can adjust their display order by dragging and dropping them in the text box. Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404901214487/btn_colr.gif) to open the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500010030382-Edit-Color-Dialog) dialog to edit the colors.

        ![Edit Color dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901270039/edtclr.gif)

        1. From the color pattern drop-down list, select the required pattern. A preview of the colors in the selected pattern will be displayed in the box below.
        2. The field values with the colors in the selected pattern are listed in the Data Items box. You can change the color for each value by selecting it and then selecting a color in the preview box.
        3. Specify the opacity of the colors in the Opacity text box.
        4. Select **OK** to apply the specified colors to the markers and return to the map wizard.
      * If you want to control the colors of the markers by aggregation values, select an aggregation object from the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add it to the Color By text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404901214487/btn_colr.gif) to open the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500010030442-Edit-Gradient-Color-Dialog) dialog to edit the colors.

        ![Edit Gradient Color dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901268759/edtgrdntclr.gif)

        1. Select a gradient color from the color drop-down list. A preview of the gradient color will be displayed on the color bar.
        2. You can further customize the gradient start color, middle color and end color by selecting the corresponding triangle below the color bar to select a color from the color palette or select **More Colors** on the color palette to access the Pick a Color dialog in which you can select a color within a wider range. The middle and start colors can be deleted, however, if the start color is deleted, a default start color will still be applied automatically. To add the start and middle colors back, select **+** and specify the color on the color palette. After you change a default gradient color, it will be saved as a customized gradient color and you will find the name changed to Customize in the color drop-down list.
        3. Select **Reversed** if you want to reverse the direction of the gradient color.
        4. Check the **Middle Value** checkbox and specify the middle data value mapping to the middle color, which takes effect only when the middle color is not null. Then the gradient color will change from the start color to the middle color, and then change from the middle color to the end color. You can also set the middle value to 0 and check the **Auto Expand Start/End value** checkbox, in which case, the negative and positive values of the maximum absolute value will be used to map to the start color and end color, and 0 will always be in the center of the data range.
        5. Select the color indicator button beside Color of Null Values to specify a color for null values on the color palette, or select **More Colors** on the color palette to access the Pick a Color dialog in which you can select a color within a wider range, or you can input the hexadecimal value of a color directly in the text box after #.
        6. Select a gradient color algorithm between two colors from the Gradient By drop-down list, which can be Auto, RGB or HSL.
        7. Specify the opacity of the gradient color in the Opacity text box.
        8. Select **OK** to apply the specified gradient color to the markers and return to the map wizard.
   3. Select an aggregation object from the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the Size By text box if you want to control the size of the markers by aggregation values, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404909190295/btn_size.gif) next to the Size By text box to specify the zoom percentage based on the default size. To restore the default size, select **Reset**.
   4. Add objects to the Label By text box to specify the labels shown above the markers by selecting them one by one and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or by dragging and dropping them to the box. When more than one object is added, you can adjust their display order by dragging and dropping them in the text box. You can select ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404901214743/btn_lbl.gif) next to the Label By text box to set the [font properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010065121-Create-Geographic-Map-Dialog#LabelBy) of the labels.
   5. Type the tip information which displays when you hover the mouse on the markers at runtime in the Marker Tip text box directly, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and then select a field or [use a formula to control the tip](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).
9. Select each group level from the Drill Path box and specify its area properties.
   1. Specifies the colors that are used to fill the areas in the Fill By text box using the same way for [specifying the marker colors](#Color).
   2. Add objects to the Label By text box to specify the labels shown above the areas by selecting them one by one and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or by dragging and dropping them to the box. When more than one object is added, you can adjust their display order by dragging and dropping them in the text box. You can select ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404901214743/btn_lbl.gif) next to the Label By text box to set the [font properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010065121-Create-Geographic-Map-Dialog#LabelBy) of the labels.
   3. Type the tip information which displays when you hover the mouse on the areas at runtime in the Area Tip text box directly, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and then select a field or formula from the drop-down list to control the tip. If the given formulas cannot meet your requirements, select **<New Formula...>** to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500010068541-Creating-Formulas-in-a-Catalog).
10. Select each group level from the Drill Path box and specify the location information of the markers and areas of the group by typing it in the Location Info text box directly or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and then select a field or formula from the drop-down list which contains the values matching the folder names in `<install_root>\gisinfo\geocode`. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

    Logi JReport also supports using longitudes and latitudes as locations of the markers, however before you can do this, you need to change the value of the className option for geocoding to *com.jinfonet.web.modules.map.service.DirectGeoCoder* in the file config.json which is stored in `<install_root>\gisinfo` for both Logi JReport Designer and Logi JReport Server before starting them, then in Logi JReport Designer create a formula as follows and select it from the Location Info drop-down list:

    `@LongitudeValue + “,” + @LatitudeValue`
11. If you are creating a geographic map in a library component, you can bind web behaviors to the markers and areas of each group level.
    1. Select a group in the Drill Path box, then select the **Web Behaviors** button. The [Web Behaviors](https://devnet.logianalytics.com/hc/en-us/articles/1500010032962-Web-Behaviors-Dialog) dialog appears.

       ![Web Behaviors dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901169431/wbbhvr.gif)
    2. In the Marker tab, select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) that appears in the text box.
       In the Web Action List dialog, bind a web action to the markers [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) in the library component, which will be triggered when the specified event occurs on the markers. The web actions you can bind include Parameter, Filter, Sort, Change Property and Send Message.
    3. To add more web behaviors, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and define them as required; if a web behavior is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif).
    4. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the behaviors, then at runtime when an event that has been bound with more than one action happens, the upper action will be triggered first.
    5. Switch to the Area tab to bind web behaviors to the areas of the selected group in the same way.
    6. Select **OK** to apply the web behaviors to the group and return to the map wizard.
    7. Select other groups in the Drill Path box and bind web behaviors to their markers and areas if needed.
12. In the Filter screen, apply a filter to reduce the data displayed in the geographic map. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

    ![Create Geological Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901278743/crtgmp_fltr_wb.gif)
13. Select **Finish** to insert the geographic map.

## Creating Geographic Maps in a Page Report

1. Position the mouse pointer at the destination where you want to insert the geographic map.
2. Do either of the following:
   * Drag ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404909233175/btn_instgmp.gif) from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Map** > **Geographic Map**.
   * Select **Home** > **Insert** > **Map** > **Geographic Map**.

   The [Create Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/1500010065121-Create-Geographic-Map-Dialog#Page) wizard appears, which contains a set of screens for helping you define a geographic map easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the data resource in the current catalog using which to create the geographic map.

   ![Create Gepgraphic Map wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909233687/crtgmp_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one. When a query is selected, select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) if required. Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the geographic map, select the **More Options** button and then:

   * Check the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if necessary, or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi JReport will still run the query separately for each dataset.
   * Check the **Current Dataset** radio button to make the geographic map inherit the dataset from its parent.
4. In the Group screen, specify the criteria for grouping data in the geographic map using the same way for [grouping data in a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables).

   ![Create Gepgraphic Map wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404909234071/crtgmp_grp.gif)
5. In the Filter screen, add filter conditions on the group-by fields that have been added to the geographic map to reduce the data. For how to define a filter, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports#DefineFilter).

   ![Create Gepgraphic Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901279127/crtgmp_fltr.gif)
6. In the Layout screen, specify the geographic data for the geographic map and the map type. Logi JReport supports the following map types: Google Maps - Roadmap, Google Maps - Satellite, Google Maps - Terrain, OpenStreetMap - Standard, OpenCycleMap - Cycle Map or OpenCycleMap - Transport Map.

   ![Create Gepgraphic Map wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901279383/crtgmp_layout.gif)

   By default, GeoData.xml in the `<install_root>\gisinfo` directory is used for mapping the geographic latitude and longitude coordinates from Google Maps, OpenStreetMap or OpenCycleMap based on the location information specified for each group in the Marker screen. When the location information key string of a group value matches the "nm" field in the XML file, you will get the related latitude and longitude value for this group value. You can also select **Browse** to import an XML file which contains predefined geographic data including latitude and longitude for the specific "nm" field and the file will be copied to `<install_root>\gisinfo` after it is imported if it does not exist in the directory. When you [publish the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely) from Logi JReport Designer to Logi JReport Server you can specify the gisinfo files you want to publish. If you do not publish the geographical information it will be created automatically when you first run the report.
7. In the Marker screen, specify the marker properties for each group level.

   ![Create Gepgraphic Map wizard - Marker](https://devnet.logianalytics.com/hc/article_attachments/4404909234327/crtgmp_mkr.gif)

   1. Select a group from the Geographic Map box.
   2. In the Location Info text box, specify the location information of the group markers. You can type in the location directly in the text box or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a field or formula from the drop-down list which contains the values matching the "nm" field in the geographic data XML file. The values seen in this Location Info field will be used to create the "nm" field values when the XML does not already exist.
   3. Specify the tip information which displays when you hover the mouse on the markers at runtime by typing it in the Marker Tip text box directly, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and then select a field or formula from the drop-down list to control the tip.
   4. To customize the image for the markers, uncheck the **Default Icon** option, then specify the image, the shadow image (only available for Google Maps types), and their width and height respectively. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, check **Constrain Proportion**.
   5. From the Hide Markers drop-down list, specify whether to show or hide the markers. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) to select a formula that returns a Boolean value to control this.
   6. Select other groups in the Geographic Map box and specify their marker properties in the same way.
8. Select **Finish** to insert the geographic map.

   If you have used the menu command to insert the geographic map and selected a panel in a banded object as the its destination, after finishing the wizard, you need to select the mouse button in the destination once again in order to insert the geographic map there.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029122-Geographic-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063861-Modifying-Geographic-Maps)
