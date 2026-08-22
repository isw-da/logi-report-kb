---
title: "Edit Summary Dialog Box"
id: 28897998557965
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897998557965-Edit-Summary-Dialog-Box
updated_at: 2024-09-30T09:09:25Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Edit Summary Dialog Box

You can use the Edit Summary dialog box to edit a summary. This topic describes the options in the dialog box.
    

Designer displays the Edit Summary dialog box when you right-click a summary and select Edit Summary from the shortcut menu in the Catalog Manager or in the Data panel.

Designer displays these options:

Resource

This box lists all the available resources that you can use for the summary.

Summaries

This option shows the name of the summary. You can also choose to create a new summary or edit another one by selecting <Create...> or the name of the summary from the drop-down list.

Aggregate Function

This drop-down list contains the aggregate functions that you can use to compute the selected field. Select the function you need. 

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Summary On

Specify the field on which the summary is to compute. To specify the  field, select it in the Resource box and then select  beside Summary On to add it to the text box.

Static Summary

Select it if you want the summary to take effect on a specific group that you define in the Group By text box.

- 
Group By
Specify the field by which to group the data.
    To specify the group-by field, select it in the Resource box and then select  beside Group By to add it to the text box.    

Dynamic Summary

Select it if you want the summary to take effect on the group according to the number that you specify in the Group By text box.

- 
Group By
Specify on which group you want the summary to take effect.
    To specify the group level, first select Up or Down from the drop-down list, then in the combo box, select a value or type an integer between 0 to 127.

Special Function

When the group-by field is Numeric, String, Date, or Time data type, you can select a special function for the field from the drop-down list to further specify to which level to group the data. If you select Customize, Designer displays the Customized Function dialog box for you to set the function.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Apply

Select to apply all changes and leave the dialog box open.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
