---
title: "Creating and Saving Dashboards"
id: 1500009771761
section: "Introduction to the Logi Report JDashboard Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771761-Creating-and-Saving-Dashboards
updated_at: 2021-07-24T00:49:25Z
---

# Creating and Saving Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard)

# Creating and Saving Dashboards

This topic describes how you can create and save dashboards and insert a variety of components in dashboards.

This topic contains the following sections:

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
   * In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser#Start) of the Server Console, select **Dashboard** in the **Create** category.
   * In the Server Console, open the **Resources** page and select **New** > **Dashboard** on the task bar.

   JDashboard creates a blank dashboard.

   ![Create Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404880562967/dshbrd_crtdsh1.gif)
2. The upper section with the text "Dashboard Title" of the editing area is the dashboard header, where you can insert labels, images, and special fields. The dashboard body is the section below the header. In the body you can insert report components, library components, filter controls, third-party objects, and HTML components.
3. When you hover the mouse on the header section, JDashboard outlines the header and you will see the border between the header and the body. You can resize the two sections by dragging the border line. You can hide the header using the arrow button that appears at the bottom right of the header.

   ![Create Dashboard - Header Section](https://devnet.logianalytics.com/hc/article_attachments/4404880563351/dshbrd_crtdsh2.gif)

After you enter JDashboard, you may want to create more dashboards in the same web browser. For more information, select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#New).

## Inserting Components in a Dashboard

You can insert library components and report data components as well as labels, images, special fields, filter controls, third-party objects, and HTML components into dashboards via the Resources panel. To access the panel, select the **Show Resources** button ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif) on the toolbar.

### Inserting Library Component References

When you insert a library component from the component library into a dashboard, you are not copying it from the component library, but instead referencing it. In this sense, after you edit a library component in Logi Report Designer and then republish it to the component library, you will see the changes in all the dashboards that reference the library component. If you make any changes to a library component in a dashboard. JDashboard saves the changes into the dashboard only without affecting the source library component. However, if the same change in a library component happens both at design time in Logi Report Designer and at runtime in a dashboard, the runtime change has higher priority.

**To reference a library component into the dashboard body:**

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. In the **Component Library** folder, browse to find the library component you want to insert, and then drag it to the destination in the dashboard body.

### Inserting Report Data Components

You can insert data components, such as tables, crosstabs, charts, KPIs, and geographic maps in reports, into dashboards directly. JDashboard will convert them into library components automatically when you insert them.

For reports (excluding [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports)) that use [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views) as data sources, JDashboard can convert all data components in them to library components successfully.

However, page reports may use queries as data sources other than business views. For a data component that is created using a query, only when there is a business view based on only the query in the catalog, can JDashboard convert the component to a library component and use it in dashboards.

Currently library components do not support some features of page report components. After you insert the latter into dashboards, JDashboard will remove those features. This may result in that the data components in dashboards look different from when they are in page reports. For features JDashboard does not support, JDashboard will ignore or remove them, or apply the default values to them.

The following table lists how JDashboard deals with the unsupported page report features:

| In Page Report Components | In Library Components |
| --- | --- |
| Display types like Barcode and Checkbox | Ignored |
| Special fields | Removed |
| Dynamic resources | Changed to constant resources |
| Master/Detail reports | Ignored |
| Subreports | Removed |
| Nested data components that is one contains another | The ownership is removed, and the involved data components are regarded as individual components. |
| Definition properties | Ignored |
| Formula-controlled properties | Default values are applied. |
| Other components | Removed |

**To insert a report data component into the dashboard body:**

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Expand the **Reports** node to locate the report that contains the desired data component.
3. Expand the report.
4. Drag the data component into the dashboard body.
5. If the data component uses parameters, JDashboard will apply the default values. You can change the parameter values via the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#ConfigPanel) after JDashboard loads the component.

After you insert it into a dashboard, the report data component runs with the report's catalog. It will not be able to run if the catalog is removed or updated. The [runtime filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard) will not affect the report data components in dashboards.

### Inserting Analysis Templates As Components

