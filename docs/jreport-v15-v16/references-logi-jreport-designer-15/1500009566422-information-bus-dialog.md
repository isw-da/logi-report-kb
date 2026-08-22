---
title: "Information Bus Dialog"
id: 1500009566422
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566422-Information-Bus-Dialog
updated_at: 2021-07-24T05:55:07Z
---

# Information Bus Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566402-Incremental-Condition-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587561-Insert-Aggregation-Dialog)

# Information Bus Dialog

The Information Bus dialog appears when you select File > Information Bus. It helps you to edit the Information Bus content saved with user information in the current catalog.  [See the dialog](javascript:%20void(null)).

![Information Bus dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893875095/infmtnbus.gif)

Information Bus is a built-in object in Logi JReport containing information from information containers of three levels: global level, organization level and user level. System admin can get or put information in all information containers. Organization admin can get or put information in the global level information container, its own organization level information container and the user level information containers that belong to its organization. Organization user can get or put information in the global level information container, the organization level information container it belongs and its own user level information container.

**Information container list**

Shows a tree structure according to the user definition in the information containers in the current catalog. The users here are the same as those created for [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security).

**Information box**

Displays information created for the selected information container, which are key-value pairs of information that can be put or got by authorized users when calling APIs and writing formulas with the following functions:

* [GetInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#GetInfo)
* [GetOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#GetOrgInfo)
* [GetUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#GetUserInfo)
* [PutInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#PutInfo)
* [PutOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#PutOrgInfo)
* [PutUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#PutUserInfo)
* [RemoveInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#RemoveInfo)
* [RemoveOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#RemoveOrgInfo)
* [RemoveUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#RemoveUserInfo)

To edit information for a container, select it from the container list, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the information box. In the Key and Value cells, double-click to specify the key and value respectively. To remove an information line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).

**OK**

Applies the changes and closes this dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566402-Incremental-Condition-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587561-Insert-Aggregation-Dialog)
