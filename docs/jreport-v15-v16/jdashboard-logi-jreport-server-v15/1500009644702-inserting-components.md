---
title: "Inserting Components"
id: 1500009644702
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644702-Inserting-Components
updated_at: 2021-07-24T20:55:17Z
---

# Inserting Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644642-Creating-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard)

# Inserting Components

You can insert library components and report data components as well as labels, images, special fields, filtering tools, third-party objects, and HTML components into dashboards via the Resources panel. To access the panel, select the **Show Resources** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar.

Below is a list of the sections covered in this topic:

* [Inserting Library Component References](#LC)
* [Inserting Report Data Components](#Report)
* [Inserting Analysis Templates As Components](#VA)
* [Inserting a Label/Dashboard Title](#Label)
* [Inserting an Image](#Image)
* [Inserting a Special Field](#SF)
* [Inserting a Filter Control](#Filter)
* [Inserting a Third-Party Gadget via URL](#URL)
* [Inserting an HTML Component](#HTML)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting Library Component References

When inserting a library component from the component library into a dashboard, you are not copying it from the component library, but instead referencing it. In this sense, when a library component is edited in Logi JReport Designer and republished to the component library, the changes will be reflected in all the dashboards that reference the library component, and any changes made to a library component in a dashboard will be saved into the dashboard only without affecting the source library component. However, if the same change in a library component is made both at design time in Logi JReport Designer and at runtime in a dashboard, the runtime change has higher priority.

To reference a library component into the dashboard body:

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. Expand the **Component Library** node, browse to find the library component you want to insert, then drag it to the destination in the dashboard body.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting Report Data Components

Data components such as tables, crosstabs, charts, KPI components, and geographic maps in reports can be directly inserted into dashboards after being converted into library components automatically.

For reports that use [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views) as data sources, all data components can be converted to library components successfully.

However, page reports may use queries as data sources other than business views, therefore, only when the queries have corresponding business views, can the components be converted to library components and used in dashboards. So if you would like your page report components to be added in dashboards, you need to make sure the components are created on business views or if on queries a business view is created using each of the queries.

Currently library components do not support some features of page report components, after the latter are inserted into dashboards, those features will be removed. This may result in that the data components in dashboards look different from when they are in page reports. For features that are not supported in JDashboard, they will either be ignored, removed, or applied with the default values.

The following table lists how JDashboard deals with the unsupported page report features:

| In Page Report Components | In Library Components |
| --- | --- |
| Display types like Barcode, Check box, and so on | Ignored |
| Special fields | Removed |
| Dynamic resources | Changed to constant resources |
| Master/Detail reports | Ignored |
| Subreports | Removed |
| Nested data components that is one contains another | The ownership is removed and the involved data components are regarded as individual components. |
| Definition properties | Ignored |
| Formula-controlled properties | Default values are applied. |
| Other components | Removed |

**To insert a report data component into the dashboard body:**

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Reports node, expand the report that contains the desired data component and drag the component into the dashboard body.
3. If the report component uses parameters, the default values will be applied. You can change the parameter values via the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#ConfigPanel) after the component is loaded.

The inserted report data component runs with the report's catalog so it will not be able to run if the catalog is removed or updated. The report data component is not controlled by the [runtime filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting Analysis Templates As Components

Analysis templates after being saved into the server resource tree can be inserted into dashboards as components. This feature requires a license for [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009667781-Visual-Analysis).

**To insert an analysis template as component into the dashboard body:**

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Reports node, browse to the target analysis template (.va) and you will find a VCTObject under it. Drag the VCTObject into the dashboard body.

The inserted analysis template will be wrapped into a runtime library component and its data presentation area and legend area without legend icons will be displayed, just for viewing. However if no field binds with any legend, the legend area will not be shown. The default title is the server resource name of the parent analysis template without the suffix .va.

The inserted analysis templates cannot be [exported](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components) or [printed](https://devnet.logianalytics.com/hc/en-us/articles/1500009644762-Printing-Library-Components), therefore when exporting or printing a dashboard, they will not be listed and the cells containing them will be left blank.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Label/Dashboard Title

Labels can be inserted in the dashboard header. A dashboard title is a special label.

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **Label**/**Dashboard Title** to the destination in the dashboard header.
3. Double-select the label/title and edit the text.
4. [Edit the properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#EditHeaderObj) of the label/title such as font, size, color, and so on if you want.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting an Image

Images can be inserted in the dashboard header.

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **Image** to the destination in the dashboard header. The [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009670341-Insert-Image) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920589847/insrtimg.gif)
3. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**, then input the image URL or paste the URL in the File URL text field.
   * To use an image in the image library of JDashboard, select **Library**, then select the image in the My Pictures box.
4. Select **OK** to insert the image.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Special Field

Special fields can be inserted in the dashboard header.

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **Special Field** to the destination in the dashboard header. The [Insert Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009646142-Insert-Special-Field) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920589335/insrtspclfld.gif)

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
4. [Edit the properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#EditHeaderObj) of the special field such as font, size, color, and so on if you want.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Filter Control

Filter controls can be inserted in the dashboard body. They are used to filter component data. For details, see [Filtering Component Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Third-Party Gadget via URL

A web page can be inserted in the dashboard body. All you need to do is give its URL. Note that some websites such as `http://www.google.com` do not allow Gadgets to load them.

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **URL Frame** into the dashboard body. The [Insert URL Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009646162-Insert-URL-Frame) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926752535/insrturl.gif)
3. In the Title text field, give a title for the frame that will display the contents of the web page.
4. In the URL text box, type in the URL of the web page. If needed, select the **Add Parameter** button to open the [Select Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009670501-Select-Parameter) dialog to insert a parameter to the URL to compose a dynamic URL (if no data source is specified, the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009646262-Select-Data-Source) dialog will be displayed for you to select the data source that contains the parameter you want first).

   You should provide a complete URL address. A URL without "http://", for example www.jinfonet.com, will not be automatically added "http://" since it is regarded a relative path, which may lead to that the URL cannot be opened in some browsers.
5. If you would like the specified web page to refresh periodically, select **Auto refresh**, then specify the time interval at which to refresh it.
6. Select **OK**. The specified web page will be inserted into the dashboard. You can then view the web page from JDashboard. If parameters are used in the URL, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif) on the toolbar to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values) as you want, then you can get different web pages based on different parameter values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting an HTML Component

An HTML component allows for typing text, comments, and messages using a simple-featured text editor. It can be inserted in the dashboard body.

1. Select **Show Resources**![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif) on the toolbar to display the Resources panel.
2. From the Toolbox node, drag **HTML** to the destination in the dashboard body. The [Insert HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009670321-Insert-HTML) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920590103/insrthtml.gif)
3. Specify a title for the HTML component.
4. In the text box, type text directly. You can make use of the buttons above the text box to format the text such as font face, size, style, color, and alignment, insert images into the HTML component and create hyperlinks on the text and images in the HTML component.
5. Select **OK** to insert the HTML component.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644642-Creating-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard)