After you save analysis templates into the server resource tree, you can insert them into dashboards as components. To do this, you should have the license for [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009742882-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly).

**To insert an analysis template as component into the dashboard body:**

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Expand the **Reports** node to locate the target analysis template with .va as the suffix.
3. Expand the analysis template. You will find a VCTObject under it.
4. Drag this **VCTObject** into the dashboard body.

JDashboard will wrap the analysis template into a runtime library component, and display its data presentation area and legend area without legend icons, just for viewing. However, if no field binds with any legend, JDashboard will not display the legend area. The default title is the server resource name of the parent analysis template without the suffix .va.

You cannot export or print the inserted analysis templates. Therefore, when you export or print a dashboard, JDashboard will not display them and will leave the cells containing them blank.

### Inserting a Label/Dashboard Title

You can insert labels in the dashboard header. A dashboard title is a special label.

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Drag **Label** or **Dashboard Title** from the **Toolbox** to the destination in the dashboard header.
3. Double-click the label or title and edit the text.
4. You can hover the mouse pointer on the label and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404885533975/btn_dshbrd_edt.gif) that appears around it to edit its properties such as font, size, and color in the [Edit Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009745422-Edit-Label-Dialog-Box-Properties) dialog box.

### Inserting an Image

You can insert images in the dashboard header.

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Drag **Image** from the **Toolbox** to the destination in the dashboard header. JDashboard displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009773481-Insert-Image-Dialog-Box-Properties) dialog box.

   ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880444311/insrtimg.gif)
3. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**, and then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**, and then type the image URL or paste the URL in the **File URL** text box.
   * To use an image in the image library of JDashboard, select **Library**, and then select the image in the **My Pictures** box.
4. Select **OK** to insert the image.

After you insert an image in the dashboard header, if you want to change it, hover the mouse pointer on the image and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404885533975/btn_dshbrd_edt.gif) that appears around it, then in the [Edit Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009773301-Edit-Image-Dialog-Box-Properties) dialog box, select another image to replace the current one.

### Inserting a Special Field

You can insert special fields in the dashboard header.

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Drag **Special Field** from the **Toolbox** to the destination in the dashboard header. JDashboard displays the [Insert Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009773501-Insert-Special-Field-Dialog-Box-Properties) dialog box.

   ![Insert Special Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880442903/insrtspclfld.gif)

   You can insert these types of special fields in the dashboard header:

   * **User Name**  
      The user name with which you log onto Logi Report Server.
   * **Modified Date**  
      The date when the dashboard was last modified.
   * **Modified Time**  
      The time when the dashboard was last modified.
   * **Print Date**  
      The date to run the dashboard.
   * **Print Time**  
      The time to run the dashboard.
3. Choose the desired special field and select **OK** to insert it into the header.
4. You can hover the mouse pointer on the special field and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404885533975/btn_dshbrd_edt.gif) that appears around it to edit its properties such as font, size, and color in the [Edit Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009745462-Edit-Special-Field-Dialog-Box-Properties) dialog box.

### Inserting a Filter Control

You can insert filter controls in the dashboard body and use them to filter component data. For more information, see [Filtering Component Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard).

### Inserting a Third-Party Gadget via URL

You can insert a web page in the dashboard body. All you need to do is give its URL.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)Some web sites such as `http://www.google.com` do not allow Gadgets to load them.

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Drag **URL Frame** from the **Toolbox** into the dashboard body. JDashboard displays the [Insert URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009745522-Insert-URL-Frame-Dialog-Box-Properties) dialog box.

   ![Insert URL Frame dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880442647/insrturl.gif)
3. In the **Title** text box, give a title for the frame that will display the content of the web page.
4. In the **URL** text box, type the URL of the web page. You can select **Add Parameter** to open the [Select Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009745642-Select-Parameter-Dialog-Box-Properties) dialog box to insert a parameter to the URL to compose a dynamic URL (if no data source is specified, JDashboard will display the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009773621-Select-Data-Source-Dialog-Box-Properties) dialog box for you to select the data source that contains the parameter you want first).

   You should provide a complete URL address. Take a URL without "http://" as an example, for instance, www.jinfonet.com, JDashboard will not automatically add "http://" to the URL because it thinks that the URL is a relative path. This may lead to that you cannot open the URL in some browsers.
