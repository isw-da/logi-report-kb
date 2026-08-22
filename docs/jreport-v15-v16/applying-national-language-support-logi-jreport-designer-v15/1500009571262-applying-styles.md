---
title: "Applying Styles"
id: 1500009571262
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571262-Applying-Styles
updated_at: 2021-07-24T05:53:43Z
---

# Applying Styles

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571322-Managing-CSS-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles)

# Applying Styles

You can apply a style in the process of creating a report or at any time when designing a report. During report design, if you have applied more than one style to a component, these styles will be combined.

The following introduces all the ways of specifying a style. Choose the appropriate methods available to you.

* **Using wizards**  
   Report wizards contain a Style screen for you to specify a style.
* **Using the style drop-down list on the toolbar**  
   The style drop-down list ![](https://devnet.logianalytics.com/hc/article_attachments/4404889275287/btn_stybx.gif) on the Home menu tab provides a list of styles for choosing. In this way you can apply a style to one or more selected objects.
* **Using the Report Inspector**  
   There is a Style Group property in the Others category of the Properties sheet for a page report tab or web report in the Report Inspector. It allows you to specify an XSD style.

**Notes:**

* There are 15 sets of demo XSD styles provided by Logi JReport, which can be applied to crosstabs, tables, banded objects and DBFields converted from previous versions. Other components can only apply the XSD styles which are created by yourself. XSD styles are primarily for compatibility with previous versions.
* By default, the demo XSD styles are not included in either the Style box of the report wizards or the style drop-down list on the toolbar. If you want to have them displayed, uncheck the option "Only CSS styles available in the style list" in the Component category of the Options dialog.
* If you choose to apply a style by setting the Style Group property, later when you preview, export or publish the report, you will be asked to select the style group you want to use or publish. The style specified by the Style Group property will be applied automatically only when you directly run the report on Logi JReport Server.
* When applying CSS styles, you may get warning message showing the CSS properties that are not supported by Logi JReport. If you want to cancel the warning message, uncheck the option "Show warning message when CSS properties are not supported by Logi JReport" in the General category of the Options dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571322-Managing-CSS-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles)
