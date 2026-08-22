---
title: "Adding a Table of Contents in a Report"
id: 5735569955863
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report
updated_at: 2022-11-02T08:23:04Z
---

# Adding a Table of Contents in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report)

# Adding a Table of Contents in a Report

You can add a table of contents in a page or web report, to enable easy navigation of the report content when previewing the report in Designer and in the report outputs. This topic describes how to add a Table of Contents in a report.

1. Open the report, and for a page report, switch to the page report tab.
2. Select an existing [page panel](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Panel) in the Report Inspector, then do either of the following:
   * Navigate to **Insert** > **TOC Page**.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Right-click in any blank area in the page panel in the design area and select **Insert** > **TOC Page** from the shortcut menu.

   ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Designer displays the [Insert TOC Page dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566615063-Insert-TOC-Page-Dialog-Box).

   ![Insert TOC Page  dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898405881623/insttocpg.gif)
3. Specify where you want to place the TOC, before or after the current page panel.
4. Designer adds a table of contents in the report at the specified location, and automatically creates a [TOC page panel](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#TOC) to position the TOC.

   ![Insert TOC in Report](https://devnet.logianalytics.com/hc/article_attachments/9898405909271/rpt_toc1.gif)
5. In the Report Inspector, specify the **TOC Anchor** and **Anchor Display Value** properties of the objects in the report that you want to add in the TOC. Basically, you can include data components, tabulars, text boxes, group panels in banded object, and DBFields, formula fields, parameter fields, images, and labels inside banded objects in the TOC. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")However, the objects should be in page panels that are after the TOC page panel, so Designer can create TOC entries for them.
6. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")You can select the node representing the web report or page report tab and set the [Ignore TOC Anchor of Parent](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#IgnoreParentTOCAnchor) and [Continuous Page Number with TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#ContinuousPageNumber) properties.
7. ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")Double-click the TOC or right-click it and select **Format** from the shortcut menu. Designer displays the [Format TOC Title & Levels dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7933801563543-Format-TOC-Title-Levels-Dialog-Box).

   ![Format TOC Title & Levels dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898403100439/fmttoc.gif)
8. In the **Title** text box, type the text you want to display as the title of the TOC, then specify the font style and spacing of the title.
9. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a TOC level and specify the font style, spacing, leader character, and other options for TOC entries of this level.
10. Repeat the preceding step to add more TOC levels and edit the formatting of each level.
11. Select **OK** to finish customizing the TOC style.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can also specify the style of the TOC by setting [properties of the TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735517701399-TOC-Container-Properties) in the Report Inspector. However, once you define the formatting for the TOC title or TOC entries in any level in the Format TOC Title & Levels dialog box, it overrides the formatting specified in the Report Inspector.
12. You can insert the **TOC Page Number** special field in the header or footer of the TOC page panel to display page number for the TOC. Logi Report Engine calculates the number for the TOC pages differently than the report pages.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) By default, Designer does not show the header or footer of the TOC page panel. To insert objects in them, you need to first edit their **Invisible** property to "true", or you can select in the TOC page and navigate to **View** > **Page Header**/**Page Footer**.
13. Select the **View** tab to preview the report and select **Show TOC Page** to display the table of contents in the report.

    ![Preview Report with TOC](https://devnet.logianalytics.com/hc/article_attachments/9898405922455/rpt_toc2.gif)
14. Select an item in the TOC and Designer opens the page containing the corresponding object.

After adding TOC in a report, when you export or print the report in Designer or at runtime, and when you run the report in advanced mode or schedule to run it in formats except Web Report for a web report, you can also use the TOC in the report output to easily locate the content you need to focus on.

In addition to the table of contents generated by inserting the TOC Page object, Designer also provides the [TOC object](https://devnet.logianalytics.com/hc/en-us/articles/5735585983511-TOC-Properties) for each page report tab and web report in the Report Inspector. This TOC object corresponds to the TOC tree of the report. When you add an object in the table of contents of a report, you also include the object in its TOC tree. You can view the TOC tree of a report in the following scenarios:

* When previewing the report in Designer, you can select **TOC**![TOC button](https://devnet.logianalytics.com/hc/article_attachments/9898422078487/btn_toc.gif) on the View tab toolbar to display the TOC tree.
* When exporting the report to [HTML](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML) and [PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF) in Designer, you can select the TOC option to enable displaying the TOC tree in the Table of Contents panel of the PDF and HTML browsers.
* At runtime, you can view the TOC tree in the TOC Browser of Page Report Studio when running a page report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report)
