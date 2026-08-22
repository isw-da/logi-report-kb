---
title: "Elasticsearch Connection Wizard Dialog Box"
id: 1500010096501
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096501-Elasticsearch-Connection-Wizard-Dialog-Box
updated_at: 2021-07-23T19:15:20Z
---

# Elasticsearch Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058882-Edit-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058902-Elasticsearch-Data-Source-Options-Dialog-Box)

# Elasticsearch Connection Wizard Dialog Box

You can use the Elasticsearch Connection Wizard dialog box to [set up an Elasticsearch connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010095381-Working-with-XML-Connections-in-a-Catalog) to get data from an Elasticsearch data source. This topic describes the options in the dialog box.

Designer displays the Elasticsearch Connection Wizard dialog box when you select OK in the [Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058902-Elasticsearch-Data-Source-Options-Dialog-Box). You see the following screens in the dialog box:

* [Modify Schema Properties Screen](#Modify)
* [Transformed Relational Schema Screen](#Transformed)
* [Add Table Screen](#Add)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish transforming the Elasticsearch schema to a relational schema.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Modify Schema Properties Screen

Use this screen to specify properties of the Elasticsearch schema.

![Elasticsearch Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404856972823/elstcschcnctnwzd_mdfy.gif)

**Schema**

The box lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4404856879895/btn_elmnt.gif)stands for element.

**Properties**

The box lists all the properties of the selected elements in the schema.

* **Name**  
  The column shows the properties of the selected elements.
* **Value**  
  The column shows the values of the properties for the selected elements.

## Transformed Relational Schema

This screen lists the relational tables built based on the transformed relational schema structure.

![Elasticsearch Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848580887/elstcschcnctnwzd_trnsfrmd.gif)

## Add Table

Use this screen to add tables that are transformed from the relational schema to the connection. Designer does not display this screen when you use the dialog box for editing an existing Elasticsearch connection.

![Elasticsearch Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856973079/elstcschcnctnwzd_adtbl.gif)

**Tables**

The box lists the tables transformed from the Elasticsearch schema.

**Added Tables**

The box lists the tables that you add from the relational schema.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058882-Edit-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058902-Elasticsearch-Data-Source-Options-Dialog-Box)
