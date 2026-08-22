---
title: "Designing the Report Pages"
id: 1500010101321
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages
updated_at: 2021-07-23T19:16:50Z
---

# Designing the Report Pages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101161-Creating-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101401-Applying-True-Type-Fonts-in-Reports)

# Designing the Report Pages

A report page is a medium which contains the layout result for a single page of a report. At runtime, Logi Report Engine generates a page or multiple pages according to the page panel settings. For reports, each page has its own page header and page footer, which are controlled by the page panel settings for them. In library components, there is no page header and page footer. This topic introduces the features of report pages and how you can apply them to design the report pages for your reports.

A report page has the following features:

* [Page Panel](#Panel)
* [Page Header and Footer](#Header)
* [Page Settings](#Setting)
* [Page Break](#Break)
* [Page Mode](#Mode)
  + [Pagination Mode](#Pagination)
  + [Continuous Mode](#Continuous)

## Page Panel

A page panel is a template where you design a page. You can define information for it and define information for pages designed with this page panel accordingly at the same time. Here, information covers all factors of a page, including page size, margin, and orientation. In a page report tab, Designer also supports multiple page panels. For multiple page panels, you have to define each page panel's page settings individually.

You can insert page panels into the report body of a page report tab. For banded reports which are restricted flow layout reports that can contain only one single horizontal banded object, you can add one page panel separately for the banded header, banded footer, and detail panel of the banded object whose parent is the report body.

**To insert a page panel:**

1. Select **Insert** > **Page Panel**. Designer displays the [Page Panel dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060042-Page-Panel-Dialog-Box).

   ![Page Panel dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856822039/pgpnl.gif)
2. Choose whether the new page keeps the original page settings or it applies new settings.
3. Select **OK**. If
   you specify to insert a page panel where the new page has new page settings,
   Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) for you to adjust the settings for the new page panel.

To remove a page panel from a page report tab, set the mouse pointer to the beginning of the page panel and then press the **Backspace** key.

## Page Header and Footer

Page header and footer are areas in the top and the bottom page margins, where you can add almost any components. You can insert fields, such as page numbers and topic headings, in the page header and footer.

When you create a page report tab or a web report or when you add a new page panel in a page report tab, Designer generates a page header and page footer at the same time. You can show or hide them by selecting or unselecting **Page Header** and **Page Footer** on the **View** menu tab.

## Page Settings

Settings for a page are the same as with a page panel which Designer uses as a template to design this page. All pages designed with the same page panel apply the same page settings, so you just need to set the settings for one page panel to apply them to all these pages.

To adjust the page settings, you can use either of the following two methods:

* **Adjusting via the Page Setup dialog box**
  1. Select **File** > **Page Setup**. Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box).

     ![Page Setp dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848402327/pgstup_gnrl.gif)
  2. In the **General** tab of the dialog box, set the size, orientation, and margin for the page. You can select the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents in the page is unpredictable and when the report is not huge.

     The Export tab is for defining page properties for the output of each export format. For more information, see [Exporting Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result).
  3. Select **OK** to apply your settings.

* **Adjusting via the Report Inspector**
  1. Select **View** > **Inspector**.
  2. In the Report Inspector, select the **Page Panel** node the properties of which you want to customize.
  3. Set the [property values](https://devnet.logianalytics.com/hc/en-us/articles/1500010062242-Page-Panel-Properties) according to your requirements.

## Page Break

Designer generates a new page when the space in a page has been fully occupied, or when for a page report tab there exists a break control in this page, for example, you insert a page break in the page. You can insert page breaks into the report body level. To insert a page break in a page report tab, select **Insert** > **Page Break**.

For banded reports which are restricted flow layout reports that can contain only one single horizontal banded object, you can add a page break separately for the banded header, banded footer, and detail panel of the banded object when the following conditions are satisfied:

* The parent of the banded object is the report body.
* The page panel for the banded header, banded footer, and detail panel of the banded object are not all added.

## Page Mode

You can set the page mode of a page report tab or a web report to be either pagination mode or continuous mode (to switch between the two page modes, select or unselect **Page Layout** on the **View** menu tab).

### Pagination Mode

Pagination mode displays the page margins and enables multiple pages when running the report. In this mode, you can specify the page shape and size in the page panel settings. Once defined, Designer lays out the contents of the page report tab or web report according to these specifications. If the contents exceed the specified size, the page break control starts a new page with the same size.

In addition, the total page size is determined both by the contents' size and by the page breaking control, such as Fill Whole Page, On New Page, and Page Break.

### Continuous Mode

In continuous mode (Page Layout unselected), the report becomes a single continuous page at runtime, which is useful for dashboard style reports where multiple pages are not wanted. However, if the report is very large, it may run out of memory and be very unresponsive in continuous mode.

In continuous page mode, only the component breaking control works. Designer lays out the whole page report tab or web report in a single page, and it has no specific shape and size. If you do not set any component breaking control, Designer lays out all of the components in the same page, and the size of the page depends on the size of the contents.

In continuous page mode, Designer skips all of the properties that you specify in pagination mode, including the page breaks in page panel. In this way, if there is more than one page panel in a page report tab, Designer lays out all contents contained in different page panels in the same page, and it only lays out the first page panel's page header and footer.

**Component breaking rule**

Designer provides you with an option for adding page breaks to a component in continuous page mode. This kind of page break is not based on space, but on logic. For example, you can set a group break to occur every 20 detail panels, no matter how big these 20 detail panels are.

The following components have logic break functionality:

* Banded objects which are available in page reports   
  The logic break acts only on the sub components - detail panel and group panel. In this case, there are two properties in the Report Inspector to control the component logic break: Current Block Index and Items per Block.
* Tables  
  The logic break acts only on the sub components - table detail in page reports and table group. In this case, there are two properties in the Report Inspector to control the component logic break: Current Block Index and Items per Block.
* Crosstabs in page reports that use query resources   
  The logic break acts on the whole crosstab. In this case, there are four properties in the Report Inspector to control component logic break: Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101161-Creating-Bursting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101401-Applying-True-Type-Fonts-in-Reports)
