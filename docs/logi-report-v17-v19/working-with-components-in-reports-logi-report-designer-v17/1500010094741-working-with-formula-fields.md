---
title: "Working with Formula Fields"
id: 1500010094741
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields
updated_at: 2021-07-23T19:14:45Z
---

# Working with Formula Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields)

# Working with Formula Fields

[Formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010060962-Working-with-Formulas) are calculated from DBFields, other formulas, summaries, and parameters. This topic introduces how you can insert formula fields in a report and add conditional formats to the formula fields.

For the formula fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Formula Fields in a Report](#Insert)
* [Adding Conditional Formats to Formula Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the formula field example, open `<install_root>\Demo\Reports\SampleComponents\UsingFormula.cls`.

## Inserting Formula Fields in a Report

You can insert formula fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).

* **For a business view-based report**  
  Select the formula from the [Dynamic Resources > Formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) node in the Data panel and drag it to the destination.
* **For a query-based report**  
  You have two ways to insert a formula into a query-based report.
  + **By dragging and dropping**  
    Select the formula from the Formulas node in the Data panel, then drag it to the destination. If the given formulas are not what you want, select the **<New Formula...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog) as required.
  + **Using dialog box**
    1. Position the mouse pointer at the destination where you want to insert the formula.
    2. Select **Insert** > **Formula** or **Home** > **Insert** > **Formula**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box).

       ![Insert Fields dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848523671/instfld.gif)
    3. Select the required formula from the **Formulas** node. You can select multiple formulas to insert them all a time.
    4. If you select multiple formulas, in the **Insert Layout** box, specify the layout of the formula fields in the report. By default, Designer arranges them in the default layout. You can arrange the formula fields horizontally or vertically by selecting **Horizontal** or **Vertical**, and customize the space between them.
    5. Select the **Insert** button to insert the formula fields into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* In a query-based report, not all formulas in the catalog are valid in the current context, so under the Formulas node in the Insert Fields dialog box or the Data panel, Designer only lists the valid formulas that are based on DBFields from the current dataset.
* If you insert a formula into the detail panel of a data component, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the formula and its name label in the same panel. If you do not want Designer to insert the name label automatically, you can clear **Insert field name label with field** in the Options dialog box (File > Options > Component > Insert field name label with field).

## Adding Conditional Formats to Formula Fields

You can add conditional formats to formula fields in a report, then when a specified condition is fulfilled, Logi Report automatically applies the format defined on the condition to the field values. This is very useful to highlight values that the report users may need to act on at runtime.

To add conditional format to a formula field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields)
