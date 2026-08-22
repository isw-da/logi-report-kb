---
title: "Export to Fax Dialog"
id: 1500010030742
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030742-Export-to-Fax-Dialog
updated_at: 2021-07-24T10:38:52Z
---

# Export to Fax Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065921-Export-to-Excel-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030782-Export-to-Logi-JReport-Result-Dialog)

# Export to Fax Dialog

The Export to Fax dialog helps you to [export a report to fax](https://devnet.logianalytics.com/hc/en-us/articles/1500010033102-Exporting-to-Fax). It appears when you select File > Export > To Fax.

![Export to Fax dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901166359/expt2fax.gif)

The following are details about options in the dialog:

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Quality**

Specifies the quality of the fax. It can be one of the following: Best, Normal, or Fast.

**Include Cover Sheet**

Specifies whether to send a cover sheet with the fax. If Yes, you can specify what you want to display on the cover sheet.

* **Fax Number**  
   Specifies the fax number of the recipient.
* **Phone Number**  
   Specifies the phone number of the sender.
* **To**  
   Specifies information of the recipient.
* **From**  
   Specifies information of the sender.
* **Company**  
   Specifies information of the company.
* **Date**  
   Specifies the day on which the fax is sent.
* **RE**  
   Specifies the subject of the fax.
* **Comments**  
   Specifies some comments to the fax.
* **Urgent**  
   Specifies whether or not the fax is urgent.
* **For Review**  
   Specifies whether or not only review is required for the fax.
* **Please Comment**  
   Specifies whether or not comments are required for the fax.
* **Please Reply**  
   Specifies whether or not a reply is required for the fax.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) for the fax. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065921-Export-to-Excel-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030782-Export-to-Logi-JReport-Result-Dialog)
