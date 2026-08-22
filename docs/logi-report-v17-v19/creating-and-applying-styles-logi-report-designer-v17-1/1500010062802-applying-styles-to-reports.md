---
title: "Applying Styles to Reports"
id: 1500010062802
section: "Creating and Applying Styles - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports
updated_at: 2021-07-23T19:16:52Z
---

# Applying Styles to Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062822-Working-with-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094121-Defining-Report-Security)

# Applying Styles to Reports

You can apply a style in the process of creating a report or at any time when designing a report. This topic describes how you can apply styles to reports as well as make the objects in reports inherit the style from their parents.

This topic contains the following sections:

* [Applying a Style to a Report](#Report)
* [Inheriting Styles](#Inherit)

## Applying a Style to a Report

The following shows all the ways of applying a style to a report. Choose the appropriate methods available to you.

* **Using wizards**

  The report wizard contains a **Style** screen for you to specify a style.
* **Using the style drop-down list on the toolbar**

  The style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404848369559/btn_stybx.gif) on the **Home** menu tab provides a list of styles for choosing. In this way, you can apply a style to one or more selected objects.
* **Using the Report Inspector**

  You can use the **Style Group** property in the **Others** category of the Properties sheet for the [Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#StyleGroup) or [Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010100981-Web-Report-Properties#StyleGroup) object in the Report Inspector to apply an XSD style to a page report tab or web report. For page report tabs, you can also specify a style group for different export formats using the [Style Group for Export](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#ExportStyleGroup) properties.

  Once you have applied a style group to a page report tab or a web report via the Style Group property, when you [preview](https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports) or [export](https://devnet.logianalytics.com/hc/en-us/articles/1500010060882-Printing-and-Exporting-Reports) the report, Designer prompts you the Select Style Group dialog box to specify a style group for the report; when you [publish the report to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely), Designer displays the Publish Additional Resources dialog box for you to select the style groups to publish with the report. By selecting a style group at runtime, you can change the look and feel of your report in a dynamic way.

After applying a style in a report, if you further edit the corresponding style file, you need to apply the style again to make the changes take effect. When you apply a style to an object more than once, Designer combines and overwrites (for the same properties) the properties defined for this object in all the styles you have ever selected.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* There are 15 sets of demo XSD styles provided by Logi Report, which can be applied to crosstabs, tables, banded objects and DBFields converted from previous versions. Other components can only apply the XSD styles which are created by yourself. XSD styles are primarily for compatibility with previous versions.
* By default, the demo XSD styles are not included in either the Style box of the report wizards or the style drop-down list on the toolbar. If you want to have them displayed, clear the option "Only CSS styles available in the style list" in the Component category of the Options dialog box.
* If you choose to apply a style by setting the Style Group property, later when you preview, export or publish the report, you will be asked to select the style group you want to use or publish. The style specified by the Style Group property will be applied automatically only when you directly run the report on Server.
* When applying CSS styles, you may get warning message showing the CSS properties that are not supported by Logi Report. If you want to cancel the warning message, clear the option "Show warning message when CSS properties are not supported by Logi Report" in the General category of the Options dialog box.

## Inheriting Styles

The four types of data components - table, crosstab, chart, and banded object can remember the style applied to them, therefore, objects inside them by default inherit their styles. If you want to make these objects take on different appearances, you can apply styles to them independently. To do this, in the design area, select an object that is inside any of the four data components and select a style from the style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404848369559/btn_stybx.gif) on the **Home** menu tab.

For a table, crosstab, chart, or banded object that is inside another banded object, you can also cancel the way of inheriting style from its parent while creating or editing it with the report wizard by clearing the **Inherit Style** option in the **Style** screen and then selecting the style you prefer in the Style box.

![Inherit Style](https://devnet.logianalytics.com/hc/article_attachments/4404848396567/style_apply.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062822-Working-with-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094121-Defining-Report-Security)
