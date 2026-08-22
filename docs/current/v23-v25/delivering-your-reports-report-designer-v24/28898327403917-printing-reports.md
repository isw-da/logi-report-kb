---
title: "Printing Reports"
id: 28898327403917
section: "Delivering Your Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898327403917-Printing-Reports
updated_at: 2024-09-30T09:13:36Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Printing Reports

Designer relies on JDK to create the printable version of a report. By default, Designer applies the JDK 1.4 printing method, but you can use other versions. This topic introduces how you can customize the printing options in Designer and print a page or web report using different printing methods.

This topic contains the following sections:

- Specifying the Printing Options

- Printing with the JDK 1.4 Printing Method

- Printing with the JDK 1.1 Printing Method (deprecated)

- Printing with the JDK 1.2 Printing Method (deprecated)

## 
Specifying the Printing Options

Before you can print reports, you need to first specify the printing options in the Options dialog box.

- Navigate to File > Options. Designer displays the Options dialog box.

- Select Print in the Category box, and select a method  from the Print panel. By default, the Use JDK1.4 printing method is selected.
    

- If you want to separate a large page during printing, select Separate large pages. When you print a report with a report page size which is larger than the print paper size, Designer prints the report in multiple pages serially, that is, Designer automatically separates a large page of a report.

- Select Apply to save the changes, and then select OK to close the dialog box.

## 
Printing with the JDK 1.4 Printing Method

Compared with JDK 1.1 and JDK 1.2, the JDK 1.4 printing method provides you with a more diverse selection of options for printing reports, such as paper tray and color appearance.

To print a  report with the JDK 1.4 printing method

- Specify the printing method as Use JDK1.4 printing method in the Print category of the Options dialog box.

- Open the page or web report that you want to print.

- Navigate to File > Print. Designer displays the Print dialog box.
    

- Follow the window instructions to specify the settings.

- Select Print to print the report.

## 
Printing with the JDK 1.1 Printing Method (deprecated)

The JDK 1.1 printing method is quick in speed, but the print quality cannot be guaranteed.

To print a report with the JDK 1.1 printing method

- Specify the printing method as Use JDK1.1 printing method in the Print category of the Options dialog box.

- Open the page or web report that you want to print.

- Navigate to File > Print. Designer displays the Print dialog box.
    

- In order to overcome the limitation of JDK 1.1.x, Designer is required to be calibrated on the very first print so that the lines and text can be printed correctly. You only need to calibrate once for each printer that Designer uses. Select Test, and follow the window instructions.

- Select OK to print the report.

## 
Printing with the JDK 1.2 Printing Method (deprecated)

The JDK 1.2 printing method provides you with a satisfactory result, even for .gif files, but is slow in speed.

To print a report with the JDK 1.2 printing method

- Specify the printing method as Use JDK1.2 printing method in the Print category of the Options dialog box.

- Open the page or web report that you want to print.

- Navigate to File > Print. Designer displays the Page Setup dialog box.
    

- Specify the settings according to your requirements.

- Select OK to print the report.

Previous Topic  Next Topic
