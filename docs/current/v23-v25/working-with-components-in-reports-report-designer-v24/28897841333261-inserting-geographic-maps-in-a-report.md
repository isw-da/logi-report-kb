---
title: "Inserting Geographic Maps in a Report"
id: 28897841333261
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897841333261-Inserting-Geographic-Maps-in-a-Report
updated_at: 2024-09-30T09:10:15Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Inserting Geographic Maps in a Report

You can create geographic maps in a report easily using the geographic map wizard. However, the procedure you use with the wizard varies with the report type: web report/library component and page report. This topic introduces how you can create a geographic map using the geographic map wizard in different reports.

This topic contains the following sections:

- Creating Geographic Maps in a Web Report/Library Component

- Creating Geographic Maps in a Page Report

## 
Creating Geographic Maps in a Web Report/Library Component

- Position the mouse pointer at the allowed report location where you want to insert the geographic map.

- Do one of the following:
    
- From the Components panel, drag the Geographic Map icon  in the Visual category to the destination.

- Navigate to Insert > Map > Geographic Map.

- Navigate to Home > Insert > Map > Geographic Map.

Designer displays the Create Geographic Map dialog box. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.

- In the Data screen, specify the dataset you want to use to create the
     geographic map.
    

- In the Display screen, specify the map type from the Map Type drop-down list. It can be one of the following: OpenStreetMap - Standard, OpenCycleMap - Cycle Map, OpenCycleMap - Transport Map, Google Maps - Roadmap, Google Maps - Satellite, and Google Maps - Terrain.
    

- The Resources box lists all group objects  and aggregation objects  in the business view from which the dataset the geographic map applies is created , and the dynamic formulas used as Group  and dynamic formulas used as Aggregation  that you have created for the business view in the current report. You can use them to create the geographic map. You can also further edit the business view and the objects in the Resources box.
    
- To edit the business view, right-click the business view or any object in it and select Edit from the shortcut menu, then edit the business view in the Business View Editor dialog box as required.

- To change the display name of the business view or an object, right-click the business view or the object and select Rename from the shortcut menu. Type the new name in the name text box and select outside the box to confirm the new name.

- To delete an object, right-click it and select Delete from the shortcut menu.

- In the Drill Path box, specify how to group the data in the geographic map.
    
- To add a group, select a group object or dynamic formulas used as Group in the Resources box and select Add or drag the object from the Resources box to the selected node in the Drill Path box.

- To delete an unwanted group, select it and select Remove or drag it out of the Drill Path box.

- Use Move Up and Move Down to adjust the group levels.

- For any group, you can specify a Select N Condition for it.

 When you add more than one groups to the Drill Path box, the go-down and go-up actions on the geographic map follow this hierarchical path. By default, the geographic map only displays the values of the first group level  in the Designer view mode, exported result, Web Report Studio, and JDashboard.

- To enable setting the marker and area options for all groups, select Enable Marker  and Enable Area. You must select one of the two checkboxes at least and Designer selects Enable Marker by default.

- Select each group level from the Drill Path box and specify its marker options.

- 
Specify the shape of the markers using any of the following methods.
        
- If you want to use a shape as the markers, select  next to the Shape By box and select a shape from the shape list, then select outside the shape list to apply the selected shape.

- If you want to use an image to be the shape of the markers, select , then select the checkbox ahead of Advanced in the shape list. Designer applies a default image as the shape of the markers. If you want to customize the image, after selecting the checkbox, select Advanced to open the Advanced dialog box to specify the image.
              

- Clear the Default Icon option.

-  Type the URL for a web image in the Image text box, or select Browse to specify a local image.

- Specify the width and height of the image.

- If you want to change the width and height of the image at the same time in a certain proportion, select Constrain Proportion.

- If the map applies any Google Maps type, you can further specify a shadow image for the markers.

- Select OK to apply the image and return to the map wizard.

- If you want to control the shape of the markers by values, select the group object that represents the currently selected group level, or a group object of a higher level than the current level, or an aggregation object in the Resources box and add it to the Shape By text box, then select  to open the Edit Shapes dialog box to edit the shapes.
              

