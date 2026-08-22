---
title: "Select Values Dialog Box Properties"
id: 45203999997325
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203999997325-Select-Values-Dialog-Box-Properties
updated_at: 2026-04-30T14:10:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Select Values Dialog Box Properties

You can use the Select Values dialog box to select one or more values of a field. This topic describes the properties in the dialog box.

Server displays the dialog box when you do either of the following:

- Right-click any value of a detail field in a table or banded object, and then select Filter > Select Values from the shortcut menu.
            

- In the Edit Dataset Filter dialog box or Filter dialog box, select More in a value list.
            

Available Values

Select the values you want to filter data with. You can select multiple values at a time. 

When there are more than 300 values, Server uses the Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.

Search button

Select to launch the search bar to search for values.

- 
Text box
      Type the text you want to search for. Server lists the values containing the matched text.

- 
XClose button
      Select to close the search bar.

- 
More button
 Select to show more search properties.
      
- 
Highlight All
          Select to highlight all matched text. 

- 
Match Case
          Select to search for text that meets the case of the typed text. 

- 
Match Whole Word
 Select to search for text that looks the same as the typed text.

- 
Advanced
 Select to display the search bar in the advanced mode. Then, you can customize the value range as you want.
            The advanced properties available on the search bar vary with field types:

- 
For a field of the String type

There are two search conditions. Select one and type characters, then select OK to start searching. To clear the characters, select X. Select Cancel to close the search bar. 

- 
Start with
                  Select to search for the first characters among the values. 

- 
End with
                Select to search for the last characters among the values. 

- 
For a field of Numeric type

You can use five operators for composing the search condition. Select one from the operator list, type value in the text box, then select OK o start searching. To clear the value, select X in the text box. Select Cancel to close the search bar. 

- 
>
                Greater than

- 
>=
                Greater than or equal to

- 
<
                Less than

- 
<=
                Less than or equal to

- 
between
                Server locates the data values between a range of values indicated by a start value and an end value. The second value should not be smaller than the first value, otherwise the search result will be null.

- 
For a field of Date/Time type

You can use five operators for composing the search condition. Select one from the operator list, select the Calendar icon  to select a value from the calendar, then select OK to start searching. Select Cancel to close the search bar. 

- 

    When you selected Highlight All, you can use this button to go to the previous matched text.

- 

    When you selected Highlight All, you can use this button to go to the next matched text.

Clear button

Select to cancel the selection of values.

OK

Select to apply the values you specified here. 

Cancel

Select to cancel the selection of field values and close the dialog box.

Help button

Select to view information about the dialog box.

Close button

Select to cancel the selection of field values and close the dialog box.
