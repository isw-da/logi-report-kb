---
title: "Example: Using Geographic Map"
id: 1500009606322
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606322-Example-Using-Geographic-Map
updated_at: 2021-07-24T16:05:15Z
---

# Example: Using Geographic Map

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606342-Modifying-Geographic-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629181-Shape-Maps)

# Example: Using Geographic Map

This topic demonstrates how to add a geographic map in a library component and use it in JDashboard.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **Home** > **New** > **Library Component**.
3. In the Select Component for Library Component dialog, select **Blank** and select **OK**.
4. Drag the **Geographic Map** button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404904369559/btn_instgmp.gif) from the Components panel to the library component. The Create Geographic Map wizard appears.
5. In the Data screen, select **WorldWideSalesBV** from Data Source 1. Then select **Next**.
6. In the Display screen, add the fields **Country** and **State** in the Customers table as the group-by fields one by one to the Drill Path box.
7. Select the **Enable Area** checkbox. The Enable Marker checkbox is selected by default.

   Next, we will define the marker and area properties for the country group level.
8. Select **Country** in the Drill Path box, select **Country** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Shape By text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404904275735/btn_shp.gif) beside the text box.
9. In the Edit Shapes dialog, select anywhere in the Data Items box and select **Ctrl** + **A** on the keyboard to select all countries, then select ![Solid Circle button](https://devnet.logianalytics.com/hc/article_attachments/4404904433047/btn_crcl.gif) in the preview box below the pattern name to apply the shape to all countries. Select **OK** to apply the shape.

   ![Edit Shapes](https://devnet.logianalytics.com/hc/article_attachments/4404904433303/cmpnt_map_geo_exmpl0.gif)
10. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Color By text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif) beside the text box.
11. In the Edit Gradient Color dialog, keep the default gradient color, select the **Middle Value** checkbox and set its value to 625816.73, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    ![Edit Gradient Color](https://devnet.logianalytics.com/hc/article_attachments/4404904433559/cmpnt_map_geo_exmpl1.gif)
12. Select the aggregation **Total Cost** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Size By text box, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404904276375/btn_size.gif) beside the text box to specify the zoom percentage to **370%**. Select outside of the size box to apply the zoom percentage.
13. Select **Country** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Label By text box of the Marker Options.
14. Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) beside the Marker Tip text box, then select **<New Formula...>** from its drop-down list to create a formula to control the marker tip information.
15. In the displayed dialog, type the name **MarkerTipforCountry** and select **OK**.
16. In the Formula Editor, define the formula as follows.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
     "Total Cost:" + " " + ToText(@"Orders Detail.Total Cost","$#,###.00") + "\n" +  
     "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
17. Save the formula and close the Formula Editor. MarkerTipforCountry is then displayed in the Marker Tip text box.

    ![Add a Marker Tip](https://devnet.logianalytics.com/hc/article_attachments/4404916831383/cmpnt_map_geo_exmpl2.gif)
18. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Fill By text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif) beside the text box.
19. In the Edit Gradient Color dialog, select **Green-White-Orange** from the gradient color drop-down list, which is the last color at the second line in the list, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    Next, we will specify the marker and area properties for the state group level.
20. Select **State** in the Drill Path box, select **State** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Shape By text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404904275735/btn_shp.gif) beside the text box.
21. In the Edit Shapes dialog, select **Pattern1** from the pattern drop-down list to apply the shapes in the pattern to all states, then select **OK**.
22. Select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404904276375/btn_size.gif) beside the Size By text box to specify the zoom percentage to **230%**. Select outside of the size box to apply the zoom percentage.
23. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Fill By text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif) beside the text box.
24. In the Edit Gradient Color dialog, select **Green** as the gradient color, which is the second color in the color list, specify the opacity to **80%**, then select **OK** to apply the gradient color.
25. Select **State** from the Customers table in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the Label By text box of the Area Options. Repeat this to add Total Sales from the Orders Detail table to the Label By text box.
26. Repeat [steps 14 to 17](#Steps) to create another formula AreaTipforState to control the area tip information.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
    "State:" + " " + @"Customers.State" + "\n" +  
    "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
27. Repeat [steps 14 to 17](#Steps) to create another formula LocationInfoforState for the Location Info option.

    `@"Customers.State" + "," + @"Customers.Country"`

    ![Add Location Info](https://devnet.logianalytics.com/hc/article_attachments/4404904433815/cmpnt_map_geo_exmpl3.gif)
28. Select **Next** to go to the Filter screen. Select the **Add Condition** button to add a condition line, and specify the filter condition as **@Country != USA**, then select **Finish** to create the map.

    ![Add a Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404916831639/cmpnt_map_geo_exmpl4.gif)
29. Select the **View** tab to preview the geographic map. The map shows as a static map and you can see the formats defined in the Display screen of the map wizard are applied to the map markers and areas.

![Preview the geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404904434327/cmpnt_map_geo_exmpl5.gif)

30. Select **Home**/**File** > **Save** to save the library component as **Sales Map by Country.lc**.
31. [Publish the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#Remotely) to the default location on Logi Report Server together with the resources used by it.
32. Create a dashboard on Logi Report Server.
33. In the Resources panel, browse to find the library component Sales Map by Country.lc in the Component Library node and drag it to the dashboard body. When you hover the mouse on a marker, its tip information will be displayed just as we defined in the map wizard.

    **![Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404904434583/cmpnt_map_geo_exmpl6.gif)**
34. In this geographic map component, there are two group levels, first by Country and then by State, so for the higher group level, you can perform the go-down action, and for the lower group level the go-up action. Hover your mouse over the marker **Country: Germany**, select it, or right-click it and select **Go Down** from the shortcut menu. The geographic map will jump one group level down to show the information of states in Germany, and you can find the filter condition "Country: Germany" displayed at the bottom of the geographic map.

    ![Click Geographic Map in Dashboard with Information of a State](https://devnet.logianalytics.com/hc/article_attachments/4404904434839/cmpnt_map_geo_exmpl7.gif)
35. You can scroll the mouse over the geographic map to make it zoom out or zoom in. By scrolling the mouse down, a wider area can be shown on the map.

    ![Zoom Out the Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404916831895/cmpnt_map_geo_exmpl8.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606342-Modifying-Geographic-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629181-Shape-Maps)
