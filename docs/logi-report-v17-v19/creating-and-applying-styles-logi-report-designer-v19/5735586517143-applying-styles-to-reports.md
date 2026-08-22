---
title: "Applying Styles to Reports"
id: 5735586517143
section: "Creating and Applying Styles - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports
updated_at: 2022-11-02T08:23:11Z
---

# Applying Styles to Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586532503-Working-with-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506649879-Defining-Report-Security)

# Applying Styles to Reports

You can apply a style in the process of creating a report or at any time when designing a report. This topic describes how you can apply styles to reports and make the objects in reports inherit the style from their parents.

This topic contains the following sections:

* [Applying a Style to a Report](#Report)
* [Inheriting Styles](#Inherit)

## Applying a Style to a Report

The following shows all the ways of applying a style to a report. Choose the appropriate methods available to you.

* **Using wizard**  
  The component wizard contains a Style screen for you to specify a style.
* **Using the style drop-down list on the toolbar**  
  The style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/9898404584215/btn_stybx.gif) in the Home ribbon provides a list of styles for choosing. In this way, you can apply a style to one or more selected objects.
* **Using the Report Inspector**  
  You can use the **Style Group** property in the Report Inspector to apply an XSD style to a [page report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup). For page report tabs, you can also specify a style group for different export formats using the [Style Group for Export](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#ExportStyleGroup) properties.

  Once you have applied a style group to a page report tab or a web report via the Style Group property, when you [preview](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports) or [export](https://devnet.logianalytics.com/hc/en-us/articles/5735567895703-Printing-and-Exporting-Reports) the report, Designer prompts you the Select Style Group dialog box to specify a style group for the report; when you [publish the report to Server](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources#Remotely), Designer displays the Publish Additional Resources dialog box for you to select the style groups to publish with the report. By selecting a style group at runtime, you can change the look and feel of your report in a dynamic way.

After applying a style in a report, if you further edit the corresponding style file, you need to apply the style again to make the changes take effect. When you apply a style to an object more than once, Designer combines and overwrites (for the same properties) the properties defined for this object in all the styles you have ever selected.

The following are some tips for you when applying a style to a report:

* There are 15 sets of demo XSD styles provided by Logi Report, which you can apply to crosstabs, tables, banded objects, and DBFields converted from previous versions. Other components can only apply the XSD styles that you create by yourself. XSD styles are primarily for compatibility with previous versions.
* By default, the demo XSD styles are not included in either the Style box of the component wizards or the style drop-down list on the toolbar. If you want to display them, clear "Only CSS styles available in the style list" in the Component category of the Options dialog box.
* If you choose to apply a style by setting the Style Group property, later when you preview, export, or publish the report, Designer prompts you to select the style group you want to use or publish. The style specified by the Style Group property will be applied automatically only when users directly run the report on Server.
* When applying CSS styles, you may get warning message showing the CSS properties that Logi Report does not support. If you want to cancel the warning message, clear "Show warning message when CSS properties are not supported by Logi Report" in the General category of the Options dialog box.

## Inheriting Styles

Tables, crosstabs, charts, banded objects, and KPIs, can remember the style applied to them, therefore, objects inside them by default inherit their styles. If you want to make these objects take on different appearances, you can apply styles to them independently. To do this, in the design area, select an object that is inside any of the component and select a style from the style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/9898404584215/btn_stybx.gif) in the **Home** ribbon.

For a table, crosstab, chart, or banded object that is inside another banded object, or a KPI chart, you can also cancel the way of inheriting style from its parent while creating or editing it with the component wizard, by clearing **Inherit Style** in the **Style** screen and then selecting the style you prefer in the Style box.

![Inherit Style](https://devnet.logianalytics.com/hc/article_attachments/9898422784151/style_apply.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586532503-Working-with-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506649879-Defining-Report-Security)
