---
title: "Auto Refresh Dialog Box Properties"
id: 4405683697687
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683697687-Auto-Refresh-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:52Z
---

# Auto Refresh Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690530839-JDashboard-Dialog-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690531863-Color-Picker-Dialog-Box-Properties)

# Auto Refresh Dialog Box Properties

You can use the Auto Refresh dialog box to pause or resume the auto refresh action and [customize the auto refresh action of a library component](https://devnet.logianalytics.com/hc/en-us/articles/4405690495383-General-Operations-in-JDashboard#Refresh). This topic describes the properties in the dialog box.

The dialog box varies with the resource you choose to auto refresh: [the data components that are created on a business view](#AutoRefreshBV) or [the objects that are not bound with data](#AutoRefresh).

---

When you select the Options button ![](https://devnet.logianalytics.com/hc/article_attachments/4420453392151/btn_dshbrd_more.gif) on the component title bar of a library component, select **Auto Refresh**, and select a business view that the data components use as the data source in the library component; or right-click a data component which uses the business view as the data source in the library component, and select **Auto Refresh** from the shortcut menu. Server displays the Auto Refresh dialog box as follows and helps you to automatically refresh the data components in the library component that use the business view based on a defined interval.

![Auto Refresh dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453613975/autorefrsh_bv.gif)

**Refresh Interval**

Specify to pause or refresh the library component, and the time interval for data refresh.

* ![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4420447290903/btn_dshbrd_pause.gif)/![Play button](https://devnet.logianalytics.com/hc/article_attachments/4420461692439/btn_dshbrd_play.gif)**Pause/Play button**  
   Select to pause/resume the refresh action.

* **Interval**   
  Select or type the time interval at which you want to automatically refresh the library component.

**Incremental Fetch**

Select if you want to fetch incremental data when auto refreshing the library component. Then specify the following properties:

* **Incremental Condition**  
  Select to open the [Incremental Condition dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683709463-Incremental-Condition-Dialog-Box-Properties) to specify conditions to filter the incremental data. The incremental condition does not work on crosstabs or real time charts.
* **Unique Key**  
  Specify a unique key for the library component. Select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420447035159/btn_chsr1.gif) to open the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690542871-Unique-Key-Dialog-Box-Properties) to specify a unique key.
* **Value Number**  
  Specify the number of values for incremental fetch.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

---

When you select the Options button ![](https://devnet.logianalytics.com/hc/article_attachments/4420453392151/btn_dshbrd_more.gif) on the component title bar of a library component and select **Auto Refresh** > **Others**, Server displays the Auto Refresh dialog box as follows and helps you to automatically refresh the objects in the library component which are not bound with data at runtime based on a defined interval.

![Auto Refresh dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453614231/autorefrsh.gif)

![Pause button](https://devnet.logianalytics.com/hc/article_attachments/4420447290903/btn_dshbrd_pause.gif)/![Play button](https://devnet.logianalytics.com/hc/article_attachments/4420461692439/btn_dshbrd_play.gif)**Pause/Play button**

Select to pause/resume the refresh action.

**Interval**

Specify the time interval at which to automatically refresh the objects.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690530839-JDashboard-Dialog-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690531863-Color-Picker-Dialog-Box-Properties)
