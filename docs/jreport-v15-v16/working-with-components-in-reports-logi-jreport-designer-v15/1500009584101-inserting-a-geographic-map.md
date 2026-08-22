---
title: "Inserting a Geographic Map"
id: 1500009584101
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map
updated_at: 2021-07-24T05:55:59Z
---

# Inserting a Geographic Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563462-Geographic-Maps)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers)

# Inserting a Geographic Map

This topic introduces how to insert a geographic map into a web report, library component, and page report.

Below is a list of the sections covered in this topic:

> * [Inserting a Geographic Map to a Web Report](#Web)
> * [Inserting a Geographic Map to a Library Component](#LC)
> * [Inserting a Geographic Map to a Page Report](#Page)

## Inserting a Geographic Map to a Web Report

1. Position the mouse pointer at the destination where you want to insert the geographic map. A geographic map can be inserted to the blank area in a web report.
2. Do either of the following:
   * Drag the **Geographic Map** button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404889376407/btn_instgmp.gif) from the Visual category of the Components panel.
   * Select **Insert** > **Map** > **Geographic Map**.
   * Select **Home** > **Insert** > **Map** > **Geographic Map**.

   The [Create Geographic Map Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009586081-Create-Geographic-Map-Dialog-for-Web-Report-) appears.
3. In the Data screen of the wizard, select a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) in the current catalog on which the geographic map will be created.

   ![Create Geological Map - Data in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893937175/crtgmp_dt_wb.gif)
4. In the Display screen, specify the map type from the Map Type drop-down list, it could be OpenStreetMap - Standard, OpenCycleMap - Cycle Map, OpenCycleMap - Transport Map, Google Maps - Roadmap, Google Maps - Satellite or Google Maps - Terrain.

   ![Create Geological Map wizard - Display in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893937431/crtgmp_dsply_wb.gif)
5. The Resources box lists all the elements in the selected business view, you can further edit the business view if you want.

   To edit the business view, right-click the business view or any element in it and select **Edit** from the shortcut menu. The Business View Editor is displayed. [Edit the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562622-Editing-a-Business-View) as you want.

   To change the display name of the business view or an element, right-click the business view or the element and select **Rename** from the shortcut menu. Enter the new name in the name text box and select outside of the box to confirm the new name.

   To delete an element, right-click the element and select **Delete** from the shortcut menu.
6. Add the fields from the Resources box to the Drill Path box as the grouping criteria. To add a field, select the field in the Resources box as the group by field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the selected node in the Drill Path box. If a field is not required, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) or drag and drop it out of the Drill Path box. To adjust the order of the added group levels, select the group and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) above the Drill Path box.

   **For an added group, you can specify the Select N condition for it. To do this:**

   1. Select the group by field in the Drill Path box, then select the **Select N** button. The [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog appears.

      ![Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893854615/slctn.gif)
   2. You will see that the field you have just selected is displayed in the In text box. From the Select N drop-down list, select **Top N** or **Bottom N**, and then further specify a number or an Integer-typed parameter. If the number or the parameter value is N, then the first or last N groups in that group level will be displayed.
   3. To display all the other groups that do not match the Select N condition (which are by default hidden) in an additional group, check the **Other** box and type a name for the additional group.
   4. Select **OK** to accept the condition.
7. To enable setting the marker and area properties for all groups, check the **Enable Marker** and **Enable Area** checkboxes (one of the two checkboxes must be checked at least and Enable Marker is checked by default).
8. Select each group level from the Drill Path box and specify its marker properties.
   1. Specify the shape of the markers in any of the following ways.
      * If you want to use a shape as the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif) next to the Shape By box and select a shape from the shape list, then select outside of the shape list to apply the selected shape.
      * If you want to use an image to be the shape of the markers, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif), then check the checkbox ahead of the **Advanced** option in the shape list. A default image will then be applied as the shape of the markers. If you want to customize the image, after checking the checkbox, select **Advanced** to open the [Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009564522-Advanced-Dialog#Map) dialog to specify the image.

        ![Shape Advanced dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893956887/advncd2.gif)

        1. Uncheck the **Default Icon** option.
        2. Input the URL for a web image in the Image text box, or select the **Browse** button to specify a local image.
        3. Specify the width and height of the image.
        4. If you want to change the width and height for the image at the same time in a certain proportion, check **Constrain Proportion**.
        5. If the map is of any Google Maps type, you can further specify a shadow image for the markers.
        6. When done, select **OK** to apply the images and return to the map wizard.
      * If you want to control the shapes of the markers by field values, select the group field that represents the currently selected group level, or a group field of a higher level than the current level in the Drill Path box, or an aggregation field from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the Shape By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif) to open the [Edit Shapes](https://devnet.logianalytics.com/hc/en-us/articles/1500009565382-Edit-Shapes-Dialog) dialog to edit the shapes.

        ![Edit Shapes dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893922327/edtshp.gif)

        1. From the shape pattern drop-down list, select the required pattern. A preview of the shapes in the selected pattern will be displayed in the box below.
        2. The field values with the shapes in the selected pattern are listed in the Data Items box. You can change the shape for each value by selecting it and then selecting a shape in the preview box. Note that if an aggregation field has been added to control the shapes, the Data Items box will be blank. You cannot customize the shapes and the default shapes in the selected pattern will be applied at runtime.
        3. Select **OK** to apply the specified shapes to the markers and return to the map wizard.
   2. Specify the color of the markers in any of the following ways.
      * Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) next to the Color By text box and select a color from the color palette or select **More Colors** on the color palette to open the Pick a Color dialog, with which you can set a full range of color.
      * If you want to control the colors of the markers by group values, select the group field that represents the currently selected group level, or a group field of a higher level than the current level in the Drill Path box from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the Shape By text box. You can add more than one group fields and when several group fields are added, you can adjust the order of the fields by dragging and dropping them in the text box. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) to open the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565222-Edit-Color-Dialog) dialog to edit the colors.

        ![Edit Color dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889368855/edtclr.gif)

        1. From the color pattern drop-down list, select the required pattern. A preview of the colors in the selected pattern will be displayed in the box below.
        2. The field values with the colors in the selected pattern are listed in the Data Items box. You can change the color for each value by selecting it and then selecting a color in the preview box.
        3. Specify the opacity of the colors in the Opacity text box.
        4. Select **OK** to apply the specified colors to the markers and return to the map wizard.
      * If you want to control the colors of the markers by aggregation values, select an aggregation field from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Color By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) to open the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009565282-Edit-Gradient-Color-Dialog) dialog to edit the colors.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404893925527/edtgrdntclr.gif)

        1. Select a gradient color from the color drop-down list. A preview of the gradient color will be displayed on the color bar.
        2. You can further customize the gradient start color, middle color and end color by selecting the corresponding triangle below the color bar to select a color from the color palette or select **More Colors** on the color palette to access the Pick a Color dialog in which you can select a color within a wider range. The middle and start colors can be deleted, however, if the start color is deleted, a default start color will still be applied automatically. To add the start and middle colors back, select **+** and specify the color on the color palette. After you change a default gradient color, it will be saved as a customized gradient color and you will find the name changed to Customize in the color drop-down list.
        3. Select **Reversed** if you want to reverse the direction of the gradient color.
        4. Check the **Middle Value** checkbox and specify the middle data value mapping to the middle color, which takes effect only when the middle color is not null. Then the gradient color will change from the start color to the middle color, and then change from the middle color to the end color. You can also set the middle value to 0 and check the **Auto Expand Start/End value** checkbox, in which case, the negative and positive values of the maximum absolute value will be used to map to the start color and end color, and 0 will always be in the center of the data range.
        5. Select the color image button beside Color of Null Values to specify a color for null values on the color palette, or select **More Colors** on the color palette to access the Pick a Color dialog in which you can select a color within a wider range, or you can input the hexadecimal value of a color directly in the text box after #.
        6. Select a gradient color algorithm between two colors from the Gradient By drop-down list, which can be Auto, RGB or HSL.
        7. Specify the opacity of the gradient color in the Opacity text box.
        8. Select **OK** to apply the specified gradient color to the markers and return to the map wizard.
   3. Select an aggregation field from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the Size By text box if you want to control the size of the markers by aggregation values, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404893879191/btn_size.gif) next to the Size By text box to specify the zoom percentage based on the default size. To restore the default size, select **Reset**.
   4. Add the fields to the Label By text box to specify the labels shown above the markers by selecting them one by one and selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or by dragging and dropping them to the box, then select ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404893879447/btn_lbl.gif) next to the Label By text box to set the font properties of the labels. When more than one field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
   5. Type the tip information which displays when you hover the mouse on the markers at runtime in the Marker Tip text box directly. You can also use a formula to control the tip.
