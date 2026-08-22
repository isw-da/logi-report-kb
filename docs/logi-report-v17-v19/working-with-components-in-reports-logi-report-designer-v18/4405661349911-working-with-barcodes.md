---
title: "Working with Barcodes"
id: 4405661349911
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661349911-Working-with-Barcodes
updated_at: 2022-01-27T20:34:22Z
---

# Working with Barcodes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664407575-Built-in-UDOs-JHyperLink-and-JRotator)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664400279-Working-with-Ranks)

# Working with Barcodes

You can create both linear barcodes such as Code 39, Code 128, EAN, and UPC, and 2D barcodes like QR Code in page reports which use query resources. This topic describes how you can create linear barcodes and QR Codes in a report respectively.

You can also create a barcode component by first inserting a label, DBField, formula, summary, parameter, or special field and then [changing its display type to Barcode or QR Code](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports#Barcode).

This topic contains the following sections:

* [Inserting a Linear Barcode in a Report](#Linear)
* [Inserting a QR Code in a Report](#QRCode)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Where you can insert a barcode in a report depends on what you have selected as its source. See [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship) for more information.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the barcode component example, open `<install_root>\Demo\Reports\SampleComponents\Barcode.cls`.

## Inserting a Linear Barcode in a Report

1. Position the mouse pointer at the destination where you want to insert the barcode.
2. Do one of the following:
   * From the **Components** panel, drag the **Barcode** icon ![Barcode icon](https://devnet.logianalytics.com/hc/article_attachments/4420550952599/icon_brcd.gif) in the Others category to the report.
   * Navigate to **Insert** > **Barcode**.
   * Navigate to **Home** > **Insert** > **Barcode**.

   Designer displays the [Barcode Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661461911-Barcode-Expert-Dialog-Box).

   ![Barcode Expert dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542178839/brcd.gif)
3. Select a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) in the current page report from the **Barcode Resources** drop-down list to get data resources for the barcode, then specify the source of the barcode: a DBField, formula, summary, or parameter. When you select to insert the barcode into a data component, Designer disables the dataset drop-down list and you can only use resources from the current dataset to create the barcode.
4. From the **Symbology** drop-down list, select the required barcode type . You can preview the format of the selected symbology in the **Sample** box. For detailed information on the symbologies of barcodes, refer to the professional barcode technical documentation.
5. From the **Scale Mode** drop-down list, select the unit for the values of the quiet zone, narrow width, supplement, height, and ratio.
6. In the **Quite Zone** text box, specify the space around the barcode (most symbologies require quiet zones that precede and follow the barcode).
7. In the **Narrow Width** text box, set the barcode bar width.
8. You can specify the supplement of the barcode. If you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you do not need to set the supplement.
9. In the **Height** text box, set the height of the barcode bars.
10. Specify the width ratio of the thick bar to the thin bar in the **Ratio** text box if you select the barcode type as Code 39 or Codabar. The ratio can only be **2.0** or **3.0**. Designer treats any ratio value not equal to 2.0 or 3.0 as 2.0.
11. You can change the default value of the barcode in the **Default Message** text box, which Designer applies to the barcode in design mode.
12. Select **Enable Checking Digits** if you want to include check digits in the barcode.
13. If you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you can select **Display HR** to display the barcode numbers together with the barcode.
14. If you choose the Code 128 symbology, you can specify whether to enable optimizing the length of the barcode.
15. Select **Insert** to close the dialog box.
16. Select in the location where you want to display the barcode.

## Inserting a QR Code in a Report

1. Position the mouse pointer at the destination where you want to insert the QR Code.
2. Do one of the following:
   * From the **Components** panel, drag the **QR Code** icon ![QR Code icon](https://devnet.logianalytics.com/hc/article_attachments/4420551006615/icon_qrcd.gif) in the Others category to the report.
   * Navigate to **Insert** > **QR Code**.
   * Navigate to **Home** > **Insert** > **QR Code**.

   Designer displays the [QR Code Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661683735-QR-Code-Expert-Dialog-Box).

   ![QR Code Expert dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542105239/qrcd.gif)
3. Select a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) in the current page report from the **QR Code Resources** drop-down list to get data resources for the QR Code, then specify the source of the QR Code: a DBField, formula, summary, or parameter. When you select to insert the QR Code into a data component, Designer disables the dataset drop-down list and you can only use resources from the current dataset to create the QR Code.
4. Set the margin between the image in the middle of the QR Code and the border of the QR Code.
5. Select the error correction level for the QR Code. Error correction helps in making a QR Code stay readable, even when some pixels are missing. There are four correction levels. Level "L" means 7% of the code words can be recovered from a damaged symbol, level "M" means 15%, level "Q" 25%, and level "H" 30%. T he higher the level is, the bigger the QR Code gets.
6. You can change the default value of the QR Code in the **Default Message** text box, which Designer applies to the QR Code in design mode. If you also want to use this value as the value of the QR Code in the report, select **Use Default Message**, then Designer ignores the data field you select as the source of the QR Code.
7. Select **Insert** to close the dialog box.
8. Select in the location where you want to display the QR Code.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664407575-Built-in-UDOs-JHyperLink-and-JRotator)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664400279-Working-with-Ranks)
