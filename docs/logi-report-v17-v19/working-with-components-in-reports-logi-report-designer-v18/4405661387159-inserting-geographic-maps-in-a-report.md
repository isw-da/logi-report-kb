---
title: "Inserting Geographic Maps in a Report"
id: 4405661387159
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661387159-Inserting-Geographic-Maps-in-a-Report
updated_at: 2022-01-27T20:34:32Z
---

# Inserting Geographic Maps in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661388183-General-Introduction-to-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661389335-Modifying-Geographic-Maps)

# Inserting Geographic Maps in a Report

You can create geographic maps in a report easily using the geographic map wizard, however, the wizard varies with the report type: web report/library component and page report. Meanwhile, if you want to create geographic maps in a page report, you need to make sure the page report uses query resources, meaning you cannot create geographic maps in page reports that are based on business views. This topic introduces how you can create a geographic map with the geographic map wizard in different report.

You can insert geographic maps into the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship). When you insert a geographic map into a banded object in a page report, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the geographic map and its parent.

This topic contains the following sections:

* [Creating Geographic Maps in a Web Report/Library Component](#Web)
* [Creating Geographic Maps in a Page Report](#Page)

## Creating Geographic Maps in a Web Report/Library Component

1. Position the mouse pointer at the destination where you want to insert the geographic map.
2. Do one of the following:
   * From the **Components** panel, drag the **Geographic Map** icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/4420402508055/icon_geomap.gif) in the **Visual** category to the destination.
   * Navigate to **Insert** > **Map** > **Geographic Map**.
   * Navigate to **Home** > **Insert** > **Map** > **Geographic Map**.

   Designer displays the [Create Geographic Map Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box#Web), which contains a set of screens for helping you define a geographic map easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the business view in the current catalog that you want to use to create the geographic map.

   ![Create Geological Map wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4420394842135/crtgmp_dt_wb.gif)
4. In the **Display** screen, specify the map type from the **Map Type** drop-down list. It can be one of the following: OpenStreetMap - Standard, OpenCycleMap - Cycle Map, OpenCycleMap - Transport Map, Google Maps - Roadmap, Google Maps - Satellite, and Google Maps - Terrain.

   ![Create Geological Map wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4420402508951/crtgmp_dsply_wb.gif)
5. The **Resources** box lists all the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4420410873495/bv_grp.gif) and aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4420394888471/bv_agg.gif) in the specified business view, and the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4420402567703/bv_dynfmla_grp.gif) and dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4420410877719/bv_dynfmla_agg.gif) that you have created for the business view in the current report. You can use them to create the geographic map.

   In the Resources box, you can also further edit the business view and the objects.

   * To edit the business view, right-click the business view or any object in it and select **Edit** from the shortcut menu, then [edit the business view](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog) in the Business View Editor dialog box as required.
   * To change the display name of the business view or an object, right-click the business view or the object and select **Rename** from the shortcut menu. Type the new name in the name text box and select outside of the box to confirm the new name.
   * To delete an object, right-click it and select **Delete** from the shortcut menu.
