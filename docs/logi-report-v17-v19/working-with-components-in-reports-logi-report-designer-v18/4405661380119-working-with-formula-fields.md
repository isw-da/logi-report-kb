---
title: "Working with Formula Fields"
id: 4405661380119
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields
updated_at: 2022-01-27T20:34:29Z
---

# Working with Formula Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields)

# Working with Formula Fields

[Formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664600343-Working-with-Formulas) are calculated from DBFields, other formulas, summaries, and parameters. This topic introduces how you can insert formula fields in a report and add conditional formatting to the formula fields.

For the formula fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Formula Fields in a Report](#Insert)
* [Adding Conditional Formatting to Formula Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the formula field example, open `<install_root>\Demo\Reports\SampleComponents\UsingFormula.cls`.

## Inserting Formula Fields in a Report

You can insert formula fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship).

**For a business view-based report**

Select the formula from the [Dynamic Resources > Formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) node in the Data panel and drag it to the destination.

**For a query-based report**

You can insert a formula into a query-based report using either of the following two methods:

* **By dragging and dropping**  
  In the **Data** panel, select the formula from the **Formulas** node , then drag it to the destination. If the predefined formulas are not what you want, select the **<New Formula...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog) as required.
* **Using dialog box**
  1. Position the mouse pointer at the destination where you want to insert the formula.
  2. Navigate to **Insert** > **Formula** or **Home** > **Insert** > **Formula**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661626647-Insert-Fields-Dialog-Box).

     ![Insert Fields dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556241047/instfld.gif)
  3. Select the required formula from the **Formulas** node. You can select multiple formulas to insert them all a time.
  4. If you select multiple formulas, in the **Insert Layout** box, specify the layout of the formula fields in the report. By default, Designer arranges them in the default layout. You can arrange the formula fields horizontally or vertically by selecting **Horizontal** or **Vertical**, and customize the space between them.
  5. Select **Insert** to insert the formula fields into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* In a query-based report, not all formulas in the catalog are valid in the current context, so under the Formulas node in the Insert Fields dialog box or the Data panel, Designer only lists the valid formulas that are based on DBFields from the current dataset.
* If you insert a formula into the detail panel of a data component, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the formula and its name label in the same panel. If you do not want Designer to insert the name label automatically, clear "Insert field name label with field" in the Component category of the Options dialog box.

## Adding Conditional Formatting to Formula Fields

You can add conditional formatting to formula fields in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to a formula field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields)