9. Select each group level from the Drill Path box and specify its area properties.
   1. Specifies the colors that are used to fill the areas
      in the Fill By text box using the same way for [specifying the marker colors](#Color).
   2. Add the fields to the Label By text box to specify the labels shown above the areas by selecting them one by one and selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or by dragging and dropping them to the box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893879447/btn_lbl.gif) next to the Label By text box to set the font properties of the labels. When more than one field is added, you can adjust the order of the fields by dragging and dropping them in the text box.
   3. Type the tip information which displays when you hover the mouse on the areas at runtime in the Area Tip text box directly. You can also use a formula to control the tip.
10. Select each group level from the Drill Path box and specify the locations of the markers and areas of the group by selecting a DBField or a formula from the Location Info drop-down list which contains the values matching the folder names in `<install_root>\gisinfo\geocode`. For example you may group by Country and State. For State, you would want to use a formula fStateCountry that concatenates state and country so Google Maps, OpenStreetMap or OpenCycleMap knows which state to use such as "New York, USA" or "California, USA".

    Logi JReport also supports using longitudes and latitudes as locations of the markers, however before you can do this, you need to change the value of the className option for geocoding to *com.jinfonet.web.modules.map.service.DirectGeoCoder* in the file config.json which is stored in `<install_root>\gisinfo` for both Logi JReport Designer and Logi JReport Server before starting them, then in Logi JReport Designer create a formula as follows and select it from the Location Info drop-down list: `@LongitudeValue + “,” + @LatitudeValue`.