6. In the **Drill Path** box, specify how to group the data in the geographic map.

   To add a group, select a group object or dynamic formulas used as Group in the Resources box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif) or drag the object from the Resources box to the selected node in the Drill Path box; to delete an unwanted group, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif) or drag it out of the Drill Path box. You can use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif) to adjust the group levels. For any group, you can specify a Select N condition for it (for more information about the feature, see [Specifying Select N Conditions for the Groups)](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#SelectN).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) When you add more than one groups to the Drill Path box, the go-down and go-up actions on the geographic map follow this hierarchical path. By default, the geographic map only displays the values of the first group level in the Designer view mode, exported result, Web Report Studio, and JDashboard.
7. To enable setting the marker and area options for all groups, select **Enable Marker** and **Enable Area** (you must select one of the two checkboxes at least and Designer selects Enable Marker by default).
8. Select each group level from the **Drill Path** box and specify its marker options.
   1. Specify the shape of the markers in any of the following ways.
      * If you want to use a shape as the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4420410706199/btn_shp.gif) next to the **Shape By** box and select a shape from the shape list, then select outside of the shape list to apply the selected shape.

        ![Shape List](https://devnet.logianalytics.com/hc/article_attachments/4420394760471/cmpnt_map_geo_inst_shplst.gif)
      * If you want to use an image to be the shape of the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4420410706199/btn_shp.gif), then select the checkbox ahead of **Advanced** in the shape list. Designer applies a default image as the shape of the markers. If you want to customize the image, after selecting the checkbox, select Advanced to open the [Advanced dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664428567-Advanced-Dialog-Box#Map) to specify the image.

        ![Shape Advanced dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410846743/advncd2.gif)

        1. Clear the **Default Icon** option.
        2. Type the URL for a web image in the **Image** text box, or select **Browse** to specify a local image.
        3. Specify the width and height of the image.
        4. If you want to change the width and height for the image at the same time in a certain proportion, select **Constrain Proportion**.
        5. If the map is of any Google Maps type, you can further specify a shadow image for the markers.
        6. Select **OK** to apply the image and return to the map wizard.
      * If you want to control the shapes of the markers by values, select the group object that represents the currently selected group level, or a group object of a higher level than the current level, or an aggregation object in the Resources box and add it to the **Shape By** text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4420410706199/btn_shp.gif) to open the [Edit Shapes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664465175-Edit-Shapes-Dialog-Box) to edit the shapes.

        ![Edit Shapes dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402484887/edtshp.gif)

        1. From the shape pattern drop-down list, select the required pattern. Designer displays a preview of the shapes in the selected pattern in the box below.
        2. The **Data Items** box lists the field values with the shapes in the selected pattern. You can change the shape for each value by selecting it and then selecting a shape in the preview box. Note that if you have added an aggregation field to control the shapes, the Data Items box is blank. You cannot customize the shapes and Server applies the default shapes in the selected pattern at runtime.
        3. Select **OK** to apply the specified shapes to the markers and return to the map wizard.
   2. Specify the color of the markers in any of the following ways.
      * Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420410706839/btn_colr.gif) next to the **Color By** text box and select a color from the color palette or select **More Colors** in the color palette to open the Pick a Color dialog box, with which you can set a full range of color.
      * If you want to control the colors of the markers by group values, select the group object that represents the currently selected group level or a group object of a higher level than the current level in the Resources box and add it to the **Shape By** text box. You can add more than one group objects and when you add several group objects, you can adjust their display order by dragging and dropping them in the text box. Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420410706839/btn_colr.gif) to open the [Edit Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661507479-Edit-Color-Dialog-Box) to edit the colors.

        ![Edit Color dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394820887/edtclr.gif)

        1. From the color pattern drop-down list, select the required pattern. Designer displays a preview of the colors in the selected pattern in the box below.
        2. The **Data Items** box lists the field values with the colors in the selected pattern. You can change the color for each value by selecting it and then selecting a color in the preview box.
        3. Specify the opacity of the colors in the **Opacity** text box.
        4. Select **OK** to apply the specified colors to the markers and return to the map wizard.
      * If you want to control the colors of the markers by aggregation values, select an aggregation object in the Resources box and add it to the **Color By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420410706839/btn_colr.gif) to open the [Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661511703-Edit-Gradient-Color-Dialog-Box) to edit the colors.

        ![Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402491031/edtgrdntclr.gif)

        1. Select a gradient color from the color drop-down list. Designer displays a preview of the gradient color on the color bar.
        2. You can further customize the gradient start color, middle color, and end color by selecting the corresponding triangle below the color bar to select a color from the color palette, or select **More Colors** in the color palette to access the Pick a Color dialog box in which you can select a color within a wider range. You can delete the middle and start colors; however, if you delete the start color, Designer applies a default start color automatically. To add the start and middle colors back, select the **plus sign** icon **+** and specify the color in the color palette. After you change a default gradient color, Designer saves it as a customized gradient color and you can find the name changes to **Customize** in the color drop-down list.
        3. Select **Reversed** if you want to reverse the direction of the gradient color.
        4. Select **Middle Value** and specify the middle data value mapping to the middle color, which takes effect only when the middle color is not null. Then the gradient color changes from the start color to the middle color, and then from the middle color to the end color. You can also set the middle value to **0** and select **Auto Expand Start/End value**, in which case, Designer applies the negative and positive values of the maximum absolute value to map to the start color and end color, and 0 is always in the center of the data range.
        5. Select the color indicator button beside **Color of Null Values** to specify a color for null values in the color palette, or select **More Colors** in the color palette to access the Pick a Color dialog box in which you can select a color within a wider range, or you can type the hexadecimal value of a color in the text box after **#**.
        6. Select a gradient color algorithm between two colors from the **Gradient By** drop-down list, which can be Auto, RGB, or HSL.
        7. Specify the opacity of the gradient color in the **Opacity** text box.
        8. Select **OK** to apply the specified gradient color to the markers and return to the map wizard.
   3. Select an aggregation object in the Resources box and add it to the **Size By** text box if you want to control the size of the markers by aggregation values, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4420402431255/btn_size.gif) next to the Size By text box to specify the zoom percentage based on the default size. To restore the default size, select **Reset**.

      ![Size Zooming Bar](https://devnet.logianalytics.com/hc/article_attachments/4420402431767/cmpnt_map_geo_inst_size.gif)
   4. Add fields to the **Label By** text box to specify the labels shown above the markers. When you add more than one field, you can adjust their display order by dragging and dropping them in the text box. You can select ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4420394761367/btn_lbl.gif) next to the Label By text box to set the [font properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box#LabelBy) of the labels.

      ![Label Font Propeties dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410707863/cmpnt_map_geo_inst_label.gif)
   5. In the **Marker Tip** text box, type the tip information which displays when users hover the mouse on the markers at runtime directly, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and then select a field or [use a formula to control the tip](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).
9. Select each group level in the **Drill Path** box and specify its area options.
   1. Specify the colors to fill the areas in the **Fill By** text box in the same way as you [specify the marker colors](#Color).
   2. Add fields from the Resources box to the **Label By** text box to specify the labels shown above the areas. When you add more than one field, you can adjust their display order by dragging and dropping them in the text box. You can select ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4420394761367/btn_lbl.gif) next to the Label By text box to set the [font properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box#LabelBy) of the labels.
   3. In the **Area Tip** text box, type the tip information which displays when users hover the mouse on the areas at runtime, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and then select a field or [use a formula to control the tip](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).
10. Select each group level in the **Drill Path** box and specify the location information of the markers and areas of the group in the **Location Info** text box. You can type the location in the text box or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and select a field or formula from the drop-down list which contains the values matching the folder names in `<install_root>\gisinfo\geocode`. For example, you may group by Country and State. For State, you would want to use a formula "fStateCountry" that concatenates state and country so Google Maps, OpenStreetMap, or OpenCycleMap knows which state to use such as "New York, USA", or "California, USA".

    Logi Report also supports using longitudes and latitudes as locations of the markers, however, before you can do this, you need to change the value of the "className" option for geocoding to *com.jinfonet.web.modules.map.service.DirectGeoCoder* in the file **config.json** which is stored in `<install_root>\gisinfo` for both Designer and Server before starting them, then in Designer create a formula as follows and select it from the Location Info drop-down list:

    `@LongitudeValue + “,” + @LatitudeValue`
11. If you are creating a geographic map in a library component, you can bind web behaviors to the markers and areas of each group level.
    1. Select a group in the **Drill Path** box, then select **Web Behaviors**. Designer displays the [Web Behaviors dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664592279-Web-Behaviors-Dialog-Box).

       ![Web Behaviors dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410653719/wbbhvr.gif)
    2. In the **Marker** tab, select a trigger event from the drop-down list in the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif).
       In the Web Action List dialog box, bind a web action that you want to trigger at runtime when the specified event occurs on the markers [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Action) in the library component. The web actions you can bind include Parameter, Filter, Sort, Change Property, and Send Message.
    3. To add more web behaviors, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif) and define them as required. To delete an unwanted web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif).
    4. Adjust the order of the behaviors using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif), then at runtime, when an event that has been bound with more than one action happens, JDashboard triggers the upper action first.
    5. Switch to the **Area** tab to bind web behaviors to the areas of the selected group in the same way.
    6. Select **OK** to apply the web behaviors to the group and return to the map wizard.
    7. Select other groups in the Drill Path box and bind web behaviors to their markers and areas.
