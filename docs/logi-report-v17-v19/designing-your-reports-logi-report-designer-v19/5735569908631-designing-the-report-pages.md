---
title: "Designing the Report Pages"
id: 5735569908631
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages
updated_at: 2022-11-02T08:23:01Z
---

# Designing the Report Pages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534125591-Creating-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports)

# Designing the Report Pages

A report page is a medium that contains the layout result for a single page of a report. This topic introduces the features of report pages and how you can apply them to design pages for your reports.

A report page has the following features:

* [Page Panel](#Panel)
  + [TOC Page Panel](#TOC)
* [Page Header and Footer](#Header)
  + [TOC Page Header and Footer](#TOCHF)
* [Page Settings](#Setting)
* [Page Break](#Break)
* [Page Mode](#Mode) 
  + [Specifying the Page Mode of a Report](#SpecifyMode)
  + [Adding Component Break Controls in a Report](#CompBreak)

## Page Panel

A page panel is a template where you design a page. You can specify its settings and settings for pages designed with this page panel accordingly at the same time. The settings cover all factors of a page, including page size, margin, and orientation.

In a page report tab, you can insert as many page panels as you need in the report body. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")However, a web report can contain at most three page panels and one of them must be a [TOC page panel](#TOC) in the middle. You can specify page settings for each page panel differently.

**To insert a page panel into a page report tab**

1. Select an existing page panel in the Report Inspector.
2. Do either of the following:
   * Navigate to **Insert** > **Page Panel**.
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Right-click in any blank area in the page panel in the design area and select **Insert** > **Page Panel** from the shortcut menu.
3. Designer displays the [Insert Page Panel dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566576023-Insert-Page-Panel-Dialog-Box).

   ![Insert Page Panel dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898422971799/instpgpnl.gif)
4. Choose whether the new page panel keeps current page settings or it applies new settings.
5. Select **OK**. Designer inserts a new page panel next to the current one, or if
   you specify to insert a page panel where pages designed by this page panel have new page settings,
   Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box) for you to edit settings for the new page panel first.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**To insert a page panel in a web report**

After [adding a TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) in a web report, you can insert one more page panel in the web report.

1. Select the existing page panel in the Report Inspector.
2. Do either of the following:
   1. Navigate to **Insert** > **Page Panel**.
   2. Right-click in any blank area in the page panel in the design area and select **Insert** > **Page Panel** from the shortcut menu.
3. In the Insert Page Panel dialog box, specify whether the new page panel keeps current page settings or it applies new settings, then select **OK**.
4. When you specify to apply new page settings to this page panel,
   Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box) for you to edit its page settings.
5. Designer inserts a new page panel before or after the TOC page panel, depending on the position of the existing page panel. Anytime, the TOC page panel must be in the middle of the three page panels.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) In a web report, you should place the components you want to display in Web Report Studio in the page panel that is after the TOC page panel. At runtime, components in the page panel before the TOC page panel and the TOC pages generated by the TOC page panel in a web report can only display when you export the report. You can use the page panel before the TOC page panel to present additional information when you export or print the web report, such as a cover or preface for the report.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**To delete a page panel**

1. Select the page panel in the Report Inspector.
2. Right-click in any blank area in the page panel in the design area and select **Delete Page** from the shortcut menu.

For a page report tab, you can also delete a page panel by placing the mouse pointer to the beginning of the page panel and selecting **Backspace** on the keyboard.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You cannot delete the first page panel in a page report tab.
* When you delete a page panel from a page report tab, if the page panel contains content, Designer moves the content to the previous page panel.

### TOC Page Panel

When you insert the TOC Page object into your page report tab or web report, Designer automatically creates the TOC page panel to position the table of contents generated by the object. You cannot insert TOC page panel directly, while you can customize its page settings in the same way as you do for a general page panel. A report can have only one TOC page panel.

To remove the TOC page panel, delete the table of contents in it and Designer deletes the TOC page panel at the same time. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")When you delete the TOC page panel from a web report, Designer also deletes the page panel before the TOC page panel if there is one.

## Page Header and Footer

Each page in a page report or web report has its own page header and page footer. They are the areas in the top and bottom page margins, where you can add almost any components. You can insert fields, such as page numbers and topic headings, in the page header and footer.

When you create a page report tab or a web report or when you add a new page panel in a page report tab, Designer generates a page header and page footer at the same time. By default, Designer does not display the header or footer of the page panels. You can show or hide them for each page panel by selecting in the page panel and then selecting or clearing **Page Header** and **Page Footer** in the **View** ribbon.

### TOC Page Header and Footer

The TOC page panel also has its own page header and footer and you can show or hide them and insert objects in them. However, different from the header and footer of a general page, the TOC page header and footer can only contain labels and the special field TOC Page Number, ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Export Page Number, and Export Total Page Number.

## Page Settings

All pages designed with the same page panel apply the same page settings, so you just need to set the settings for one page panel to apply them to all these pages.

To customize the page settings, you can use either of the following two methods:

* **Customizing via the Page Setup dialog box**
  1. For a page report tab containing multiple page panels, place the mouse pointer inside the page panel first.
  2. Select **Page Setup** in the **Home** or **File** ribbon. Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box).

     ![Page Setp dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898422989079/pgstup_gnrl19.2.gif)
  3. In the **General** tab,
     + ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")For a page report tab or web report, specify the [page mode](#SpecifyMode) of the report using the **Page Layout** option.
     + Specify the size, orientation, and margin of the pages.
     + You can select **Auto Fit** to calculate the page width/height according to the width/height of the content within the pages dynamically, which is useful when the width/height of the content in the pages is unpredictable and when the report is not huge.
     + For a page report tab, you can also [use constant level formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) some page properties, if you have [bound a data resource to its report body](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports).
  4. Use the **Export** tab to define page settings for the output of different export formats. See [Customizing Page Settings for Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Page).
  5. Select **OK** to apply your settings.

* **Customizing via the Report Inspector**
  1. In the Report Inspector, select the **Page Panel** node in the report structure tree (for a page report tab containing multiple page panels, select the node representing the page panel you want to customzie).
  2. Set the [property values](https://devnet.logianalytics.com/hc/en-us/articles/5735533484311-Page-Panel-Properties) according to your requirements.

## Page Break

When laying out a report, Logi Report generates a new page when the space in a page has been fully occupied, or when for a page report tab there exists a break control in this page, for example, you insert a page break in the page.

You can insert page breaks in the report body of a page report tab only.

1. In the Report Inspector, select a page panel of the page report tab.
2. Do either of the following:
   * Navigate to **Insert** > **Page Break**
   * ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Right-click in any blank area in the page panel in the design area and select **Insert** > **Page Break**.

## Page Mode

Each page report tab and web report applies a page mode to determine the layout of the report pages, which can be either pagination mode or continuous mode. By default, Designer applies pagination mode to the reports.

* **Pagination Mode**  
  Pagination mode displays the page margins and enables multiple pages. In this mode, you can specify the page shape and size in the [page panel settings](#Setting). Once defined, Logi Report lays out the content of the page report tab or web report according to these specifications. If the content exceeds the specified size, the page break control starts a new page with the same size. The report's total page size in pagination mode is determined both by the content's size and by the page break controls, such as Fill Whole Page, On New Page, and Page Break.
* **Continuous Mode**  
  In continuous mode, the whole report displays in a single page that has no specific shape and size (the size of the page depends on the size of the content), which is useful for dashboard style reports where multiple pages are not wanted. However, if the report is very large, it may run out of memory and be very unresponsive. In continuous page mode, Logi Report skips all properties that you specify in pagination mode, including the [page breaks](#Break) in page panel. In this way, when there is more than one page panel in a page report tab, Logi Report displays all content contained in different page panels in the same page, and only displays the first page panel's page header and footer. However, when you display a page report tab or web report in continuous mode, you can specify [component break controls](#CompBreak) to display some components in different pages.

### Specifying the Page Mode of a Report

When designing a page report tab or web report in Designer, ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")you can customize the page mode of the report to display it in either of the two modes in different scenarios. For example, you can display a page report tab in multiple pages when you view it in Designer, while in a single page in the HTML output.

1. Select **Page Setup** in the **Home** or **File** ribbon.
2. In the **General** tab of the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box), ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")keep **Page Layout** selected to display the report in multiple pages. To display the report in a single page, clear the option. This setting determines the page layout of the report in Designer view mode, and in Page Report Studio as well, for a page report tab.
3. In the **Export** tab, select each format from the **Export To** drop-down list, then select or clear Page Layout to specify the page mode of the corresponding report output. See [Customizing Page Settings for Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Page).
4. Select **OK** to apply the settings.

You can also select or clear **Page Layout** in the **View** ribbon to switch between the two page modes, ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")which corresponds to the Page Layout option in the General tab of the Page Setup dialog box.

### Adding Component Break Controls in a Report

When you display a page report tab or web report in continuous page mode, if you do not want to display all components of the report in the same page, Designer provides you the alternative to add page breaks in some components. This type of page break is not based on space, but on logic. For example, you can set a break to occur every 20 detail panels, no matter how big these 20 detail panels are.

You can apply logic page break to the following components: banded objects, tables, and query-based crosstabs.

* In a banded object, the logic break acts only on its child detail panel and group panels. You can use the [Current Block Index and Items per Block](https://devnet.logianalytics.com/hc/en-us/articles/9898557673239-Banded-Detail-Panel-Properties#BlockIndex) properties of the child objects to control the component logic break.
* In a table, the logic break acts only on its child detail row (available to query-based table only) and group rows. You can use the Current Block Index and Items per Block properties of the child objects to control the component logic break.
* In a query-based crosstab, the logic break acts on the whole crosstab. You can use the four crosstab properties to control component logic break: [Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block](https://devnet.logianalytics.com/hc/en-us/articles/5735585354647-Crosstab-Properties#BlockIndex).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534125591-Creating-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports)
