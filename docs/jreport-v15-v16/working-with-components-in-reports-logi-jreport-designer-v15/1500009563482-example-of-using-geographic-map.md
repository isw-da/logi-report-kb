---
title: "Example of Using Geographic Map"
id: 1500009563482
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563482-Example-of-Using-Geographic-Map
updated_at: 2021-07-24T05:56:00Z
---

# Example of Using Geographic Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583981-KPI-Components)

# Example of Using Geographic Map

This topic uses OpenStreetMap to demonstrate how to add a geographic map in a library component and use it in JDashboard.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Select **Home** > **New** > **Library Component**.
3. In the Select Component for Library Component dialog, select **Blank** and select **OK**.
4. Drag the **Geographic Map** button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/4404889376407/btn_instgmp.gif) from the Components panel to the library component. The Create Geographic Map wizard appears.
5. In the Data screen, select **WorldWideSalesBV** from Data Source 1. Then select **Next**.
6. In the Display screen, add the fields **Country** and **State** in the Customers table as the group by fields one by one to the Drill Path box.
7. Check the **Enable Area** checkbox. The Enable Marker checkbox is checked by default.

   Next, we will define the marker and area properties for the country group level.
8. Select **Country** in the Drill Path box, select **Country** from the Customers table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Shape By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif) beside the text box.
9. In the Edit Shapes dialog, select anywhere in the Data Items box and select **Ctrl** + **A** on the keyboard to select all countries, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889407383/btn_crcl.gif) in the preview box below the pattern name to apply the shape to all countries. Select **OK** to apply the shape.

   ![Edit Shapes dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889407639/cmpnt_map_ggl_exmpl0.gif)
10. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Color By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) beside the text box.
11. In the Edit Gradient Color dialog, keep the default gradient color, check the **Middle Value** checkbox and set its value to **625816.73**, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    ![Edit Gradient Color dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893982871/cmpnt_map_ggl_exmpl1.gif)
12. Select the aggregation **Total Cost** from the Orders Detail table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Size By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893879191/btn_size.gif) beside the text box to specify the zoom percentage to **370%**. Select outside of the size box to apply the zoom percentage.
13. Select **Country** from the Customers table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Label By text box of the Marker Options.
14. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) beside the Marker Tip text field, then select **<New Formula...>** from its drop-down list to create a formula to control the marker tip information.
15. In the displayed dialog, enter the name **MarkerTipforCountry** and select **OK**.
16. In the Formula Editor, define the formula as follows.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
     "Total Cost:" + " " + ToText(@"Orders Detail.Total Cost","$#,###.00") + "\n" +  
     "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
17. Save the formula and close the Formula Editor. MarkerTipforCountry is then displayed in the Marker Tip text field.

    ![Create Geographic Map wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404889408151/cmpnt_map_ggl_exmpl2.gif)
18. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Fill By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) beside the text box.
19. In the Edit Gradient Color dialog, select **Green-White-Orange** from the gradient color drop-down list, which is the last color at the second line in the list, specify the opacity to **80%**, then select **OK** to apply the gradient color.

    Next, we will specify the marker and area properties for the state group level.
20. Select **State** in the Drill Path box, select **State** from the Customers table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Shape By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893878935/btn_shp.gif) beside the text box.
21. In the Edit Shapes dialog, select **Pattern1** from the pattern drop-down list to apply the shapes in the pattern to all states, then select **OK**.
22. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893879191/btn_size.gif) beside the Size By text box to specify the zoom percentage to **230%**. Select outside of the size box to apply the zoom percentage.
23. Select the aggregation **Total Sales** from the Orders Detail table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Fill By text box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889337239/btn_colr.gif) beside the text box.
24. In the Edit Gradient Color dialog, select **Green** as the gradient color, which is the second color in the color list, specify the opacity to **80%**, then select **OK** to apply the gradient color.
25. Select **State** from the Customers table in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Label By text box of the Area Options. Repeat this to add Total Sales from the Orders Detail table to the Label By text box.
26. Repeat [steps 14 to 17](#Steps) to create another formula AreaTipforState to control the area tip information.

    `"Country:" + " " + @"Customers.Country" + "\n" +  
    "State:" + " " + @"Customers.State" + "\n" +  
    "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
27. Repeat [steps 14 to 17](#Steps) to create another formula LocationInfoforState for the Location Info option.

    `@"Customers.State" + "," + @"Customers.Country"`

    ![Create Geographic Map wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404889408407/cmpnt_map_ggl_exmpl3.gif)
28. Select **Next** to enter the Filter screen. Select the **Add Condition** button to add a condition line, and specify the filter condition as **@Country != USA**, then select **Finish** to create the map.

    ![Create Geographic Map wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893983127/cmpnt_map_ggl_exmpl4.gif)
29. Select **GeoMarker1** and **GeoArea1** in the Report Inspector by pressing the Ctrl key on the keyboard and set their Invisible property to **true**. This is to hide information about the state group level from displaying at the initial map to improve the map appearance. You can still get the state information by applying the go-down action on the countries.
30. Select **Hone**/**File** > **Save** to save the library component as **Sales Map by Country.lc**.
31. [Publish the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely)to the default location on Logi JReport Server together with the resources used by it.
32. Create a dashboard on Logi JReport Server.
33. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893983383/cmpnt_map_ggl_exmpl_cmpnt.gif) on the side bar to display the Resources panel.
34. Browse to find the library component Sales Map by Country.lc in the Component Library node and then drag it to the dashboard body. You can see the formats we defined in the Display screen of the Create Geographic Map wizard are applied to the markers and areas, and when you hover the mouse on a marker, its tip information will also be displayed just as we defined.

    ![Geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404893983639/cmpnt_map_ggl_exmpl5.gif)
35. In this geographic map component, there are two group levels, first by Country and then by State. For the higher group level, you can perform the go-down action, and for the lower group level, the go-up action. Hover your mouse over the marker **Country: Germany**, select it, or right-click it and select **Go Down** from the shortcut menu. The geographic map will jump one group level down to show the information of states in Germany.

    ![Geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404893983895/cmpnt_map_ggl_exmpl6.gif)
36. You can scroll the mouse over the geographic map to make it zoom out or zoom in. By scrolling the mouse down, a wider area will be shown on the map.

    ![Geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404893984151/cmpnt_map_ggl_exmpl7.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583981-KPI-Components)
