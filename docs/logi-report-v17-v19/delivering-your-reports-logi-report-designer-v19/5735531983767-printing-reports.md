---
title: "Printing Reports"
id: 5735531983767
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531983767-Printing-Reports
updated_at: 2022-11-02T07:57:57Z
---

# Printing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567895703-Printing-and-Exporting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports)

# Printing Reports

Designer relies on JDK to create the printable version of a report. By default, Designer applies the JDK 1.4 printing method, but you can use other versions. This topic introduces how you can customize the printing options in Designer and print a page or web report using different printing methods.

This topic contains the following sections:

* [Specifying the Printing Options](#Option)
* [Printing with the JDK 1.4 Printing Method](#JDK1.4)
* [Printing with the JDK 1.1 Printing Method (deprecated)](#JDK1.1)
* [Printing with the JDK 1.2 Printing Method (deprecated)](#JDK1.2)

## Specifying the Printing Options

Before you can print reports, you need to first specify the printing options in the Options dialog box.

1. Navigate to **File** > **Options**. Designer displays the Options dialog box.
2. Select **Print** in the **Category** box, and select a method from the Print panel. By default, the **Use JDK1.4 printing method** is selected.

   ![Options dialog box - Print category](https://devnet.logianalytics.com/hc/article_attachments/9898459800727/optn_print.gif)
3. If you want to separate a large page during printing, select **Separate large pages**. When you print a report with a report page size which is larger than the print paper size, Designer prints the report in multiple pages serially, that is, Designer automatically separates a large page of a report.
4. Select **Apply** to save the changes, and then select **OK** to close the dialog box.

## Printing with the JDK 1.4 Printing Method

Compared with JDK 1.1 and JDK 1.2, the JDK 1.4 printing method provides you with a more diverse selection of options for printing reports, such as paper tray and color appearance.

**To print a report with the JDK 1.4 printing method**

1. Specify the printing method as **Use JDK1.4 printing method** in the Print category of the Options dialog box.
2. Open the page or web report that you want to print.
3. Navigate to **File** > **Print**. Designer displays the Print dialog box.

   ![Print dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476833687/frmt_print_14.gif)
4. Follow the window instructions to specify the settings.
5. Select **Print** to print the report.

## Printing with the JDK 1.1 Printing Method (deprecated)

The JDK 1.1 printing method is quick in speed, but the print quality cannot be guaranteed.

**To print a report with the JDK 1.1 printing method**

1. Specify the printing method as **Use JDK1.1 printing method** in the Print category of the Options dialog box.
2. Open the page or web report that you want to print.
3. Navigate to **File** > **Print**. Designer displays the Print dialog box.

   ![Print dialog box for JDK 1.1 printing method](https://devnet.logianalytics.com/hc/article_attachments/9898476836631/frmt_print_11.gif)
4. In order to overcome the limitation of JDK 1.1.x, Designer is required to be calibrated on the very first print so that the lines and text can be printed correctly. You only need to calibrate once for each printer that Designer uses. Select **Test**, and follow the window instructions.
5. Select **OK** to print the report.

## Printing with the JDK 1.2 Printing Method (deprecated)

The JDK 1.2 printing method provides you with a satisfactory result, even for .gif files, but is slow in speed.

**To print a report with the JDK 1.2 printing method**

1. Specify the printing method as **Use JDK1.2 printing method** in the Print category of the Options dialog box.
2. Open the page or web report that you want to print.
3. Navigate to **File** > **Print**. Designer displays the Page Setup dialog box.

   ![Page Setup dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898459829143/frmt_print_12.gif)
4. Specify the settings according to your requirements.
5. Select **OK** to print the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567895703-Printing-and-Exporting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports)
