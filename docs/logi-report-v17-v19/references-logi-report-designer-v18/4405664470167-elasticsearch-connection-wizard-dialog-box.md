---
title: "Elasticsearch Connection Wizard Dialog Box"
id: 4405664470167
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664470167-Elasticsearch-Connection-Wizard-Dialog-Box
updated_at: 2022-01-27T20:38:18Z
---

# Elasticsearch Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661533079-Edit-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661534231-Elasticsearch-Data-Source-Options-Dialog-Box)

# Elasticsearch Connection Wizard Dialog Box

You can use the Elasticsearch Connection Wizard dialog box to [set up an Elasticsearch connection](https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog) to get data from an Elasticsearch data source. This topic describes the options in the dialog box.

Designer displays the Elasticsearch Connection Wizard dialog box when you select OK in the [Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661534231-Elasticsearch-Data-Source-Options-Dialog-Box). You see the following screens in the dialog box:

* [Modify Schema Properties Screen](#Modify)
* [Transformed Relational Schema Screen](#Transformed)
* [Add Table Screen](#Add)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Modify Schema Properties Screen

Use this screen to specify properties of the Elasticsearch schema.

![Elasticsearch Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4420550928023/elstcschcnctnwzd_mdfy.gif)

**Schema**

This box lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4420542089239/btn_elmnt.gif)stands for element.

**Properties**

This box lists properties and values of the properties for the selected elements in the schema.

## Transformed Relational Schema Screen

This screen lists the relational tables that Designer builds based on the transformed relational schema structure. Select **Next** to confirm the transformation result and go to the Add Table screen.

![Elasticsearch Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4420556199447/elstcschcnctnwzd_trnsfrmd.gif)

## Add Table Screen

Use this screen to add tables that Designer transforms from the Elasticsearch data source to the connection. Designer does not display this screen when you use the dialog box for editing an existing Elasticsearch connection.

![Elasticsearch Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4420542154647/elstcschcnctnwzd_adtbl.gif)

**Tables**

This box lists the tables that Designer transforms from the Elasticsearch data source, which you can add to the Elasticsearch connection.

**Added Tables**

This box lists the tables that you add to use in the Elasticsearch connection.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified tables in the Tables box to use in the Elasticsearch connection.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661533079-Edit-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661534231-Elasticsearch-Data-Source-Options-Dialog-Box)
