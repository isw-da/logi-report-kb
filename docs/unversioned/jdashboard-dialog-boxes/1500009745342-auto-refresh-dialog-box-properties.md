---
title: "Auto Refresh Dialog Box Properties"
id: 1500009745342
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745342-Auto-Refresh-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:00Z
---

# Auto Refresh Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745322-JDashboard-Dialog-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773261-Color-Picker-Dialog-Box-Properties)

# Auto Refresh Dialog Box Properties

You can use the Auto Refresh dialog box to pause or resume the auto refresh action and [customize the auto refresh action of a library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Refresh). This topic describes the options in the dialog box.

The dialog box varies with the resource you choose to auto refresh: [the data components that are created on a business view](#AutoRefreshBV) or [the objects that are not bound with data](#AutoRefresh).

---

When you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the component title bar of a library component, select Auto Refresh from the option list, and select a business view that is used by the data components as the data source in the library component, or right-click a data component which uses the business view as the data source in the library component, and select Auto Refresh from the shortcut menu, Server displays the Auto Refresh dialog box as follows and helps you to automatically refresh the data components in the library component which are created based on the business view on a defined interval.

![Auto Refresh dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885537815/autorefrsh_bv.gif)

**Refresh Interval**

Specifies to pause or refresh the library component, and the time interval for data refresh.

* ![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4404880463383/btn_dshbrd_pause.gif) / ![Play button](https://devnet.logianalytics.com/hc/article_attachments/4404880465175/btn_dshbrd_play.gif)  
   Pauses/resumes the refresh action.

* **Interval**   
  Specifies the time interval at which to automatically refresh the library component.

**Incremental Fetch**

Specifies whether to fetch incremental data when auto refreshing the library component.

* **Incremental Condition**  
   Opens the [Incremental Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009773441-Incremental-Condition-Dialog-Box-Properties) dialog box to specify conditions to filter the incremental data when the Incremental Fetch option is selected. The incremental condition does not work on crosstabs and real time charts.

**Unique Key**

Specify a unique key for the library component. You can manually type the unique key or select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885376663/btn_chsr1.gif) to open the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009773681-Unique-Key-Dialog-Box-Properties) dialog box to specify a unique key.

**Value Number**

Specify the number of values for incremental fetch.

**OK**

Select **OK** to apply the change you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

---

When you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the component title bar of a library component and then select Auto Refresh > Others from the options list, Server displays the Auto Refresh dialog box as follows and helps you to automatically refresh the objects in the library component which are not bound with data at runtime based on a defined interval.

![Auto Refresh dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885538327/autorefrsh.gif)

![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4404880463383/btn_dshbrd_pause.gif) / ![Play button](https://devnet.logianalytics.com/hc/article_attachments/4404880465175/btn_dshbrd_play.gif)

Pauses/resumes the refresh action.

**Interval**

Specifies the time interval at which to automatically refresh the objects.

**OK**

Select **OK** to apply the change you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Auto Refresh dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745322-JDashboard-Dialog-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773261-Color-Picker-Dialog-Box-Properties)
