---
title: "Example: Using Geographic Maps"
id: 5735521085463
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521085463-Example-Using-Geographic-Maps
updated_at: 2022-11-02T04:13:11Z
---

# Example: Using Geographic Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564357015-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps)

# Example: Using Geographic Maps

This topic presents an example to demonstrate how you can add a geographic map in a library component and perform data analysis on it in a dashboard.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **Home** > **New** > **Library Component**.
3. In the Select Component for Library Component dialog box, select **Blank** and select **OK**.
4. From the **Components** panel, drag the **Geographic Map** icon ![Geographic Map icon](https://devnet.logianalytics.com/hc/article_attachments/9898532332951/icon_geomap.gif) in the **Visual** category to the library component. Designer displays the Create Geographic Map dialog box.
5. In the **Data** screen, select **WorldWideSalesBV** in Data Source 1, then select **Next**.
6. In the **Display** screen, add the group objects **Country** and then **State** as the group-by fields to the **Drill Path** box.
7. Select **Enable Area**. Designer selects **Enable Marker** by default.

Next, we define the marker and area properties for the Country group level.

1. Select **Country** in the Drill Path box.
2. Drag the group object **Country** from the **Resources** box to the **Shape By** text box, then select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/9898462357399/btn_shp.gif) beside the text box.
3. In the Edit Shapes dialog box, select anywhere in the **Data Items** box and select **Ctrl+A** on the keyboard to select all countries, then select the icon ![Solid Circle icon](https://devnet.logianalytics.com/hc/article_attachments/9898534576535/cmpnt_map_geo_crclicon.gif.gif) in the preview box below the pattern name to apply the shape to all countries. Select **OK** to apply the shape.

   ![Edit Shapes](https://devnet.logianalytics.com/hc/article_attachments/9898534580759/cmpnt_map_geo_exmpl0.gif)
4. Drag the aggregation object **Total Sales** from the Resources box to the **Color By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/9898479465111/btn_colr.gif) beside the text box.
5. In the Edit Gradient Color dialog box, keep the default gradient color, select **Middle Value** and set its value to **625816.73**, specify the opacity to **80%**, then select **OK** to apply the gradient color.

   ![Edit Gradient Color](https://devnet.logianalytics.com/hc/article_attachments/9898534601111/cmpnt_map_geo_exmpl1.gif)
6. Drag the aggregation object **Total Cost** from the Resources box to the **Size By** text box, then select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/9898479472407/btn_size.gif) beside the text box to specify the zoom percentage to **370%**. Select outside the size box to apply the zoom percentage.
7. Drag the group object **Country** from the Resources box to the **Label By** text box under Marker Options.
8. Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) beside the **Marker Tip** text box, then select **<New Formula...>** from its drop-down list to create a formula to control the marker tip information.
9. In the Enter Formula Name dialog box, type **MarkerTipforCountry** and select **OK**.
10. In the Formula Editor dialog box, define the formula as follows:

    `"Country:" + " " + @"Customers.Country" + "\n" +  
     "Total Cost:" + " " + ToText(@"Orders Detail.Total Cost","$#,###.00") + "\n" +  
     "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
11. Save the formula and close the Formula Editor dialog box. Designer adds MarkerTipforCountry in the Marker Tip text box automatically.

    ![Add a Marker Tip](https://devnet.logianalytics.com/hc/article_attachments/9898518316951/cmpnt_map_geo_exmpl2.gif)
12. Drag the aggregation object **Total Sales** from the Resources box to the **Fill By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/9898479465111/btn_colr.gif) beside the text box.
13. In the Edit Gradient Color dialog box, select **Green-White-Orange** from the gradient color drop-down list, which is the last color at the second line in the list, specify the opacity to **80%**, then select **OK** to apply the gradient color.

Now, we specify the marker and area properties for the State group level.

1. Select **State** in the Drill Path box.
2. Drag the group object **State** from the Resources box to the **Shape By** text box.
3. Select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/9898479472407/btn_size.gif) beside the **Size By** text box to specify the zoom percentage to **230%**. Select outside the size box to apply the zoom percentage.
4. Drag the aggregation object **Total Sales** from the Resources box to the **Fill By** text box, then select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/9898479465111/btn_colr.gif) beside the text box.
5. In the Edit Gradient Color dialog box, select **Green** as the gradient color, which is the second color in the color list, specify the opacity to **80%**, then select **OK** to apply the gradient color.
6. Drag the group object **State** from the Resources box to the **Label By** text box under Area Options. Repeat this to add **Total Sales** to the Label By text box.
7. Repeat [steps 15 to 18](#Steps) to create another formula **AreaTipforState** to control the area tip information.

   `"Country:" + " " + @"Customers.Country" + "\n" +  
   "State:" + " " + @"Customers.State" + "\n" +  
   "Total Sales:" + " " + ToText(@"Orders Detail.Total Sales","$#,###.00")`
8. Create the formula **LocationInfoforState** for the **Location Info** option.

   `@"Customers.State" + "," + @"Customers.Country"`

   ![Add Location Info](https://devnet.logianalytics.com/hc/article_attachments/9898518322071/cmpnt_map_geo_exmpl3.gif)
9. Select **Next**.
10. In the **Filter** screen, select **Add Condition** to add a condition line and specify the filter condition as **Country != USA**.

    ![Add a Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/9898518330775/cmpnt_map_geo_exmpl4.gif)
11. Select **Finish** to create the map.
12. Select the **View** tab to preview the geographic map. The map shows as a static map and Designer applies the settings we have defined in the Display screen of the map wizard to the map markers and areas.

![Preview the geographic map](https://devnet.logianalytics.com/hc/article_attachments/9898534620183/cmpnt_map_geo_exmpl5.gif)

13. Navigate to **Home** > **Save** to save the library component as **Sales Map by Country.lc**.
14. [Publish the library component](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources#Remotely) to the default location on Server together with the resources it uses.
15. Create a dashboard on Server.
16. In the **Resources** panel of JDashboard, locate the library component Sales Map by Country.lc in the **Component Library** node and drag it to the dashboard body.
17. Point to a marker, and JDashboard displays its tip information just as what we have defined in the map wizard.

    ![Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/9898518340247/cmpnt_map_geo_exmpl6.gif)
18. There are two group levels in this geographic map component, first by Country and then by State, so for the higher group level, we can perform the go-down action, and for the lower group level the go-up action. Point to the marker representing **Germany**, select it, or right-click it and select **Go Down** from the shortcut menu. The geographic map jumps one group level down to show the information of states in Germany, and JDashboard displays the filter condition "Country: Germany" at the bottom of the geographic map.

    ![Click Geographic Map in Dashboard with Information of a State](https://devnet.logianalytics.com/hc/article_attachments/9898518348183/cmpnt_map_geo_exmpl7.gif)
19. Scroll the mouse over the geographic map to zoom it out or in. By scrolling the mouse down, we can get a wider area on the map.

    ![Zoom Out the Geographic Map in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/9898518359191/cmpnt_map_geo_exmpl8.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564357015-Modifying-Geographic-Maps)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps)
