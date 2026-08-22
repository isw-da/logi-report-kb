---
title: "Creating and Saving Dashboards"
id: 1500009712541
section: "JDashboard Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards
updated_at: 2021-11-03T06:58:23Z
---

# Creating and Saving Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712661-Running-Dashboards)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard)

# Creating and Saving Dashboards

The topic introduces how to create and save a dashboard.

Below is a list of the sections covered in this topic:

* [Creating a Dashboard](#Create)
* [Inserting Components in a Dashboard](#Insert)

+ [Inserting Library Component References](#LC)
+ [Inserting Report Data Components](#Report)
+ [Inserting Analysis Templates As Components](#VA)
+ [Inserting a Label/Dashboard Title](#Label)
+ [Inserting an Image](#Image)
+ [Inserting a Special Field](#SF)
+ [Inserting a Filter Control](#Filter)
+ [Inserting a Third-Party Gadget via URL](#URL)
+ [Inserting an HTML Component](#HTML)

* [Saving a Dashboard](#Save)

## Creating a Dashboard

1. Do either of the following:
   * In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Dashboard** in the Create category.
   * In the Logi JReport Server console, open the Resources page and select **New** > **Dashboard** on the task bar.

   A blank dashboard is created in JDashboard.

   ![Create Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4412139612823/dshbrd_crtdsh1.gif)
2. The upper section with the text "Dashboard Title" of the editing area is the dashboard header, where you can insert labels, images, and special fields. The dashboard body is the section below the header. In the body you can insert report components, library components, filtering tools, third-party objects, and HTML components.
3. When the mouse hovers on the header section, the header is outlined and you will see the border between the header and the body. You can resize the two sections by dragging the border line. The arrow button that appears at the bottom right of the header is used to hide the header.

   ![Create Dashboard - Header Section](https://devnet.logianalytics.com/hc/article_attachments/4412139613463/dshbrd_crtdsh2.gif)

After you have entered JDashboard, you may want to create more dashboards in the same web browser as explained  [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard#New).

## Inserting Components in a Dashboard

You can insert library components and report data components as well as labels, images, special fields, filtering tools, third-party objects, and HTML components into dashboards via the Resources panel. To access the panel, select the **Show Resources** button ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) on the toolbar.

### Inserting Library Component References

When inserting a library component from the component library into a dashboard, you are not copying it from the component library, but instead referencing it. In this sense, when a library component is edited in Logi JReport Designer and republished to the component library, the changes will be reflected in all the dashboards that reference the library component, and any changes made to a library component in a dashboard will be saved into the dashboard only without affecting the source library component. However, if the same change in a library component is made both at design time in Logi JReport Designer and at runtime in a dashboard, the runtime change has higher priority.

**To reference a library component into the dashboard body:**

1. In the Resources panel, expand the **Component Library** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Browse to find the library component you want to insert, then drag it to the destination in the dashboard body.

### Inserting Report Data Components

Data components such as tables, crosstabs, charts, KPIs and geographic maps in reports can be directly inserted into dashboards after being converted into library components automatically.

For reports (excluding [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports)) that use [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009719021-An-Introduction-to-Business-Views) as data sources, all data components can be converted to library components successfully.

However, page reports may use queries as data sources other than business views. For a data component that is created using a query, only when there is a business view in the catalog created based on only the query, can the component be converted to a library component and used in dashboards.

Currently library components do not support some features of page report components, after the latter are inserted into dashboards, those features will be removed. This may result in that the data components in dashboards look different from when they are in page reports. For features that are not supported in JDashboard, they will either be ignored, removed, or applied with the default values.

The following table lists how JDashboard deals with the unsupported page report features:

| In Page Report Components | In Library Components |
| --- | --- |
| Display types like Barcode, Checkbox, and so on | Ignored |
| Special fields | Removed |
| Dynamic resources | Changed to constant resources |
| Master/Detail reports | Ignored |
| Subreports | Removed |
| Nested data components that is one contains another | The ownership is removed and the involved data components are regarded as individual components. |
| Definition properties | Ignored |
| Formula-controlled properties | Default values are applied. |
| Other components | Removed |

**To insert a report data component into the dashboard body:**

1. In the Resources panel, expand the **Reports** node to locate the report that contains the desired data component (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Expand the report and drag the data component into the dashboard body.
3. If the data component uses parameters, the default values will be applied. You can change the parameter values via the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard#ConfigPanel) after the component is loaded.

The inserted report data component runs with the report's catalog so it will not be able to run if the catalog is removed or updated. The report data component is not controlled by the [runtime filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard).

### Inserting Analysis Templates As Components

Analysis templates after being saved into the server resource tree can be inserted into dashboards as components. This feature requires a license for [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009686042-Visual-Analysis).

**To insert an analysis template as component into the dashboard body:**

1. In the Resources panel, expand the **Reports** node to locate the target analysis template with .va as the suffix (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Expand the analysis template and you will find a VCTObject under it. Drag this VCTObject into the dashboard body.

The inserted analysis template will be wrapped into a runtime library component and its data presentation area and legend area without legend icons will be displayed, just for viewing. However if no field binds with any legend, the legend area will not be shown. The default title is the server resource name of the parent analysis template without the suffix .va.

The inserted analysis templates cannot be exported or printed, therefore when exporting or printing a dashboard, they will not be listed and the cells containing them will be left blank.

### Inserting a Label/Dashboard Title

Labels can be inserted in the dashboard header. A dashboard title is a special label.

1. In the Resources panel, expand the **Toolbox** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Drag **Label**/**Dashboard Title** to the destination in the dashboard header.
3. Double-click the label/title and edit the text.
4. If needed, hover the mouse pointer on the label and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412112613143/btn_dshbrd_edt.gif) that appears around it to edit its properties such as font, size, color and so on in the [Edit Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009688202-Edit-Label)  dialog.

### Inserting an Image

Images can be inserted in the dashboard header.

1. In the Resources panel, expand the **Toolbox** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Drag **Image** to the destination in the dashboard header. The [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009714181-Insert-Image) dialog appears.

   ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139571863/insrtimg.gif)
3. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**, then input the image URL or paste the URL in the File URL text box.
   * To use an image in the image library of JDashboard, select **Library**, then select the image in the My Pictures box.
4. Select **OK** to insert the image.

After an image is inserted in the dashboard header, if you want to change it, hover the mouse pointer on the image and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412112613143/btn_dshbrd_edt.gif) that appears around it, then in the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009688182-Edit-Image) dialog, select another image to replace the current one.

### Inserting a Special Field

Special fields can be inserted in the dashboard header.

1. In the Resources panel, expand the **Toolbox** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Drag **Special Field** to the destination in the dashboard header. The [Insert Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009688302-Insert-Special-Field) dialog appears.

   ![Insert Special Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131481751/insrtspclfld.gif)

   You can insert these types of special fields in the dashboard header:

   * **User Name**  
      The user name with which you log onto Logi JReport Server.
   * **Modified Date**  
      The date when the dashboard was last modified.
   * **Modified Time**  
      The time when the dashboard was last modified.
   * **Print Date**  
      The date to run the dashboard.
   * **Print Time**  
      The time to run the dashboard.
3. Choose the desired special field and select **OK** to insert it into the header.
4. If needed, hover the mouse pointer on the special field and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412112613143/btn_dshbrd_edt.gif) that appears around it to edit its properties such as font, size, color and so on in the [Edit Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009688222-Edit-Special-Field) dialog.

### Inserting a Filter Control

Filter controls can be inserted in the dashboard body. They are used to filter component data. For details, see [Filtering Component Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard).

### Inserting a Third-Party Gadget via URL

A web page can be inserted in the dashboard body. All you need to do is give its URL. Note that some web sites such as `http://www.google.com` do not allow Gadgets to load them.

1. In the Resources panel, expand the **Toolbox** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Drag **URL Frame** into the dashboard body. The [Insert URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009714201-Insert-URL-Frame) dialog appears.

   ![Insert URL Frame dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112611479/insrturl.gif)
3. In the Title text box, give a title for the frame that will display the contents of the web page.
4. In the URL text box, type in the URL of the web page. If needed, select the **Add Parameter** button to open the [Select Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009688362-Select-Parameter) dialog to insert a parameter to the URL to compose a dynamic URL (if no data source is specified, the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009688342-Select-Data-Source) dialog will be displayed for you to select the data source that contains the parameter you want first).

   You should provide a complete URL address. A URL without "http://", for example www.jinfonet.com, will not be automatically added "http://" since it is regarded a relative path, which may lead to that the URL cannot be opened in some browsers.
5. If you would like the specified web page to refresh periodically, select **Auto refresh**, then specify the time interval at which to refresh it.
6. Select **OK**. The specified web page will be inserted into the dashboard. You can then view the web page from JDashboard. If parameters are used in the URL, you can select ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) on the toolbar to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686902-Specifying-Parameter-Values-for-a-Dashboard) as you want, then you can get different web pages based on different parameter values.

To further edit the web page information, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard#TitleBar) and select **Edit Setting** from the drop-down menu. In the [Edit URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009714041-Edit-URL-Frame) dialog, edit the URL of the web page and other settings as required.

### Inserting an HTML Component

An HTML component allows for typing text, comments, and messages using a simple-featured text editor. It can be inserted in the dashboard body.

1. In the Resources panel, expand the **Toolbox** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) to display the Resources panel if it is closed).
2. Drag **HTML** to the destination in the dashboard body. The [Insert HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009714161-Insert-HTML) dialog appears.

   ![Insert HTML dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112611735/insrthtml.gif)
3. Specify a title for the HTML component.
4. In the text box:
   * Type text directly and format the text such as font face, size, style, color and alignment using the corresponding buttons.
   * If you want to use an image in the HTML component, select ![Insert Image button](https://devnet.logianalytics.com/hc/article_attachments/4412131482007/btn_dshbrd_img.gif) and select the required one via the [Insert Image dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009714181-Insert-Image).
   * You can also select some text or an image and select ![Hyperlink button](https://devnet.logianalytics.com/hc/article_attachments/4412139572631/btn_dshbrd_lnk.gif) to create hyperlink on the text or image in the [Hyperlink dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009688282-Hyperlink).
5. Select **OK** to insert the HTML component.

To further edit the HTML component, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on its [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard#TitleBar) and select **Edit Setting** from the drop-down menu. In the [Edit HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009688162-Edit-HTML) dialog, edit its title and contents as required.

## Saving a Dashboard

To save the changes you made to the current dashboard tab, select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4412112482455/btn_save.gif) on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and select **Save** from the option list. You can only save a single tab as a dashboard, you cannot save the entire JDashboard containing multiple tabs. Each tab must be saved separately as a different dashboard.

If the dashboard is newly created and has not yet been saved, the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009714381-Save-As#Save) dialog appears.

![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112608919/svas_dshlc.gif)

1. In the Save In section, browse to the folder in the server resource tree where you want to save the dashboard. You can use the button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4412112541463/btn_dshbrd_up.gif) to return to the parent folder.

   The resource table shows the resources in the current directory. Select the column names to change the order of the report in the table list if required.
2. In the File Name box, enter the name of the dashboard or use the default name.
3. If you want to save the report together with the sort and filter criteria, check **Save Sort Criteria** and **Save Filter Criteria** correspondingly. With the criteria saved, JDashboard will automatically apply them to the dashboard the next time it is opened.
4. Select **OK** to save the dashboard.

To save a copy of a dashboard, select ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) on the toolbar, select **Save As** from the option list to show the Save As dialog, and then do as above. If you are saving to an existing file, a Confirm dialog will be displayed asking whether you want to replace the file or [save a new version into the file](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions#Save).

After saving your dashboard into the server resource tree, you can browse to its directory in the server resource tree in the server console and [run it directly](https://devnet.logianalytics.com/hc/en-us/articles/1500009712661-Running-Dashboards).

**Note:** You will not be able to save the dashboard to locations where you do not have the Write permission.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712661-Running-Dashboards)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard)
