---
title: "General Operations in JDashboard"
id: 1500009644662
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard
updated_at: 2021-07-24T20:55:18Z
---

# General Operations in JDashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644702-Inserting-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669301-Manipulating-Data-Components)

# General Operations in JDashboard

This topic provides a general view of the operations you can perform in JDashboard.

Below is a list of the sections covered in this topic:

* [Operations on Dashboards](#Dashboard)
* [Operations on Objects in the Dashboard Header](#Header)
* [Operations on Components in the Dashboard Body](#Body)

## Operations on Dashboards

* **Creating a new blank dashboard in the current web browser**  
   The ways to create a dashboard differ depending on whether your Logi JReport Server is enabled with [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009667781-Visual-Analysis).
  + When Visual Analysis is disabled, choose a method from the following:
    - Select **+** beside the rightmost dashboard tab.
    - Select the **New** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif) on the toolbar.
    - Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **New** from the option list.
  + When Visual Analysis is enabled, choose a method from the following:
    - Select **+** beside the rightmost dashboard tab.
    - Put the mouse pointer on the **+** button beside the rightmost dashboard tab for one second until a drop-down menu displays, then select **Dashboard**  from the menu.
    - On the toolbar, select the **New** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif) and then select **New Dashboard**.
    - On the toolbar, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) and then select **New** > **Dashboard**.

  A blank dashboard tab will be added in the browser. You can then [add components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644702-Inserting-Components) to customize the dashboard.
* **Opening another dashboard in the current web browser**  
   Select the **Open** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357783/btn_open.gif)on the toolbar, or select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) and then select **Open** from the option list. In the appearing dialog, browse to the desired folder, select the dashboard you want to open and then select **OK**, or simply double-click the dashboard to open it.
