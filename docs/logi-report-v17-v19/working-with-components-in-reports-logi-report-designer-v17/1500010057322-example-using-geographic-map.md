---
title: "Example: Using Geographic Map"
id: 1500010057322
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057322-Example-Using-Geographic-Map
updated_at: 2021-07-23T19:14:47Z
---

# Example: Using Geographic Map

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057362-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps)

# Example: Using Geographic Map

This topic demonstrates how you can add a geographic map in a library component and use it in JDashboard.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **Home** > **New** > **Library Component**.
3. In the Select Component for Library Component dialog box, select **Blank** and select **OK**.
4. From the **Components** panel, drag the **Geographic Map** icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/4404856991127/icon_geomap.gif) in the Visual category to the library component. Designer displays the Create Geographic Map wizard.
5. In the **Data** screen, select **WorldWideSalesBV** from Data Source 1. Then select **Next**.
6. In the **Display** screen, add the fields **Country** and **State** in the Customers table as the group-by fields one by one to the **Drill Path** box.
7. Select the **Enable Area** checkbox. Designer selects the **Enable Marker** checkbox by default.

   Next, we define the marker and area properties for the country group level.
8. Select **Country** in the Drill Path box, select **Country** from the Customers table in the Resources box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Shape By** text box, then select the button ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404856923543/btn_shp.gif) beside the text box.
9. In the Edit Shapes dialog box, select anywhere in the **Data Items** box and select **Ctrl + A** on the keyboard to select all countries, then select the icon ![Solid Circle button](https://devnet.logianalytics.com/hc/article_attachments/4404848669975/btn_crcl.gif) in the preview box below the pattern name to apply the shape to all countries. Select **OK** to apply the shape.

   ![Edit Shapes](https://devnet.logianalytics.com/hc/article_attachments/4404848670487/cmpnt_map_geo_exmpl0.gif)
10. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Color By** text box, then select the button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856924055/btn_colr.gif) beside the text box.
11. In the Edit Gradient Color dialog box, keep the default gradient color, select the **Middle Value** checkbox and set its value to **625816.73**, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    ![Edit Gradient Color](https://devnet.logianalytics.com/hc/article_attachments/4404857041303/cmpnt_map_geo_exmpl1.gif)
12. Select the aggregation **Total Cost** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Size By** text box, then select the button ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404856924311/btn_size.gif) beside the text box to specify the zoom percentage to **370%**. Select outside of the size box to apply the zoom percentage.
13. Select **Country** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Label By** text box of the Marker Options.
14. Select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) beside the **Marker Tip** text box, then select **<New Formula...>** from its drop-down list to create a formula to control the marker tip information.
15. In the Enter Formula Name dialog box, type the name **MarkerTipforCountry** and select **OK**.
16. In the Formula Editor dialog box, define the formula as follows.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
     "Total Cost:" + " " + ToText(@"Orders Detail.Total Cost","$#,###.00") + "\n" +  
     "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
17. Save the formula and close the Formula Editor dialog box. Designer now displays MarkerTipforCountry in the Marker Tip text box.

    ![Add a Marker Tip](https://devnet.logianalytics.com/hc/article_attachments/4404848670743/cmpnt_map_geo_exmpl2.gif)
18. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Fill By** text box, then select the button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856924055/btn_colr.gif) beside the text box.
19. In the Edit Gradient Color dialog box, select **Green-White-Orange** from the gradient color drop-down list, which is the last color at the second line in the list, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    Next, we specify the marker and area properties for the state group level.
20. Select **State** in the Drill Path box, select **State** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the Shape By text box, then select the button ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404856923543/btn_shp.gif) beside the text box.
21. In the Edit Shapes dialog box, select **Pattern1** from the pattern drop-down list to apply the shapes in the pattern to all states, then select **OK**.
22. Select the button ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404856924311/btn_size.gif) beside the Size By text box to specify the zoom percentage to **230%**. Select outside of the size box to apply the zoom percentage.
23. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the Fill By text box, then select the button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856924055/btn_colr.gif) beside the text box.
24. In the Edit Gradient Color dialog box, select **Green** as the gradient color, which is the second color in the color list, specify the opacity to **80%**, then select **OK** to apply the gradient color.
25. Select **State** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the Label By text box of the Area Options. Repeat this to add Total Sales from the Orders Detail table to the Label By text box.
26. Repeat [steps 14 to 17](#Steps) to create another formula AreaTipforState to control the area tip information.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
    "State:" + " " + @"Customers.State" + "\n" +  
    "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
27. Repeat [steps 14 to 17](#Steps) to create another formula LocationInfoforState for the Location Info option.

    `@"Customers.State" + "," + @"Customers.Country"`

    ![Add Location Info](https://devnet.logianalytics.com/hc/article_attachments/4404857041687/cmpnt_map_geo_exmpl3.gif)
28. Select **Next** to go to the **Filter** screen. Select the **Add Condition** button to add a condition line, and specify the filter condition as **@Country != USA**, then select **Finish** to create the map.

    ![Add a Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404848671255/cmpnt_map_geo_exmpl4.gif)
29. Select the **View** tab to preview the geographic map. The map shows as a static map and you can see the formats defined in the Display screen of the map wizard are applied to the map markers and areas.

![Preview the geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404848672023/cmpnt_map_geo_exmpl5.gif)

30. Select **Home** > **Save** to save the library component as **Sales Map by Country.lc**.
31. [Publish the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely) to the default location on Server together with the resources it uses.
32. Create a dashboard on Server.
33. In the Resources panel, browse to find the library component Sales Map by Country.lc in the **Component Library** node and drag it to the dashboard body. When you hover the mouse on a marker, JDashboard displays its tip information just as we defined in the map wizard.

    ![Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404848672279/cmpnt_map_geo_exmpl6.gif)
34. In this geographic map component, there are two group levels, first by Country and then by State, so for the higher group level, you can perform the go-down action, and for the lower group level the go-up action. Hover your mouse over the marker **Country: Germany**, select it, or right-click it and select **Go Down** from the shortcut menu. The geographic map jumps one group level down to show the information of states in Germany, and you can find the filter condition "Country: Germany" displayed at the bottom of the geographic map.

    ![Click Geographic Map in Dashboard with Information of a State](https://devnet.logianalytics.com/hc/article_attachments/4404857042199/cmpnt_map_geo_exmpl7.gif)
35. You can scroll the mouse over the geographic map to make it zoom out or zoom in. By scrolling the mouse down, you can get a wider area on the map.

    ![Zoom Out the Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404857042967/cmpnt_map_geo_exmpl8.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057362-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps)
