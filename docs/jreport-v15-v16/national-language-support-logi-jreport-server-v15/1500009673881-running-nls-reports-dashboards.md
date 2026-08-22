---
title: "Running NLS Reports/Dashboards"
id: 1500009673881
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673881-Running-NLS-Reports-Dashboards
updated_at: 2021-07-24T20:53:57Z
---

# Running NLS Reports/Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649222-Editing-Resource-Tree-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)

# Running NLS Reports/Dashboards

When you have NLS enabled for a report or library component on the Logi JReport Administration page, or have an NLS report or library component published to the server from Logi JReport Designer, you can then run the report or dashboard that contains the library component in the specified languages.

Before running a report or dashboard, make sure you have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) on it when it's in the Public Reports folder in the server resource tree.

**To directly run an NLS report/dashboard in a specified language:**

1. On the Logi JReport Console page, Select **Profile** on the system toolbar, then select  **Customize****Server Preferences** on the task bar of the Profile page.
2. Select the **Advanced** tab, check **Enable NLS**  and choose the language from the Default Language drop-down list, in which you want the NLS report/dashboard to display by default, then select the corresponding encoding from the Default Encoding drop-down list.
3. Select **OK** to save the changes.
4. Select **Resources** on the system toolbar to switch to the Resources page.
5. Browse to the report/dashboard you want to run and select its name. The report result will then be displayed in the language you have specified.

**To run an NLS report in a specified language in Advanced mode:**

1. On the Logi JReport Console > Resources page, browse to the report you want to run, put the mouse pointer over the report row and select the **Advanced Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423319/btn_srv_advrun.gif) on the floating toolbar.
2. In the Format tab, select the **Enable NLS** checkbox, choose the language from the Using Language drop-down list, then select the corresponding encoding from the Encoding drop-down list.
3. Finish the other related options and select **Finish** to run the report. The report result will then be run in the selected language.

**To schedule an NLS report to make it run in a specified language:**

1. On the Logi JReport Console > Resources page, browse to the report you want to schedule, put the mouse pointer over the report row and select the **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422295/btn_srv_schdl.gif) on the floating toolbar.
2. In the General tab, select the **Enable NLS** checkbox, then choose the language from the Using Language drop-down list, select the corresponding encoding from the Encoding drop-down list.
3. Finish the other related options and select **Finish** to perform the task. The report result will then be run in the selected language.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649222-Editing-Resource-Tree-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)
