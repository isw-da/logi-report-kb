---
title: "Designing a Report Page"
id: 1500009571022
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page
updated_at: 2021-07-24T05:53:46Z
---

# Designing a Report Page

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592961-Previewing-a-Page-Report)

# Designing a Report Page

A report page is a medium which contains the layout result for a single page of a report tab. At runtime, a page or multiple pages can be generated in a report tab according to the page panel settings. Also, each page has its own page headers and page footers, which are controlled by the page panel settings for them.

A report page has the following features:

> * [Page Panel](#Panel)
> * [Page Headers and Footers](#Header)
> * [Page Settings](#Setting)
> * [Page Break](#Break)
> * [Page Mode](#Mode)

## Page Panel

A page panel is a template to design a page. You can define information for it and meanwhile information for pages designed with this page panel will be defined accordingly. Here, information covers all factors of a page, including page size, margin, and orientation. Also, you can define the page headers and page footers for a page panel. By default, a page panel has only one page header and page footer, but you can also set more and remove them according to your requirements.

In addition, Logi JReport Designer also supports multiple page panels. With multiple page panels, you have to define each page panel's page settings individually.

### Inserting a page panel

When inserting a page panel into a page, you can choose whether the new page will keep the original page settings or it will apply new settings.

* **Inserting a page panel where the new page keeps the original page settings**
  1. Select **Insert** > **Page Panel**.
  2. In the [Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009588101-Page-Panel-Dialog) dialog, select **Keep Current Page Setting**.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404889287831/pgpnl.gif)
  3. Select **OK** to insert the panel.
* **Inserting a page panel where the new page has new page settings** 
  1. In the Page Panel dialog, select **Use a new page setting**.
  2. Select **OK**. The Page Setup dialog will then appear for you to adjust the settings for the new page panel.

### Removing a page panel

To remove a page panel, set the mouse pointer to the beginning of the page panel and then press the **Backspace** key.

**Notes:**

* Page panels can be inserted into the report body level.
* Page panels can be inserted into banded reports which satisfy the following conditions:
  + The parent of the banded object is the report body.
  + The Position property value of the banded object is set to static.
  + There isn't any existing page panel in the report body.

## Page Headers and Footers

Page headers and footers are areas in the top and the bottom page margins, where you can add any Logi JReport components. They are added to the current page settings. Any page that uses the same settings automatically receives the header or footer that you add. You can insert fields, such as page numbers and chapter headings, in headers and footers in a text document.

A page header and page footer will be generated at the same time when a report tab is created, except for banded layout reports. For a banded layout report, a page header and page footer can only be generated after you insert a page panel into a banded panel.

You can choose to show or hide them according to your own requirements by selecting or unselecting the **Page Header** or **Page Footer** command on the View tab.

## Page Settings

Settings for a page are the same as with a page panel which is used as a template to design this page. All pages designed with the same page panel will apply the same page settings. So, you just need to set the settings for a page panel to apply them to these pages.

To adjust the page settings, the following are two ways for you to choose:

* **Adjusting via the Page Setup dialog**
  1. Select **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog appears.

     ![Page Setp dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893806871/pgstup_gnrl.gif)
  2. In the General tab of the dialog, set size, orientation and margin for the report page. You can check the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable.

     The Export tab is for defining page properties for each export result (for details, see [Exporting Report Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results)).
  3. Select **OK** to apply your settings.

* **Adjusting via the Report Inspector**
  1. Select **View** > **Report Inspector**.
  2. In the Report Inspector, select a Page Panel node the properties of which you want to customize.
  3. Set the [property values](https://devnet.logianalytics.com/hc/en-us/articles/1500009569722-Properties-of-Page-Panel-in-Page-Report) according to your requirements.

## Page Break

A new page will be generated in a report tab only when the space in a page has been fully occupied or there exists a break control in this page, for example, a page break that is inserted in the page.

To insert a page break, select **Insert** > **Page Break**.

**Notes:**

* Page breaks can be inserted into the report body level.
* Page breaks can be inserted into banded objects only when the following conditions have been met:
  + The parent of the banded object is the report body.
  + There isn't any existing page panel in the report body.
  + Its Position property of the banded object is set to static.

## Page Mode

In Logi JReport Designer, you can set the page mode of a report tab: [pagination mode](#Pagination) and [continuous mode](#Continuous).

To switch between the two page modes, you can select or unselect **Page Layout** on the View tab.

### Pagination mode

In pagination mode, the page shape and size can be specified in the page panel settings. Once set, the contents of the report tab will be laid out according to these specifications. If the contents exceed the specified size, the page break control will start a new page with the same size.

In addition, the total page size is determined both by the contents' size and by the page breaking control, such as Fill Whole Page, On New Page, Page Break.

### Continuous mode

In continuous page mode, only the component breaking control will work. The whole report tab is laid out in a single page, and has no specific shape and size. If no component breaking control has been set, all of the components will be laid out in the same page, and the size of the page will depend on the size of the contents.

In continuous page mode, all of the properties set in pagination mode will be simply skipped, including the page breaks in page panel. In this way, if there is more than one page panel in a report tab, all contents contained in different page panels will be laid out in the same page, and only the first page panel's page header and footer will be laid out.

**Component breaking rule**

Logi JReport Designer provides you with an option for adding page breaks to a component in continuous page mode. This kind of page break is not based on space, but on logic. For example, you can set a group break to occur every 20 detail panels, no matter how big these 20 detail panels are.

The following three components have logic break functionality: banded object, table and crosstab:

* For banded objects, the logic break acts only on the sub-components - detail panel and group panel.
* For tables, the logic break acts only on the sub-components - table detail and table group.
* For crosstabs, the logic break acts on the whole crosstab.

And, several properties are related to the component logic break:

* For banded objects and tables, there are two related properties: Current Block Index and Items per Block.
* For crosstabs, there are four related properties: Current Row Block Index, Current Column Block Index, Items per Row Block and Items per Column Block.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592961-Previewing-a-Page-Report)