12. In the **Filter** screen, apply a filter to reduce the data to display in the geographic map. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter.

    ![Create Geological Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420402509207/crtgmp_fltr_wb.gif)
13. Select **Finish** to insert the geographic map.

## Creating Geographic Maps in a Page Report

1. Position the mouse pointer at the destination where you want to insert the geographic map.
2. Do either of the following:
   * From the **Components** panel, drag the **Geographic Map** icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/4420402508055/icon_geomap.gif) in the **Visual** category to the destination.
   * Navigate to **Insert** > **Map** > **Geographic Map**.
   * Navigate to **Home** > **Insert** > **Map** > **Geographic Map**.

   Designer displays the [Create Geographic Map dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box#Page), which contains a set of screens for helping you define a geographic map easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the data resource in the current catalog that you want to use to create the geographic map.

   ![Create Gepgraphic Map wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4420394842391/crtgmp_dt.gif)

   If the predefined data resources are not what you want, you can select the first item under a resource node to create a data resource of the type in the current catalog to use. When you select a query, you can select **Edit** to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog). Designer then automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) based on the selected data resource in the page report.

   If you want to use an existing dataset in the current page report to create the geographic map, select **More Options**.
   Select **Existing Dataset** and select a dataset. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Create) in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
4. In the **Group** screen, specify the criteria for grouping data in the geographic map using the same way for [grouping data in a table](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables).

   ![Create Gepgraphic Map wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4420402509591/crtgmp_grp.gif)