11. In the Filter screen, you may define some filter conditions to filter the data displayed in the geographic map. You can select a predefined filter from the specified business view if there are any from the Filter drop-down list to apply, or select **User Defined** in the list to [define a new filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

    ![Create Geographic Map wizard - Filter in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404889376663/crtgmp_fltr_wb.gif)
12. Select **Finish** to insert the geographic map.

## Inserting a Geographic Map to a Library Component

1. Follow above [steps 1 to 10](#Web)  in inserting a geographic map to a web report to specify the geographic map information in the Data and Display screens of the [Create Geographic Map Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009564902-Create-Geographic-Map-Dialog-for-Library-Component-).
2. Select each group level from the Drill Path box to bind web behaviors to the markers and areas of the group.
   1. Select the **Web Behaviors** button. The [Web Behaviors](https://devnet.logianalytics.com/hc/en-us/articles/1500009567882-Web-Behaviors-Dialog) dialog appears.

      ![Web Behaviors dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893845271/wbbhvr.gif)
   2. In the Marker tab, select a trigger event from the drop-down list in the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to open the Web Action List dialog, where you can bind a web action to the markers which will be triggered when the specified event occurs on the markers.

      To add a web behavior line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), and if a web behavior is not required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.

      Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the behaviors. Then at runtime, when an event that has been bound with more than one action happens, the upper action will be triggered first.
   3. Switch to the Area tab and follow the same steps to bind web behaviors to the map areas.
   4. Select **OK** to apply the web behaviors to the group and return to the map wizard.

   The web actions you can bind to the map markers and areas include Filter, Sort, Parameter, Property and SendMessage. For details about these web actions, refer to [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).
3. In the Filter screen, you may define some filter conditions to filter the data displayed in the geographic map. You can select a predefined filter from the specified business view if there are any from the Filter drop-down list to apply, or select **User Defined** in the list to [define a new filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).
4. Select **Finish** to insert the geographic map.

## Inserting a Geographic Map to a Page Report

If you want to use geographic maps in a page report, you need to make sure the page report is created using query resources. Geographic map is not supported in page reports that are based on business views.

1. Position the mouse pointer at the destination where you want to insert the geographic map. A geographic map can be inserted into the page report areas listed in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship).
2. Do either of the following:
   * Drag the **Geographic Map** button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404889376407/btn_instgmp.gif) from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Map** > **Geographic Map**.
   * Select **Home** > **Insert** > **Map** > **Geographic Map**.

   The [Create Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/1500009564922-Create-Geographic-Map-Dialog-for-Page-Report-) wizard appears.
