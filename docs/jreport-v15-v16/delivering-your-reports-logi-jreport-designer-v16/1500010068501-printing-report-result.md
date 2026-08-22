---
title: "Printing Report Result"
id: 1500010068501
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068501-Printing-Report-Result
updated_at: 2021-07-24T10:38:14Z
---

# Printing Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033062-Printing-and-Exporting-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result)

# Printing Report Result

Logi JReport relies on the JDK to create the printable version of report result. By default the JDK 1.4 printing method is used, but you can use other versions if needed.

Below is a list of the sections covered in this topic:

* [Specifying Printing Options](#Option)
* [Printing with the JDK 1.4 Printing Method](#JDK1.4)
* [Printing with the JDK 1.1 Printing Method (deprecated)](#JDK1.1)
* [Printing with the JDK 1.2 Printing Method (deprecated)](#JDK1.2)

## Specifying Printing Options

Before you can print reports, you need to first specify the printing options in the Options dialog.

**To specify printing options:**

1. Select **File** > **Options**. The Options dialog appears.
2. Select **Print** in the Category box, and select a method of your choosing from the Print panel. By default, the **Use JDK1.4 printing method** is selected.

   ![Options dialog - Print category](https://devnet.logianalytics.com/hc/article_attachments/4404909146391/optn_print.gif)
3. If you want to separate a large page during printing, select **Separate large pages**. When you print a report with a report page size which is larger than the print paper size, the report will be printed in multiple pages serially. That is, Logi JReport will automatically separate a large page of a report.
4. Select the **Apply** button to save the changes, and then select the **OK** button to close the dialog.

## Printing with the JDK 1.4 Printing Method

Compared with JDK 1.1 and JDK 1.2, the JDK 1.4 printing method provides you with a more diverse selection of options for printing reports, such as paper tray, and color appearance.

**To print a report with the JDK 1.4 printing method:**

1. Specify the printing method as **Use JDK1.4 printing method** in the Print category of the Options dialog.
2. Open the report you want to print.
3. Select **File** > **Print**. The Print dialog appears.

   ![Print dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901162903/frmt_print_14.gif)
4. Follow the window instructions to specify the settings.
5. Select **Print** to print the report.

## Printing with the JDK 1.1 Printing Method (deprecated)

The JDK 1.1 printing method is quick in speed, but the print quality cannot be guaranteed.

**To print a report with the JDK 1.1 printing method:**

1. Specify the printing method as **Use JDK1.1 printing method** in the Print category of the Options dialog.
2. Open the report you want to print.
3. Select **File** > **Print**. The Print dialog appears.

   ![Print dialog for JDK 1.1 printing method](https://devnet.logianalytics.com/hc/article_attachments/4404901163159/frmt_print_11.gif)

   In order to overcome the limitation of JDK 1.1.x, Logi JReport is required to be calibrated on the very first print so that the lines and text can be printed correctly. You will only need to calibrate once for each printer that Logi JReport uses. Select the **Test** button, and follow the window instructions.
4. Select **OK** to print the report.

## Printing with the JDK 1.2 Printing Method (deprecated)

The JDK 1.2 printing method will provide you with a satisfactory result, even for .gif files, but is slow in speed.

**To print a report with the JDK 1.2 printing method:**

1. Specify the printing method as **Use JDK1.2 printing method** in the Print category of the Options dialog.
2. Open the report you want to print.
3. Select **File** > **Print**. The Page Setup dialog appears.

   ![Page Setup dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909146647/frmt_print_12.gif)
4. Specify the settings according to your requirements.
5. Select **OK** to print the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033062-Printing-and-Exporting-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result)