5. In the **Filter** screen, add filter conditions based on the group-by fields you have added to the geographic map to reduce the data. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Gepgraphic Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420410816535/crtgmp_fltr.gif)
6. In the **Layout** screen, specify the geographic data for the geographic map and the map type. Logi Report supports the following map types: Google Maps - Roadmap, Google Maps - Satellite, Google Maps - Terrain, OpenStreetMap - Standard, OpenCycleMap - Cycle Map, and OpenCycleMap - Transport Map.

   ![Create Gepgraphic Map wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420394842903/crtgmp_layout.gif)

   By default, Designer uses **GeoData.xml** in the `<install_root>\gisinfo` directory for mapping the geographic latitude and longitude coordinates from Google Maps, OpenStreetMap, or OpenCycleMap based on the location information specified for each group in the Marker screen. When the location information key string of a group value matches the "nm" field in the XML file, you get the related latitude and longitude value for this group value. You can also select **Browse** to import an XML file which contains predefined geographic data including latitude and longitude for the specific "nm" field and Designer copies the file to `<install_root>\gisinfo` after it imports the file if it does not exist in the directory. When you [publish the report](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources#Remotely) from Designer to Server, you can specify the gisinfo files you want to publish. If you do not publish the geographical information, Server creates it automatically when you first run the report at runtime.
7. In the **Marker** screen, specify the marker settings for each group level.

   ![Create Gepgraphic Map wizard - Marker](https://devnet.logianalytics.com/hc/article_attachments/4420410816791/crtgmp_mkr.gif)

   1. Select a group from the **Geographic Map** box.
   2. In the **Location Info** text box, specify the location information of the group markers. You can type the location in the text box or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and select a field or formula from the drop-down list which contains the values matching the "nm" field in the geographic data XML file. Designer applies the values in this Location Info text box to create the "nm" field values if the XML does not already exist.
   3. In the **Marker Tip** text box, specify the tip information which displays when users hover the mouse on the markers at runtime. You can type the tip in the text box or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) and then select a field or formula from the drop-down list to control the tip.
   4. To customize the image for the markers, clear **Default Icon**, then specify the image, the shadow image (only available for Google Maps types), and their width and height respectively. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, select **Constrain Proportion**.
   5. From the **Hide Markers** drop-down list, specify whether to show or hide the markers. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420410598551/btn_fmla.gif) to select a formula that returns a Boolean value to control this.
   6. Select other groups in the Geographic Map box and specify their marker settings in the same way.
8. Select **Finish** to insert the geographic map.

   If you have used the menu command to insert the geographic map and selected a panel in a banded object as the its destination, after finishing the dialog box, you need to select in the destination once again in order to insert the geographic map there.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661388183-General-Introduction-to-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661389335-Modifying-Geographic-Maps)
