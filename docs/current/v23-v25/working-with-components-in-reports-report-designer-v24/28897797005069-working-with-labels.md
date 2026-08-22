---
title: "Working with Labels"
id: 28897797005069
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897797005069-Working-with-Labels
updated_at: 2024-09-30T09:14:13Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Working with Labels

A label is an object containing a string, which is typically a brief description used to identify a field or other value nearby. This topic describes how you can insert and format labels in a report.

For the labels in a report, you can use them as the trigger object of links, and  change their display types if you want.

This topic contains the following sections:

- Inserting Labels in a Report

- Formatting the Labels in a Report 

See an example: The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type  in a report. For the label component example, open <install_root>\Demo\Reports\SampleComponents\ForLabel.cls.

## 
Inserting Labels in a Report

You can insert labels in the report areas listed in Component Placement in Different Report Type.

To insert a label in a report, use either of the following methods:

-  From the Components panel, drag the Label icon  in the Basic category to the destination in the report. 

- Navigate to Insert > Label or Home > Insert > Label, then select in the location where you want to display the label. 

Designer inserts a label with the default text "Label". You can then edit the text of a label.

- To edit the full text of a label, double-click the label to select the text, then type the replacement text.

- To edit a portion of a label's text, double-click the label, then select in the label and drag to select the portion, after that, type the replacement text. 

You can also modify a label's text by using the Text property value in the Report Inspector.

 You can neither drag nor use the Insert menu to insert labels into charts. For more information about chart labels, see Formatting Chart Labels.

## 
Formatting the Labels in a Report 

You can format the label text using options in the Format ribbon, for example, you can change the font size, color, and alignment of the text. 

To format a label, first select the label, then perform any of the following operations:

- To change the alignment of a label, select the required alignment button: Justify, Left, Center or Right. Designer then aligns the text in the label according to your selection.

- To change the font face, select Font Face Box and then select the required font from the drop-down list. The fonts introduced with "*" are True Type Fonts. For more information, see Applying True Type Fonts in Reports.

- To change the font size, select Font Size Box and then select the required size from the drop-down list (or type the required value in the text box and then select Enter on the keyboard).

- To change the font style, select the corresponding font style buttons: Bold, Italic, and Underline.

- To change the background color of the label, select Background Color ; to change the foreground color of the label text, select Foreground Color.

Previous Topic  Next Topic
