---
title: "Auto Refresh Dialog Box Properties"
id: 28891512945037
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891512945037-Auto-Refresh-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:56Z
source_host: docs-report.zendesk.com
---
# 
Auto Refresh Dialog Box Properties 

You can use the Auto Refresh dialog box to pause or resume the auto refresh action and customize the auto refresh action of a library component. This topic describes the properties in the dialog box.

The dialog box varies with the resource you choose to auto refresh: the data components that are created on a business view or the objects that are not bound with data. 

When you select the Options button  on the component title bar of a library component, select Auto Refresh, and select a business view that the data components use as the data source in the library component; or right-click a data component which uses the business view as the data source in the library component, and select Auto Refresh from the shortcut menu. Server displays the Auto Refresh dialog box as follows. You can use it to automatically refresh the data components in the library component that use the business view based on a defined interval.

Refresh Interval

Specify to pause or refresh the library component, and the time interval for data refresh. 

- 
/Pause/Play button
  Select to pause/resume the refresh action.

- 
Interval 
Select or type the time interval at which you want to automatically refresh the library component.

Incremental Fetch

Select if you want to fetch incremental data when auto refreshing the library component. Then specify the following properties:

- 
Incremental Condition
Select to open the Incremental Condition dialog box to specify conditions to filter the incremental data. The incremental condition does not work on crosstabs or real time charts. 

- 
Unique Key
Specify a unique key for the library component. Select the ellipsis button  to open the Unique Key dialog box to specify a unique key.
            

- 
Value Number
Specify the number of values for incremental fetch.
            

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

When you select the Options button  on the component title bar of a library component and select Auto Refresh > Others, Server displays the Auto Refresh dialog box as follows and helps you to automatically refresh the objects in the library component which are not bound with data at runtime based on a defined interval. 

/Pause/Play button

Select to pause/resume the refresh action.

Interval 

Specify the time interval at which to automatically refresh the objects.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
