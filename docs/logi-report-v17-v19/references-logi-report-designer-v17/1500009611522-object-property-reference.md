---
title: "Object Property Reference"
id: 1500009611522
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611522-Object-Property-Reference
updated_at: 2021-07-24T16:03:50Z
---

# Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634041-XML-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties)

# Object Property Reference

This topic introduces the properties of objects in Logi Report Designer. It explains the [report object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties) shown in the Report Inspector and [catalog data object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009634561-Catalog-Data-Object-Properties) in the Catalog Manager respectively.

Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what can be achieved with each property.
* Some properties are just used to show related information and cannot be edited.
* Some properties can be [controlled by a formula or expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). If a formula is selected to control a property, it will be automatically generated as an expression prefixed by an @ sign. Also, some properties must be known by Logi Report Engine before a page break, so that it can lay out the object. In a formula or expression, the special field PageNumber is the switch for setting the page break calculation time. If PageNumber is used in the formula or expression, then the calculation time will be after the page break, if PageNumber is not used, the calculation time will be before the page break. For this reason, Logi Report will set the calculation time for controlling whether the formula or expression will be marked as before page break or after page break. For most properties, the property can be controlled by formula or expression at any time without concern about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.
* The unit of the measurement properties like Width, Height, Thickness, and so on is determined by the [Units](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Display) setting in the Options dialog, which can either be inch or centimeter.
* You can use the search bar to easily locate the desired property of an object (to display the search bar, select the **Search** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif) at the upper right corner of the Properties sheet). The search bar is closed when you select another object.

  ![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404911620119/btn_srchtlbr.gif)

  + **Text box**  
     Type in the text you want to search for and the properties containing the matched text will be listed.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404904186775/btn_close1.gif)  
     Clear the text in the text box.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404911620375/btn_srchtlbr_adv.gif)  
     Lists more search options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that looks the same as the typed text.
    - **Include Sub-Node**   
       Available only in the Report Inspector. If selected, property searching will be performed within the property list of the selected object as well as those of its child objects.

**Tip:** When you hover the mouse on any property in Logi Report Designer, a tip is displayed showing a brief description about the property. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404911645719/btn_tiphelp.gif) on the tip to open the corresponding help doc or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404911645975/btn_tipcls.gif) to close the tip. If you do not want to display the property tips, clear **Show tips** in the Options dialog (**File** > **Options** > **General** > **Show tips**).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634041-XML-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties)
