---
title: "Select N Dialog Box"
id: 45190585894669
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190585894669-Select-N-Dialog-Box
updated_at: 2026-04-30T15:14:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Select N Dialog Box

You can use the Select N dialog box to specify the Select N condition to filter the records or groups in a data component. This topic describes the options in the dialog box.
    

Designer displays the Select N dialog box when you select Select N in the Group screen of the banded/table wizard, or in the Display screen of the map wizard.

Designer displays these options:

In

This option shows where to apply the Select N condition, the whole object or a specific group.

Select N

Specify the Select N condition.

- 
All
Select to display all the records, or all the groups in the specified group level in the data component.

- 
Top N
Select and specify a number in the text box below to display the first N records, or the first N groups in the specified group level in the data component. You can also select a parameter which returns an integer from the drop-down list to dynamically define the Top N condition.

- 
Bottom N
Select and specify a number in the text box below to display the last N records, or the last N groups in the specified group level in the data component. You can also select a parameter which returns an integer from the drop-down list to dynamically define the Bottom N condition.

Other

Designer enables this option when you use the dialog box for defining the Select N condition for a specific group level. Select it to display all the other groups of this group level that don't match the Select N condition (which are by default hidden) in another group. Specify the name for this group in the text box.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