5. If you would like the specified web page to refresh periodically, select **Auto refresh**, and then specify the time interval at which to refresh it.
6. Select **OK**. JDashboard will insert the specified web page into the dashboard. You can then view the web page from JDashboard. If you have added parameters in the URL, you can select the **Enter Parameter Values** icon ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880189463/btn_dshbrd_prm.gif) on the toolbar to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009743882-Specifying-Parameter-Values-for-a-Dashboard). Then you can get different web pages based on different parameter values.

To further edit the web page information, select the **Edit** button ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#TitleBar) and then select **Edit Setting** from the drop-down menu. JDashboard displays the [Edit URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009773321-Edit-URL-Frame-Dialog-Box-Properties) dialog box. Edit the URL of the web page and other settings as you want.

### Inserting an HTML Component

An HTML component enables you to type text, comments, and messages using a simple-featured text editor. You can insert it in the dashboard body.

1. Select the **Show Resources** icon ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif). JDashboard displays the Resources panel.
2. Drag **HTML** from the **Toolbox** to the destination in the dashboard body. JDashboard displays the [Insert HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties) dialog box.

   ![Insert HTML dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885526935/insrthtml.gif)
3. Specify a title for the HTML component.
4. In the text box:
   * Type text directly and format the text such as font face, size, style, color, and alignment using the corresponding buttons.
   * If you want to use an image in the HTML component, select the **Insert Image** icon ![Insert Image button](https://devnet.logianalytics.com/hc/article_attachments/4404880443543/btn_dshbrd_img.gif). JDashboard displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009773481-Insert-Image-Dialog-Box-Properties) dialog box. Specify an image in the dialog box.
   * You can also select some text or an image and then select the **Hyperlink** icon ![Hyperlink button](https://devnet.logianalytics.com/hc/article_attachments/4404880447127/btn_dshbrd_lnk.gif) to create hyperlink on the text or image in the [Hyperlink dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009773421-Hyperlink-Dialog-Box-Properties).
5. Select **OK** to insert the HTML component.

To further edit the HTML component, select the **Edit** button ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on its [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#TitleBar) and then select **Edit Setting** from the drop-down menu. JDashboard displays the [Edit HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties) dialog box. Edit its title and content in the dialog box.

## Saving a Dashboard

To save the changes you made to the current dashboard tab, select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif) on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) and then select **Save** from the option list. You can only save a single tab as a dashboard. When JDashboard contains multiple tabs, you should save each tab separately as a different dashboard.

If the dashboard is newly created and you have not saved it yet, JDashboard displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties#Save) dialog box.

![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880436503/svas_dshlc.gif)

1. In the **Save In** section, browse to the folder in the server resource tree where you want to save the dashboard. You can use the button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404885385367/btn_dshbrd_up.gif) to return to the parent folder.

   JDashboard displays the resources in the current directory. You can select the column names to change the order of the resources.
2. In the **File Name** box, type the name of the dashboard or keep the default name.
3. If you want to save the report together with the sort and filter criteria, select **Save Sort Criteria** and **Save Filter Criteria** correspondingly. With the criteria saved, JDashboard will automatically apply them to the dashboard the next time you open it.
4. Select **OK** to save the dashboard.

To save a copy of a dashboard,

1. Select the **Options** icon ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) on the toolbar. JDashboard displays a submenu.
2. Select **Save As**. JDashboard displays the Save As dialog box.
3. Do the same as above.

If you are saving to an existing file, JDashboard will display a Confirm dialog box asking whether you want to replace the file or [save a new version into the file](https://devnet.logianalytics.com/hc/en-us/articles/1500009748782-Creating-Versions#Save).

After saving a dashboard into the server resource tree, you can browse to its directory in the server resource tree in the Server Console and [run it directly](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You will not be able to save dashboards to locations where you do not have the **Write** permission.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard)