- From the shape pattern drop-down list, select the required pattern. Designer displays a preview of the shapes in the selected pattern in the box below.

- The Data Items box lists the field values with the shapes in the selected pattern. You can change the shape for each value by selecting it and then selecting a shape in the preview box. Note that if you have added an aggregation field  to control the shapes, the Data Items box is blank. You cannot customize the shapes and Server applies the default shapes in the selected pattern at runtime.

- Select OK to apply the specified shapes to the markers and return to the map wizard.

- 
Specify the color of the markers using any of the following methods.
        
- Select  next to the Color By text box to specify a color using the color palette.

- If you want to control the color of the markers by group values, select the group object that represents the currently selected group level or a group object of a higher level than the current level in the Resources box and add it to the Color By text box. You can add more than one group objects and when you add several group objects, you can adjust their display order by dragging and dropping them in the text box. Select  to open the Edit Color dialog box to edit the colors.
            

- From the color pattern drop-down list, select the required pattern. Designer displays a preview of the colors in the selected pattern in the box below.

- The Data Items box lists the field values with the colors in the selected pattern. You can change the color for each value by selecting it and then selecting a color in the preview box.

- Specify the opacity of the colors in the Opacity text box.

- Select OK to apply the specified colors to the markers and return to the map wizard.

- If you want to control the color of the markers by aggregation values, select an aggregation object in the Resources box and add it to the Color By text box, then select  to open the Edit Gradient Color dialog box to edit the colors.
            

- Select a gradient color from the color drop-down list. Designer displays a preview of the gradient on the color bar.

- Customize the starting color, middle color, and ending color of the gradient by selecting the corresponding triangle below the color bar to specify a color using the color palette. You can select the trash can icon  to delete the middle color or starting color, and select the plus sign icon + to specify the color again. When you delete the starting color, Designer applies a default starting color automatically. You cannot delete the middle color or add it when there is no starting color. After you change a default gradient color, Designer saves it as a customized gradient and you can find its name changed to Customize in the gradient color drop-down list.

- Select Reversed if you want to reverse the direction of the gradient.

- When the gradient has a middle color, Designer enables the Middle Value option. You can select it and specify the middle value you want to map to the middle color  (Designer ignores the value you specify if it is not between the start value and end value). Then the gradient changes from the starting color to the middle color, and then from the middle color to the ending color. You can also set the middle value to 0 and select Auto Expand Start/End value, in which case, Designer applies the negative and positive values of the maximum absolute value to map to the starting color and ending color, and 0 is always in the middle of the data range.

- Select the color indicator beside Color of Null Values to specify a color for null values using the color palette, or  type the hexadecimal RGB value of a color in the text box after #.

- From the Gradient By drop-down list, select the gradient algorithm you want to use for colors of the gradient: Auto, RGB, or HSL.

- Specify the opacity of the gradient in the Opacity text box.

- Select OK to apply the specified gradient color to the markers and return to the map wizard.

- Select an aggregation object in the Resources box and add it to the Size By text box if you want to control the size of the markers by aggregation values, then select  next to the Size By text box to specify the zoom percentage based on the default size. To restore the default size, select Reset.

- Add fields to the Label By text box to specify the labels shown above the markers. When you add more than one field, you can adjust their display order by dragging and dropping them in the text box. You can select  next to the Label By text box to set the font properties of the labels.

- In the Marker Tip text box, type the tip information which displays when users hover the mouse on the markers at runtime  directly, or select   and then select a field or use a formula to control the tip.

- Select each group level in the Drill Path box and specify its area options. 

- Specify the colors to fill the areas in the Fill By text box in the same way as you specify the marker colors.

- Add fields from the Resources box to the Label By text box to specify the labels shown above the areas. When you add more than one field, you can adjust their display order by dragging and dropping them in the text box. You can select  next to the Label By text box to set the font properties of the labels.
      

- In the Area Tip text box, type the tip information which displays when users hover the mouse on the areas at runtime, or select  and then select a field or use a formula to control the tip.

