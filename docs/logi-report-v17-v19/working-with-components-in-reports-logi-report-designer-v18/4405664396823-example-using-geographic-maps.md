---
title: "Example: Using Geographic Maps"
id: 4405664396823
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664396823-Example-Using-Geographic-Maps
updated_at: 2022-01-27T20:34:32Z
---

# Example: Using Geographic Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661389335-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664397975-Using-Shape-Maps)

# Example: Using Geographic Maps

This topic demonstrates how you can add a geographic map in a library component and use it in JDashboard.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **Home** > **New** > **Library Component**.
3. In the Select Component for Library Component dialog box, select **Blank** and select **OK**.
4. From the **Components** panel, drag the **Geographic Map** icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/4420556208919/icon_geomap.gif) in the **Visual** category to the library component. Designer displays the Create Geographic Map dialog box.
5. In the **Data** screen, select **WorldWideSalesBV** in Data Source 1, then select **Next**.
6. In the **Display** screen, add the group objects **Country** and then **State** as the group-by fields to the **Drill Path** box.
7. Select **Enable Area**. Designer selects **Enable Marker** by default.

   Next, we define the marker and area properties for the Country group level.
8. Select **Country** in the Drill Path box.
9. Drag the group object **Country** from the **Resources** box to the **Shape By** text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4420542155927/btn_shp.gif) beside the text box.
10. In the Edit Shapes dialog box, select anywhere in the **Data Items** box and select **Ctrl+A** on the keyboard to select all countries, then select the icon ![Solid Circle icon](https://devnet.logianalytics.com/hc/article_attachments/4420556241559/cmpnt_map_geo_crclicon.gif.gif) in the preview box below the pattern name to apply the shape to all countries. Select **OK** to apply the shape.

    ![Edit Shapes](https://devnet.logianalytics.com/hc/article_attachments/4420556241815/cmpnt_map_geo_exmpl0.gif)
11. Drag the aggregation object **Total Sales** from the Resources box to the **Color By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420542157335/btn_colr.gif) beside the text box.
12. In the Edit Gradient Color dialog box, keep the default gradient color, select **Middle Value** and set its value to **625816.73**, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    ![Edit Gradient Color](https://devnet.logianalytics.com/hc/article_attachments/4420556242327/cmpnt_map_geo_exmpl1.gif)
13. Drag the aggregation object **Total Cost** from the Resources box to the **Size By** text box, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4420556209815/btn_size.gif) beside the text box to specify the zoom percentage to **370%**. Select outside of the size box to apply the zoom percentage.
14. Drag the group object **Country** from the Resources box to the **Label By** text box under Marker Options.
15. Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) beside the **Marker Tip** text box, then select **<New Formula...>** from its drop-down list to create a formula to control the marker tip information.
16. In the Enter Formula Name dialog box, type **MarkerTipforCountry** and select **OK**.
17. In the Formula Editor dialog box, define the formula as follows:

    `"Country:" + " " + @"Customers.Country" + "\n" +  
     "Total Cost:" + " " + ToText(@"Orders Detail.Total Cost","$#,###.00") + "\n" +  
     "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
18. Save the formula and close the Formula Editor dialog box. Designer adds MarkerTipforCountry in the Marker Tip text box automatically.

    ![Add a Marker Tip](https://devnet.logianalytics.com/hc/article_attachments/4420550975895/cmpnt_map_geo_exmpl2.gif)
19. Drag the aggregation object **Total Sales** from the Resources box to the **Fill By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420542157335/btn_colr.gif) beside the text box.
20. In the Edit Gradient Color dialog box, select **Green-White-Orange** from the gradient color drop-down list, which is the last color at the second line in the list, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    Now, we specify the marker and area properties for the State group level.
21. Select **State** in the Drill Path box.
22. Drag the group object **State** from the Resources box to the **Shape By** text box.
23. Select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4420556209815/btn_size.gif) beside the **Size By** text box to specify the zoom percentage to **230%**. Select outside of the size box to apply the zoom percentage.
24. Drag the aggregation object **Total Sales** from the Resources box to the **Fill By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420542157335/btn_colr.gif) beside the text box.
25. In the Edit Gradient Color dialog box, select **Green** as the gradient color, which is the second color in the color list, specify the opacity to **80%**, then select **OK** to apply the gradient color.
26. Drag the group object **State** from the Resources box to the **Label By** text box under Area Options. Repeat this to add **Total Sales** to the Label By text box.
27. Repeat [steps 15 to 18](#Steps) to create another formula **AreaTipforState** to control the area tip information.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
    "State:" + " " + @"Customers.State" + "\n" +  
    "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
28. Create the formula **LocationInfoforState** for the **Location Info** option.

    `@"Customers.State" + "," + @"Customers.Country"`

    ![Add Location Info](https://devnet.logianalytics.com/hc/article_attachments/4420556242583/cmpnt_map_geo_exmpl3.gif)
29. Select **Next**.
30. In the **Filter** screen, select **Add Condition** to add a condition line and specify the filter condition as **Country != USA**.

    ![Add a Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4420550976407/cmpnt_map_geo_exmpl4.gif)
31. Select **Finish** to create the map.
32. Select the **View** tab to preview the geographic map. The map shows as a static map and Designer applies the formats we have defined in the Display screen of the map wizard to the map markers and areas.

![Preview the geographic map](https://devnet.logianalytics.com/hc/article_attachments/4420542198295/cmpnt_map_geo_exmpl5.gif)

33. Navigate to **Home** > **Save** to save the library component as **Sales Map by Country.lc**.
34. [Publish the library component](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources#Remotely) to the default location on Server together with the resources it uses.
35. Create a dashboard on Server.
36. In the **Resources** panel of JDashboard, locate the library component Sales Map by Country.lc in the **Component Library** node and drag it to the dashboard body.
37. Point to a marker, and JDashboard displays its tip information just as what we have defined in the map wizard.

    ![Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4420550976663/cmpnt_map_geo_exmpl6.gif)
38. There are two group levels in this geographic map component, first by Country and then by State, so for the higher group level, we can perform the go-down action, and for the lower group level the go-up action. Point to the marker representing **Germany**, select it, or right-click it and select **Go Down** from the shortcut menu. The geographic map jumps one group level down to show the information of states in Germany, and JDashboard displays the filter condition "Country: Germany" at the bottom of the geographic map.

    ![Click Geographic Map in Dashboard with Information of a State](https://devnet.logianalytics.com/hc/article_attachments/4420550977175/cmpnt_map_geo_exmpl7.gif)
39. Scroll the mouse over the geographic map to zoom it out or in. By scrolling the mouse down, we can get a wider area on the map.

    ![Zoom Out the Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4420556243223/cmpnt_map_geo_exmpl8.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661389335-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664397975-Using-Shape-Maps)
