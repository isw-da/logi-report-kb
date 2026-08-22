---
title: "Barcode Expert Dialog Box"
id: 12480076930061
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480076930061-Barcode-Expert-Dialog-Box
updated_at: 2026-02-25T23:50:04Z
source_host: docs-report.zendesk.com
---
# 
Barcode Expert Dialog Box

You can use the Barcode Expert dialog box to create and edit a barcode object and then insert it in a report. This topic describes the options in the dialog box.
    

Designer displays the Barcode Export dialog box when you navigate to Insert > Barcode or drag the Barcode icon  from the Components panel to a query-based page report.

Designer displays these options:

Barcode Resources

This drop-down list contains the data resources that you can use for the barcode. The data source of a barcode can be database fields, formulas, summaries, or parameters.

Symbology

This drop-down list contains the barcode types that you can create in Designer. You can select from the following: UPC-A, UPC-E, EAN-13, EAN-8, Code39, Code128, and Codabar.

Scale Mode

Select the unit for values of Quiet Zone, Narrow Width, Supplement, Height, and Ratio. You can select from the following: Mils (0.001 inch), Metric (0.01 millimeter), and Points (1/72 inch).

Quiet Zone

Specify the space around the barcode where there are no dark marks. Most symbologies require a quiet zone which precedes the following barcode.

Narrow Width

Specify the barcode bar width.

Supplement

Specify the supplement. Some barcode types, such as CODE39, CODE128, and Codabar, do not have supplements.

Height

Specify the height of the barcode.

Ratio

Specify the width ratio of the thick bar to the thin bar in the CODE39/ Codabar barcode. The ratio box can have only 2 effective values, 2.0 and 3.0. Designer regards any ratio values that are not equal to 2.0 or 3.0 as 2.0. Enabled only for CODE39 and Codabar.

Default Message

Specify the default value of the barcode, which Designer applies to the barcode in design mode.

Enable Checking Digits

Select to enable the checking digits.

Display HR

Designer enables this option only for CODE39, CODE128, and Codabar. Select it if you want to display the barcode numbers together with the barcode. 

Enable Length Optimization

Designer enables this option only for Code 128. Select it if you want to enable optimizing the length of the barcode.

Insert

Select to accept the settings and insert the barcode into your report.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
