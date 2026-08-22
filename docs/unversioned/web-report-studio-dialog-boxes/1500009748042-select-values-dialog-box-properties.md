---
title: "Select Values Dialog Box Properties"
id: 1500009748042
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748042-Select-Values-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:12Z
---

# Select Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776301-Select-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties)

# Select Values Dialog Box Properties

This topic describes how you can use the Select Values dialog box to select one or more values to apply a filter criterion. Server displays the dialog box when you right-click on any value of a detail field in a table or banded object and select Filter > Select Values from the shortcut menu.

![Select Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880334999/slctvalue.gif)

**Available Values**

Specifies the values to filter data with. Multiple values can be selected.

When there are more than 300 values, Logi Report will use Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)**Search**

Launches the search bar to search for values.

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
   type the text you want to search for and the values containing the matched text will be listed.
* **X**  
   Closes the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
  + **Advanced**  
     Displays the search bar in the advanced mode. With the advanced options, you can customize the value range as you want.

    The advanced options available on the search bar vary with field types:

    - **For fields of the String type**

      ![Advanced - String Fields](https://devnet.logianalytics.com/hc/article_attachments/4404880335255/btn_srchtlbr_string.gif)

      There are two search conditions. Select one and specify characters in the text box, then select the **OK** button to start searching. To clear the characters you enter, select **X** in the text box. The Cancel button is used to close the search bar.

      * **Start with**  
         Searches for the first characters among the values.
      * **End with**  
         Searches for the last characters among the values.
    - **For fields of Numeric type**  

      ![Advanced - Numeric Fields](https://devnet.logianalytics.com/hc/article_attachments/4404880335767/btn_srchtlbr_num.gif)

      Five operators are supported for composing the search condition. Select one from the operator drop-down list and type value in the text box to compose the condition, then select the **OK** button to start searching. To clear the value you enter, select **X** in the text box. The Cancel button is used to close the search bar.

      * **>**  
         Greater than
      * **>=**  
         Greater than or equal to
      * **<**  
         Less than
      * **<=**  
         Less than or equal to
      * **between**  
         The data values are located between a range of values indicated by a start value and an end value. If selected, the second input value should not be smaller than the first input value, otherwise the search result will be null.
    - **For fields of Date/Time type**

      ![Advanced - Date/Time Fields](https://devnet.logianalytics.com/hc/article_attachments/4404885444759/btn_srchtlbr_date.gif)

      Five [operators](#Operator) are supported for composing the search condition. Select one from the operator drop-down list and select the **Calendar** icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif) to select a value from the calendar to compose the condition, then select the **OK** button to start searching. The Cancel button is used to close the search bar.
* ![Previous button](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
   When Highlight All is selected, you can use this button to go to the previous matched text.
* ![Next button](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404880145431/btn_clear.gif)

Cancels the selection of values.

**OK**

Closes the dialog box and filters the field with the value you specified.

**Cancel**

Cancels filtering the field and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776301-Select-Value-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties)
