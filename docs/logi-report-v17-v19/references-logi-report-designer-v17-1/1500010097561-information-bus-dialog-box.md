---
title: "Information Bus Dialog Box"
id: 1500010097561
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097561-Information-Bus-Dialog-Box
updated_at: 2021-07-23T19:15:38Z
---

# Information Bus Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097541-Incremental-Condition-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097581-Insert-Aggregation-Dialog-Box)

# Information Bus Dialog Box

You can use the Information Bus dialog box to edit the Information Bus content that Designer saves with user information in the current catalog. This topic describes the options in the dialog box.

Designer displays the Information Bus dialog box when you select File > Information Bus.

Information Bus is a built-in object in Logi Report containing information from information containers of three levels: global level, organization level, and user level. System admin can get or put information in all information containers. Organization admin can get or put information in the global level information container, its own organization level information container, and the user level information containers that belong to its organization. Organization user can get or put information in the global level information container, the organization level information container it belongs, and its own user level information container.

![Information Bus dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856920599/infmtnbus.gif)

You see the following options in the dialog box:

**Information container list**

The box shows a tree structure according to the user definition in the information containers in the current catalog. The users here are the same as those for [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094141-Setting-Up-Business-View-Security).

**Information box**

The box displays the information created for the selected information container, which are key-value pairs of information that authorized users can put or get by calling APIs and writing formulas with the following functions:

* [GetInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#GetInfo)
* [GetOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#GetOrgInfo)
* [GetUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#GetUserInfo)
* [PutInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#PutInfo)
* [PutOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#PutOrgInfo)
* [PutUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#PutUserInfo)
* [RemoveInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#RemoveInfo)
* [RemoveOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#RemoveOrgInfo)
* [RemoveUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#RemoveUserInfo)

To edit information for a container, select it from the container list, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the information box, and then double-click the Key and Value cells to specify the key and value respectively. To remove an information line, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097541-Incremental-Condition-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097581-Insert-Aggregation-Dialog-Box)
