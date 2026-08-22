---
title: "Web Report Properties"
id: 12480378693005
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480378693005-Web-Report-Properties
updated_at: 2026-03-03T14:21:40Z
source_host: docs-report.zendesk.com
---
# 
Web Report Properties

This topic describes the properties of a Web Report object.

| Property Name | Description |
| --- | --- |
| General |  |
| Default Format for Viewing Report | Specifies the default format to view the report on Server. Default is to adopt the format setting on Server. If you select a specific format, you can further configure the format options. Choose an option from the drop-down list.  Select to adopt the format setting on Server. HTML Select to view the report in HTML. Select the ellipsis in the value cell to configure the format options in the HTML Option dialog box. PDF Select to view the report in PDF. Select the ellipsis in the value cell to configure the format options in the PDF Option dialog box. Excel Select to view the report in Excel. Select the ellipsis in the value cell to configure the format options in the Excel Option dialog box. Text Select to view the report in Text. Select the ellipsis in the value cell to configure the format options in the Text Option dialog box. RTF Select to view the report in RTF. Select the ellipsis in the value cell to configure the format options in the RTF Option dialog box. XML Select to view the report in XML. Select the ellipsis in the value cell to configure the format options in the XML Option dialog box. PostScript Select to view the report in PostScript. Select the ellipsis in the value cell to configure the format options in the PostScript Option dialog box. Web Report Select to view the report in Web Report Studio. Select the ellipsis in the value cell to configure the format options in the Web Report Option dialog box. Data type: Enumeration This property only controls direct running of the report on Server, but has no effect on advanced running or scheduled running of the report. |
| Result Buffer |  |
| Result Buffer Size | Specifies the number of the report pages to store in the buffer. The default size 4 indicates Report Engine allocates four pages of the report to the result buffer, and stores the other pages on disk. If you have enough memory, you can increase the result buffer size to store more pages of the report, so that you can get better performance. Data type: Integer |
| Others |  |
| Click Priority | Specifies the priority of the actions to be triggered at runtime when users select certain objects that are bound with some actions in the report. Select the ellipsis in the value cell to set the priority in the Click Priority dialog box. Data type: String |
| Constrained Data | Specifies whether to constrain users to use the business views the report applies only, if they need to add more data components into the report at runtime. Data type: Boolean |
| Embedded Fonts | Specifies the True Type Fonts (TTF) and Open Type Fonts (OTF) that you want to embed in the PDF output of the report, if you have used TTF or OTF in the report. You can select multiple fonts from the value drop-down list by pressing the Ctrl or Shift key. Both TTF and OTF fonts will be embedded in the generated PDF to ensure correct display on any device. See Delivering TTF in PDF. Data type: String |
| Continuous Page Number with TOC | Specifies whether to calculate pages for the Export Page Number and Export Total Page Number special fields in the report continuously when the report contains a TOC page panel. Data type: Boolean |
| Ignore TOC Anchor of Parent | Specifies whether to ignore the TOC Anchor property of objects that act as parent containers of other objects in the report, when generating Tables of Contents for the report. When you set this property to "true", Report Engine generates a TOC entry for an object if its TOC Anchor property is "true", even when you do not include its parent object in the TOC. If you do not want to create TOC entries for those child objects when their parent objects are excluded, set this property to "false". Data type: Boolean |
| No Temp File | Specifies whether to create temporary files for the report. You gain faster performance if you do not create the temporary files (true), while have better accuracy in data calculation with the temporary files (false). Data type: Boolean |
| On Parameter Value Change | Specifies the formulas for validating the parameter values in the report. After you specify the formulas, when users change the parameter values at runtime, Report Engine passes the values to the formulas first for validation: if the values are valid, Report Engine applies them to the parameters; otherwise, it displays the messages you define in the formulas. Choose the view elements in the business view the web report uses that are mapped to the required formulas from the drop-down list (to select multiple view elements, use the Ctrl or Shift key on the keyboard, then select outside the value cell to confirm). For example, for a String type parameter that requires a value of 4-7 characters, you can define a formula like this: if(length(@P_String) > 8 ) "The value is too long." else if (length(@P_String)