* **Showing, hiding and resizing the dashboard header**  
   To show or hide the dashboard header, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Show**/**Hide Dashboard Header** from the option list.

  Even though the dashboard header is open, its border is unseen by default. However, when you drag objects into the dashboard editing area, you will see the area is divided into two sections with the activated section highlighted in gray: the upper section is the header and the lower the body. Or you can simply press **Ctrl** on the keyboard to make the border between the header and body shown. Then drag the border line vertically to adjust the size of the header and body.
* **Removing all filters from a dashboard**  
   JDashboard provides the ability to remove all the filters from the current dashboard at one time including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi JReport Designer. To do this, select the **Clear Filters** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920647319/btn_dshbrd_clrfltr.gif) on the toolbar, or select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) and then select **Clear Filters** from the option list.
* **Refreshing the current dashboard**  
   Select the **Refresh** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358935/btn_refresh.gif) on the toolbar to refresh the data of the current dashboard.
* **Applying a theme to the current dashboard**  
   Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Themes** from the option list. In the [Themes](https://devnet.logianalytics.com/hc/en-us/articles/1500009646302-Themes) dialog, select a theme from the left panel and then select **OK**.
* **Customizing the way of showing the component title bar**  
   You can customize the way of showing the component title bar and icons on it for each component in the current dashboard.

1. Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Component Title Bar** from the option list.
2. In the [Customize Component Title Bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009645942-Customize-Component-Title-Bar) dialog, select a component from the component box on the left.
3. Specify the way of showing its component title bar and the icons on it: Always Show, Show When Mouse Over or Never Show. Icons on the component title bar allow you to edit a component so it is recommended not to select the Never Show option.
4. Repeat the above steps to customize the component bar for other components in the dashboard.
5. If you want to apply the profile settings for the component title bar, check **Use Profile**, then the settings defined for the component title bar in the [JDashboard profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009669321-Customizing-JDashboard-Profile#Title) will be used for all components in the dashboard.
6. Select **OK** to apply the changes.

* **Exiting JDashboard**  
   If you want to exit JDashboard and release the resources, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Exit** from the option list. Do not use the close button on the browser window as that may not release the resources used by JDashboard.
* **Asking for help**  
  At any time, you can select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Help** from the option list to access the JDashboard help documents. Furthermore, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif) in any dialog to show the help document about the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Operations on Objects in the Dashboard Header

* **Moving an object**  
   Place the mouse pointer on the object then select the mouse button and it becomes a four-arrow icon, then drag to the desired position.
* **Resizing an object**   
   Place the mouse pointer on the object until an orange rectangle appears, next move the pointer on the right border, bottom border, or the bottom right corner until the pointer becomes a two-arrow icon, then drag to the desired position.

The following operations require using the object's title bar icons, which could always display on the object or display when mouse over, depending on your [customization](#TitleBar).

* **Editing an object**  
   Hover the mouse pointer on the object and then select the **Edit** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920594967/btn_dshbrd_edt.gif) that appears around the object.
  + For a label or the dashboard title, you can edit the text related properties like font face, font color, and so on in the [Edit Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009645962-Edit-Label) dialog.
  + For a special field, you can change it to another special field and edit the text related properties in the [Edit Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009645982-Edit-Special-Field) dialog.
  + For an image, you can select another image to replace the current one in the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009670281-Edit-Image) dialog.
* **Deleting an object**   
   Hover the mouse pointer on the object and then select the **Delete** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif) that appears around the object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Operations on Components in the Dashboard Body

* **Resizing a component**  
   Place the mouse pointer on the component's right border, bottom border, or the bottom right corner until the pointer becomes a two-arrow icon, then drag to the desired position.
* **Navigating component data via scrollbar**  
   For tables, crosstabs and charts, you can use the scrollbar to navigate their data if the container cannot display all data of the component.
* **Turning component pages**  
   If a table or a crosstab contains more than one page, a page navigation bar specific for the component will be available right below the component. You can use the navigation bar to view the desired pages:
  + Select a number to go to that page.
  + Input a number in the text field.
  + Select **Prev** to go to the previous page.
  + Select **Next** to go to the next page.
* **Going to links**  
   Once an object in a library component has been linked to a report, a web page, or an e-mail address, you can right-click the trigger object and select **Show Linked Target** from the shortcut menu to launch the linked target. If the select priority of the link action is specified to be the highest for the library component at design time, you can also directly select the trigger object to open the link.
* **Automatically Arranging Components in the Current Dashboard**  
  Sometimes you may drag many library components to random positions in a dashboard and would like them to look neat, there is a simple way to do this: on the toolbar, select the **Arrange** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926780183/btn_dshbrd_autoarng.gif), or select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) and then select **Arrange** from the option list, the dashboard layout will then be adjusted immediately. Arrange is an instant action, selecting it once will arrange the layout once, and in this sense it benefits when you seldom need to reorder the layout.

  In the case when frequent reorder of dashboard layout is required, select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Auto Arrange**  on the option list. Then later each time a library component is resized, moved, removed, or added, the dashboard body will be rearranged automatically so that the library components will be placed neatly. When Auto Arrange is checked, it functions similarly as [responsive view](#Responsive).
* **Automatically Scaling Dashboard Components According to Browser Window**

  JDashboard is able to responsive to any size of browsers on any mobile devices or computers. Dashboard contents excluding the dashboard header can automatically scale and fold according to the current browser window size, as long as the window is smaller than the designed dashboard size. Information presented will always be legible and the layout will perfectly adapt to best utilize the available display screen. This is called responsive view. It is always available to mobile devices. When JDashboard runs on computers, you can enable/disable it by customizing the JDashboard properties via [profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009669321-Customizing-JDashboard-Profile#Edit), and specify whether it is applied by default in the JDashboard view mode by setting the profile option View Dashboards in Responsive Mode.

  When running JDashboard on computers, if Responsive View is enabled, you can open or close it as follows:

  + Select the **Open Responsive Mode** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360215/btn_rspnsvopn.gif) or **Close Responsive Mode** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360599/btn_rspnsvcls.gif) on the toolbar.
  + Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select/deselect **Responsive View**.

The following operations require using the component title bar or icons on the bar, which could always display on the component or display when mouse over, depending on your [customization](#TitleBar).

* **Moving a component**  
   Place the mouse pointer on the component title bar, select the mouse button and it becomes a four-arrow icon, then drag to the desired position.
* **Editing a component**  
   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **Edit Setting** from the drop-down menu.
  + For a filter control, edit its settings in the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009670241-Edit-Filter-Control) dialog.
  + For a web page frames, edit the URL of the web page and other settings in the [Edit URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009646002-Edit-URL-Frame) dialog.
  + For an HTML component, edit its title and contents in the [Edit HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009670261-Edit-HTML) dialog.
* **Exporting a component**  
   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **Export** from the drop-down menu. In the Export dialog, choose the format to which you want to export the library component, then select **OK**.
* **Maximizing a component**  
   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920648087/btn_dshbrd_max.gif) on the component title bar and the component will take up the whole dashboard body. By selecting the button again the component will be restored to the original size.
* **Editing the title of a component**  
   Double-select on the component title bar and it will become editable. Input the new title and select **Enter** on the keyboard to confirm the change.
* **Customizing the auto refresh action**  
   For a library component that uses only one business view as the data source, if its Auto Refresh feature is enabled, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **Refresh** from the drop-down menu to adjust the refresh interval or pause the auto refresh action with the [Refresh Interval](https://devnet.logianalytics.com/hc/en-us/articles/1500009670461-Refresh-Interval) dialog.
  + To change the refresh interval, select the drop-down list to select the new interval. Currently there are only 3 values available, which are ordinal multiples (starting from 2) of the default interval value defined in Logi JReport Designer.
  + To make the auto refresh action paused, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920584215/btn_dshbrd_pause.gif).
  + To resume the auto refresh action after it is stopped, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926750871/btn_dshbrd_play.gif).

**Making use of the configuration panel**  
 Each library component can be equipped with a configuration panel. The configuration panel can be used to [specify parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values#LC) to its library component, to filter or sort the data of its library component, or to change properties of objects in its library component. For how a configuration panel is configured, see "Using the Configuration Panel" in the *Logi JReport Designer User's Guide*.

Once a configuration panel has been defined for a library component, you can open it in JDashboard and then perform actions as defined. To do this, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **Edit Setting** from the drop-down menu to display the configuration panel. After specifying values in the panel, select OK to apply the values in the library component. The Cancel button is used to close the configuration panel.

* **Showing component information**  
   Information about a component such as a library component's ID, the author and his/her e-mail address, and the description about the component are provided. To view the information, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **About** from the drop-down menu. A panel will be displayed showing the information. You can select the OK button in the panel to close the panel.
* **Deleting a component**  
   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the component title bar and select **Delete** from the drop-down menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644702-Inserting-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669301-Manipulating-Data-Components)
