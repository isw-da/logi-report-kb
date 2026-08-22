---
title: "General Operations in JDashboard"
id: 1500009712601
section: "JDashboard Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard
updated_at: 2021-11-03T06:58:23Z
---

# General Operations in JDashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712621-Manipulating-Data-Components)

# General Operations in JDashboard

This topic provides a general view of the operations you can perform in JDashboard.

Below is a list of the sections covered in this topic:

* [Operations on JDashboard](#JDashboard)
* [Operations on Dashboards](#Dashboard)
* [Operations on Objects in the Dashboard Header](#Header)
* [Operations on Components in the Dashboard Body](#Body)

## Operations on JDashboard

* **Applying a theme to JDashboard**  
   Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Themes** from the option list. In the [Themes](https://devnet.logianalytics.com/hc/en-us/articles/1500009714401-Themes) dialog, select a theme from the left panel and then select **OK**.
* **Exiting JDashboard**  
   If you want to exit JDashboard and release the resources, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Exit** from the option list. Do not use the close button on the browser window as that may not release the resources used by JDashboard.
* **Asking for help**  
   At any time, you can select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Help** from the option list to access the JDashboard help documents. Furthermore, you can select ![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif) in any dialog to show the help document about the dialog.

## Operations on Dashboards

* **Creating a new blank dashboard in the current web browser**  
   The ways to create a dashboard differ depending on whether your Logi JReport Server is enabled with [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009686042-Visual-Analysis).
  + When Visual Analysis is disabled, choose a method from the following:
    - Select **+** beside the rightmost dashboard tab.
    - Select the **New** button ![New button](https://devnet.logianalytics.com/hc/article_attachments/4412139483159/btn_newobj.gif) on the toolbar.
    - Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **New** from the option list.
  + When Visual Analysis is enabled, choose a method from the following:
    - Select **+** beside the rightmost dashboard tab.
    - Put the mouse pointer on the **+** button beside the rightmost dashboard tab for one second until a drop-down menu displays, then select **Dashboard**  from the menu.
    - On the toolbar, select the **New** button ![New button](https://devnet.logianalytics.com/hc/article_attachments/4412139483159/btn_newobj.gif) and then select **New Dashboard**.
    - On the toolbar, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and then select **New** > **Dashboard**.

  A blank dashboard tab will be added in the browser. You can then [add components](https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards#Insert) to customize the dashboard.
* **Opening another dashboard in the current web browser**  
   Select the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4412139483415/btn_open.gif)on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and then select **Open** from the option list. In the appearing dialog, browse to the desired folder, select the dashboard you want to open and then select **OK**, or simply double-click the dashboard to open it.
* **Showing, hiding and resizing the dashboard header**  
   To show or hide the dashboard header, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Show**/**Hide Dashboard Header** from the option list.

  Even though the dashboard header is open, its border is unseen by default. However, when you drag objects into the dashboard editing area, you will see the area is divided into two sections with the activated section highlighted in gray: the upper section is the header and the lower the body. Or you can simply press **Ctrl** on the keyboard to make the border between the header and body shown. Then drag the border line vertically to adjust the size of the header and body.
* **Removing all filters from a dashboard**  
   JDashboard provides the ability to remove all the filters from the current dashboard at one time including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi JReport Designer. To do this, select the **Clear Filters** button ![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/4412112631191/btn_dshbrd_clrfltr.gif) on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and then select **Clear Filters** from the option list.
* **Refreshing the current dashboard**  
   Select the **Refresh** button ![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4412139483927/btn_refresh.gif) on the toolbar to refresh the data of the current dashboard.
* **Customizing the way of showing the component title bar**  
   You can customize the way of showing the component title bar and icons on it for each component in the current dashboard.

1. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Component Title Bar** from the option list. The [Customize Component Title Bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009714021-Customize-Component-Title-Bar) dialog appears.

   ![Customize Component Title Bar dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131485975/cstmzttlbar.gif)
2. Select a library component from the component box on the left.
3. Specify the way of showing its component title bar and the icons on it: Always Show, Show When Mouse Over or Never Show. Icons on the component title bar allow you to edit a component so it is recommended not to select the Never Show option.
4. Repeat the above steps to customize the component bar for other library components in the dashboard.
5. If you want to apply the profile settings for the component title bar, check **Use Profile**, then the settings defined for the component title bar in the [JDashboard profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009712641-Customizing-JDashboard-Profile#Title) will be used for all library components in the dashboard.
6. Select **OK** to apply the changes.

* **Viewing in-memory cube status**  
   If the [Show Status When Using Cube Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#CubeStatus) option is enabled in the server profile, you will find the Cube Status button ![Cube Status button](https://devnet.logianalytics.com/hc/article_attachments/4412139509399/btn_cbstts.gif) on the toolbar, by selecting which you can view the information about whether the data components in the current dashboard apply [in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009691322-Managing-In-memory-Cubes) and the reasons if not in the [Cube Status](https://devnet.logianalytics.com/hc/en-us/articles/1500009714001-Cube-Status) dialog.
* **Setting a dashboard as the server home page**  
  Setting a dashboard as the Logi JReport Server console home page allows for a faster and easier access to the frequently visited dashboard with its latest data. When you log onto the Logi JReport Server console, you will be directed to the Home tab right away which displays the dashboard. Later you can select the Home tab on the system toolbar of the Logi JReport Server console to switch to the dashboard directly. The Home tab is available after you have set a dashboard as the server home page.

  Before you can set a dashboard as the server home page, you need to first enable the feature in the server profile by checking the **Use a Dashboard** checkbox for the option [Home Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#HomePage). Then:

  1. Open the dashboard that you are going to view a lot and make sure it has been saved.
  2. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and you can see Set as Server Home is enabled in the option list. Select the option to set the dashboard as the home page.

## Operations on Objects in the Dashboard Header

* **Moving an object**  
   Place the mouse pointer on the object then select the mouse button and it becomes a four-arrow icon, then drag to the desired position.
* **Resizing an object**   
   Place the mouse pointer on the object until an orange rectangle appears, next move the pointer on the right border, bottom border, or the bottom right corner until the pointer becomes a two-arrow icon, then drag to the desired position.

* **Editing an object**  
   Hover the mouse pointer on the object and then select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412112613143/btn_dshbrd_edt.gif) that appears around the object.
  + For a label or the dashboard title, you can edit the text related properties like font face, font color, and so on in the [Edit Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009688202-Edit-Label) dialog.
  + For a special field, you can change it to another special field and edit the text related properties in the [Edit Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009688222-Edit-Special-Field) dialog.
  + For an image, you can select another image to replace the current one in the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009688182-Edit-Image) dialog.
* **Deleting an object**   
   Hover the mouse pointer on the object and then select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif) that appears around the object.

## Operations on Components in the Dashboard Body

* **Resizing a component**  
   Place the mouse pointer on the component's right border, bottom border, or the bottom right corner until the pointer becomes a two-arrow icon, then drag to the desired position.
* **Navigating component data via scrollbar**  
   For tables, crosstabs and charts, you can use the scrollbar to navigate their data if the container cannot display all data of the component.
* **Turning component pages**  
   If a table or a crosstab contains more than one page, a page navigation bar specific for the component will be available right below the component. You can use the navigation bar to view the desired pages:
  + Select a number to go to that page.
  + Input a number in the text box.
  + Select **Prev** to go to the previous page.
  + Select **Next** to go to the next page.
* **Going to links**  
   When an object in a library component is linked to a report, a web page, or an e-mail address, you can right-click the trigger object and select **Show Linked Target** from the shortcut menu to launch the linked target. If the select priority of the link action is specified to be the highest for the library component at design time, you can also directly select the trigger object to open the link.
* **Automatically arranging components in the current dashboard**  
  Sometimes you may drag many library components to random positions in a dashboard and would like them to look neat, there is a simple way to do this: on the toolbar, select the **Arrange** button ![Arrange button](https://devnet.logianalytics.com/hc/article_attachments/4412131508247/btn_dshbrd_autoarng.gif), or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and then select **Arrange** from the option list, the dashboard layout will then be adjusted immediately. Arrange is an instant action, selecting it once will arrange the layout once, and in this sense it benefits when you seldom need to reorder the layout.

  In the case when frequent reorder of dashboard layout is required, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select **Auto Arrange**  on the option list. Then later each time a library component is resized, moved, removed, or added, the dashboard body will be rearranged automatically so that the library components will be placed neatly. When Auto Arrange is checked, it functions similarly as [responsive view](#Responsive).
* **Automatically scaling dashboard components according to browser window**

  When JDashboard is in [view mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009686862-JDashboard#Mode), it can be responsive to any size of browsers on any mobile devices or computers. Dashboard contents excluding the dashboard header can automatically scale and fold according to the current browser window size, as long as the window is smaller than the designed dashboard size. Information presented is always legible and the layout perfectly adapts to best utilize the available display screen. This is called responsive view. It is always available to mobile devices. When JDashboard runs on computers, you can specify whether it is applied by default in the JDashboard view mode and how components are folded via the [View Dashboards in Responsive Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009712641-Customizing-JDashboard-Profile#Responsive) option in the JDashboard profile.

  When running JDashboard on computers in the view mode, if Responsive View is enabled, you can open or close it as follows:

  + Select the **Open Responsive Mode** button ![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4412112483735/btn_rspnsvopn.gif) or the **Close Responsive Mode** button ![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4412139485079/btn_rspnsvcls.gif) on the toolbar.
  + Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar and select/deselect **Responsive View**.

The following operations require using the component title bar or icons on the bar, which could always display on the component or display when mouse over, depending on your [customization](#TitleBar).

* **Moving a component**  
   Place the mouse pointer on the component title bar, select the mouse button and it becomes a four-arrow icon, then drag to the desired position.
* **Maximizing a component**  
   Select ![Maximize icon](https://devnet.logianalytics.com/hc/article_attachments/4412139611671/btn_dshbrd_max.gif) on the component title bar and the component will take up the whole dashboard body. By selecting the button again the component will be restored to the original size.
* **Editing the title of a component**  
   Double-click on the component title bar and it will become editable. Input the new title and select **Enter** on the keyboard to confirm the change.
* **Showing component information**  
   Information about a component such as a library component's ID, the author and his/her e-mail address, and the description about the component are provided. To view the information, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the component title bar and select **About** from the drop-down menu. A panel will be displayed showing the information. You can select the OK button in the panel to close the panel.
* **Deleting a component**  
   Select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the component title bar and select **Delete** from the drop-down menu.
* **Making use of the configuration panel**  
   The configuration panel can be used to [specify parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686902-Specifying-Parameter-Values-for-a-Dashboard#LC) to its library component, and if defined to filter or sort the data of the library component or change properties of objects in the library component.

To open the configuration panel of a library component in JDashboard and perform actions, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the component title bar and select **Edit Setting** from the drop-down menu to display the configuration panel. After specifying values in the panel, select OK to apply the values to the library component. The Cancel button is used to close the configuration panel.

* **Automatically refreshing a library component**  
   JDashboard supports automatically refreshing the data components as well as objects that are not bound with data in a library component based on specified interval and conditions.

  **To automatically refreshing the data components in a library component:**

  1. Do either of the following:
     + Select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the component title bar and point to **Auto Refresh** on the drop-down menu. All the business views used by the data components in the library component are listed on the submenu. Select the name of a business view. In this way, all the data components using the specified business view will be automatically refreshed when the auto refresh action takes place.
     + Right-click a data component in the library component and select **Auto Refresh** from the shortcut menu. In this way, other data components in the library component which use the same business view as the specified data component will also be automatically refreshed when the auto refresh action takes place.

     The [Auto Refresh](https://devnet.logianalytics.com/hc/en-us/articles/1500009713981-Auto-Refresh#AutoRefreshBV) dialog appears.

     ![Auto Refresh dialog - business view](https://devnet.logianalytics.com/hc/article_attachments/4412139575447/autorefrsh_bv.gif)
  2. Select ![Play button](https://devnet.logianalytics.com/hc/article_attachments/4412131486615/btn_dshbrd_play.gif) to enable the auto refresh action, then specify the refresh interval by inputting the time interval in the combo box that follows or selecting the drop-down list to select a value.

     When the auto refresh action is started, to make it stopped, select ![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4412139575703/btn_dshbrd_pause.gif).
  3. If you only want to fetch incremental data for each auto refresh, check the **Incremental Fetch** checkbox, then select the **Incremental Condition** button to specify the condition in the [Incremental Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009714121-Incremental-Condition) dialog.

     The dialog has the basic and advanced modes for you to define the incremental condition using either [simple expressions](#Simple) or  [complex expressions.](#Complex)

     + **To define the incremental condition using simple expressions:**
       1. Make sure the dialog is in the basic mode.

          ![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139573143/incrmntlcndtn_basic.gif)
       2. Select the field on which the filter will be based from the field drop-down list.
       3. From the operator drop-down list, set the operator with which to compose the condition expression.
       4. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. You can also select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list to
       5. If you want to add another condition line, from the logic operator drop-down list,
          - To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
          - To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

          Repeat this to add more condition lines if required. To delete a condition line, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112514327/btn_pgrpt_no.gif) on its left.
     + **To define the incremental condition using complex expressions:**
       1. Switch the dialog to the advanced mode.

          ![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112612247/incrmntlcndtn_advanced.gif)
       2. Select the **Add Condition** button to add a condition line.
       3. From the field drop-down list, select the field on which the filter will be based.
       4. From the operator drop-down list, set the operator with which to compose the filter expression.
       5. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. You can also select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) and then
       6. To add another condition line, select the **Add Condition** button and define the expression as required. Then select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
       7. Repeat the above steps to add more condition lines if necessary.

          To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

          To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

          To delete a condition line or a group, select it and select the **Delete** button.
  4. To specify a unique key for the components, manually input the unique key or select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412112488471/btn_chsr1.gif) to open the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009688402-Unique-Key) dialog to specify one.

     ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131477271/unqkey.gif)

     Once a unique key is defined, each time when the data components automatically updates themselves, the data that has the same unique key value as the previously loaded data records will be filtered and only data with different unique key value will be added to the data components. For instance, if you add the fields Country and Product ID as the unique key, when a record with the product ID 1 in USA has already been loaded into the data components, no more records of this product ID in USA will be added to them because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the data components will be updated each time new records are added to the database with more recent times.
  5. In the Value Number text box, specify the number of values for incremental fetch.
  6. Select **OK** to save the changes.

**To automatically refreshing the objects in a library component that are not bound with data:**

1. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the component title bar, select **Auto Refresh** from the drop-down menu, and then choose **Others** from the submenu to open the [Auto Refresh](https://devnet.logianalytics.com/hc/en-us/articles/1500009713981-Auto-Refresh#AutoRefresh) dialog.

   ![Auto Refresh dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131486871/autorefrsh.gif)
2. Select ![Play button](https://devnet.logianalytics.com/hc/article_attachments/4412131486615/btn_dshbrd_play.gif) to enable the auto refresh action, then specify the refresh interval by inputting the time interval in the combo box that follows or selecting the drop-down list to select a value.

   When the auto refresh action is started, to make it stopped, select ![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4412139575703/btn_dshbrd_pause.gif).
3. Select **OK** to save the changes and close the dialog.

**Tip:** If the auto refresh action is configured on a library component at design time in Logi JReport Designer, when you open the Auto Refresh dialog for the library component in JDashboard, the settings specified at design time will be loaded into the dialog by default. You can edit the settings as you want and when you save the dashboard, the auto refresh configuration will be saved into the dashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712621-Manipulating-Data-Components)
