---
title: "Web Wizard Dialog"
id: 1500009608122
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608122-Web-Wizard-Dialog
updated_at: 2021-07-24T16:04:42Z
---

# Web Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634001-Web-Report-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610862-Windows-Media-Player-Parameter-Dialog)

# Web Wizard Dialog

The Web Wizard helps you to [export a report to HTML format](https://devnet.logianalytics.com/hc/en-us/articles/1500009610982--Exporting-to-HTML). It appears when you select File > Export > To HTML.

The wizard contains the following tabs: [Report](#Report), [Directory](#Directory), [Image Chart](#Chart) and [Note](#Note).

**Previous**

Retains changes and returns to the previous tab.

**Next**

Retains changes and goes to the next tab.

**Finish**

Completes the exporting.

**Cancel**

Does not retain any changes and closes the wizard.

**Help**

Displays the help document about this feature.

## Report

Specifies the options applied to the report.

![Web Wizard - Report](https://devnet.logianalytics.com/hc/article_attachments/4404904226583/webwzrd_rpt.gif)

**Export to**

Specifies whether to export the report result to a single HTML file or multiple HTML files.

**Web Page Name**

Specifies the name of the exported file.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404911669015/btn_mvup3.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904224919/btn_mvdwn3.gif)

Moves the specified report tab one step down.

**Web Browser**

Specifies the web browser for which the HTML result adapts.

**Text Overflow**

Specifies whether the text overflow is visible or hidden.

**No Margin**

Specifies whether to remove the margins originally set when the report was designed.

**Drilldown**

Specifies whether to generate the drilldown files when exporting the report, which allow you to drill down on the summaries in grouped banded objects in the exported HTML file.

**TOC**

Specifies whether to enable the TOC (Table of Contents) in the exported HTML file.

**No Hyperlink**

If the option is selected, there will be no hyperlinks for navigating previous and Next Topics on the navigation bar of the exported HTML file. Enabled only when Single File is selected.

**No Page Number**

If the option is selected, there will be no page number information showing the current page number and total page number on the navigation bar of the exported HTML file. Enabled only when Single File is selected.

**Embedded CSS**

Specifies whether to embed the cascading style sheet (CSS) in the exported HTML files; otherwise, the .css file will be generated individually. Enabled only when Multiple Files is selected.

**Section 508 Compliant Output**

If the option is selected, the accessibility attributes defined for the report objects via the Report Inspector will be exported to the HTML result which is Section 508 compliant. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility) for more information.

When Section 508 Compliant Output is selected, the Use HTML Data Table and Relative Font Size options will be selected and disabled. The output will be Section 508 compliant including HTML data table, accessible attributes, and relative font feature.

**Use HTML Data Table**

Specifies whether the table and crosstab components will be output as table objects in the HTML result.

**Absolute Font Size**

Specifies whether to generate the report result using an absolute font size, which means the font size is fixed and cannot be adjusted according to the font size settings in the web browser.

**Relative Font Size**

Specifies whether to generate the report result using a relative font size, which means the font size can be adjusted according to the font size settings in the web browser.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported HTML file. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

## Directory

Specifies the location in which to place the exported HTML file.

![Web Wizard - Directory](https://devnet.logianalytics.com/hc/article_attachments/4404911671191/webwzrd_drctry.gif)

## Image Chart

Specifies in which image format charts in the report will be converted to: Auto Select, GIF, JPG (JPEG) or PNG. If Auto Select, the image format will be set to JPG or GIF by the Logi Report system automatically.

![Web Wizard - Image Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904226839/webwzrd_cht.gif)

## Note

This tab includes important information about HTML.

![Web Wizard - Note](https://devnet.logianalytics.com/hc/article_attachments/4404911671447/webwzrd_note.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634001-Web-Report-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009610862-Windows-Media-Player-Parameter-Dialog)
