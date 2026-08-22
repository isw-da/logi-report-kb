---
title: "Enter Values Dialog"
id: 1500009608062
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608062-Enter-Values-Dialog
updated_at: 2021-07-24T16:04:42Z
---

# Enter Values Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631021-Enter-Parameter-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608082-Excel-Option-Dialog)

# Enter Values Dialog

The Enter Values dialog helps you to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values#Multiple). It appears when you select the down arrow ![](https://devnet.logianalytics.com/hc/article_attachments/4404911646487/btn_drpdwn1.gif) in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009631021-Enter-Parameter-Values-Dialog) dialog if the parameter allows for multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911649943/entervlu.gif)

The following are details about options in the dialog:

**All Values**

Available when the parameter's Enable the "All Values" Option property is true. It specifies whether to apply all values to the parameter, which could be all values of the parameter determined by Logi Report, all values in the database, or all the available values according to the [Scope of All Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#AllScope) setting of the parameter.

Only when this option is unselected, can the following options for adding values be enabled.

**Available Values**

Lists all predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, values of the display column are listed here.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When the parameter has more than 500 values, after you scroll down to the bottom of the value list, the down arrow will appear at the end. You can then select the down arrow to display more values.

**Enter Values**

Available when the parameter's Allow Type-in of Value property is true. It allows you to add values for the parameter manually.

* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif)**Calendar icon**  
  Opens the calendar to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values#Date). Available only when the parameter is of the Date, DateTime, or Time type.

**Selected Values**

Lists the values selected. The selected values are case sensitive.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif)

Displays the Sort drop-down menu to sort the values in ascending or descending order. The No Sort item is selected by default in the drop-down menu which means the values are listed based on the original order of their mapping fields in the database.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif)**Search**

Opens the search box to search for values. To start the search, type in the text you want to search for and the values containing the matched text will be listed.

In the search box, there are the following options:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404911683351/btn_srchbox_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404904186775/btn_close1.gif)  
   Closes the search box and cancels the search.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904203415/btn_addarrow1.gif)

Adds the selected values from the Available Values box to the Selected Values box, or adds the value you type in the Enter Values text box to the Selected Values box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911650199/btn_rmvarrow1.gif)

Removes the selected values from the Selected Values box.

![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404904203671/btn_addall1.gif)

Adds all the listed values from the Available Values box to the Selected Values box.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404911650967/btn_rmvall1.gif)

Removes all the values from the Selected Values box.

**OK**

Closes the dialog and selects the specified values for the parameter.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631021-Enter-Parameter-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608082-Excel-Option-Dialog)
