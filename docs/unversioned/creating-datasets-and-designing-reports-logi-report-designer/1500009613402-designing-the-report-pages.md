---
title: "Designing the Report Pages"
id: 1500009613402
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages
updated_at: 2021-07-24T16:03:21Z
---

# Designing the Report Pages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636121-Creating-Bursting-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636141-Making-High-Efficiency-Reports)

# Designing the Report Pages

A report page is a medium which contains the layout result for a single page of a report. At runtime, a page or multiple pages can be generated according to the page panel settings. For reports each page has its own page header and page footer, which are controlled by the page panel settings for them. In library components there is no page header and page footer.

A report page has the following features:

* [Page Panel](#Panel)
* [Page Header and Footer](#Header)
* [Page Settings](#Setting)
* [Page Break](#Break)
* [Page Mode](#Mode)
  + [Pagination Mode](#Pagination)
  + [Continuous Mode](#Continuous)

## Page Panel

A page panel is a template to design a page. You can define information for it and meanwhile information for pages designed with this page panel will be defined accordingly. Here, information covers all factors of a page, including page size, margin, and orientation. In a page report tab, Logi Report Designer also supports multiple page panels. With multiple page panels, you have to define each page panel's page settings individually.

Page panels can be inserted into the report body of a page report tab. For banded reports which are restricted flow layout reports that can contain only one single horizontal banded object, one page panel can be added separately for the banded header, banded footer, and detail panel of a banded object whose parent is the report body.

**To insert a page panel:**

1. Select **Insert** > **Page Panel**. The [Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009609542-Page-Panel-Dialog) dialog appears.

   ![Page Panel dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911609239/pgpnl.gif)
2. Choose whether the new page will keep the original page settings or it will apply new settings.
3. Select **OK**. If
   you specify to insert a page panel where the new page has new page settings,
   the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog will then appear for you to adjust the settings for the new page panel.

To remove an added page panel from a page report tab, set the mouse pointer to the beginning of the page panel and then press the **Backspace** key.

## Page Header and Footer

Page header and footer are areas in the top and the bottom page margins, where you can add almost any Logi Report components. You can insert fields, such as page numbers and topic headings, in page header and footer in a text document.

A page header and page footer will be generated at the same time when a page report tab or a web report is created or when a new page panel is added in a page report tab.

You can choose to show or hide them according to your own requirements by selecting or unselecting the **Page Header** or **Page Footer** command on the View tab.

## Page Settings

Settings for a page are the same as with a page panel which is used as a template to design this page. All pages designed with the same page panel will apply the same page settings. So, you just need to set the settings for one page panel to apply them to all these pages.

To adjust the page settings, the following are two ways for you to choose:

* **Adjusting via the Page Setup dialog**
  1. Select **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog appears.

     ![Page Setp dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904180247/pgstup_gnrl.gif)
  2. In the General tab of the dialog, set size, orientation and margin for the report page. You can select the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable and when the report to export is not huge.

     The Export tab is for defining page properties for each export result (for details, see [Exporting Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009634061-Exporting-Report-Result)).
  3. Select **OK** to apply your settings.

* **Adjusting via the Report Inspector**
  1. Select **View** > **Inspector**.
  2. In the Report Inspector, select a Page Panel node the properties of which you want to customize.
  3. Set the [property values](https://devnet.logianalytics.com/hc/en-us/articles/1500009612542-Page-Panel-Properties) according to your requirements.

## Page Break

A new page will be generated when the space in a page has been fully occupied or when for a page report tab there exists a break control in this page, for example, a page break that is inserted in the page. Page breaks can be inserted into the report body level. To insert a page break in a page report tab, select **Insert** > **Page Break**.

For banded reports which are restricted flow layout reports that can contain only one single horizontal banded object, a page break can be added separately for the banded header, banded footer, and detail panel of a banded object when the following conditions have been met:

* The parent of the banded object is the report body.
* The page panel for the banded header, banded footer, and detail panel of the banded object are not all added.

## Page Mode

In Logi Report Designer, you can set the page mode of a page report tab or a web report to be either pagination mode or continuous mode (to switch between the two page modes, you can select or unselect **Page Layout** on the View tab).

### Pagination Mode

In pagination mode, the page shape and size can be specified in the page panel settings. Once set, the contents of the page report tab or web report will be laid out according to these specifications. If the contents exceed the specified size, the page break control will start a new page with the same size.

In addition, the total page size is determined both by the contents' size and by the page breaking control, such as Fill Whole Page, On New Page, Page Break.

### Continuous Mode

In continuous page mode, only the component breaking control will work. The whole page report tab or web report is laid out in a single page, and has no specific shape and size. If no component breaking control has been set, all of the components will be laid out in the same page, and the size of the page will depend on the size of the contents.

In continuous page mode, all of the properties set in pagination mode will be simply skipped, including the page breaks in page panel. In this way, if there is more than one page panel in a page report tab, all contents contained in different page panels will be laid out in the same page, and only the first page panel's page header and footer will be laid out.

**Component breaking rule**

Logi Report Designer provides you with an option for adding page breaks to a component in continuous page mode. This kind of page break is not based on space, but on logic. For example, you can set a group break to occur every 20 detail panels, no matter how big these 20 detail panels are.

The following components have logic break functionality:

* Banded objects which are available in page reports   
   The logic break acts only on the sub-components - detail panel and group panel. There are two properties in the Report Inspector that are related to the component logic break: Current Block Index and Items per Block.
* Tables  
   The logic break acts only on the sub-components - table detail in page reports and table group. There are two properties in the Report Inspector that are related to the component logic break: Current Block Index and Items per Block.
* Crosstabs in page reports that are created using query resources   
   The logic break acts on the whole crosstab. There are four properties in the Report Inspector that are related to the component logic break: Current Row Block Index, Current Column Block Index, Items per Row Block and Items per Column Block.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636121-Creating-Bursting-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636141-Making-High-Efficiency-Reports)