- Select each group level in the Drill Path box and specify the location information of the markers and areas of the group in the Location Info text box. You can type the location in the text box or select  and select a field or formula from the drop-down list which contains the values matching the folder names in <install_root>\gisinfo\geocode. For example, you may group by Country and State. For State, you would want to use a formula "fStateCountry" that concatenates state and country so Google Maps, OpenStreetMap, or OpenCycleMap knows which state to use such as "New York, USA", or "California, USA".
    Report also supports using longitudes and latitudes as locations of the markers, however, before you can do this, you need to change the value of the "className" option for geocoding to com.jinfonet.web.modules.map.service.DirectGeoCoder in config.json located in <install_root>\gisinfo for both Designer and Server before starting them, then in Designer create a formula as follows and select it from the Location Info drop-down list:

@LongitudeValue + “,” + @LatitudeValue

- If you are creating a geographic map in a library component, you can add web behaviors to the markers and areas of each group level.
    

- In the Dataset Filter screen, filter the dataset the geographic map applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.  

- Select Finish to insert the geographic map.

## 
Creating Geographic Maps in a Page Report

 You cannot create geographic maps in business view-based page reports.

- Position the mouse pointer at the allowed report location where you want to insert the geographic map.

- Do either of the following:
    
- From the Components panel, drag the Geographic Map icon  in the Visual category  to the destination.

- Navigate to Insert > Map > Geographic Map.

- Navigate to Home > Insert > Map > Geographic Map.

Designer displays the Create Geographic Map dialog box. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.

- In the Data screen, specify the dataset you want to use to create the
     geographic map. 
    

- In the Group screen, specify the criteria for grouping data in the geographic map using the same way for grouping data in a table.
    

- In the Filter screen, filter the geographic map by adding conditions based on the group-by fields you have added to it. Select here for how to define a filter.
    

- In the Layout screen, specify the geographic data for the geographic map and the map type.

- By default, Designer uses GeoData.xml in the <install_root>\gisinfo directory  for mapping the geographic latitude and longitude coordinates from Google Maps, OpenStreetMap, or OpenCycleMap based on the location information specified for each group in the Marker screen. When the location information key string of a group value matches the "nm" field in the XML file, you get the related latitude and longitude value for this group value. You can also select Browse to import an XML file that contains predefined geographic data including latitude and longitude for the specific "nm" field. Designer copies the file  to <install_root>\gisinfo after it imports the file if it does not exist in the directory. When you publish the report from Designer to Server, you can specify the gisinfo files you want to publish. If you do not publish the geographical information, Server creates it automatically when you first run the report at runtime.

- From the Map Type drop-down list, select the map type. Report supports the following map types: Google Maps - Roadmap, Google Maps - Satellite, Google Maps - Terrain, OpenStreetMap - Standard, OpenCycleMap - Cycle Map, and OpenCycleMap - Transport Map.

- 
In the Marker screen, specify the marker settings for each group level.
    

-  Select a group from the Geographic Map box.

- In the Location Info text box, specify the location information of the group markers. You can type the location in the text box or select  and select a field or formula from the drop-down list which contains the values matching the "nm" field in the geographic data XML file. Designer applies the values in this Location Info text box to create the "nm" field values if the XML does not already exist.

- In the Marker Tip text box, specify the tip information which displays when users hover the mouse on the markers at runtime. You can type the tip in the text box or select  and then select a field or formula from the drop-down list to control the tip.

- To customize the image for the markers, clear Default Icon, then specify the image, the shadow image (only available for Google Maps types), and their width and height respectively. If you want to change the width and height for the image/shadow image at the same time in a certain proportion, select Constrain Proportion.

- From the Hide Markers drop-down list, specify whether to show or hide the markers. You can also select  to select a formula that returns a Boolean value to control this.

- Select other groups in the Geographic Map box and specify their marker settings in the same way. 

- Select Finish to insert the geographic map.

- If you have selected a panel in a banded object as the destination and used the menu command to insert the geographic map, after finishing the Geographic Map dialog box, you need to select in the destination once again to insert the geographic map there.

Previous Topic  Next Topic