3. In the Data screen, select the data resource on which to create the geographic map. If the given data resources are not what you want, select the first item  in the corresponding resource node to create one. When a query is selected, select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query) if required. Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the geographic map, select the **More Options** button and then:

   * Check the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if necessary, or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi JReport will still run the query separately for each dataset.
   * Check the **Current Dataset** radio button to make the geographic map inherit the dataset from its parent.

   ![Create Gepgraphic Map wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404893937687/crtgmp_dt.gif)
4. In the Group screen, add the fields as the grouping criteria. For more information about data grouping, see [Grouping the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Create Gepgraphic Map wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404889376919/crtgmp_grp.gif)
5. In the Filter screen, you may define some optional filter conditions to filter the data displayed in the geographic map. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Create Gepgraphic Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893937943/crtgmp_fltr.gif)
6. In the Layout screen, specify the geographic data for the geographic map, which is GeoData.xml in the `<install_root>\gisinfo` directory by default. If the XML file that you specify does not exist it will be created in the `<install_root>\gisinfo` directory. The geographic data XML file is used to map the geographic latitude and longitude coordinates from Google Maps, OpenStreetMap or OpenCycleMap based on the location information specified for each group in the Marker tab. When the location information key string of a group value matches the "nm" field in the XML file, you will get the related latitude and longitude value for this group value.

   ![Create Gepgraphic Map wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404893938199/crtgmp_layout.gif)

   You can also import an XML file which contains predefined geographic data including latitude and longitude for the specific "nm" field. By default, the XML file is located in the `<install_root>\gisinfo` directory, if not, the file will be copied to this directory after it is imported. When you publish the report from Designer you can specify the gisinfo files to publish to the Server from the Geographic Information tab.

   If you do not publish the geographical information it will be created automatically when you first run the report.

   Then specify the map type from the Map Type drop-down list, which can be Google Maps - Roadmap, Google Maps - Satellite, Google Maps - Terrain, OpenStreetMap - Standard, OpenCycleMap - Cycle Map or OpenCycleMap - Transport Map.
7. In the Marker screen, select each group level from the Geographic Map box and specify its marker properties.

   ![Create Gepgraphic Map wizard - Marker](https://devnet.logianalytics.com/hc/article_attachments/4404893938455/crtgmp_mkr.gif)

   Specify the location of the markers by selecting a DBField or a formula from the Location Info drop-down list which contains the values matching the "nm" field in the geographic data XML file. The values seen in this Location Info field will be used to create the "nm" field values when the XML does not already exist.

   Specify the tip information which displays when you hover the mouse on the markers at runtime by typing it in the Marker Tip text box directly. You can also use a formula to control the tip.

   To customize the image for the markers, uncheck the **Default Icon** option, then specify the image, the shadow image (only available for Google Maps types), and their width and height respectively. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, check **Constrain Proportion**.

   Specify whether to show or hide the markers. You can simply select true or false from the Hide Markers drop-down list, or use a formula to control it.
8. Select **Finish** to insert the geographic map.

   If you have used the Insert menu tab command to insert the geographic map into a page report, and specified to insert it to position other than the report body or tabular cell, after selecting Finish in the wizard, you need to drag it to the destination using your mouse in order to insert the geographic map where you want it.

When a geographic map has been created, you can:

* Further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the geographic map.
* Apply some filter conditions to narrow down the records displayed in the geographic map the same as you do for a table (for details, see [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)).
* Set up a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link) between the geographic map and its parent when it is inserted into a banded object in a page report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563462-Geographic-Maps)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers)
