---
title: "Information Bus Dialog Box"
id: 4405661623063
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661623063-Information-Bus-Dialog-Box
updated_at: 2022-01-27T20:35:27Z
---

# Information Bus Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664520343-Incremental-Condition-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661624087-Insert-Aggregation-Dialog-Box)

# Information Bus Dialog Box

You can use the Information Bus dialog box to edit the Information Bus content that Designer saves with user information in the current catalog. This topic describes the options in the dialog box.

Designer displays the Information Bus dialog box when you navigate to File > Information Bus.

Information Bus is a built-in object in Logi Report containing information from information containers of three levels: global level, organization level, and user level. System admin can get or put information in all information containers. Organization admin can get or put information in the global level information container, its own organization level information container, and the user level information containers that belong to its organization. Organization user can get or put information in the global level information container, the organization level information container it belongs, and its own user level information container.

![Information Bus dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550887575/infmtnbus.gif)

You see the following options in the dialog box:

**Information container list**

This box shows a tree structure according to the user definition in the information containers in the current catalog. The users here are the same as those for [business view security](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security).

**Information box**

This box displays the information created for the selected information container, which are key-value pairs of information that authorized users can put or get by calling APIs and writing formulas with the following functions:

* [GetInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#GetInfo)
* [GetOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#GetOrgInfo)
* [GetUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#GetUserInfo)
* [PutInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#PutInfo)
* [PutOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#PutOrgInfo)
* [PutUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#PutUserInfo)
* [RemoveInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#RemoveInfo)
* [RemoveOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#RemoveOrgInfo)
* [RemoveUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions#RemoveUserInfo)

To edit information for a container, select it from the container list, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) above the information box, and then double-click the Key and Value cells to specify the key and value respectively. To remove an information line, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664520343-Incremental-Condition-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661624087-Insert-Aggregation-Dialog-Box)
