---
title: "XML Option Dialog Box"
id: 12480207595021
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480207595021-XML-Option-Dialog-Box
updated_at: 2026-02-25T23:48:32Z
source_host: docs-report.zendesk.com
---
# 
XML Option Dialog Box

You can use the XML Option dialog box to predefine the options for directly running a report in XML on Server. This topic describes the options in the dialog box.
    

Designer displays the XML Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "XML" and then select the ellipsis  in the value cell in the Report Inspector.

Designer displays these options:

Only Data

Select to only generate data of the report in the XML output.

When you select Only Data, the XML output contains only the database column information, and the corresponding XML schema file contains only the structure information of the report; if you do no select Only Data, the XML output also contains elements controlled by formulas, and the XML schema file contains all the detail information from the report, including all the property values of each report object.

Run Linked Report

Select to generate the reports that you link with the report (not including the detail reports) in the XML output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
