---
title: "Applying Styles"
id: 1500010034922
section: "Creating and Applying Styles - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034922-Applying-Styles
updated_at: 2021-07-24T10:37:42Z
---

# Applying Styles

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070981-CSS-Styles) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063221-Defining-Report-Security)

# Applying Styles

You can apply a style in the process of creating a report or at any time when designing a report.

The following introduces all the ways of specifying a style. Choose the appropriate methods available to you.

* **Using wizards**

  The report wizard contains a Style screen for you to specify a style.
* **Using the style drop-down list on the toolbar**

  The style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404901109655/btn_stybx.gif) on the Home menu tab provides a list of styles for choosing. In this way you can apply a style to one or more selected objects.
* **Using the Report Inspector**

  There is a Style Group property in the Others category of the Properties sheet for [page report tabs](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#StyleGroup) and [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034542-Web-Report-Properties#StyleGroup) in the Report Inspector. It allows you to apply an XSD style to a page report tab or web report. For page report tabs, you can also specify a style group for different export formats using the [Style Group for Export](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#ExportStyleGroup) properties.

  Once a page report tab or a web report is applied with a style group via the Style Group property, when you [preview](https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports) or [export](https://devnet.logianalytics.com/hc/en-us/articles/1500010033062-Printing-and-Exporting-Reports) the report, you will be prompted the Select Style Group dialog to specify a style group for the report; when you [publish the report to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely), the Publish Additional Resources dialog will appear for you select the style groups to publish with the report. By selecting a style group at runtime, you can change the look and feel of your report in a dynamic way.

After applying a style in a report, if the corresponding style file is edited, you need to apply the style again to make the changes take effect. When you apply a style to an object more than once, properties defined for this object in all the styles you have ever selected will be combined and overwritten (for the same properties).

**Notes:**

* There are 15 sets of demo XSD styles provided by Logi JReport, which can be applied to crosstabs, tables, banded objects and DBFields converted from previous versions. Other components can only apply the XSD styles which are created by yourself. XSD styles are primarily for compatibility with previous versions.
* By default, the demo XSD styles are not included in either the Style box of the report wizards or the style drop-down list on the toolbar. If you want to have them displayed, uncheck the option "Only CSS styles available in the style list" in the Component category of the Options dialog.
* If you choose to apply a style by setting the Style Group property, later when you preview, export or publish the report, you will be asked to select the style group you want to use or publish. The style specified by the Style Group property will be applied automatically only when you directly run the report on Logi JReport Server.
* When applying CSS styles, you may get warning message showing the CSS properties that are not supported by Logi JReport. If you want to cancel the warning message, uncheck the option "Show warning message when CSS properties are not supported by Logi JReport" in the General category of the Options dialog.

## Inheriting Styles

The four types of data components - table, crosstab, chart and banded object can remember the style applied to them, therefore objects inside them by default will inherit their styles. If you want to make these objects take on different appearances, you can apply styles to them independently. To do this, in the design area select an object that is inside any of the four data components and select a style from the style drop-down list ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404901109655/btn_stybx.gif) on the Home menu tab.

For a table, crosstab, chart or banded object that is inside another banded object, you can also cancel the way of inheriting style from its parent while creating or editing it with the report wizard by unchecking the Inherit Style option in the Style screen and then selecting the style you prefer in the Style box.

![Inherit Style](https://devnet.logianalytics.com/hc/article_attachments/4404909119255/style_apply.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070981-CSS-Styles) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063221-Defining-Report-Security)
