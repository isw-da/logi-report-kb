---
title: "Exporting Reports"
id: 28898316389517
section: "Delivering Your Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898316389517-Exporting-Reports
updated_at: 2024-09-30T09:07:48Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Exporting Reports

This topic introduces how you can export page and web reports to different formats. It also describes the two useful configuration methods for customizing the page settings and layout precision of each export format.

You can export a page or web report to the following file formats:

- Mail

- Report Result

- HTML

- PDF

- Excel

- Text

- RTF

- XML

- PostScript

- Fax

## 
Customizing Page Settings for Report Outputs

Before exporting a report, you can customize the page settings for the output of each export format. For a library component, the page settings take effect when users export the library component in JDashbaord.

- Navigate to File > Page Setup. Designer displays the Page Setup dialog box.

- Select the Export tab.

- Select a format from the Export To drop-down list.

- By default, Designer applies pagination mode to the output of the format for a page report tab or web report. Clear Page Layout if you want to apply continuous mode, so the output displays in a single page.

- Designer enables the page options when you do not clear Page Layout and automatically applies the page settings that you define in the General tab of the dialog box to the output of the format. You can clear Auto and specify different page settings for the output.

- Select other formats to customize the page layout and page settings of the output.

- Select OK to accept the settings. 

When you clear the Auto option for an export format and select OK in the Page Setup dialog box, Designer adds a corresponding export page setting object to the report structure tree in the Report Inspector. You can edit the page properties for the output of the export format there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer removes its export page setting object automatically from the report structure tree.

 Server also applies the page layout and page settings you specify for any export format when users advanced run and schedule to run the page report tab or web report in this format at runtime.

## 
Customizing the Layout Precision for Report Outputs

You can customize the layout precision to apply when exporting reports in  Designer. However for page reports, the customized precision can take effect only in report tabs whose Precision Sensitive property is "true".

- Navigate to File > Options.

- In the Options dialog box, select Export to in the Category box.

- Select the Layout Precision. Designer displays the Advanced Export Settings dialog box.
    

- Select Customize for each format.   By default, Designer selects Optimize for speed over visual effect, meaning, Designer decides the precision level which is oriented towards speed more than visualization. 

- Select System Default Settings, then in the Precision Settings dialog box, edit the precision level for each format and select OK.
    

Designer provides two precision levels: High and Low. High precision provides better layout but slower efficiency, while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision because faster performance is guaranteed at the same time. By default, when you export a report to formats such as PDF, RTF, Excel, Fax, or PostScript, Designer exports the text  with high precision, thus the report layout of these formats is different from other formats such as HTML, Report Result, XML, and Text.

- In the Advanced Export Settings dialog box, select the checkbox for the required formats to apply the defined precision level and select OK. For formats that you do not  select, Designer determines their precision.

- Select OK in the Options dialog box to apply the settings.

 You can export a report in either design or view mode. However, if you modify the report after opening it, you should use view mode to export it. To do this, select the View tab, and then select Refresh Data on the toolbar. Designer then refetches data in the report from the database. After that, you can export the report to the required format.

Previous Topic  Next Topic
