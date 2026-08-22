---
title: "Working with Barcodes"
id: 1500010094341
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094341-Working-with-Barcodes
updated_at: 2021-07-23T19:14:37Z
---

# Working with Barcodes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057482-Built-in-UDOs-JHyperLink-and-JRotator)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094841-Working-with-Ranks)

# Working with Barcodes

In Designer, you can create both linear barcodes such as Code 39, Code 128, EAN, and UPC, and 2D barcodes like QR Code in page reports which use query resources. This topic introduces how you can create linear barcodes and QR Codes in a report respectively.

You can insert a barcode in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).

This topic contains the following sections:

* [Inserting a Linear Barcode in a Report](#Linear)
* [Inserting a QR Code in a Report](#QRCode)

## Inserting a Linear Barcode in a Report

1. Position the mouse pointer at the destination where you want to insert the barcode.
2. Select **Insert** > **Barcode**, or **Home** > **Insert** > **Barcode**. Designer displays the [Barcode Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058082-Barcode-Expert-Dialog-Box).

   ![Barcode Expert dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857009047/brcd.gif)
3. Select a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) in the current page report from the **Barcode Resources** drop-down list to get data resources for the barcode, then specify the source of the barcode: a DBField, formula, summary, or parameter. When you select to insert the barcode into a data component, Designer disables the dataset drop-down list and you can only use resources from the current dataset to create the barcode.
4. From the **Symbology** drop-down list, select the required barcode type . You can preview the format of the selected symbology in the **Sample** box. For detailed information on the symbologies of barcodes, refer to the professional barcode technical documentation.
5. From the **Scale Mode** drop-down list, select the unit for the values of the quiet zone, narrow width, supplement, height, and ratio.
6. In the **Quite Zone** text box, specify the space around the barcode (most symbologies require quiet zones that precede and follow the barcode).
7. In the **Narrow Width** text box, set the barcode bar width.
8. You can specify the supplement of the barcode. If you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you do not need to set the supplement.
9. In the **Height** text box, set the height of the barcode bars.
10. Specify the width ratio of the thick bar to the thin bar in the **Ratio** text box if you select the barcode type as Code 39 or Codabar. The ratio can only be **2.0** or **3.0**. Designer treats any ratio value not equal to 2.0 or 3.0 as 2.0.
11. You can change the default value of the barcode in the **Default Message** text box. Designer applies the value for the barcode in design mode.
12. Select the **Enable Checking Digits** checkbox if you want to include check digits in the barcode.
13. If you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you can select **Display HR** to display the barcode numbers together with the barcode.
14. If you choose the Code 128 symbology, you can specify whether to enable optimizing the length of the barcode in the report result.
15. Select **Insert** to close the dialog box, then select the mouse button in the location where you want to display the barcode.

## Inserting a QR Code in a Report

1. Position the mouse pointer at the destination where you want to insert the QR Code.
2. Select **Insert** > **QR Code**, or **Home** > **Insert** > **QR Code**. Designer displays the [QR Code Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098301-QR-Code-Expert-Dialog-Box).

   ![QR Code Expert dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856900887/qrcd.gif)
3. Select a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) in the current page report from the **QR Code Resources** drop-down list to get data resources for the QR Code, then specify the source of the QR Code: a DBField, formula, summary, or parameter. When you select to insert the QR Code into a data component, Designer disables the dataset drop-down list and you can only use resources from the current dataset to create the QR Code.
4. Set the margin between the image in the middle of the QR Code and the border of the QR Code.
5. Select the error correction level for the QR Code. Error correction helps in making a QR Code stay readable, even when some pixels are missing. There are four correction levels. Level "L" means 7% of the code words can be recovered from a damaged symbol, level "M" means 15%, level "Q" 25%, and level "H" 30%. The higher the level is, the bigger the QR Code gets.
6. You can change the default value of the QR Code in the **Default Message** text box, which Designer applies for the QR Code in design mode. If you want to use it as the value of the QR Code in the report result, select **Use Default Message**, then Designer ignores the data field you select as the source of the QR Code.
7. Select **Insert** to close the dialog box, then select the mouse button in the location where you want to display the QR Code.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Where you can insert a barcode in a report depends on what you have selected as its source.
* You can also create a barcode component by first inserting a label, DBField, formula, summary, parameter, or special field and then [changing its display type to Barcode or QR Code](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports#Barcode).

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the barcode component example, open `<install_root>\Demo\Reports\SampleComponents\Barcode.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057482-Built-in-UDOs-JHyperLink-and-JRotator)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094841-Working-with-Ranks)
