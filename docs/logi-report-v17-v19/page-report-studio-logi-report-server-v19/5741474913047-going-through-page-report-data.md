---
title: "Going Through Page Report Data"
id: 5741474913047
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data
updated_at: 2022-10-31T17:18:14Z
---

# Going Through Page Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438817175-Automatic-Drilling-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454332311-Adding-Conditional-Formats-to-Fields-in-Page-Report)

# Going Through Page Report Data

You can choose to show certain groups of records in a banded object and switch among the groups to see the data you want. This topic describes how you can perform the four going actions in banded objects in page reports: go-to, go-up, go-down, and go-to-detail.

You can think of the going action as being like a filter. When you go to a group you filter the other groups out of the report. The going action does not apply to banded objects that you created in Page Report Studio. It is available only for banded objects that you created in Logi Report Designer which contain groups and have not been converted to use a business view. If a banded object has been converted to use a business view or is created from a business view you will see [Drilling](https://devnet.logianalytics.com/hc/en-us/articles/5741438817175-Automatic-Drilling-Page-Report-Data) instead of Going.

See the following diagram about go-up and go-down:

![Going Diagram](https://devnet.logianalytics.com/hc/article_attachments/9905662129431/pgrpt_edit_drl_go1.gif)

* [Go-To](#Go-to)  
   The go-to action enables you to switch the data presented in a banded object from any group to any other group.
* [Go-Up](#Go-up)  
  The go-up action enables you to jump up one group level to get the records of a particular group.
* [Go-Down](#Go-down)  
  The go-down action enables you to jump down one group level to get the records of a particular group.
* [Go-to-Detail](#Go-to-detail)  
  The go-to-detail action enables you to concentrate on the details of a group.

After you perform a going action, Server re-loads the data in the banded object from the data buffer, showing only the records in the selected group. You can also view, print, and export the new report created by going to other format in the same way as the original report.

In addition, when you perform the going actions on a report, Server creates a report chain. You can select the **Back** button ![Back button](https://devnet.logianalytics.com/hc/article_attachments/9905619459095/btn_back.gif) or **Next** button ![Next button](https://devnet.logianalytics.com/hc/article_attachments/9905660473367/btn_next.gif) button on the toolbar to return to the previous level or go forward to the next level in the report chain. You can also select the **Visited Reports** button ![Visted Reports button](https://devnet.logianalytics.com/hc/article_attachments/9905631747863/btn_goto.gif) and then select a report to switch to that report directly.

The following sections describe how to use the going actions based on the banded object in the report **Detail Report Corporate Overview.cls** in the Public Reports > SampleReports folder.

## Go-To

1. Put the mouse pointer over the Detail Report Corporate Overview.cls report row and select the **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/9905658476183/btn_srv_run.gif) on the floating toolbar to run the report.

   ![Run Report](https://devnet.logianalytics.com/hc/article_attachments/9905674095639/pgrpt_edit_drl_go2.gif)
2. Right-click the product category **Blends** and select **Go To** > **Blends** > **Kona Mountain** from the shortcut menu.

   ![Go To Vietnam](https://devnet.logianalytics.com/hc/article_attachments/9905674121239/pgrpt_edit_drl_go3.gif)

   Then only the data about Kona Mountain is displayed.

   ![Data About Vietnam](https://devnet.logianalytics.com/hc/article_attachments/9905674135831/pgrpt_edit_drl_go4.gif)
3. To return to the original status, select ![Back button](https://devnet.logianalytics.com/hc/article_attachments/9905619459095/btn_back.gif) on the toolbar, or right-click any value and then select **Go To** > **ROOT** on the shortcut menu.

You may notice that the result is not dependent on what you right-clicked, in other words, you can right-click any field value in the banded object or even the blank part of a group header/footer panel or detail panel, in order to perform a go-to action.

## Go-Up

For a go-up action, you need to right-click a group header/footer panel or any object in the panel, at the same time, you should make sure that this group level is lower than some other group levels.

1. Undo the go-to action in the preceding example.
2. Right-click any product name, for example French Roast, and select **Go Up**  > **Espresso** from the shortcut menu.

   ![Go Up to LATAM](https://devnet.logianalytics.com/hc/article_attachments/9905674152983/pgrpt_edit_drl_go5.gif)

   Then only the data about Espresso is displayed.

   ![Data About LATAM](https://devnet.logianalytics.com/hc/article_attachments/9905662306327/pgrpt_edit_drl_go6.gif)

At Step 2, you may find that items listed on the Go Up submenu are product categories of the Categories group level which is one level higher than the current group level - Product Name. That is, the go-up action enables you to focus your attention on the groups of a higher level than what you right-click.

## Go-Down

For a go-down action, you need to right-click a group header/footer panel or any object in the panel. At the same time, you should make sure that this group level is higher than some other group levels.

1. Undo the go-up action in the preceding example.
2. Right-click **Blends** and select **Go Down**  > **Italian Roast** from the shortcut menu.

   ![Go Down to Singapore](https://devnet.logianalytics.com/hc/article_attachments/9905674226455/pgrpt_edit_drl_go7.gif)

   Then data about Italian Roast is displayed.

   ![Data About Singapore](https://devnet.logianalytics.com/hc/article_attachments/9905662356375/pgrpt_edit_drl_go8.gif)

At Step 2, you may find that items listed on the Go Down submenu are product names of the Category group level which is one level higher than the group level of Product Name, and only product names in the Blends category are displayed. That is, the go-down action enables you to focus your attention on the groups of a lower level than what you right-click, and only those lower-level groups which are related with the higher-level group value you right-click will be concerned.

## Go-to-Detail

If a banded object contains group information, then you can use a field, label, image, or shape map in a group header/footer panel of the banded object to obtain information of that group, and a chart in a banded object also has the similar function. You should predefine the go-to-detail action at the report design time. For more information, see Obtaining Detailed Information from a Banded Object in the *Logi Report Designer Guide*.

1. Undo the go-down action in the preceding example.
2. Right-click **Bold** and select **Go to Detail** from the shortcut menu. Server only displays the data about this category. You can also select **Bold** directly to perform the go-to-detail action, provided that the report designer has given the "Go to detail" action the highest Click Priority for the corresponding report at design time.

   ![Go to Detail](https://devnet.logianalytics.com/hc/article_attachments/9905662386327/pgrpt_edit_drl_go9.gif)

**Tip:** When performing the go-to-detail action from a banded object, if a group footer contains nothing it will be hidden by default.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438817175-Automatic-Drilling-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454332311-Adding-Conditional-Formats-to-Fields-in-Page-Report)
